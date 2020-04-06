############################################
#                Word Count                #
############################################
## A challenge from KickStart Coding Bootcamp!!!

# Write an application that reads in a text file and generate a word
# count for each word it encounters.

## Read in the file:

dickins = open('great_expectations.txt').read()

## Clean out punctuations and make lower case
## using .replace() and .lower() methods
special_chars = ['"', '!', '@', '#', '$', '%', 
'^', '&', "*", '(', ')', '_', '+', '-', '=',
'`', '~', '[', ']', '|', ';', 
"'", ',', '/', '<', '>', '?', '.', ':', '“', '”']
for item in special_chars:
    dickins = dickins.replace(item, '')
dickins = dickins.lower()
## had a bit of trouble w/ quotations because of 
## left and right quotation marks '“', '”', are
## different from regular ones '"'.

## use the .split() method to put all the words into a list
## .split() gets rid of all the spaces and paragraph breaks
dickins = dickins.split()

## once in a list, it's probably easier to sort through it
##  and count all the strings
## check the length of the list?!?
total = len(dickins)
print("Total number of words in this text:", total)

## Sort the output either alphabetically, or by count.
## I'll need the word And the number (pair)
## use a dictionary
dictionary = {}
for word in dickins:
    ## using .get(), I was able to get the key and assign
    ## a value to 0
    dictionary[word] = dictionary.get(word, 0) + 1

word_numb = []
for key, value in dictionary.items():
    ## here I changed the order around
    word_numb.append((value, key))

word_numb.sort(reverse=True)
#print(word_numb)

## Only print the top X number, e.g. top 100
## Use string formatting methods to make the output easy to read.
for value, key in word_numb:
    if value > 100:
        print(value, '=', key)


# Full Requirements/TODO:
# - Sort the output either alphabetically, or by count.
# - Only print the top X number, e.g. top 100.
# - It should ignore case and punctuation.
# - Use string formatting methods to make the output easy to read.
# - The output, for example, might be something like:
#       the 1801
#       and 910
#        to 794
#       ...etc
