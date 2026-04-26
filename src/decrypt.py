#!/usr/bin/env python3

import argparse
import base64

def decrypt(ciphertext):
    decoded_ciphertext = base64.b64decode(ciphertext).decode('utf-8')
    plaintext = ''
    for character in decoded_ciphertext:
        codepoint = ord(character)
        codepoint = (codepoint + 0x88000) % 0x110000
        plaintext += chr(codepoint)
    return plaintext

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='rot88.py', description='Encrypt or decrypt a message using rot88')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-o', '--outputfile', type=str)
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            ciphertext = file.read()
    else:
        ciphertext = args.message
    plaintext = decrypt(ciphertext)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(plaintext)
    else:
        print(plaintext, end='')
