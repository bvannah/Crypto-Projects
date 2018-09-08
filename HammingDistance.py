def getHamming(string1, string2):
    assert len(string1)==len(string2)
    ret=0
    bits1=stringToBits(string1)
    bits2=stringToBits(string2)
    for i in range(len(bits1)):
        if(((bits1[i]=='0') | (bits1[i]=='1')) & ((bits1[i]=='0') | (bits1[i]=='1'))):
            if(bits1[i] != bits2[i]): #if the bits dont match
                ret += 1
    return ret

def stringToBits(string):
    intBytes=bin(int.from_bytes(string.encode(), 'big'))[2:] #skip the 0b prefix
    leadingZeros=len(string)*8-len(intBytes)
    for i in range(leadingZeros):
        #add leading zero
        intBytes="0"+intBytes
    #TODO: leading zeros
    
    return  intBytes#encodes string into bits, big endian? doesn't change hamming distance either way, as long as it is consistient
        

def main():
    print(getHamming("this is a test", "wokka wokka!!!"))
    
if __name__== "__main__":
    main()