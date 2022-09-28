#! /usr/bin/env python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re


phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code first group 0
    (\s|-|\.)?                        # separator               1
    (\d{3})                           # first 3 digits          2
    (\s|-|\.)                         # separator               3
    (\d{4})                           # last 4 digits           4
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension               5
    )''', re.VERBOSE)


email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+			# username in a character class 
	@							# @ symbol
	[a-zA-Z0-9.-]+				# domain name
	(\.[a-zA-Z]{2,4})			# Dot something
	)''', re.VERBOSE) 



text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
	phone_num = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phone_num += ' x' + groups[8]
	matches.append(phone_num)

for groups in email_regex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found')

