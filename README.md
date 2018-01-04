# Data Encryption Algorithm and GUI
This project implement the data encryption algorithm using Python
it can decode or encode the content.
Then designed the GUI using Qt5

Encryption	algorithm:
Step	1:	key	generation
1. Generate	a	32	bit	key	by generating	a	random	32-bit	binary	number	(can	be	stored	as	an	
unsigned	integer)	and	store	it	in	a	file	named	‘my_key.txt’	as	a	8-byte	string	
representing	that	number	as	a	hex-string.
2. Share	this	key	with	whoever	shall	be	enabled	to	decrypt	your	data.	(never	over	the	
Internet	if	you	want	to	keep	it	secure!)
Step	2:	encryption
1. Convert	whatever	data	type	to	its	string	representation.
2. For	processing,	break	the	string	representation	into	4-byte	packages,	encrypt	these	
packages	using	PACKAGE	XOR	KEY	(bitwise	XOR) and	assemble	those	packages	in	hex	
format	as	the	encrypted	message.
3. Double	encrypt	that	message	using	the	mirrored	key	(swap	bits	0	and	31,	1	and	30,	…,	of	
the	KEY	and	use	that	as	the	key)
Step	3:	decryption
• Develop	a	decryption	procedure	using	the	relation	(X	XOR	KEY)	XOR	KEY	=	X	(Try	
applying	xor	1	and	xor	0	to	any	binary	number	once,	then	twice	to	see	how	this	works)2. Decoding algorithm
Create a class Crypto which includes the following methods:
o SetKey(keyfilename): # set a previously generated key from file
o GenerateKey(): # generate a brand new key using random values. Each run should
generate a different (random) key.
o GenerateKey(32digit_binary_string) # generate a brand new key from value
o Encrypt(string): # return encrypted string
o UnEncrypt(string): # return deciphered string
