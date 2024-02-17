import string

def count_words():
    counter = {}

    path = input("Enter the name of the file: ")

    try: 
        with open(path, 'r') as file:
            for line in file:
                line.lower()
                words = line.split()
                for word in words:
                    if word in string.punctuation:
                        continue
                    if word in counter:
                        counter[word] += 1
                    else:
                        counter[word] = 1
        for word, count in counter.items():
            print(f"{word}: {count}")
    except Exception:
        print("there is no such file")
        n = input("1 to exit\n2 to try again\n::")
        if n == 2:
            count_words()

if __name__ == '__main__':
    count_words()