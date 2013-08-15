class EduInt:
	__value = 0

	def __init__(self, value):
		self.__value = value

	def __str__(self):
		return str(self.__value)

	'''
		Binary number's power 
		O(logn)
		a ** n = (a ** (n/2)) * (a ** (n/2))
		a ** n = (a ** (n - 1)) * a
	'''
	def powm(self, n, m):
		v = self.__value;
		d = 1
		while (n > 0):
			if (n & 1 == 1):					
				d = (d * v) % m
			v = (v * v) % m			
			n = n >> 1
		return d