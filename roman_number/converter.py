## Convert Integer to Roman Number and vice versa

class Converter:

	def int_to_roman(self, num):
		"Convert integer to roman number"
		val = [1, 4, 5, 9, 10,
			   40, 50, 90, 100,
			   400, 500, 900, 1000]

		sb = ["I", "IV", "V", "IX", "X",
			  "XL", "L", "XC", "C",
			  "CD", "D", "CM", "M"]

		roman_num = ""
		int_num = num
		i = len(val)-1
		while int_num > 0:
			for _ in range(int_num // val[i]):
				roman_num += sb[i]
				int_num -= val[i]
			i -= 1
		return roman_num

	def roman_to_int(self, s):
		"Convert roman number to integer"
		roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
					 'C': 100, 'D': 500, 'M': 1000}
		int_num = 0
		for i in range(len(s)):
			if i > 0 and roman_val[s[i]] > roman_val[s[i-1]]:
				int_num += roman_val[s[i]] - 2 * roman_val[s[i-1]]
			else:
				int_num += roman_val[s[i]]
		return int_num


########## Unit Tests ##########
def test():
	converter = Converter()
	assert(converter.int_to_roman(1) == 'I')
	assert(converter.int_to_roman(4000) == 'MMMM')
	assert(converter.roman_to_int('MMMCMLXXXVI') == 3986)
	assert(converter.roman_to_int('MMMM') == 4000)
	assert(converter.roman_to_int('IX') == 9)
	print('All test passed.')

test()