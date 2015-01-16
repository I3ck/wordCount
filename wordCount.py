import sys
import getopt
import operator

inputfile = ""
outputfile = ""
wordcounts = dict()


if __name__ == "__main__":
	argv = sys.argv[1:]

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["inputfile=","outputfile="])
	except getopt.GetoptError:
		print 'wordCount.py -i <inputfile> -o <outputfile>'
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-h':
			print 'wordCount.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	if inputfile == "" or outputfile == "":
		print "something went wrong, use wordCount.py -h"
		sys.exit(2)


	with open(inputfile) as f:
		for line in f:
			words = line.split()
			for word in words:
				if word in wordcounts:
					wordcounts[word] +=1
				else:
					wordcounts[word] = 1

	sortedcounts = sorted(wordcounts.items(), key=operator.itemgetter(1))
	sortedcounts.reverse()

	with open(outputfile, 'w') as f:


		for item in sortedcounts:
			word = item[0]
			count = item[1]
			f.write(str(count).zfill(4) + " * " + word + "\n")

