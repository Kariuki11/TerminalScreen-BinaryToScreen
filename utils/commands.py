def handle_command(byte, screen):
    """
    Handle a single byte command and execute the appropriate action.
    :param byte: Command byte
    :param screen: TerminalScreen instance
    """
    if byte == b"S":  # Screen Setup
        width, height, color_mode = 10, 5, 0  # Example dimensions
        screen.__init__(width, height, color_mode)

    elif byte == b"D":  # Draw Character
        x, y, char, color = 2, 3, "A", "red"  # Example parameters
        screen.draw_character(x, y, char, color)

    elif byte == b"T":  # Render Text
        x, y, text, color = 1, 1, "Hello", "green"
        for i, char in enumerate(text):
            screen.draw_character(x + i, y, char, color)

    elif byte == b"C":  # Clear Screen
        screen.clear_screen()

    elif byte == b"R":  # Render Screen
        screen.render()

    else:
        print(f"Unknown command: {byte}")
