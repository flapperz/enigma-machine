import random

# global variable
alphabetNumber = 26


class Rotor:


    def __init__(self, charMap = None):

        self.charMap = charMap
        self.rCharMap = []
        self.rotorIndicator = 0
        
        self.initialize()
            
    def initialize(self):
        if (self.charMap == None):
            self.charMap = list(range(alphabetNumber))
            random.shuffle(self.charMap)
        
        self.rCharMap = [self.charMap.index(i) for i in range(alphabetNumber)]
    
    def passCharInt(self, charInt, forward=True):
        if forward:
            return self.charMap[charInt]
        else:
            return self.rCharMap[charInt]

    def rotate(self, encode=True):
        if encode:
            self.rotorIndicator += 1
        else:
            self.rotorIndicator -= 1
        
        self.rotorIndicator %= alphabetNumber
        return self.rotorIndicator

class Enigma:
    def __init__(self, rotorNumber=3):
        self.rotorNumber = rotorNumber
        self.rotors = []

        self.initialize()

    def initialize(self):
        for i in range(self.rotorNumber):
            self.rotors.append(Rotor())
    
    def rotateRotor(self, encode=True):
        if (encode):
            idc = 0
            for rotorIdx in range(self.rotorNumber):
                rotor = self.rotors[rotorIdx]
                if idc == 0:
                    rotor.rotate(encode = encode)
        else:
            idc = alphabetNumber-1
            for rotorIdx in range(self.rotorNumber):
                rotor = self.rotors[rotorIdx]
                if idc == alphabetNumber-1:
                    rotor.rotate(encode = encode)
                    
            

    def encodeChar(self, char):
        buffer = ord(char) - ord('a')
        # rotate
        self.rotateRotor(encode=True)

        # forward pass
        for rotorIdx in range(self.rotorNumber):
            rotor = self.rotors[rotorIdx]
            buffer = rotor.passCharInt(buffer, forward=True)

        # backward pass
        for rotorIdx in range(self.rotorNumber-2, -1, -1):
            rotor = self.rotors[rotorIdx]
            buffer = rotor.passCharInt(buffer, forward=False)

        output = chr(buffer + ord('a'))
        return output
    
    def decodeChar(self, char):
        buffer = ord(char) - ord('a')
        # rotate
        self.rotateRotor(encode=False)

        # forward pass
        for rotorIdx in range(self.rotorNumber-1):
            rotor = self.rotors[rotorIdx]
            buffer = rotor.passCharInt(buffer, forward=True)

        # backward pass
        for rotorIdx in range(self.rotorNumber-1, -1, -1):
            rotor = self.rotors[rotorIdx]
            buffer = rotor.passCharInt(buffer, forward=False)    

        output = chr(buffer + ord('a'))    
        return output

    def encode(self, text):
        output = ''
        print(text)
        for char in text:
            char = char.lower()
            
            if char.isalpha():
                output += self.encodeChar(char)
            else:
                output += char    

        return output

    def decode(self, text):
        text = text[::-1]
        output = ''
        for char in text:
            char = char.lower()

            if char.isalpha():
                output += self.decodeChar(char)
            else:
                output += char    

        output = output[::-1]
        return output

if __name__ == '__main__':
    enigma = Enigma()
    text = input().strip()
    # text = 'a'
    encodedText = enigma.encode( text )
    decodedText = enigma.decode( encodedText )

    print('input  : ', text)
    print('encode : ', encodedText)
    print('decode : ', decodedText)


