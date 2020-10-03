# -*- coding: utf-8 -*-
__author__ = "Janik Klauenberg"
__copyright__ = "TBA"
__credits__ = ["Janik Klauenberg"]

__license__ = "None"
__version__ = "0.9"
__maintainer__ = "Janik Klauenberg (https://github.com/janik6882)"
__email__ = "support@klauenberg.eu"
__status__ = "V0.2"

import sys


normal_alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                   "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                   "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                   "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
crypt = {y: x for x, y in normal_alphabet.items()}
allowed_chars = "abcdefghijklmnopqrstuvwxyz"


def encrypt(enc_str, key_str):
    enc_str = enc_str.lower()
    key_str = key_str.lower()
    pub = str()
    vals_pub = list()
    vals_enc = list()
    vals_key = list()
    # TBA replace dict with ord()/chr()
    for i in enc_str:
        vals_enc.append(ord(i))
    for i in key_str:
        vals_key.append(ord(i))
    if len(vals_enc)>len(vals_key):
        vals_key = vals_key * int(round((len(vals_enc)/float(len(vals_key)))+0.49))
    for i in range(len(enc_str)):
        vals_pub.append(int(vals_key[i]+vals_enc[i]))
    for i in range(len(vals_pub)):
        val = vals_pub[i]
        #while val <= 0:
        #    val+=26
        #while val>26:
        #    val-=26
        pub+=chr(i)
    return pub

def decrypt(dec_str, key_str):
    dec_str = dec_str.lower()
    key_str = key_str.lower()
    pub= str()
    vals_pub = list()
    vals_dec = list()
    vals_key = list()
    for i in dec_str:
        vals_dec.append(ord(i))
        print ord(i)
    for i in key_str:
        vals_key.append(ord(i))
        print vals_key
    if len(vals_dec)>len(vals_key):
        vals_key = vals_key * int(round((len(vals_dec)/float(len(vals_key)))+0.49))
    for i in range(len(vals_dec)):
        vals_pub.append(int(vals_dec[i]-vals_key[i]))
    print vals_pub
    for i in range(len(vals_pub)):
        val = vals_pub[i]
        while val <= 0:
            val+=255
        while val>255:
            val-=255
        pub+=chr(i)
        print vals_pub
    return pub

def check_string(to_test, allowed):
    """
    Comment: checks if a string only contains valid charachters
    Input: a string to be tested and a string with allowed characters
    Output: Bool
    Special: Nothing special
    """
    if Set(to_test).issubset(Set(allowed)):
        return True
    else:
        return False


x = decrypt("abc", "a")

print encrypt(x, "ab")
