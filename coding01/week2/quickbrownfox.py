txt = "the quick brown fox jumps over the lazy dog"
alphabets = "abcdefghijklmnopqrstuvwxyz"

for alpha in alphabets:
	count = 0

	for i in txt:
			if alpha == i or alpha.upper() == i:
		count = count + 1

print(alpha + ": " + str(count))			