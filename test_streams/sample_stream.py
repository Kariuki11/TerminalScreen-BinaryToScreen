# Sample test byte stream simulating incoming data
test_stream = [
    b"SETUP 20 10 0\n",  # Set up the screen with dimensions and color mode
    b"DRAW 5 5 X red\n",  # Draw 'X' at (5, 5) in red color
    b"DRAW 10 5 O green\n",  # Draw 'O' at (10, 5) in green color
    b"RENDER\n",  # Render the screen to display the content
    b"CLEAR\n",  # Clear the screen
    b"RENDER\n",  # Render the screen again to show it cleared
    b"TEXT 2 2 Hello World\n"  # Render "Hello World" starting at (2, 2)
]
