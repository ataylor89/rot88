#!/usr/bin/env python3

import argparse
import base64

def encrypt(plaintext):
    ciphertext = ''
    for character in plaintext:
        codepoint = ord(character)
        codepoint = (codepoint + 0x88000) % 0x110000
        ciphertext += chr(codepoint)
    bytearr = ciphertext.encode('utf-8')
    encoded_ciphertext = base64.b64encode(bytearr).decode('utf-8')
    return encoded_ciphertext

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='rot88.py', description='Encrypt or decrypt a message using rot88')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-o', '--outputfile', type=str)
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            plaintext = file.read()
    else:
        plaintext = args.message
    ciphertext = encrypt(plaintext)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(ciphertext)
    else:
        print(ciphertext, end='')
