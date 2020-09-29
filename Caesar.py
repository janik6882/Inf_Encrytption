# -*- coding: utf-8 -*-
__author__ = "Janik Klauenberg"
__copyright__ = "TBA"
__credits__ = ["Janik Klauenberg"]

__license__ = "None"
__version__ = "0.9"
__maintainer__ = "Janik Klauenberg (https://github.com/janik6882)"
__email__ = "support@klauenberg.eu"
__status__ = "V0.1"

from Tkinter import *
import sys
from sets import Set

# Basic Global Vars (Dict with Letter and Value, reversed and a string with
# all allowed charachters
normal_alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                   "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                   "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                   "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
crypt = {y:x for x,y in normal_alphabet.iteritems()}
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
    try:
        temp_var = int(num)
    except ValueError:
        print ("RTFM. Please read the manual")
        return
    inp = inp.lower()
    if not check_string(inp, allowed_chars):
        print ("RTFM. Please read the manual")
    pub = str()
    temp = list()
    for i in inp:
        temp.append(normal_alphabet[i])
    for i in range(len(temp)):
        tempo = temp[i]+num
        while tempo <=0:
            tempo+=26
        while tempo >26:
            tempo-=26
        temp[i]=tempo
    for i in temp:
        pub+=crypt[i]
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

    num-=2*num
    return encrypt(inp, num)



if __name__ == '__main__':
    # Set Gui to True if you want to use the Gui, set to False of not.
    # Startvars:
    Gui = False
    def get_e1_val():
        Label(root, text=v1.get()).grid(row=3)
    def TK_decrypt():
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
        decrypted = decrypt(inp, num)
        res.set(str(decrypted))
    def TK_encrypt():
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

    #Wenn sie die Gui nicht nutzen wollen setzen sie bitte laufen zu true
    laufend = not Gui
    while laufend:
        test1 = raw_input("wollen sie ver(1) oder entschluesseln(2) oder abbrechen(c):\n")
        if test1=="1":
            text1 = raw_input("ihr zu verschluesselnder text bitte:\n")
            num1 = int(raw_input("ihre verschiebung bitte:\n"))
            verschluesslt = "ihr verschluesselter text:\n{pub}"
            print verschluesslt.format(pub=encrypt(text1, num1))
        elif test1=="2":
            text2 = raw_input("ihr zu entschluesselnder text bitte:\n")
            num2 = int(raw_input("ihre verschiebung bitte:\n"))
            entschluesselt = "ihr entschluesselter text:\n{priv}"
            print entschluesselt.format(priv=decrypt(text2, num2))
        elif test1 == "c":
            sys.exit(0)
    if not laufend:
        root = Tk()
        v1 = StringVar()
        v2 = IntVar()
        res = StringVar()
        Label(root, text="input").grid(row=0)
        Label(root, text="verschiebung").grid(row=1, column=0)
        e1 = Entry(root, textvariable=v1).grid(row=0, column=1)
        e2 = Entry(root, textvariable=v2).grid(row=1, column=1)
        b1 = Button(text="encrypt", command=TK_encrypt).grid(row=2,column=0)
        b2 = Button(text="decrypt", command=TK_decrypt).grid(row=2, column=1)
        Label(root, text="Ergebnis: ").grid(row=3, column=0)
        x = Label(root, textvariable=res).grid(row=3, column=1)
        root.mainloop()
