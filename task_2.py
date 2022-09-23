# a program that asks the user to enter a character, checks and prints whether the character is a consonant or a vowel.

ch = input('Enter a character: ').lower()

print('is a Vowel' if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u') else 'is a Consonant')
