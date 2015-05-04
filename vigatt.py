"""
Run the Kasiski test on a ciphertext string.

The Kasiski test reports the distance between repeated
strings in the ciphertext.
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

import operator, re

def make_dict(text):
	return

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


def problem(n):
    myList = []
    for i in range(1, n+1):
        if n % i == 0:
            myList.append(i)

    return myList


def main():
	text = '''GERGHDEVNIYMXQXUXGFPAXVVVOCBWGNUMDDXRVYBXOYRLWCGQIPNISRMQZNEWRYXVHEWCRLRIISHCRPXFTIFMEWGOGRMRLTOAJIQTUJTPWNKZSHKSEXXSCCVNECMXRMFTSCJRGBGJHGSGGBEUPLHNGRZNXMAZGFDRSPHCGIFEGHMSGASZXKVTGRSELSCAIBYRRKCVFTIWTQEAWNVXALNKVFTJEGXUHDTEEBFIHYWCXTHHGRVGWCGKEGBFBHCGHKZHNQYPARGSYXNVFBUGHRGKWPJMGRUOIYMAMVUGGXLTLHWCRGBTOIGSATERCMREXGISGEGBFBBMHRKEQGWTGHXFPNLLBEHTPWRVKGIFIQBJQXNPVGVGDDQNMYSBYXVVJQDKTHMVFHAMRGTSPLHREVQIPMPTCSCEMAXVFXLKZHUSGLGERGHDEVNIYMXQLRTMWAWFNLVRDLQNMYSBYXVVRZIFIBKPOCBGBFGIICVFVZSCAICKRQIGGRVIMERSTKRDWGGNEXCGGXUFJOGCHRLZUCCHNKFICBGBFGIIYXVHEOAFEEWESHQEFLLAERMBGJAPIMAZJIRFEYZFFXRLZLYOGBXBUISPIMAIIORRMPXSMPLCNWMSGQEERZHXQXUXFFTRMPTCZNNSFLZPACXBUISPIWHVYOHWWGXDPJRMGBJWCDINLZPACXBWFGDZCNGPYCMAAIIORRMPTCATYRFVIMERSYHXMGCPNMVRICGUGFZDECUTJFPGWRWRBJKFRKFTACKNEZGHSIFMYSTJIPMICCGGSKFBIGIEYFICBEGBFBLYWVGMCATIQBEORYWRBEHWCYABKSSQXNMVGLFMPAHITQXVHESSULRMYSGPIDNZFXLKFNJDTAXRWTFXKMATCGIMTEHMWSCXUXZFSCGERGHXMRXXPGIMPNPVBUMVPXDSCRMFNEQDLWGBKIIGSATCHWCISYRFVSIQMYOIRLVLZGPTMBERHXMRBYKVTPMTAKCULSGUVWCEJBKTSSRSVGTFXKMATKSDLIFXCTPQKVOVBXLXUXWWURLNFVBSK'''
	dictionary = {}
	lengdict = {}
	sorted_y = []

	for x in range(3,11):
		for y in range(len(text) - x +1):
			window = text[y:y+x]
			if window in dictionary:
				dictionary[window]+=1
			else:
				dictionary[window]=1


	sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
	sorted_x.reverse()
	#print sorted_x[0:30]
	for z in range(90):

		for a in list(re.finditer(sorted_x[z][0], text)):
			print sorted_x[z][0]
			sorted_y.append(a.start())
			print a.start()
		#print sorted_y
		
		mindistance = 10000
		for x in range(len(sorted_y)):
			for y in range(len(sorted_y)):
				distance = abs(sorted_y[y]- sorted_y[x])

				if distance < mindistance and distance != 0:
					mindistance = distance

		print "mindistance = " + str(mindistance)

		print
		if mindistance != 0 and mindistance >= 3:
					if mindistance in lengdict:
						lengdict[mindistance]+=1
					else:
						lengdict[mindistance]=1
		sorted_y = []

	sorted_len = sorted(lengdict.items(), key=operator.itemgetter(1))
	sorted_len.reverse()
	print sorted_len
	print 
	print len(text)
	biglist = []
	
	for a in range(len(sorted_len)):
		myList = problem(sorted_len[a][0])
		for x in range(sorted_len[a][1]):
			biglist += myList



	factordict = {}
	for a in range(len(biglist)):
		if biglist[a] in factordict:
			factordict[biglist[a]]+=1
		else:
			factordict[biglist[a]]=1

	factors = sorted(factordict.items(), key=operator.itemgetter(1))
	factors.reverse()

	print factors
	#for i in range[30]
	#	printsorted_x[i]




main()