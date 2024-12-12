from screen import TerminalScreen
from parser import ByteStreamParser

def main():
    """
    Main logic to set up the screen, handle commands, and test functionality.
    """
    # Initialize the screen (10x5 in monochrome mode for this test)
    screen = TerminalScreen(10, 5, 0)

    # Initialize the parser with the screen
    parser = ByteStreamParser(screen)

    # Example byte stream representing a sequence of commands
    # S: Screen setup, D: Draw character, T: Render text, C: Clear screen, R: Render screen
    command_stream = [
        b"S",  # Initialize screen (optional if already initialized in TerminalScreen)
        b"D",  # Draw character (e.g., A at 2,3 in red)
        b"T",  # Render text (e.g., "Hello" starting at 1,1 in green)
        b"C",  # Clear the screen
        b"R"   # Render the screen
    ]

    print("Executing commands from byte stream:")
    parser.parse_stream(command_stream)

if __name__ == "__main__":
    main()







# from screen import TerminalScreen

# def main():
#     """
#     Main logic to set up the screen and test basic functionality.
#     """
#     # Initialize the screen (10x5 in monochrome mode for this test)
#     screen = TerminalScreen(10, 5, 0)

#     # Draw some characters
#     screen.draw_character(2, 3, "A", "red")
#     screen.draw_character(5, 1, "B", "green")

#     # Render the screen
#     print("Initial screen state:")
#     screen.render()

#     # Clear the screen and re-render
#     screen.clear_screen()
#     print("\nScreen after clearing:")
#     screen.render()

#     # Draw some additional characters after clearing
#     screen.draw_character(4, 2, "C", "blue")
#     screen.draw_character(6, 4, "D", "yellow")
#     print("\nScreen with new characters:")
#     screen.render()


# if __name__ == "__main__":
#     main()
