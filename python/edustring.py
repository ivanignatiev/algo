class EduString:
	__str = ""

	def __init__(self, str):
		self.__str = str

	def __str__(self):
		return self.__str

	'''
		Simple substring search
		O(n * k) , n = len(_str), k = len(needle)
		@param string needle Substring
	'''
	def simpleSearch(self, needle):
		if (len(needle) == 0):
			return 0
		index = 0
		sublen = 0
		dlen = len(self.__str) - len(needle) + 1
		if (dlen <= 0):
			return -1
		while (index < dlen):
			while (index < dlen
					and needle[0] != self.__str[index]):
				index = index + 1
			if (index < dlen):
				while (sublen < len(needle) 
						and needle[sublen] == self.__str[index + sublen]):
					sublen = sublen + 1
				if (sublen == len(needle)):
					return (index)
			index = index + 1
		return -1
