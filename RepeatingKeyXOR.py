import HammingDistance
import base64
import SingleByteXORCipher2
#TODO: Test input to bytes process
def repeatingKeyXOR(filename, maxKeySize=40): #gets a file, returns the key
#    file=open(filename, 'r')
#    fileStr=(file.read())
#    fileStr=''.join( c for c in fileStr if  c != '\n' )
#    fileStr=base64ToASCII(fileStr)
#    print(fileStr)
    fileStr="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    keySize=getKeySize(str(fileStr), maxKeySize)
    blocks = getSplitBlocks(fileStr, keySize)
    #print(blocks[0])
    key=[]
    for block in blocks:
        cipherTuple = SingleByteXORCipher2.singleByteXORCipher(block)
        print(cipherTuple)
        blockKey = cipherTuple[0]
        key.append(blockKey)   
    return key

def getKeySize(string, maxKeySize):
    keySizeList=[]
    for keySize in range(1, maxKeySize):
        str1=string[0:keySize]
        str2=string[keySize:keySize*2]
        str3=string[keySize*2:keySize*3]
        str4=string[keySize*3:keySize*4]
        hamming12=HammingDistance.getHamming(str1, str2)
        hamming34=HammingDistance.getHamming(str3, str4)
        avgHammingDist=(hamming12+hamming34)/2
        score=avgHammingDist/keySize
        keySizeList.append((keySize, score))
    keySizeList.sort(key=getScore)
    return (keySizeList[0])[0]

def getScore(keySize): #gets the score for each keySize, used by getKeySize
    return keySize[1]

def base64ToASCII(str64): #converts from b64 to ascii string, used by getKeySize
    bytes64=bytearray(str64, 'ascii') 
    ret=base64.b64decode(bytes64)  #is it encode or decode?
    return ret

def getSplitBlocks(fileString, keySize):
    ret =[]
    for i in range(keySize):
        block=[] #the block for the ith characters 
        charIndex=i #start with the first ith character
        while(charIndex<len(fileString)): #until the end of the whole string
            block.append(fileString[charIndex])
            charIndex+=keySize
        ret.append(block) #add the block of ith characters to the total blocks
    
    
    return ret

def main():
    print(repeatingKeyXOR("6.txt"))
    
if __name__== "__main__":
    main()
