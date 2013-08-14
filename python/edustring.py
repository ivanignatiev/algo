class EduString:
	__str = ""

	def __init__(self, str):
		self.__str = str

	def toString(self):
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
		while (index < len(self.__str)):
			while (index < len(self.__str) 
					and needle[0] != self.__str[index]):
				index = index + 1
			while (sublen < len(needle) 
					and index < len(self.__str) 
					and needle[sublen] == self.__str[index + sublen]):
				sublen = sublen + 1
			if (sublen == len(needle)):
				return (index)
			index = index + 1
		return -1
