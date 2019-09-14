def challenge1():
	for i in range(0, 101, 2):
		print(i, end=' ')

# challenge1()

def challenge2():
	a = 'KABOOM'
	for i in range(0, len(a)):
		b = 0
		while b < 3:
			print(a[i], end=' ')
			b += 1

# challenge2()

def challenge3():
	a = "askaliceithinkshe'llknow"
	for i in range(0, len(a), 2):
		print(a[i], end=' ')
# challenge3()

def challenge4():
	for i in range(1, 5):
		for f in range(5, 8):
			print("%d | %d | %d" % (i, f, i*f))

challenge4()
