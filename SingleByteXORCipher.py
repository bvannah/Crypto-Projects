def decryptUsingByte(bytesToDecrypt, byteUsed): #returns a string, does a single-byte XOR cipher
    ret = ""
    for byteIndex in range(len(bytesToDecrypt)): #for each byte in the string
        ret = ret + chr(bytesToDecrypt[byteIndex] ^ byteUsed)
    return ret

def evaluateStr(toEvaluate): #returns a float, evaluates what percentage of the string is common english ASCII letters
    count = 0 #counts the number of english ASCII letters
    for char in toEvaluate:
        byte = ord(char)
        if(((byte>=0x41)&(byte<=0x5a))  |  ((byte>=0x61)&(byte<=0x7a)) | (byte == 0x20)): #if it's upper-case, lower-case, or a space
            count+=1
    return  count/float(len(toEvaluate))

def evaluateStrTuple(tupl):
    return evaluateStr(tupl[0])

def strToBytes(toConvert): #returns an array of bytes, converts string of bytes to array of bytes
    ret = []
    charIndex = 0
    while charIndex<len(toConvert): #for each two-characters of the string (a byte)
        #first char in byte
        if ((0x30 <= ord(toConvert[charIndex])) & (ord(toConvert[charIndex])<=0x39)): #must be an int 0-9
            highNib=int(float(toConvert[charIndex])) #map to byte value
        if ((0x41<=ord(toConvert[charIndex])) & (ord(toConvert[charIndex])<=0x5a)): #must be upper case
            highNib=ord(toConvert[charIndex])-55 #map to proper hex value. 0x41-0xA = 55
        if ((0x61<=ord(toConvert[charIndex])) & (ord(toConvert[charIndex])<=0x7a)): #must be lower case
            highNib=ord(toConvert[charIndex])-87 #map to proper hex value. 0x61-0x0a = 87

        charIndex += 1 #second char in byte
        if (charIndex>=len(toConvert)): #odd number of bytes 
            continue #handle separate case
        if ((0x30 <= ord(toConvert[charIndex])) & (ord(toConvert[charIndex])<=0x39)): #must be an int 0-9
            lowNib=int(float(toConvert[charIndex])) #map to byte value
        if ((0x41<=ord(toConvert[charIndex])) & (ord(toConvert[charIndex])<=0x5a)): #must be upper case
            lowNib=ord(toConvert[charIndex])-55 #map to proper hex value. 0x41-0xA = 55
        if ((0x61<=ord(toConvert[charIndex])) & (ord(toConvert[charIndex])<=0x7a)): #must be lower case
            lowNib=ord(toConvert[charIndex])-87 #map to proper hex value. 0x61-0x0a = 87
        charIndex += 1
        ret.append(highNib*16+lowNib)
    return ret


def singleByteXORCipher(inputString): #has the option to print all of the possible decryptions with more than 80% 'common ascii letters'
    highAscii = [] #function returns a tuple of a tuple ((the string with the highest ascii evaluation score, its key), its score) 
    inputBytes = strToBytes(inputString)
    for byte in range(256): #for each possible byte
        testStr = decryptUsingByte(inputBytes, byte)
        if(evaluateStr(testStr)>.80): #if a string is more than 80% ascii, 
            highAscii.append((testStr, byte)) #then it is good enough to look at
    highAscii.sort(key=evaluateStrTuple, reverse=True)
    if(len(highAscii) == 0): #if we didn't find anything with more than 80% Ascii
        return (("", 0), 0)
    return (highAscii[0], evaluateStrTuple(highAscii[0]))
    
def main():
    testString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(singleByteXORCipher(testString))
    print(len(testString))
    
if __name__== "__main__":
    main()

    
    
    

#etaoinshrdlc
#display top 5 english values