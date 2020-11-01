import sys

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
with open (keyfile) as fp:
	key = fp.read()[:-1]
with open (inpfile) as fp:
	inp = fp.read()[:-1]
debug = False

if (debug):
	print("mode:"+ mode)
	print("key: "+ key)
	print("inp: "+ inp)

counter = 0
output = []
while (counter < len(inp)):
	output.append(ord(inp[counter]) ^ ord(key[counter % len(key)]))
	counter += 1


if (mode == "numOut"):
	res = ""
	for i in output:
		res+= str(hex(i)[2:]) +" "
	print(res)

if (mode == "human"):
	res = ""
	for i in output:
		res+= chr(i)
	print(res)

