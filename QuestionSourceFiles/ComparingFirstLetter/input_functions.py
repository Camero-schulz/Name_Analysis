#!/usr/bin/env python3

try:
    import tty
    import sys
    import termios
except:
    print("tty, sys, and termios are required to run key_input")

# key_input:
# takes in list of character that are accepted, returns the character input or -1 if it fails
# known bugs: 1. removes backspace functionality from future text inputs
def key_input(in_options): #created by Joe Mather, 1231960
    try:
        error_response = 0
        tty.setcbreak(sys.stdin) #makes it so that the terminal takes in a single input at a time and doesn't echo it
        error_response = 1
        while True:
            key = sys.stdin.read(1)  #reads a single keypress
            if key in in_options:
                print(key)

                #https://stackoverflow.com/questions/8757915/how-to-turn-console-echo-back-on-after-tty-setcbreak
                fd = sys.stdin.fileno() #returns file desciptor as fd
                old = termios.tcgetattr(fd) #returns list of all fd attributes 
                old[3] = old[3] | termios.ECHO
                termios.tcsetattr(fd, termios.TCSADRAIN, old) #makes it so that future input is echoed in the terminal
                return key
    except:
        if (error_response == 1): #only runs if the code this is reversing runs
            try:
                fd = sys.stdin.fileno()
                old = termios.tcgetattr(fd)
                old[3] = old[3] | termios.ECHO
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            except:
                print("Error: could not access libraries required for key_input")
        return -1