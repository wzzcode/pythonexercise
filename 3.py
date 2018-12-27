def mutate(r1,r2):
	return r2,r1

import math

def max_of_domino(L,R,first,last,W):
	if (last-first) == 0:
		return
	else:
		# R[first-1] = 0
		# L.append
		Max = simplify_max_of_domino(L,R,first,last)
	return Max

def simplify_max_of_domino(L,R,first,last):
	if (last-first) == 1 :
		max = R[first] * L[last]
	else:
		mid = int(math.ceil((first + last)/2))
		if L[mid]>R[mid]:
			MaxL1 = simplify_max_of_domino(L,R,first,mid)
			MaxR1 = simplify_max_of_domino(L,R,mid,last)
			Max1 = MaxL1 + MaxR1
			mutate(L[mid],R[mid])
			MaxL0 = simplify_max_of_domino(L,R,first,mid)
			MaxR0 = simplify_max_of_domino(L,R,first,mid)
			Max0 = MaxL0 + MaxR0
			if Max1 > Max0:
				Max = Max1 , w[mid] = 1
			else:
				Max = Max0 , w[mid] = 0		
		else:
			MaxL0 = simplify_max_of_domino(L,R,first,mid)
			MaxR0 = simplify_max_of_domino(L,R,mid,last)
			Max0 = MaxL0 + MaxR0
			mutate(L[mid],R[mid])
			MaxL1 = simplify_max_of_domino(L,R,first,mid)
			MaxR1 = simplify_max_of_domino(L,R,mid,last)
			Max1 = MaxL1 + MaxR1
			if Max1 > Max0:
				Max = Max1 , w[mid] = 1
			else:
				Max = Max0 , w[mid] = 0		
	return max

L=[5,4,9,7,3,11]
R=[8,2,6,7,9,10]
first = 1
last = len(L)
w=[0,1,1,0,0,1]
max_of_domino(L,R,first,last,w)
print(Max)