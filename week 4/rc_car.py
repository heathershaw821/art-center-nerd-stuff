import pygame

pygame.init()
pygame.joystick.init()

# Check for connected joysticks
joystick_count = pygame.joystick.get_count()
print(f"Number of joysticks detected: {joystick_count}")

if joystick_count == 0:
    print("No joysticks found. Please connect a joystick.")
    exit(-1)

# Get the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Joystick name: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

# Set up the display (optional, for visual feedback)
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Joystick Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            # Handle axis motion (e.g., analog sticks)
            print(f"Axis {event.axis} moved to {event.value:.2f}")
        elif event.type == pygame.JOYBUTTONDOWN:
            # Handle button presses
            print(f"Button {event.button} pressed")
        elif event.type == pygame.JOYBUTTONUP:
            # Handle button releases
            print(f"Button {event.button} released")
        elif event.type == pygame.JOYHATMOTION:
            # Handle hat (D-pad) movement
            print(f"Hat {event.hat} moved to {event.value}")

    # Basic screen update (optional)
    screen.fill((0, 0, 0)) # Black background
    pygame.display.flip()

pygame.quit()
