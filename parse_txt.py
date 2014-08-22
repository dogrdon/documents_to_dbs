from repr import repr
import re


def open_file(f):
	with open(f, 'rb') as fopen:
	    doc = fopen.read()

	    txtstr = ''

	    print type(doc)

	    doc = doc.replace('\n', '|')
	    doc = doc.replace('| |', '||')
	    #doc = doc.replace('||', ',')
	    #print doc

	    sdoc = doc.split('|||')
	    #but first change any number of tabs to a space?
	    sdoc = [re.sub(r'\t+', ' ', i) for i in sdoc]
	    sdoc = [i.replace('||', '\t') for i in sdoc]

	    print len(sdoc)

	    for x in sdoc:
	    	print x, '==============\n'


	    '''
		for line in doc:
			toadd = ''

			if line == '\n\n\n':
				toadd = '||'
				txtstr += toadd

			elif line == '\n\n':
				toadd = '|'
				txtstr += toadd

			else:
				toadd = line
				txtstr += toadd

		print repr(txtstr)
				
		txtlst = txtstr.split('||')

		print len(txtlst)
		'''
		#for e in txtlst:

		#	print e, '===-=-=-====-=-=-=-=-=-=-='
		
open_file('sandbox_docs/madagascar_test.txt')