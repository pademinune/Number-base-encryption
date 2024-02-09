
import math


def IsNum(char):
  try:
    char = int(char)
    return True
  except ValueError:
    return False

def ChangeToBase10(num,base):
  current = 0
  num = str(num)
  powers = [base**int(i) for i in range(len(num))][::-1]
  for index in range(len(num)):
    currentDigit = num[index]
    currentPower = powers[index]
    if IsNum(currentDigit):
      current+=int(currentDigit)*currentPower
    else:
      current += Letters[currentDigit]*currentPower
  return current

def ChangeFromBase10(num,base):
  current = ""
  remaining = num
  # strnum = str(num)
  powers = [base**i for i in range(int(math.log(num,base))+1)][::-1]
  for i in range(len(powers)):
    # digit = strnum[i]
    power = powers[i]
    fits = int(remaining/(power))
    remaining -= fits*power
    if fits < 10:
      current += str(fits)
    else:
      current += Digits[fits]
  return current

def ChangeToAnyBase(num1,base1,base2):
  return ChangeFromBase10(ChangeToBase10(num1,base1),base2)

ASCII = {32:" ",33:"!",35:"#",36:"$",37:"%",39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.',47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~'}

def ConvertBytes(string):
  converted = []
  Sentence = ""
  for byte in string.split():
    converted.append(ChangeToBase10(int(byte),2))
    Sentence += ASCII[ChangeToBase10(int(byte),2)]
  return converted,Sentence

def ConvertSevens(string):
  converted = []
  Sentence = ""
  for Seven in string.split():
    converted.append(ChangeToBase10(Seven,7))
    Sentence += ASCII[ChangeToBase10(Seven,7)]
  return Sentence

def EncryptSevens(string):
  converted = ""
  for char in string:
    numValue = list(ASCII.keys())[list(ASCII.values()).index(char)]
    converted += ChangeFromBase10(numValue,7) + " "
  return converted[:-1]

def Encrypt(string):
  converted = ""
  for i in range(len(string)):
    char = string[i]
    numValue = list(ASCII.keys())[list(ASCII.values()).index(char)]
    binaryConvert = ChangeFromBase10(numValue,2)
    converted += "0"*(8-len(binaryConvert)) + binaryConvert
    if i != len(string)-1:
      converted += " "
  return converted

Digits = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k'}

Letters = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20}

# for num,letter in Digits.items():
#   Letters[letter] = num
# for i in range(10,21):
#   Letters[input(str(i)+": ")] = i
# print(Letters)

# num = 12334543656
# base = 16

# NativeBase = ChangeFromBase10(num,base)

# Base10 = ChangeToBase10(NativeBase,base)

print(Encrypt("this is now in binary!"))
print(Encrypt("this is a message in base 7!"))
