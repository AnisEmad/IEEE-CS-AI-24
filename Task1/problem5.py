#task 1 problem 5

word = input("Enter a word: ")
n = len(word) - 1
i = 0
while (i < n):
    if word[i] != word[n]:
        break
    i += 1
    n -= 1
if word[i] != word[n]:
    print("not a plaindrome")
else:
    print("plaindrome")