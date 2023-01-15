with open("books/frankenstein.txt") as f:
    file_contents = f.read()

# the below function will return number of words in the document
def num_of_words(text):
    words = text.split()
    return len(words)

num_words = num_of_words(file_contents)

# this function will retrun a character and the number of times the character appeard in the form of dictonary
def count_letters(text):
    d = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter not in d:
            d[lower_letter] = 1
        else:
            d[lower_letter] += 1
    return d

dict_char = count_letters(file_contents)

def sort_on(d):
    return d["num"]

# this function will take dict as input and will return a sorted list
def dict_to_sorted_list(dict):
    list_sort = []
    for i in dict:
        list_sort.append({"char": i, "num": dict[i]})
    list_sort.sort(reverse=True,key=sort_on)
    return list_sort

sorted_list = dict_to_sorted_list(dict_char)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{num_words} words found in the frankenstein.txt file")
print()
for i in sorted_list:
    if not i['char'].isalpha():
        continue
    print(f"the {i['char']} character was found {i['num']} times")
print()
print("--- End report ---")
    




        




        

