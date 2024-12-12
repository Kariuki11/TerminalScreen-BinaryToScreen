class TerminalScreen:
    def __init__(self, width, height, color_mode):
        """
        Initializes the screen with the given dimensions and color mode.

        :param width: Number of columns (characters).
        :param height: Number of rows (characters).
        :param color_mode: Color mode (e.g., 0 for monochrome).
        """
        self.width = width
        self.height = height
        self.color_mode = color_mode
        self.screen = [[(" ", None) for _ in range(width)] for _ in range(height)]

    def draw_character(self, x, y, char, color=None):
        """
        Draws a character at the specified coordinates.
        :param x: X-coordinate (column).
        :param y: Y-coordinate (row).
        :param char: Character to draw.
        :param color: Color of the character (optional).
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.screen[y][x] = (char, color)

    def clear_screen(self):
        """
        Clears the screen by resetting all cells to the default.
        """
        self.screen = [[(" ", None) for _ in range(self.width)] for _ in range(self.height)]

    def render(self):
        """
        Renders the screen to the terminal.
        """
        from rich.console import Console
        from rich.text import Text

        console = Console()
        for row in self.screen:
            line = Text()
            for char, color in row:
                line.append(char, style=color if color else "")
            console.print(line)

# Example usage:
if __name__ == "__main__":
    screen = TerminalScreen(10, 5, 0)  # 10x5 monochrome screen
    screen.draw_character(2, 3, "A", "red")
    screen.draw_character(5, 1, "B", "green")
    screen.render()