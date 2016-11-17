import string,sys
n = string.digits + string.ascii_uppercase+string.ascii_lowercase
def m(h,bit):#umwandlend
        
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
                        t.reverse()
                        
                        return t

def reb(l,b):# von irgendwas in dec
        
        
	k = 0
	a = 0
	for i in l:
                
                k += n.index(str(i))*b**a
                a += 1
	return k


if __name__ == "__main__":
        #print(m(15,16))
        l1,l2,l3 =  sys.argv[1],sys.argv[2],sys.argv[3]
        #g = reb(sys.argv[1],int(l2))
        #print g
        #print(m(g,int(l3)))
        
        g =  reb(list(reversed(l1)),int(l2))
      
        print "".join(m(g,int(l3)))
        
        
        
        
        #print(reb(reb(sys.argv[1],int(sys.argv[2])),int(sys.argv[3])))
        
