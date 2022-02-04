def reversestring(inputword):
    """
    Python program to check if a string in palindrome
    input: Mam
    output: The String is in Palindrome
    input:Mat
    output: The String is not in Palindrome
    """

    #converting string to list
    inputlist=list(inputword)
    count=0
    inputlength=len(inputlist)-1

#looping through the word and modifying the string
    while(count<=inputlength):
        temp=inputlist[inputlength]
        inputlist[inputlength]=inputlist[count]
        inputlist[count]=temp

        print(inputlist)

        count=count+1
        inputlength=inputlength-1

    return "".join(inputlist)

#user input
inputword=input("Enter the word you want to reverse")

print("the reversed word is",reversestring(inputword))
#checking if string is in palindrome

if(reversestring(inputword).strip().lower()==inputword.strip().lower()):
    print("The String is in Palindrome")
else:
    print("The String is not in Palindrome")

