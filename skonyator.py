import sys

dict = {
0: "Chasov",
1: "Chas",
2: "Chasa",
3: "Chasa",
4: "Chasa",
5: "Chasov",
6: "Chasov",
7: "Chasov",
8: "Chasov",
9: "Chasov"
}

def humanize(n, dictionary):
assert n >= 0
last_digit = n % 10
assert dictionary.has_key(last_digit), "For key "+str(n)+" no informatiormation "
return str(n) + " " + dictionary[last_digit]

if len(sys.argv) < 2:
print "Error. Enter a valid namber"
else:
n = int(sys.argv[1])
print humanize(n, dict)