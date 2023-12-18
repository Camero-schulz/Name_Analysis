#!/usr/bin/env python3
errorCheck = 0
try:
    import tty
    import sys
    import termios
except:
    errorCheck = 1
    print("tty, sys, and termios are required to run key_input")

# key_input:
# takes in list of character that are accepted, returns the character input or -1 if it fails
# known bugs: 1. removes backspace functionality from future text inputs
#created by Joe Mather, 1231960
def key_input(in_options):
    if errorCheck != 1:
        try:
            original_settings = termios.tcgetattr(sys.stdin)
            error_response = 0
            tty.setcbreak(sys.stdin) #makes it so that the terminal takes in a single input at a time and doesn't echo it
            error_response = 1
            while True:
                key = sys.stdin.read(1)  #reads a single keypress
                if key in in_options:
                    print(key)

                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)

                    return key
        except:
            if (error_response == 1): #only runs if the code this is reversing runs
                try:
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)
                except:
                    print("Error: could not access libraries required for key_input")
            return -1