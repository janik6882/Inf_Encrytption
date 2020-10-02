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
from sets import Set


normal_alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                   "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                   "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                   "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
                   " ": 27, "1": 28, "2": 29, "3": 30, "4": 31, "5": 32,
                   "6": 33, "7": 34, "8": 35, "9": 36, "ä": 37, "ö": 38,
                   "ü": 39,
#                   "$": 39, "%": 40, "&": 41, "/": 42, "(": 43, ")": 44,
#                   "=": 45, "?": 46, "´": 47, "`": 48, "{": 49, "[": 50,
#                   "]": 51, "}": 52, "^": 53, "°": 54, "@": 55, "€": 56,
#                   "*": 57, "+": 58, "~": 59, "'": 60, "#": 61, ">": 62,
#                   "<": 63, "|": 64, ",": 65, ";": 66, ".": 67, ":": 68,
#                   "-": 69, "_": 70,
#                   "ö": 39, "ä": 40, "ü": 41
                   }
crypt = {y: x for x, y in normal_alphabet.iteritems()}
allowed_chars = "".join(list(normal_alphabet.keys()))
len_alpphabet = len(normal_alphabet)
print len_alpphabet

def encrypt(enc_str, key_str):
    enc_str = enc_str.lower()
    key_str = key_str.lower()
    pub = str()
    vals_pub = list()
    vals_enc = list()
    vals_key = list()
    # TBA replace dict with ord()/chr()
    for i in enc_str:
        vals_enc.append(normal_alphabet[i])
    for i in key_str:
        vals_key.append(normal_alphabet[i])
    if len(vals_enc)>len(vals_key):
        vals_key = vals_key * int(round((len(vals_enc)/float(len(vals_key)))+0.49))
    for i in range(len(enc_str)):
        vals_pub.append(int(vals_key[i]+vals_enc[i]))
    print vals_pub
    for i in range(len(vals_pub)):
        val = vals_pub[i]
        while val <= 0:
            val += len_alpphabet
        while val > len_alpphabet:
            val -= len_alpphabet
        print crypt[val]
        pub += crypt[val]
    return pub


def decrypt(dec_str, key_str):
    dec_str = dec_str.lower()
    key_str = key_str.lower()
    pub = str()
    vals_pub = list()
    vals_dec = list()
    vals_key = list()
    for i in dec_str:
        vals_dec.append(normal_alphabet[i])
    for i in key_str:
        vals_key.append(normal_alphabet[i])
    if len(vals_dec) > len(vals_key):
        vals_key = vals_key * int(round((len(vals_dec) / float(len(vals_key))) + 0.49))
    for i in range(len(vals_dec)):
        vals_pub.append(int(vals_dec[i]-vals_key[i]))
    for i in range(len(vals_pub)):
        val = vals_pub[i]
        while val <= 0:
            val += len_alpphabet
        while val > len_alpphabet:
            val -= len_alpphabet
        pub += crypt[val]
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


print (decrypt("xyz", "ab"))
x = encrypt("xyz", "ab")
print decrypt(x, "ab")
