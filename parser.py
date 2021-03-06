import mailbox, sys, os
from collections import Counter

def count_email(n):
	email_addresses_list = []
	for mess in mbox:

		to = str(mess['to']).split(', ')
		for email in to:
			email_addresses_list.append(email)

		email_addresses_list.append(mess['from'])

		if mess['cc'] != None:
			cc = str(mess['cc']).split(', ')
			for email in cc:
				email_addresses_list.append(email)

	print("\nTOP %s EMAIL ADDRESSES FOUND!" %n)
	print_out(Counter(email_addresses_list).most_common(n))

def pair_To_To():
	pairs_list = []
	for mess in mbox:
		to = str(mess['to']).split(', ')
		for i in range(0, len(to)):
			for j in range(i+1,len(to)):
				pairs_list.append(str(to[i]) + "---" + str(to[j]))
	return pairs_list

def pair_To_From():
	pairs_list = []
	for mess in mbox:
		to = str(mess['to']).split(', ')
		for i in range(0, len(to)):
			pairs_list.append(str(to[i]) + "---" + str(mess['from']))
	return pairs_list

def pair_To_CC():
	pairs_list = []
	for mess in mbox:
		to = str(mess['to']).split(', ')
		if (mess['cc'] != None):
			cc = str(mess['cc']).split(', ')
			for i in range(0, len(to)):
				for j in range(0, len(cc)):
					pairs_list.append(str(to[i]) + "---" + str(cc[j]))
	return pairs_list

def pair_CC_From():
	pairs_list = []
	for mess in mbox:
		if (mess['cc'] != None):
			cc = str(mess['cc']).split(', ')
			for i in range(0, len(cc)):
				print(str(cc) + "---" + str(mess['from']))
	return pairs_list

def count_pairs(n):
	pairs_list = []

	for mess in mbox:
		to = str(mess['to']).split(', ')
		for i in range(0, len(to)):
			for j in range(i+1,len(to)):
				pairs_list.append(str(to[i]) + " --- " + str(to[j]))
			pairs_list.append(str(to[i]) + " --- " + str(mess['from']))
		if (mess['cc'] != None):
			cc = str(mess['cc']).split(', ')
			for i in range(0, len(to)):
				for j in range(0,len(cc)):
					pairs_list.append(str(to[i]) + " --- " + str(cc[j]))
					pairs_list.append(str(cc[j]) + " --- " + str(mess['from']))

	print("\nTOP %s EMAIL ADDRESS PAIRS FOUND!" %n)
	print_out(Counter(pairs_list).most_common(n))

def related_emails(email, n):
	emails+
	for mess in mbox:
		if (str(mess['to']) == email):


def print_out(a):
	for email, count in a:
   		print '    %d %s' % (count, email)

def main(filename):
    try:
    	global mbox
        mbox = mailbox.mbox(filename)
        count_pairs(5)
    except (IOError):
        print("cannot open " + filename)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pyParse <filename>")
    else:
        main(sys.argv[1])