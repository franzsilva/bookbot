def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    character_list = list(text.lower())
    char_count_object = {}
    for char in character_list:
        if char in char_count_object:
            char_count_object[char] = char_count_object[char] + 1
        else:
            char_count_object[char] = 1

    return char_count_object

def sort_on(dict):
    return dict["count"]

def sorted_list_dictionary(dictionary):
    new_dic_list = []
    for char in dictionary:
        new_dic = {
            "character": char,
            "count": dictionary[char]
        }
        new_dic_list.append(new_dic)
    new_dic_list.sort(reverse=True, key=sort_on)
    return new_dic_list
