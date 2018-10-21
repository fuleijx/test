def main():
    print("This program converts a textrual messageinto a sequence ")
    print("of number respresenting the Unicode encoding of the message.\n")
    #Get the message to encode
    message = input("Please enter the message to encode: ")
    
    print("\nHere are the Unicode codes:")
    
    #Loop through th message and print out the Unicode values
    
    for ch in message:
        print(ord(ch),end=" ")
        print() #blank line before prompt
main()
    
83 116 114 105 110 103 115 32 97 114 101 32 70 117 110 33
