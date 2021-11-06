#!/usr/bin/env python3

import constant


def main():
    text = input('Please enter a single-variable function: ')
    lex_scan(text)


def lex_scan(text):
    print('Input Function: ', text)
    cp = 0 # Pointer to current character
    sp = 0 # Token-start pointer
    cc = '' # Current character
    token = '' # I.e, a character string
    lex_state = 0 # Current state of the DFA

    while cp <= len(text):
        cc = text[cp]  # Get next input character
        col = 0 # alphabetical

        if constant.DIGITS.find(cc) > 0:
            col = 1    # numeric
        elif cc == ' ':
            col = 2 # space
        else:
            col = 3 # punctuation mark

        lex_state = constant.STATE_TABLE[lex_state][col] # change state

        if lex_state == 2:
            token = text[sp:cp-sp]



if __name__ == '__main__':
    main()