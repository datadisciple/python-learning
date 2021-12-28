def num_increase(list_of_nums):
    counter = 0

    for index, num in enumerate(list_of_nums):
        if index == 0:
            prev_num = num
        else:
            if num > prev_num:
                counter += 1
            prev_num = num

    return counter
 
def sliding_window(list_of_nums, window_size):
     num_in_group = 0
     windows = []
     sum = 0
     index = 0

     while index < len(list_of_nums):
         sum += list_of_nums[index]
         num_in_group += 1
         index += 1
         
         if num_in_group == window_size:
             windows.append(sum)
             num_in_group = 0
             sum = 0
             index = index - window_size + 1
    
     return windows
         
def main():
    filename = "depth-measurements.txt"

    with open(filename, 'r') as depths:
        measurements = depths.read().splitlines()
    
    int_measurements = [ int(measurements[0]) ]

    for string_val in measurements[1:]:
        int_measurements.append(int(string_val))
    
    answer_pt1 = num_increase(int_measurements)
    print(f"there are {answer_pt1} measurements that are larger than the previous measurement")

    window_size = 3
    answer_pt2 = num_increase(sliding_window(int_measurements, window_size))
    print(f"using a {window_size}-measurment sliding window, {answer_pt2} sums are larger than their previous sum")

if __name__ == "__main__":
    main()