name = input('Enter the song title: ')

space = " "
splitted = name.split(space)

exact_name = ""

for s in splitted:
	if(s.isalpha()):
		exact_name += s 
		exact_name += space


print(exact_name)
