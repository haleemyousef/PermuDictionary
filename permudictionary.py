
# Author : Haleem Yousef
# Email  : haleemyousef01@gmail.com
# GitHub : https://github.com/haleemyousef

logo = """

	{OOO}   {OOO}           pua  					
	 I8I     I8I            :11  					
	 I8I     I8I   .oooo.    11   .ooooo.   .ooooo.  oooooooo.oooooo.	
	 I8I8I8I8I8I  `P  )88b   11  d88' `88b d88' `88b `88b' `88b' `88b	
	 I8I     I8I   .oP"888   11  888ooo888 888ooo888  888   888   888	
	 I8I.   .I8I  d8(  888   11. 888    .o 888    .o .888   888   888	
	dI8Ib   dI8Ib `Y888""8o  OOO `Y8bod8P' `Y8bod8P' 6888b  888  6888b	

				    Coded by haleemyousef			
	"""

print(logo)

print("""This script inputs a word from the user and checks all the possible permutations of its letters,
pointing out the ones that are found in the dictionary and prints their meaning, 
and eliminates all duplicates in the process.\n""")

print("Importing dependencies:")

import sys, subprocess, itertools

#Installing/Importing Pyenchant
try:
	import enchant
except ModuleNotFoundError:
	print("Installing PyEnchant:\n")
	subprocess.run([sys.executable, "-m", "pip", "install", "Pyenchant"])
	import enchant
except Exception:
	print("some weird error has happened while importing a module...")
	raise Exception()

#Installing/Importing PyDictionary
try:
	from PyDictionary import PyDictionary
except ModuleNotFoundError:
	print("Installing PyDictionary:\n")
	subprocess.run([sys.executable, "-m", "pip", "install", "PyDictionary"])
	from PyDictionary import PyDictionary
except Exception:
	print("some weird error has happened while importing a module...")
	raise Exception()


word = input("Enter a word to discover all its possible permutations: ").lower() # I recommend 7 or less letters for most stability.
word = word.replace(' ', '') # No whitespaces.
output = input("Do you wish to output this program to a text file? (Y/n): ").lower()
if output == 'y':
	file_name = "output_" + word + ".txt"
	print("Generating permutations... Data will be saved on", file_name)
	file = open(file_name, "wt")
	file.write(logo) # Comment this line if you don't want to have the logo in the output file.
	sys.stdout = file
# word.split()
d = enchant.Dict("en") # enchant for looping and filtering through words FAST.
dictionary = PyDictionary() # PyDictionary to fetch meaning from words filtered by enchant.
no_duplicates = set()
i = 2 # at least 2 letters are needed for a permutation to be called a 'word'.

while len(word) >= i:
	print(f"""
=============================================
The length of the words generated now is {i}.
=============================================
	""")
	perm_generator = itertools.permutations(word, i)
	for perm_parts in perm_generator:
		perm = ''.join(perm_parts)

		if perm not in no_duplicates:
			no_duplicates.add(perm)
		else: # word is a duplicate thus skipped.
			continue

		get_meaning = ''
		
		if d.check(perm):
			get_meaning = dictionary.meaning(perm, disable_errors=True) # Errors in this case are useless and visually unappealing.
			is_it_a_word = "YES"
		else:
			is_it_a_word = "NO"
		print(f"{perm} | is it a word? {is_it_a_word}.")
		
		if get_meaning is None: # enchant & PyDictionary libraries are not identical, sometimes a word exist in the first but not the latter.
			print("  \u2022Nothing was found on PyDictionary ):")
		elif get_meaning != '':
			for k, v_list in get_meaning.items():
				print(f"  \u2022{k}s:") # Printing the keys of the dictionary as headilnes (Noun, Verb, Adjective, Adverb, etc).
				for v in v_list:
					v = v.replace(";", ";\n\t") # Sometimes a definition can be lengthy and seperated by semicolons, I made those multilinear.
					print(f"     -{v}.") # Finally, the godd*amn defintion.
	i += 1

if output == 'y':
	file.close()
