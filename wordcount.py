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
