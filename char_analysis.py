

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

import operator, re
import numpy
from scipy import stats
from itertools import starmap, cycle


 #Frequency Finder
  # http://inventwithpython.com/hacking (BSD Licensed)


# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
englishLetterFreq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.996, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507,1.929, 0.095, 5.987, 6.327,9.056, 2.758, 0.978,2.360, 0.150, 1.974, 0.074]
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message, key):                                                                     
 
    # convert to uppercase.                                                                    
    # strip out non-alpha characters.                                                                                            
 
    # single letter encrpytion.                                                                
    def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))                              
 
    return "".join(starmap(enc, zip(message, cycle(key))))    

def increment_string(message, letter):
	newstring = list(message)

	for x in range(len(message)):
		z = ord(newstring[x]) - ord(letter) % 65
		if (z < 65):
			z += 26
		newstring[x] = chr(z)

	return ''.join(newstring)

def add_freq(freq):
	z = 0
	for x in range(len(freq)):
		z += freq[x]
	print z

#############
def print_var(freq):

	

	mu = 0
	for x in range(26):
		mu +=freq[x]
	mu/=26
	

	total = 0
	for x in range(26):
		total+=(freq[x]-mu)**2

	total/=26
	return total



################
def sub_freq(obs, norm):
	for x in range(len(obs)):
		obs[x] = obs[x] - englishLetterFreq[x]
	return obs	


##################
def get_most_likely_letter(message):
	
	minimum = 10000
	best = 'a'
	second = 'a'
	third = 'a'
	fouth = 'a'
	for letter in LETTERS:
		mes = increment_string(message, letter)


		diction = getLetterCount(mes)

		freq = getLetterfreq(diction, 150)


		obs = sub_freq(freq, englishLetterFreq)
		

		x = numpy.std(obs)
		
		if x < minimum:
		
			minimum = x
			fourth = third
			third = second
			second = best
			best = letter
	print
	
	print best + ' ' + second + ' ' + third + ' ' + fourth
	print
	return

###################
def getLetterCount(message):
	# Returns a dictionary with keys of single letters and values of the
	# count of how many times they appear in the message parameter.
	letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
	
	for letter in message:
		if letter in LETTERS:
 			letterCount[letter] += 1
	return letterCount
###################

def getOddCount(message):
	# Returns a dictionary with keys of single letters and values of the
	# count of how many times they appear in the message parameter.
	letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
	count = 1
	for letter in message:
		if count%2==1:
			if letter in LETTERS:
	 			letterCount[letter] += 1
	 	count+=1
	return letterCount
###################

def getEvenCount(message):
	# Returns a dictionary with keys of single letters and values of the
	# count of how many times they appear in the message parameter.
	letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
	count =1
	for letter in message:
		if count%2==0:
			if letter in LETTERS:
	 			letterCount[letter] += 1
	 	count += 1
	return letterCount
###################

def getLetterfreq(dictionary, size):
	# Returns a dictionary with keys of single letters and values of the
	# count of how many times they appear in the message parameter.
	letterFreq = []
	for letter in LETTERS:
 		letterFreq.append(100*dictionary[letter]/float(size))
	return letterFreq

def main():
	text = '''GERGHDEVNIYMXQXUXGFPAXVVVOCBWGNUMDDXRVYBXOYRLWCGQIPNISRMQZNEWRYXVHEWCRLRIISHCRPXFTIFMEWGOGRMRLTOAJIQTUJTPWNKZSHKSEXXSCCVNECMXRMFTSCJRGBGJHGSGGBEUPLHNGRZNXMAZGFDRSPHCGIFEGHMSGASZXKVTGRSELSCAIBYRRKCVFTIWTQEAWNVXALNKVFTJEGXUHDTEEBFIHYWCXTHHGRVGWCGKEGBFBHCGHKZHNQYPARGSYXNVFBUGHRGKWPJMGRUOIYMAMVUGGXLTLHWCRGBTOIGSATERCMREXGISGEGBFBBMHRKEQGWTGHXFPNLLBEHTPWRVKGIFIQBJQXNPVGVGDDQNMYSBYXVVJQDKTHMVFHAMRGTSPLHREVQIPMPTCSCEMAXVFXLKZHUSGLGERGHDEVNIYMXQLRTMWAWFNLVRDLQNMYSBYXVVRZIFIBKPOCBGBFGIICVFVZSCAICKRQIGGRVIMERSTKRDWGGNEXCGGXUFJOGCHRLZUCCHNKFICBGBFGIIYXVHEOAFEEWESHQEFLLAERMBGJAPIMAZJIRFEYZFFXRLZLYOGBXBUISPIMAIIORRMPXSMPLCNWMSGQEERZHXQXUXFFTRMPTCZNNSFLZPACXBUISPIWHVYOHWWGXDPJRMGBJWCDINLZPACXBWFGDZCNGPYCMAAIIORRMPTCATYRFVIMERSYHXMGCPNMVRICGUGFZDECUTJFPGWRWRBJKFRKFTACKNEZGHSIFMYSTJIPMICCGGSKFBIGIEYFICBEGBFBLYWVGMCATIQBEORYWRBEHWCYABKSSQXNMVGLFMPAHITQXVHESSULRMYSGPIDNZFXLKFNJDTAXRWTFXKMATCGIMTEHMWSCXUXZFSCGERGHXMRXXPGIMPNPVBUMVPXDSCRMFNEQDLWGBKIIGSATCHWCISYRFVSIQMYOIRLVLZGPTMBERHXMRBYKVTPMTAKCULSGUVWCEJBKTSSRSVGTFXKMATKSDLIFXCTPQKVOVBXLXUXWWURLNFVBSK'''

	dictionary = {}
	lengdict = {}
	sorted_y = []
	
	string1 = ''
	string2 = ''
	string3 = ''
	string4 = ''
	string5 = ''
	string6 = ''
	string7 = ''



	print len(text)/7
	for a in range(0,len(text),7):
		string1+=text[a]
		string2+=text[a+1]
		string3+=text[a+2]
		string4+=text[a+3]
		string5+=text[a+4]
		string6+=text[a+5]
		string7+=text[a+6]



	'''
	string1dict = getLetterCount(string1)
	string2dict = getLetterCount(string2)
	string3dict = getLetterCount(string3)
	string4dict = getLetterCount(string4)
	string5dict = getLetterCount(string5)
	string6dict = getLetterCount(string6)
	string7dict = getLetterCount(string7)

	add_freq(englishLetterFreq)

	#x = stats.chisquare(string1freq, englishLetterFreq)
	
	get_most_likely_letter(string1)
	get_most_likely_letter(string2)
	get_most_likely_letter(string3)
	get_most_likely_letter(string4)
	get_most_likely_letter(string5)
	get_most_likely_letter(string6)
	get_most_likely_letter(string7)
	'''

	#population variance
	print 'population variance for English Language'
	print_var(englishLetterFreq)


	print 'population variance for plaintext'
	regtext = '''ETHICSLAWANDUNIVERSITYPOLICIESTODEFENDASYSTEMYOUNEEDTOBEABLETOTHINKLIKEANATTACKERANDTHATINCLUDESUNDERSTANDINGTECHNIQUESTHATCANBEUSEDTOCOMPROMISESECURITYHOWEVERUSINGTHOSETECHNIQUESINTHEREALWORLDMAYVIOLATETHELAWORTHEUNIVERSITYSRULESANDITMAYBEUNETHICALUNDERSOMECIRCUMSTANCESEVENPROBINGFORWEAKNESSESMAYRESULTINSEVEREPENALTIESUPTOANDINCLUDINGEXPULSIONCIVILFINESANDJAILTIMEOURPOLICYINEECSISTHATYOUMUSTRESPECTTHEPRIVACYANDPROPERTYRIGHTSOFOTHERSATALLTIMESORELSEYOUWILLFAILTHECOURSEACTINGLAWFULLYANDETHICALLYISYOURRESPONSIBILITYCAREFULLYREADTHECOMPUTERFRAUDANDABUSEACTCFAAAFEDERALSTATUTETHATBROADLYCRIMINALIZESCOMPUTERINTRUSIONTHISISONEOFSEVERALLAWSTHATGOVERNHACKINGUNDERSTANDWHATTHELAWPROHIBITSYOUDONTWANTTOENDUPLIKETHISGUYIFINDOUBTWECANREFERYOUTOANATTORNEYPLEASEREVIEWITSSPOLICIESONRESPONSIBLEUSEOFTECHNOLOGYRESOURCESANDCAENSPOLICYDOCUMENTSFORGUIDELINESCONCERNINGPROPERUSEOFINFORMATIONTECHNOLOGYATUMASWELLASTHEENGINEERINGHONORCODEASMEMBERSOFTHEUNIVERSITYCOMMUNITYYOUAREREQUIREDTOABIDEBYT'''
	regtextcount = getLetterCount(regtext)
	regtextfreq = getLetterfreq(regtextcount, len(regtext))
	print_var(regtextfreq)

	print 'population variance for YZ'
	mes1 = encrypt(regtext, 'YZ')
	print len(mes1)
	print len(regtext)

	regtextcount = getLetterCount(mes1)
	regtextfreq = getLetterfreq(regtextcount, len(regtext))
	print_var(regtextfreq)
	

	for a in range(0,len(mes1),2):
		string1+=mes1[a]
		string2+=mes1[a+1]
		
	
	regtextcount = getLetterCount(string1)
	regtextfreq = getLetterfreq(regtextcount, len(string1))
	total = print_var(regtextfreq)
	
	regtextcount = getLetterCount(string2)
	regtextfreq = getLetterfreq(regtextcount, len(string2))
	total += print_var(regtextfreq)
	total/=2
	print total

	print 'population variance for XYZ'
	mes2 = encrypt(regtext, 'XYZ')
	regtextcount = getLetterCount(mes2)
	regtextfreq = getLetterfreq(regtextcount, len(regtext))
	print_var(regtextfreq)


	for a in range(0,len(mes2)-3,3):
		string1+=mes1[a]
		string2+=mes1[a+1]
		string3+=mes1[a+2]
		

	regtextcount = getLetterCount(string1)
	regtextfreq = getLetterfreq(regtextcount, len(string1))
	total = print_var(regtextfreq)
	
	regtextcount = getLetterCount(string2)
	regtextfreq = getLetterfreq(regtextcount, len(string2))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string3)
	regtextfreq = getLetterfreq(regtextcount, len(string3))
	total += print_var(regtextfreq)
	total/=3
	print total

	print 'population variance for WXYZ'
	mes3 = encrypt(regtext, 'WXYZ')
	regtextcount = getLetterCount(mes3)
	regtextfreq = getLetterfreq(regtextcount, len(regtext))
	print_var(regtextfreq)

	for a in range(0,len(mes3)-4,4):
		if text[a] in LETTERS:
			string1+=mes1[a]
		if text[a+1] in LETTERS:
			string2+=mes1[a+1]
		if text[a+2] in LETTERS:
			string3+=mes1[a+2]
		if text[a+3] in LETTERS:
			string4+=mes1[a+3]
		
	regtextcount = getLetterCount(string1)
	regtextfreq = getLetterfreq(regtextcount, len(string1))
	total = print_var(regtextfreq)
	
	regtextcount = getLetterCount(string2)
	regtextfreq = getLetterfreq(regtextcount, len(string2))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string3)
	regtextfreq = getLetterfreq(regtextcount, len(string3))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string4)
	regtextfreq = getLetterfreq(regtextcount, len(string4))
	total += print_var(regtextfreq)
	total/=4
	print total

	print 'population variance for VWXYZ'
	mes4 = encrypt(regtext, 'VWXYZ')
	regtextcount = getLetterCount(mes4)
	regtextfreq = getLetterfreq(regtextcount, len(regtext))
	print_var(regtextfreq)

	for a in range(0,len(mes4),5):
		string1+=mes1[a]
		string2+=mes1[a+1]
		string3+=mes1[a+2]
		string4+=mes1[a+3]
		string5+=mes1[a+4]
		
	regtextcount = getLetterCount(string1)
	regtextfreq = getLetterfreq(regtextcount, len(string1))
	total = print_var(regtextfreq)
	
	regtextcount = getLetterCount(string2)
	regtextfreq = getLetterfreq(regtextcount, len(string2))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string3)
	regtextfreq = getLetterfreq(regtextcount, len(string3))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string4)
	regtextfreq = getLetterfreq(regtextcount, len(string4))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string5)
	regtextfreq = getLetterfreq(regtextcount, len(string5))
	total += print_var(regtextfreq)
	total/=5
	print total

	print 'population variance for UVWXYZ'
	mes5 = encrypt(regtext, 'UVWXYZ')
	regtextcount = getLetterCount(mes5)
	regtextfreq = getLetterfreq(regtextcount, len(regtext))
	print_var(regtextfreq)

	for a in range(0,len(mes5)-5,6):
		string1+=mes1[a]
		string2+=mes1[a+1]
		string3+=mes1[a+2]
		string4+=mes1[a+3]
		string5+=mes1[a+4]
		string6+=mes1[a+5]
		
	regtextcount = getLetterCount(string1)
	regtextfreq = getLetterfreq(regtextcount, len(string1))
	total = print_var(regtextfreq)
	
	regtextcount = getLetterCount(string2)
	regtextfreq = getLetterfreq(regtextcount, len(string2))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string3)
	regtextfreq = getLetterfreq(regtextcount, len(string3))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string4)
	regtextfreq = getLetterfreq(regtextcount, len(string4))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string5)
	regtextfreq = getLetterfreq(regtextcount, len(string5))
	total += print_var(regtextfreq)

	regtextcount = getLetterCount(string6)
	regtextfreq = getLetterfreq(regtextcount, len(string6))
	total += print_var(regtextfreq)
	total/=6
	print total

main()
















