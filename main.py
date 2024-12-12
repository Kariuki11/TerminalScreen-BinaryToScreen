from screen import TerminalScreen

def main():
    """
    Main logic to set up the screen and test basic functionality.
    """
    # Initialize the screen (10x5 in monochrome mode for this test)
    screen = TerminalScreen(10, 5, 0)

    # Draw some characters
    screen.draw_character(2, 3, "A", "red")
    screen.draw_character(5, 1, "B", "green")

    # Render the screen
    print("Initial screen state:")
    screen.render()

    # Clear the screen and re-render
    screen.clear_screen()
    print("\nScreen after clearing:")
    screen.render()

    # Draw some additional characters after clearing
    screen.draw_character(4, 2, "C", "blue")
    screen.draw_character(6, 4, "D", "yellow")
    print("\nScreen with new characters:")
    screen.render()


if __name__ == "__main__":
    main()
