with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
def count_words(text):
    words = text.split()
    return len (words)

print (count_words(file_contents))

def count_characters(text):
    char_dict = {}
    lowered_string = text.lower() 

    for char in lowered_string:
        if char in char_dict:
            char_dict[char] += 1  
        else:
            char_dict[char] = 1  

    return char_dict


char_dict = (count_characters(file_contents))

def print_char():
    for char, count in char_dict.items():
      print(f"The '{char}' character was found {count} times")


print_char()
    




