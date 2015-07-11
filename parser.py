import mailbox, sys, os
from collections import Counter

def count_email(n):
	email_list = []
	for mess in mbox:

		to = str(mess['to']).split(', ')
		for email in to:
			email_list.append(email)

		email_list.append(mess['from'])

		if mess['cc'] != None:
			cc = str(mess['cc']).split(', ')
			for email in cc:
				email_list.append(email)

	print("\nTOP %s EMAIL ADDRESSES FOUND!" %n)
	print_out(Counter(email_list).most_common(n))

def pairToTo():
	pairs_list = []
	for mess in mbox:
		to = str(mess['to']).split(', ')
		if (len(to) > 0):
			for i in range(0, len(to)):
				for j in range(i+1,len(to)):
					print(str(to[i]) + "---" + str(to[j]))
		else:
			print("No results were found!")

def pairToFrom():
	pairs_list = []
	for mess in mbox:
		to = str(mess['to']).split(', ')
		for i in range(0, len(to)):
			print(str(to[i]) + "---" + str(mess['from']))

def pairToCC():
	pairs_list = []
	for mess in mbox:
		to = str(mess['to']).split(', ')
		if (mess['cc'] != None):
			cc = str(mess['cc']).split(', ')
			for i in range(0, len(to)):
				for j in range(0, len(cc)):
					print(str(to[i]) + "---" + str(cc[j]))

def pairCCFrom():
	pairs_list = []
	for mess in mbox:
		if (mess['cc'] != None):
			cc = str(mess['cc']).split(', ')
			for i in range(0, len(cc)):
				print(str(cc) + "---" + str(mess['from']))

def print_out(a):
	for email, count in a:
   		print '---- %s was found %d times' % (email, count)

def main(filename):
    try:
    	global mbox
        mbox = mailbox.mbox(filename)
        pairToCC()
    except (IOError):
        print("cannot open " + filename)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pyParse <filename>")
    else:
        main(sys.argv[1])