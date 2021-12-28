import csv

def get_nums(numbers_csv):
    with open(numbers_csv, 'r') as all_nums:
        bingo_numbers = []
        csv_reader = csv.reader(all_nums)

        # need to loop over the lines in csv_reader as it's just an object in memory
        for line in csv_reader:
            # iterate through each number in a row of data to build out a single list
            for num in line:
                bingo_numbers.append(num)
    
    return bingo_numbers


def generate_boards(boards_csv):
    with open(boards_csv, 'r') as all_boards:
        bingo_boards = ['card1']
        csv_reader = csv.reader(all_boards, delimiter = ' ')

        card_num = 1

        for row_num, line in enumerate(csv_reader):
            index = 0
            if (row_num + 1) % 6 == 0:
                card_num += 1
                
            if line == []:
                line = "card" + str(card_num)

            for num in line: 
                if num == '':
                    line.pop(index)
                index += 1

            bingo_boards.append(line)

    boards_dictionary = {}

    for index, board in enumerate(bingo_boards):
        if 'card' in board:
            key = board
            values = []
            continue
        values.append(board)

        if index % 5 == 0:
            boards_dictionary[key] = values
    
    return boards_dictionary


def bingo_check(bingo_board):
    # initializes 2D array to store columns
    board_columns = []
    for col_index in range(len(bingo_board[0])):
        board_columns.append(['' for i in range(len(bingo_board))])

    # pivots columns into their own rows in the board_columns list
    for row_index, board_rows in enumerate(bingo_board):
        for col_index, col in enumerate(board_rows):
            board_columns[col_index][row_index] = col
    
    is_bingo = False
    # checks rows for a bingo    
    for row in bingo_board:
        if row[0] == 'X':
            for position, value in enumerate(row):
                if value == 'X' and position == len(row) - 1:
                    is_bingo = True
                    return is_bingo
                elif value == 'X': continue
                else: break
        else: continue

    # checks cols for a bingo
    for row in board_columns:
        if row[0] == 'X':
            for position, value in enumerate(row):
                if value == 'X' and position == len(row) - 1:
                    is_bingo = True
                    return is_bingo
                elif value == 'X': continue
                else: break
        else: continue
    
    return is_bingo


def play_bingo(dict_of_boards, list_of_nums):
    winning_cards = []
    is_bingo = False

    marked_boards_dict = dict_of_boards.copy()

    for num in list_of_nums:
        for key in marked_boards_dict.keys():
            player_board = marked_boards_dict[key]
            for row in player_board:
                for col, value in enumerate(row):
                    if value == num:
                        row[col] = 'X'
            
            is_bingo = bingo_check(player_board)
            
            if is_bingo == True:
                winning_cards.append(key)
                winning_number = int(num)

        # PRINTS MARKED CARDS AFTER EACH NUM DRAWN (for debugging)
        # for key in marked_boards_dict.keys():
        #     print(key)
        #     for row in marked_boards_dict[key]:
        #         print(row)
        
        # after all cards have been checked for a bingo...
        # if the winning cards list has any values written to it
        # break out of the list_of_nums loop and return results; otherwise continue
        if len(winning_cards) >= 1: break
    
    return (winning_cards, winning_number, marked_boards_dict)


def play_losing_bingo(dict_of_boards, list_of_nums):
    cards_without_bingo = [key for key in dict_of_boards.keys()]
    winning_cards = []
    is_bingo = False

    marked_boards_dict = dict_of_boards.copy()
    last_card = False

    for num in list_of_nums:
        for card in cards_without_bingo[:]:
            # ^ important that a copy of cards_without_bingo is being used
            # ensures the index is based off the original copy and not the list getting its items removed
            player_board = marked_boards_dict[card]
            for row in player_board:
                for col, value in enumerate(row):
                    if value == num:
                        row[col] = 'X'
            
            is_bingo = bingo_check(player_board)

            if is_bingo == True:
                winning_cards.append(card)
                winning_number = int(num)

                if len(cards_without_bingo) > 1:
                    cards_without_bingo.remove(card)
                else:
                    last_card = True
            
            if last_card == True:
                break

        if last_card == True:
            break

    worst_card = cards_without_bingo[0]
    worst_card_marked = player_board

    return (worst_card, winning_number, worst_card_marked)    


def calc_unmarked(winning_cards_list, dict_of_boards, marked_boards_dict):
    for card in winning_cards_list:
        bingo_board = dict_of_boards[card]
        marked_board = marked_boards_dict[card]
        scores_dict = {}
        unmarked_sum = 0

        for row_index, row in enumerate(marked_board):
            for col_index, value in enumerate(row):
                if value != 'X':
                    unmarked_sum += int(bingo_board[row_index][col_index])
                else:
                    continue

        scores_dict[card] = unmarked_sum
    
    return scores_dict
    

def calc_total_score(unmarked_scores_dict, winning_number):
    total_score_dict = {}
    for card in unmarked_scores_dict.keys():
        total_score = unmarked_scores_dict[card] * winning_number
        total_score_dict[card] = total_score
    
    return total_score_dict


def main():
    numbers = "numbers_drawn.csv"
    boards = "boards.csv"

    bingo_boards = generate_boards(boards)
    bingo_numbers = get_nums(numbers)

    bingo_results = play_bingo(bingo_boards, bingo_numbers)
    winning_cards = bingo_results[0]
    winning_number = bingo_results[1]
    marked_boards = bingo_results[2]

    unmarked_scores = calc_unmarked(winning_cards, bingo_boards, marked_boards)
    total_scores = calc_total_score(unmarked_scores, winning_number)

    print("[--- B I N G O results ---]")
    print(f"winning number: {winning_number}")
    for card in total_scores.keys():
        card_score = total_scores[card]
        print(f"{card} → total score: {card_score}")
    
    worst_card_stats = play_losing_bingo(bingo_boards, bingo_numbers)
    worst_card = worst_card_stats[0]
    wc_winning_number = worst_card_stats[1]
    wc_marked = worst_card_stats[2]

    wc_unmarked_score = calc_unmarked([worst_card], bingo_boards, {worst_card: wc_marked})
    wc_total_score = calc_total_score(wc_unmarked_score , wc_winning_number)

    print('\n')
    print("[--- Play to L O S E ??? ---]")
    print("> choose the last card to win:")
    print(f"winning number: {wc_winning_number}")
    print(f"{worst_card} → total score: {wc_total_score[worst_card]}")

if __name__ == "__main__":
    main()