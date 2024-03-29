import pygame

display_width = 1200
display_height = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
bg_location = 'bg.png'
bg_location = pygame.transform.smoothscale(bg_location,[640,480])

pygame.init()

class Button(object):
	def __init__(self, text, color, x=None, y=None, **kwargs):
		self.surface = font.render(text, True, color)

		self.WIDTH = self.surface.get_width()
		self.HEIGHT = self.surface.get_height()

		if 'centered_x' in kwargs and kwargs['centered_x']:
			self.x = display_width // 2 - self.WIDTH // 2
		else:
			self.x = x

		if 'centered_y' in kwargs and kwargs['cenntered_y']:
			self.y = display_height // 2 - self.HEIGHT // 2
		else:
			self.y = y

	def display(self):
		screen.blit(self.surface, (self.x, self.y))

	def check_click(self, position):
		x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
		y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

		if x_match and y_match:
			return True
		else:
			return False


def starting_screen():
    screen.blit(bg, (0, 0))

    game_title = font.render('Starting Screen', True, WHITE)

    screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))

    play_button = Button('Play', RED, None, 350, centered_x=True)
    exit_button = Button('Exit', WHITE, None, 400, centered_x=True)

    play_button.display()
    exit_button.display()

    pygame.display.update()

    while True:

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Play', RED, None, 350, centered_x=True)
        else:
            play_button = Button('Play', WHITE, None, 350, centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Exit', RED, None, 400, centered_x=True)
        else:
            exit_button = Button('Exit', WHITE, None, 400, centered_x=True)

        play_button.display()
        exit_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                break
            if exit_button.check_click(pygame.mouse.get_pos()):
                break



screen = pygame.display.set_mode((display_width, display_height))
bg = pygame.image.load(bg_location)
font_addr = pygame.font.get_default_font()
font = pygame.font.Font(font_addr, 36)

starting_screen()