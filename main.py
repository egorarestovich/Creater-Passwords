from random import *
def generatePassword(chars, length):
    password = ''
    if(len(chars) != 0):
        for i in range(length):
            randomchar = randint(0, len(chars) - 1)
            password += chars[randomchar]
    elif(length != 0):
        return "Password generation is not possible"
    return password

letters = "abcdefghijklmnopqrstuvwxyz"
bigLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&+-=?@^_"
NANSymbols = "il1Lo0O"
chars = ''
print("Введите сколько поролей вы хотите создать")
countPaswords = int(input())
print("Enter 1 if you want to add small letters of the English alphabet to your password, and 0 if you do not want")
l = int(input())
print("Enter 1 if you want to add capital letters of the English alphabet to your password, and 0 if you do not want")
bl = int(input())
print("Enter 1 if you want to add numbers to your password, and 0 if you do not want to.")
n = int(input())
print("Enter 1 if you want to add special characters to your password (!#$%&+-=?@^_), and 0 if you do not want")
s = int(input())
print("Enter 1 if you want to add ambiguous characters (il1Lo0O) to the password, and 0 if you do not want")
ns = int(input())
if(l == 1):
    chars += letters
if(bl == 1):
    chars += bigLetters
if(n == 1):
    chars += numbers
if(s == 1):
    chars += symbols
if(ns == 1):
    chars += NANSymbols
print("Enter the length of the passwords")
length = int(input())
for i in range(countPaswords):
    print(generatePassword(chars, length))

#This code work at Console