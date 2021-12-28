def parse_command(command_list):
    navigation = []
    for command in command_list:
        parser = command.split(" ")
        direction = parser[0]
        position = int(parser[1])
        navigation.append([direction, position])
    
    return navigation

def navigate_course(navigation_list):
    x_pos = 0
    depth = 0
    aim = 0
    for direction, magnitude in navigation_list:
        if direction == 'forward':
            x_pos += magnitude
            depth += (aim*magnitude)
        elif direction == 'up':
            aim -= magnitude
        elif direction == 'down':
            aim += magnitude

    return(x_pos, depth)

def main():
    filename = "planned-course.txt"

    with open(filename, 'r') as course:
        commands = course.read().splitlines()

    navigation_list = parse_command(commands)
    final_position = navigate_course(navigation_list)
    print(f"(horizontal, depth): {final_position}")
    print(f"product of coordinates: {final_position[0] * final_position[1]}")

if __name__ == "__main__":
    main()