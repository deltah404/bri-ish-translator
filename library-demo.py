from modules.translator import translate
# MUST BE IN SAME DIRECTORY. FOR USE IN FILES WHERE DBT IS IN THE SAME DIRECTORY:
#                               from dbt.modules.translator import translate

phrase_to_translate = input()
print(translate(phrase_to_translate))
input()

# This file is a very basic demonstration of how to use DBT as a module in your own Python files. Feel free to use this module in Discord bots, websites etc., but please be sure to credit me (deltah)