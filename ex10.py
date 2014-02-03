tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

weird_cat = "Within \"quotes\" and with a \vvertical tab."
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print weird_cat

import time
while True:
	for i in ["/","|","\\","-","|","a"]:
		print "%s\r" % i,
