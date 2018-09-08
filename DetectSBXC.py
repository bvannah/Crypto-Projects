import SingleByteXORCipher #AKA SBXC


def getEval(SBXCTuple):
    return SBXCTuple[1]
    
def detectSBXC(filename): #returns a tuple of the most likely decryption and the line number it is on
    file = open(filename, 'r') 
    highestVals = []
    linenum=1
    for line in file:
        line=line.rstrip()
        cipher = SingleByteXORCipher.singleByteXORCipher(line) #run SBXC on each line, not including the newline character
        if(cipher[1]>.8): #if there's a decent cipher
            highestVals.append((cipher,linenum)) #add it to the list
        linenum+=1
    highestVals.sort(key=getEval, reverse=True)
    return highestVals[1]
    
def main():
    print(detectSBXC("lines.txt"))
    
if __name__== "__main__":
    main()




