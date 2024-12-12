from utils.commands import handle_command

class ByteStreamParser:
    """
    Parses a byte stream and handles commands for the terminal screen.
    """

    def __init__(self, screen):
        """
        Initialize the parser with a reference to the screen object.
        :param screen: TerminalScreen instance
        """
        self.screen = screen

    def parse_stream(self, stream):
        """
        Reads a byte stream and executes the corresponding commands.
        :param stream: An iterable byte stream
        """
        for byte in stream:
            handle_command(byte, self.screen)