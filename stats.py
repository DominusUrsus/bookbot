#Created dictionary for char_counter and stats_sorter to use later
char_dict = {}

#Split text and count the words - take output from get_book_text function
def word_counter(file_contents):
    
    book_list = file_contents.split()
    word_count = len(book_list)

    return word_count

#Read file and count each character, store in a characters dictionary
def char_counter(file_contents):
    #set all chars to lowercase
    #print("Debug: Running char_counter, char_dict created")
    low_char = file_contents.lower()
    #iterate over letters in string
    #print("Debug: low_char created")
    for char in low_char:
        #check if character is in dictionary
        if char not in char_dict:
            #add key if *not* in dictionary
            char_dict[char] = 1
        else:
            #else add +1 value 
            char_dict[char] += 1




    return char_dict

#stats_sorter function reorganizes char_counter dictionary into several dictionaries for each letter:count, adds to list, and sorts by count
def stats_sorter(char_counter):
    sorted_dict_list =[]
    #For loop against every character, and count in char_count (char_dict)
    for char, count in char_counter.items():
        #check if current char is alpha
        if char.isalpha():
            #create temp_char_dict and assign char/count to keys, append to list of dict
            temp_char_dict = {}
            temp_char_dict["char"] = char
            temp_char_dict["num"] = count
            sorted_dict_list.append(temp_char_dict)
    
    #provide sort method the key to run on
    def dict_sort(items):
        return items["num"]

    #sort our list of dicts
    sorted_dict_list.sort(reverse=True, key=dict_sort)

    return sorted_dict_list

    #iterate and move characters to separate dictionaries with Char:Count pairs
    
    

#Created dictionary for char_counter and stats_sorter to use later
char_dict = {}

#Split text and count the words - take output from get_book_text function
def word_counter(file_contents):
    
    book_list = file_contents.split()
    word_count = len(book_list)

    return word_count

#Read file and count each character, store in a characters dictionary
def char_counter(file_contents):
    #set all chars to lowercase
    #print("Debug: Running char_counter, char_dict created")
    low_char = file_contents.lower()
    #iterate over letters in string
    #print("Debug: low_char created")
    for char in low_char:
        #check if character is in dictionary
        if char not in char_dict:
            #add key if *not* in dictionary
            char_dict[char] = 1
        else:
            #else add +1 value 
            char_dict[char] += 1




    return char_dict

#stats_sorter function reorganizes char_counter dictionary into several dictionaries for each letter:count, adds to list, and sorts by count
def stats_sorter(char_counter):
    sorted_dict_list =[]
    #For loop against every character, and count in char_count (char_dict)
    for char, count in char_counter.items():
        if char.isalpha():
            temp_char_dict = {}
            temp_char_dict["char"] = char
            temp_char_dict["num"] = count
            sorted_dict_list.append(temp_char_dict)
    
    #provide sort method the key to run on
    def dict_sort(items):
        return items["num"]

    #sort our list of dicts
    sorted_dict_list.sort(reverse=True, key=dict_sort)

    return sorted_dict_list

    #iterate and move characters to separate dictionaries with Char:Count pairs
    
    