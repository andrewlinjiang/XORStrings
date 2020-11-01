import sys











if __name__ == "__main__":
	mode = sys.argv[1]
	keyfile = sys.argv[2]
	inpfile = sus.argv[3]
	with open (keyfile) as fp:
		key = fp.read()[:-1]
	with open (inpfile) as fp:
		key = fp.read()[:-1]
	debug = False

	if (debug):
		print("mode:"+mode)
		print("key: "+key)
		print("inp: "+inp)
