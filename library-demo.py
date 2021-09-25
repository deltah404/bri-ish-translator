from langs import british
# MUST BE IN SAME DIRECTORY. FOR USE IN FILES WHERE DBT IS IN THE SAME DIRECTORY:
#                               from <DBT folder name>.langs import <language>

phrase_to_translate = input()
print(british.translate_british(phrase_to_translate))
input()

# This file is a very basic demonstration of how to use DBT as a module in your own Python files. Feel free to use this module in Discord bots, websites etc., but please be sure to credit me (deltah)

# Helpful usgae tips:
#  - DBT will always return entirely lowercase strings. Don't worry about making your input lowercase as DBT will do that for you.
#  - Rename the folder that houses DBT something simple like "dbt" so the import is shorter, easier and more legible.
#  - Visit dbtranslator.tk for more help and information. Updated fairly frequently.