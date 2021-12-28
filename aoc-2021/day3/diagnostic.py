def calc_gamma(list_of_codes):
    total_chars = len(list_of_codes[0])
    index_val = []

    for char in range(total_chars):
        index_val.append(0)

    for code in list_of_codes:
        for position, char in enumerate(code):
            if char == '1':
                index_val[position] += 1
            else:
                index_val[position] -= 1
    
    master_code = []

    for index, val in enumerate(index_val):
        if val > 0:
            master_code.append('1')
        elif val == 0:
            raise Exception(f"equal number of '0' and '1' for all codes at index = {index}; no value dominates, unable to parse a master code")
        else:
            master_code.append('0')
    
    gamma_rate = ''
    gamma_rate = gamma_rate.join(master_code)

    return gamma_rate


def calc_epsilon(gamma_rate):
    epsilon_rate = gamma_rate.replace('1', 'X').replace('0', '1').replace('X', '0')

    return epsilon_rate


def calc_rating(list_of_codes, rating_type = 'o2'):
    rating_code = [list_of_codes[i] for i in range(len(list_of_codes))]
        # initialize new list based of the values in list passed in
        # without doing this, the original list will be overwritten bc of pop() — (function would only work correctly the first time it is called)
    total_chars = len(list_of_codes[0])

    for position in range(total_chars):
        most_common = 0

        for code in rating_code:
            char = code[position]            
            if char == '1':
                most_common += 1
            else:
                most_common -= 1
        
        if rating_type == 'o2':

            if most_common > 0: criteria = '1'
            elif most_common == 0: criteria = '1'
            else: criteria = '0'

        elif rating_type == 'co2':

            if most_common > 0: criteria = '0'
            elif most_common == 0: criteria = '0'
            else: criteria = '1'
        
        else:
            raise Exception(f"incorrect rating_type; accepted_value: 'o2' or 'co2'")

        index = 0

        while len(rating_code) > 1 and index < len(rating_code):
            code = rating_code[index]
            char = code[position]

            if char != criteria:
                rating_code.pop(index)
            else:
                index += 1

    rating = ''
    rating = rating.join(rating_code)    
    
    return rating


def main():
    filename = "report.txt"

    with open(filename, 'r') as report:
        binary_list = report.read().splitlines()

    gamma_rate = calc_gamma(binary_list)
    gmag = int(gamma_rate, 2)
    epsilon_rate = calc_epsilon(gamma_rate)
    emag = int(epsilon_rate, 2)
    consumption = gmag * emag

    print(f"gamma rate: {gamma_rate} = {gmag}")
    print(f"epsilon rate: {epsilon_rate} = {emag}")
    print(f"total power consumption: {consumption}")

    o2_rating = calc_rating(binary_list)
    o2_val = int(o2_rating, 2)
    co2_rating = calc_rating(binary_list, 'co2')
    co2_val = int(co2_rating, 2)

    life_rating = o2_val * co2_val

    print(f"o2_rating: {o2_rating} = {o2_val}")
    print(f"co2_rating: {co2_rating} = {co2_val}")
    print(f"life rating = {life_rating}")   


if __name__ == "__main__":
    main()