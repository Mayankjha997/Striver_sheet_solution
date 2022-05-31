def reverse_words_of_the_string(s):
    words = s.split()
    reversewords = " ".join(reversed(words))
    return reversewords


s = input("enter the string to be reversed ")
v = reverse_words_of_the_string(s)
print(v)