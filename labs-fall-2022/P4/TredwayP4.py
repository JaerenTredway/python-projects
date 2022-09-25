# TredwayP4
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: Create a translator program that gets a 
#   Norweigian phrase from the user and translates 
#   it into English.

# Display a header for the user interface:
print('\n\n***************************************************')
print('                 Micro Translator\n')

# Create a dictionary with common phrases in Norweigian 
# as the key and the translation in English as the values:
translator = {  
    'hei kompis':'hello buddy',
    'ha det bra min venn':'goodbye my friend',
    'det er bra':'that is good',
    'jeg er sulten':'I am hungry',
    'jeg elsker iskrem':'I love ice cream',
    'Python er kult':'Python is cool'
    }

# Display a list of the Norwegian phrases to the user:
norg_phrases = list(translator.keys())
print('Here is a list of Norweigian phrases that you can')
print('get translations of:\n')
print('   ',',\n    '.join(norg_phrases))

# Run a loop that does the following:
# 1. get user input, 
# 2. exit the program if the user enters 'quit',
# 3. display an error message if the input is not in the dictionary,
# 4. provide an English translation of the Norweigian input.
input_phrase = ""
while input_phrase not in translator:
    # ask the user to type in a phrase to translate:
    input_phrase = input("Enter a Norweigian phrase to translate, or enter 'quit' to leave\n-->")
    # exit condition:
    if input_phrase == 'quit':
        print('ok, ha det bra! goodbye!')
        quit()
    # check for bad input:
    if input_phrase not in translator:
        print(f'\n****ERROR CODE****> "{input_phrase}" is not in Micro Translator.')
        print('    Here are your choices:')
        print('   ','\n    '.join(norg_phrases))
    # display the translation of the phrase to the user:
    if input_phrase in translator:
        translation = translator[input_phrase]
        print('\nYour translation:\n')
        print(translation,'\n')
    # reset input_phrase to run again until user quits:
    input_phrase = ''