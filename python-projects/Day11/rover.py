class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.directions = ['N', 'E', 'S', 'W']

    def turn_left(self):
        self.direction = self.directions[(
            self.directions.index(self.direction) - 1) % 4]

    def turn_right(self):
        self.direction = self.directions[(
            self.directions.index(self.direction) + 1) % 4]

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def execute_commands(self, commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move_forward()
            else:
                print(f"Invalid command: {command}")

    def get_position(self):
        return self.x, self.y, self.direction


# Test the Rover class
rover = Rover(0, 0, 'N')
commands = "MMRMMRMRRM"
rover.execute_commands(commands)
print(rover.get_position())
