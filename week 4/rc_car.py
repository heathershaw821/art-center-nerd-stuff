import pygame

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks found.")
    exit(-1)
else:
    # Assuming the first detected joystick is the Xbox controller
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controller connected: {joystick.get_name()}")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed.")
            # Map button numbers to Xbox button names (e.g., A=0, B=1, X=2, Y=3)
        elif event.type == pygame.JOYAXISMOTION:
            # Axis values range from -1.0 to 1.0
            # Left stick X: event.axis == 0
            # Left stick Y: event.axis == 1
            # Right stick X: event.axis == 4
            # Right stick Y: event.axis == 3
            # Triggers (combined): event.axis == 2 (RT positive, LT negative)
            print(f"Axis {event.axis} moved to {event.value:.2f}")
            # Implement deadzone for analog sticks to prevent drift
            if abs(event.value) < 0.05: # Example deadzone
                pass
        elif event.type == pygame.JOYHATMOTION:
            # D-pad: event.value is a tuple (x, y) with -1, 0, or 1
            print(f"Hat {event.hat} moved to {event.value}")

    # You can also poll the joystick state directly outside the event loop
    # For example, to get current left stick position:
    # left_stick_x = joystick.get_axis(0)
    # left_stick_y = joystick.get_axis(1)
