class FG :
	class It :
		def __init__ (self, j) :
			self.a = 1
			self.b = j
			
		def __iter__ (self) :
			return self
			
		def __next__ (self) :
			ret = self.a
			print("NEXT\n")
			while self.a <= self.b :
				printf("WOO\n")
				yield ret
				self.a += 1
			raise StopIteration

	def __init__ (self,ceil) :
		self.i = 1
		self.j = ceil
		
	def __iter__ (self) :
		return FG.It(self.j)
		
def f(b) :
	if b :
		raise TypeError()
		
def h(b):
	try:
		g(b)
		print("h1",end = " ")
	except TypeError :
		print("except_h",end=" ")
	else :
		print("else_h",end=" ")
	finally:
		print("finally_h",end=" ")
	print("h2")

def g(b):
	try:
		f(b)
		print("g1",end = " ")
	except KeyError :
		print("except_g",end=" ")
	else :
		print("else_g",end=" ")
	finally:
		print("finally_g",end=" ")
	print("g2")
	