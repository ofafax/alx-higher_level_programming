#!/usr/bin/python3

if __name__ == "__main__":

	import sys
	q = len(sys.argv) - 1

	if q == 0:
		print("{} arguments.".format(q))
	elif q == 1:
		print("{} argument:".format(q))
	else:
		print("{} arguments:".format(q))
		q = 1
		for arg in argv[1:]:
			print("{}: {}".format(q, arg))
			q += 1

