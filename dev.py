def find_repeated_character(input_string):
    char_count = {}
    
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    repeated_characters = []
    
    for char, count in char_count.items():
        if count > 1:
            repeated_characters.append((char, count))
    
    return repeated_characters

input_string = "Deepchand"
repeated_chars = find_repeated_character(input_string)

for char, count in repeated_chars:
    print(f"Repeated character: {char}, Count: {count}")
