def GetNumSystem():             # NumSystem selection function
    while True:
        numSystem = input('Choose num system: BIN, OCT, DEC, HEX\n')
        if numSystem == 'BIN':
            return 2
        elif numSystem == 'OCT':
            return 8
        elif numSystem == 'DEC':
            return 10
        elif numSystem == 'HEX':
            return 16

def ConvertFromBin(_value,_numSystem):          # Binary translation function
    if _numSystem == 2:
        return _value
    elif _numSystem == 8:
        return oct(int(_value, 2))
    elif _numSystem == 10:
        return int(_value, 2)
    elif _numSystem == 16:
        return hex(int(_value, 2))

def ConvertFromOct(_value,_numSystem):          # Octal system function
    if _numSystem == 2:
        return bin(int(_value, 8))
    elif _numSystem == 8:
        return _value
    elif _numSystem == 10:
        return int(_value, 8)
    elif _numSystem == 16:
        return hex(int(_value, 8))

def ConvertFromDec(_value, _numSystem):         #Decimal system function
    if _numSystem == 2:
        return bin(int(_value))
    elif _numSystem == 8:
        return oct(int(_value))
    elif _numSystem == 10:
        return int(_value)
    elif _numSystem == 16:
        return hex(int(_value))

def ConvertFromHex(_value,_numSystem):       # Hexadecimal system function
    if _numSystem == 2:
        return bin(int(_value, 16))
    elif _numSystem == 8:
        return oct(int(_value, 16))
    elif _numSystem == 10:
        return int(_value, 16)
    elif _numSystem == 16:
        return _value

def main():
    print('Input num system: ')
    fNumSystem = GetNumSystem()         # Get input num system
    value = input('Enter a value: ')    # Get input number
    print('Output num system ')
    sNumSystem = GetNumSystem()         # Get output num system
    if fNumSystem == 2:
        print(ConvertFromBin(value, sNumSystem))
    elif fNumSystem == 8:
        print(ConvertFromOct(value, sNumSystem))
    elif fNumSystem == 10:
        print(ConvertFromDec(value, sNumSystem))
    elif fNumSystem == 16:
        print(ConvertFromHex(value, sNumSystem))



main()