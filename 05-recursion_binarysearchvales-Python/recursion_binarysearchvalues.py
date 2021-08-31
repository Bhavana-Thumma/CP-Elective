def binary_search2(arr,lo,hi,x,l):
	if hi >= lo:
		mid = (hi + lo) // 2
		l.append((mid, arr[mid]))
		if arr[mid] == x:
			return l
		elif arr[mid] > x:
			return binary_search2(arr, lo, mid - 1, x, l) 
		else:
			return binary_search2(arr, mid + 1, hi, x, l) 
	else:
		return l

def recursion_binarysearchvalues(L, v):
	l =[]
	lo = 0
	hi = len(L)-1
	return binary_search2(L,lo,hi,v,l)

	