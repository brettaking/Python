#Word reverse

def reverse(text):
    x = len(text)
    new_string = ""
    for x in range(len(text)):
        new_string = text[x] + new_string
        x = x - 1
    print new_string
    return new_string
    print new_string
      
reverse(raw_input("Enter a word."))