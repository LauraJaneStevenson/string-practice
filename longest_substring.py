def longest_substring(word):
"""Given a string, find the length of the longest 
substring without repeating characters."""


	longest = 0 
	count = 0 
	start = 0

	for i in range(1,len(word)):

		sub = word[start:i]

		if word[i] in sub:

			start = i 

			if len(sub) > longest:

				longest = len(sub)

	return longest

print(longest_substring("abcabcbb"))