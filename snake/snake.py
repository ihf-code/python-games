import pygame, random

class Snake:

    # Size of the each block in pixels
    block_size = 30

    # Size of the grid to use will be 30 x 30 etc
    grid_size = 20

    bg_color = pygame.Color("black")
    snake_color = pygame.Color("white")
    food_color = pygame.Color("green")

    # The different (x, y) velocities for each direction
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    # The different key presses and the velocity changes
    KEY_PRESSES = {
        pygame.K_LEFT: LEFT,
        pygame.K_RIGHT: RIGHT,
        pygame.K_UP: UP,
        pygame.K_DOWN: DOWN,
    }

    def __init__(self):
        # Set defaults - with random starting grid and direction of velocity
        self.screen = None
        self.body = [(random.randint(1, self.grid_size), random.randint(1, self.grid_size))]
        self.food = self.generate_food_position()
        self.velocity = random.choice(list(self.KEY_PRESSES.values()))

        # Work out the sie of the scren based on the block and grid size
        self.screen_width = self.block_size * self.grid_size
        self.screen_height = self.block_size * self.grid_size

        # The different states of the app
        self.is_running = True
        self.in_game = True

        # Run the game
        self.run()

    def run(self):
        # Init pygame and show the window and first view of the snake/food
        pygame.init()
        self.show_window()
        self.display()

        # Get a clock so we can measure the speed of the CPU
        clock = pygame.time.Clock()

        while self.is_running:
            # Set the clock speed for how fast he game runs
            clock.tick(15)

            # Only update if we are in game mode
            if self.in_game:
                self.update()

            # Handle key presses and quiting the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.key_press(event.key)
                elif event.type == pygame.QUIT:
                    self.is_running = False

    def show_window(self):
        # Set window title bar
        pygame.display.set_caption("Snake")

        # Set the size of the window
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Fill screen with black
        self.screen.fill(self.bg_color)

    def key_press(self, keypress):
        # If keypress is valid (up/down/left/right) - change the velocity
        if keypress in self.KEY_PRESSES:
            self.change_velocity(self.KEY_PRESSES[keypress])

    def generate_food_position(self):
        # Set the food to be within the snake so we run the while loop at least once
        food = self.body[0]
        while food in self.body:
            # Generate random position for the food on the grid
            food = (random.randint(1, self.grid_size), random.randint(1, self.grid_size))

        return food

    def can_change_velocity(self, velocity):
        # You can change any direction if you are only 1 block in size
        if len(self.body) == 1:
            return True

        # You cant go back on yourself if you are longer than 1 block
        if (self.velocity == self.LEFT and velocity == self.RIGHT) or \
        (self.velocity == self.RIGHT and velocity == self.LEFT) or \
        (self.velocity == self.UP and velocity == self.DOWN) or \
        (self.velocity == self.DOWN and velocity == self.UP):
            return False

        return True

    def change_velocity(self, velocity):
        # Check to make sure the velocity change is valid
        if self.can_change_velocity(velocity):
            self.velocity = velocity

    def get_block_position(self, block):
        # This is for the top left of the block on our grid
        # If block size is 30px:
        # (1,1) is (0, 0)
        # (2, 2) is (30, 30)
        # (5, 2) is (120, 30)
        x = (block[0] - 1) * self.block_size
        y = (block[1] - 1) * self.block_size
        return (x, y)

    def draw_block(self, block, color):
        # Get the top left position of the block to draw
        position = self.get_block_position(block)

        # Draw the square block
        pygame.draw.rect(self.screen, color, pygame.Rect(position, (self.block_size, self.block_size)))

    def draw_snake(self):
        # Loop through each block in the snake body and draw it
        for block in self.body:
            self.draw_block(block, self.snake_color)

    def draw_food(self):
        # Draw the food as a single block
        self.draw_block(self.food, self.food_color)

    def draw_score(self):
        # Set background to red
        self.screen.fill(pygame.Color("red"))

        # Overlay the snake and food
        self.draw_snake()
        self.draw_food()

        # Show the users score over the top
        font = pygame.font.Font('freesansbold.ttf', 120)
        text = font.render(str(len(self.body)), True, self.bg_color)
        textRect = text.get_rect()
        textRect.center = (self.screen_width // 2, self.screen_height // 2)
        self.screen.blit(text, textRect)

    def display(self):
        # Draw the whole snake
        self.draw_snake()

        # Draw the food
        self.draw_food()

        # If game has ended show draw the score
        if not self.in_game:
            self.draw_score()

        # Flip the display to show the new content we just drew
        pygame.display.flip()

    def update(self):
        # Get the updated the position of the head of the snake given the velocity
        # If you move off the edge of the screen you will wrap back around to the other side
        x = self.body[0][0] + self.velocity[0]
        if x > self.grid_size:
            x = 1
        elif x < 1:
            x = self.grid_size
        y = self.body[0][1] + self.velocity[1]
        if y > self.grid_size:
            y = 1
        elif y < 1:
            y = self.grid_size

        first_block = (x, y)

        # Insert the new position of the head of the snake
        self.body.insert(0, first_block)

        # Check to see if we have just eaten the food - if we have we dont remove the last block of the snake so it grows
        if first_block == self.food:
            # Set a new position for the food
            self.food = self.generate_food_position()
        else:
            # Remove the last block of the body to appear as if the whole snake moved
            removed_block = self.body.pop()

            # Draw over the position of the removed block to make it match the background colour
            self.draw_block(removed_block, self.bg_color)

        # Check for collisions - the first block has already been added - so dont check that part of the body
        if first_block in self.body[1:]:
            self.in_game = False

        # Display the updates to our snake
        self.display()

# Init the Snake object and run the game
snake = Snake()
