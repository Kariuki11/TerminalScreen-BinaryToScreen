from screen import TerminalScreen
from parser import ByteStreamParser

def test_byte_stream_parser():
    # Initialize the screen
    screen = TerminalScreen(10, 5, 0)

    # Initialize the parser
    parser = ByteStreamParser(screen)

    # Test byte stream
    test_stream = [
        b"SETUP 20 10 0\n",
        b"DRAW 5 5 X red\n",
        b"DRAW 10 5 O green\n",
        b"RENDER\n",
        b"CLEAR\n",
        b"RENDER\n",
        b"TEXT 2 2 Hello World\n"
    ]

    # Parse the stream
    for data in test_stream:
        parser.parse_stream(data)

if __name__ == "__main__":
    test_byte_stream_parser()
