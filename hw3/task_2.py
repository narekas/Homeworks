# The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise.
import re
phon = input('Enter a phone number: ')
print('Valid' if re.match(r'1-\d{3}-\d{3}-\d{4}', phon) or re.match(r'\d{3}-\d{3}-\d{4}', phon) else 'Invalid')
