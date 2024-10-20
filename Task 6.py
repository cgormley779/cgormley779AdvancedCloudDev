check_this_string = input("Enter word to check if it's a palindrome ")
#this line assigns a variable known as check_this_string to entered word
print (f"the word you have entered is {check_this_string}")
reversed_string = (check_this_string[::-1])
if reversed_string == check_this_string:
    print("This word is a palindrome")
else:
    print("this word isnt a palindrome")


