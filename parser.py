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
        self.buffer = b''  # Temporary buffer to accumulate bytes

    def parse_stream(self, stream):
        """
        Reads a byte stream and executes the corresponding commands.
        :param stream: An iterable byte stream
        """
        for byte in stream:
            self.buffer += byte.to_bytes(1, 'big')  # Accumulate bytes in the buffer

            # Check if a complete command is in the buffer
            if self._is_complete_command(self.buffer):
                command = self._decode_command(self.buffer)
                handle_command(command, self.screen)
                self.buffer = b''  # Reset the buffer for the next command

    def _is_complete_command(self, buffer):
        """
        Determine if the buffer contains a complete command.
        This can be based on a specific delimiter (e.g., '\n') or command length.
        :param buffer: Accumulated bytes in the buffer
        :return: True if the command is complete, False otherwise
        """
        return b'\n' in buffer  # Example: Commands end with a newline byte

    def _decode_command(self, buffer):
        """
        Decode the bytes in the buffer into a readable command string.
        :param buffer: Accumulated bytes
        :return: Decoded command string
        """
        return buffer.decode('utf-8').strip()

















# from screen import TerminalScreen

# class CommandParser:
#     def __init__(self, screen):
#         """
#         Initializes the parser with a TerminalScreen instance.
#         :param screen: Instance of the TerminalScreen class.
#         """
#         self.screen = screen

#     def handle_command(self, command):
#         """
#         Parses and handles a single command.
#         :param command: Command string to parse.
#         """
#         parts = command.strip().split()
#         if not parts:
#             return

#         cmd = parts[0].upper()

#         if cmd == "SETUP":
#             # SETUP width height color_mode
#             if len(parts) != 4:
#                 print("Invalid SETUP command")
#                 return
#             width, height, color_mode = map(int, parts[1:])
#             self.screen.__init__(width, height, color_mode)
#             print(f"Screen initialized with {width}x{height}, color mode: {color_mode}")

#         elif cmd == "DRAW":
#             # DRAW x y char [color]
#             if len(parts) < 4:
#                 print("Invalid DRAW command")
#                 return
#             x, y = map(int, parts[1:3])
#             char = parts[3]
#             color = parts[4] if len(parts) == 5 else None
#             self.screen.draw_character(x, y, char, color)

#         elif cmd == "CLEAR":
#             # CLEAR
#             self.screen.clear_screen()
#             print("Screen cleared.")

#         elif cmd == "RENDER":
#             # RENDER
#             print("Rendering screen:")
#             self.screen.render()

#         elif cmd == "TEXT":
#             # TEXT x y text [color]
#             if len(parts) < 4:
#                 print("Invalid TEXT command")
#                 return
#             x, y = map(int, parts[1:3])
#             text = " ".join(parts[3:])
#             color = None
#             if text.startswith("[") and "]" in text:
#                 color = text[1:text.index("]")]
#                 text = text[text.index("]") + 1 :]
#             self.render_text(x, y, text, color)

#         else:
#             print(f"Unknown command: {cmd}")

#     def render_text(self, x, y, text, color=None):
#         """
#         Renders text starting at (x, y).
#         :param x: X-coordinate.
#         :param y: Y-coordinate.
#         :param text: Text to render.
#         :param color: Color of the text.
#         """
#         for i, char in enumerate(text):
#             self.screen.draw_character(x + i, y, char, color)

















