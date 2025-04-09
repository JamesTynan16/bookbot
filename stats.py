def get_word_count(book):
    words = book.split()
    return len(words)

def get_character_count(book):
    all_lowercase = book.lower()
    characters = {}
    for letter in all_lowercase:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sorted_character_list(characters):
    character_list = []
    for character,count in characters.items():
        character_dict = {"character": character, "count": count}
        character_list.append(character_dict)
    
    def sort_on(dict):
        return dict["count"]
    
    character_list.sort(reverse=True, key=sort_on)
    return character_list