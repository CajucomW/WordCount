############################################
#                Word Count                #
############################################
## A challenge from KickStart Coding Bootcamp!!!

# Write an application that reads in a text file and generate a word
# count for each word it encounters.

## Read in the file:

dickins = open('great_expectations.txt').read()

## Clean out punctuations and make lower case
## using .replace and .lower methods

for item in "!@#$%^&*()_+-=`~[]\{}|;',/<>?.:":
    dickins = dickins.replace(item, '')
for quote in '"':
    dickins = dickins.replace(quote, '')
dickins = dickins.lower()

print(dickins)

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
