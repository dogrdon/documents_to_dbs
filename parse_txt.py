def open_file(f):
	with open(f, 'rb') as fopen:
		doc = fopen.read()

		txtstr = ''

		for line in doc:
			toadd = ''

			if line == '\n\n':
				toadd = '|'
				txtstr += toadd

			else:
				toadd = line
				txtstr += toadd


		txtlst = txtstr.split('||')

		for e in txtlst:

			print e, '===-=-=-====-=-=-=-=-=-=-='

open_file('sandbox_docs/madagascar_test.txt')