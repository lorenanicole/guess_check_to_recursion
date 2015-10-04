'''
Problem 1:
Write a program using iteration to determine if a word is a palindrome.

Problem 2:
Rewrite program using recursion.
'''

def iterative_is_palindrome(word):
	for index, char in enumerate(word):
		right_left_index =  -1 if index == 0 else -(index+1)
		if char.lower() != word[right_left_index].lower():
			return False
	return True


print iterative_is_palindrome("civic") == True
print iterative_is_palindrome("mom") == True
print iterative_is_palindrome("reviver") == True
print iterative_is_palindrome("racecar") == True
print iterative_is_palindrome("redivider") == True
print iterative_is_palindrome("car") == False
print iterative_is_palindrome("civics") == False
# print iterative_is_palindrome("Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned")


def recursive_is_palindrome(word):
	if len(word) < 1:
		return True
	else:
		return word[0] == word[-1] and recursive_is_palindrome(word[1:-1])

# word = word.lower().replace(" ", "").replace(",","") 
# Additional logic should you want to compare phrases!
# print recursive_is_palindrome("Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned")

print recursive_is_palindrome("civic") == True
print recursive_is_palindrome("mom") == True
print recursive_is_palindrome("reviver") == True
print recursive_is_palindrome("racecar") == True
print recursive_is_palindrome("redivider") == True
print recursive_is_palindrome("car") == False
print recursive_is_palindrome("civics") == False