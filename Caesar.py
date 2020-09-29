# -*- coding: utf-8 -*-
__author__ = "Janik Klauenberg"
__copyright__ = "TBA"
__credits__ = ["Janik Klauenberg"]

__license__ = "None"
__version__ = "0.9"
__maintainer__ = "Janik Klauenberg (https://github.com/janik6882)"
__email__ = "support@klauenberg.eu"
__status__ = "V0.2"

# Tkinter for GUI, sys for exiting Program clean, sets for string check
from Tkinter import *
import sys
from sets import Set
# Basic Global Vars (Dict with Letter and Value, reversed and a string with
# all allowed charachters
normal_alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                   "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                   "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                   "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
crypt = {y: x for x, y in normal_alphabet.iteritems()}
allowed_chars = "abcdefghijklmnopqrstuvwxyz"


def encrypt(inp, num):
    """
    Comment: encrypts a string using the caesar method.
    Input: A Input String inp and a Integer num
    Output: A upper case result of the caesar algorithm
    Special: If used with neagtive num, it decrypts. Num can be any Integer
            Dont even think of using an non Integer Value as num!!
            Only use a/A-z/Z for the input string.
    """
    # checking input for validity (num a int, inp a valid string)
    try:
        int(num)
    except ValueError:
        print ("RTFM. Please read the manual")
        return "Fehler, keine Verarbeitung moeglich"
    inp = inp.lower()
    if not check_string(inp, allowed_chars):
        print ("RTFM. Please read the manual")
        return "Fehler, keine Verarbeitung moeglich"
    # validity checks ended, creating temporary vars for use in function
    pub = str()  # pub is the resulting string which will be returned
    vals = list()  # temporary List for storing the values of every char
    for i in inp:
        # looping through input, adding the value for each Letter to temp
        vals.append(normal_alphabet[i])
    for i in range(len(vals)):
        # Looping through vals, setting enc_val=vals[i]+num (encrypted Value)
        enc_val = vals[i]+num
        # Cleaning enc_val, correcting enc_val if bigger then 26 or smaller 0
        while enc_val <= 0:
            enc_val += 26
        while enc_val > 26:
            enc_val -= 26
        # Cleaning done, adding the letter to pub
        pub += crypt[enc_val]
    # returning the upper case result of pub
    return pub.upper()


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


def decrypt(inp, num):
    """
    Comment: decrypts a String(inp) using the caear algorithm
    Input: string inp and integer num
    Output:decrypted String
    Special: Uses encrypt() with negative integer for decryption. Further docu
            at encrypt()
    """
    num -= 2*num  # changing + to - before int and other way around
    return encrypt(inp, num)

def main():
    # Set Gui to True if you want to use the Gui, set to False of not.
    # Startvars:
    Gui = True

    def TK_decrypt():
        """
        Comment: calls decrypt() and runs the decryption for the input
        Input: Takes Input from TKinter Entry
        Output: Output to Tkinter label
        Special: Checks Input for validity
        """
        inp = v1.get()  # Gets current value for v1 entry widget
        try:
            num = int(v2.get())  # checks if num is a number
        except ValueError:
            res.set("""Witzig, bitte nutze eine Nicht komma zahl.\n
                       Naechstes Mal Bedienungsanleitung lesen!!""")
            return
        except Exception as e:
            res.set("Etwas lief schief, bitte pruefe deine Eingabe")
            print e
            return
        decrypted = decrypt(inp, num)
        res.set(str(decrypted))

    def TK_encrypt():
        """
        Comment: calls encrypt() and encrypts input from TKinter entry widget
        Input: takes input from Tktiner Entry
        Output: Output to Tkinter Label
        Special: Checks input for validity
        """

        inp = v1.get()
        try:
            num = int(v2.get())
        except ValueError:
            res.set("""Witzig, bitte nutze eine Nicht komma zahl.\n
             Naechstes Mal Bedienungsanleitung lesen!!""")
            return
        except Exception as e:
            res.set("Etwas lief schief, bitte pruefe deine Eingabe")
            print e
            return
        encrypted = encrypt(inp, num)
        res.set(str(encrypted))

    laufend = not Gui
    while laufend:
        test1 = raw_input("""wollen sie ver(1) oder entschluesseln(2) oder
                          abbrechen(c):\n""")
        if test1 == "1":
            text1 = raw_input("ihr zu verschluesselnder text bitte:\n")
            num1 = raw_input("ihre verschiebung bitte:\n")
            try:
                num1 = int(num1)
                verschluesslt = "ihr verschluesselter text:\n{pub}"
                print verschluesslt.format(pub=encrypt(text1, num1))
            except ValueError:
                print ("Fahlerhafte Eingabe, bitte erneut versuchen")
        elif test1 == "2":
            text2 = raw_input("ihr zu entschluesselnder text bitte:\n")
            num2 = raw_input("ihre verschiebung bitte:\n")
            try:
                num2 = int(num2)
                entschluesselt = "ihr entschluesselter text:\n{priv}"
                print entschluesselt.format(priv=decrypt(text2, num2))
            except ValueError:
                print ("Fehlerhafte eingabe, bitte erneut versuchen")
        elif test1 == "c":
            sys.exit(0)
    if not laufend:
        root = Tk()
        v1 = StringVar()
        v2 = IntVar()
        res = StringVar()
        Label(root, text="input").grid(row=0)
        Label(root, text="verschiebung").grid(row=1, column=0)
        Entry(root, textvariable=v1).grid(row=0, column=1)
        Entry(root, textvariable=v2).grid(row=1, column=1)
        Button(text="encrypt", command=TK_encrypt).grid(row=2, column=0)
        Button(text="decrypt", command=TK_decrypt).grid(row=2, column=1)
        Label(root, text="Ergebnis: ").grid(row=3, column=0)
        Label(root, textvariable=res).grid(row=3, column=1)
        root.mainloop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        sys.exit()
