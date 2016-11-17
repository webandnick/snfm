import string
n = string.digits + string.ascii_uppercase+string.ascii_lowercase
def m(h,bit):
        
	u = True
	t = []
	while(u):
                a = h%bit
		h = h/bit
		if (a > 10):
                        t.append(n[a])
                else:
                        
                        t.append(a)
                        
		if(h == 0):
		
			return t

def reb(l,b):
        
	k = 0
	a = 0
	for i in l:
                k += n.index(str(i))*b**a
                a += 1
	return k


