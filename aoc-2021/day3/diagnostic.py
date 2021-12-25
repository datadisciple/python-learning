filename = "report.txt"

with open(filename, 'r') as report:
    binary_list = report.read().splitlines()

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

if __name__ == "__main__":
    main()