import sys
from collections import defaultdict

card_deck = sys.argv[1]

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

f = open(card_deck,'r')

#deck = defaultdict(int)
deck = []

for line in f:
    words = line.split()
    deck.append((words[0],words[1]))

print deck


# not having a mulligan equation
# no idea what this means but this is implemented formula 1 
# from the documnet
# given:
# M: number of cards left in the deck 
# N: number of cards drawing 
# X: number of copies of the specific card you want 

def formula_one(M,N,X):
	den = choose(M,N)
	
	sum = 0.0
	for k in range(1,N+1):
		first = choose(M-X,N-k)
		second = choose(X,k)
		sum += first * second 
		
	return float(sum) / float(den)

# testing if got correct probs; worked	
# print notmulligan(60,7,1)

# formula 2 
# starting with basic calculator 
# A: how many basics you want when you draw 
# N: how many cards you are drawing 
# M: number of cards left in the deck 
# Y: number of basics in the deck 

def formula_two(M,N,Y,A):
	
	num_sum = 0.0
	for k in range(A,N+1):
		num_sum += choose(M-Y,N-k) * choose(Y,k)
	
	den_sum = 0.0
	for k in range(1,N+1):
		den_sum += choose(M-Y,N-k)*choose(Y,k)
	
	return float(num_sum) / float(den_sum)
	
# tester
# print formula_two(60,7,2,2)	
# it works 

# probability of getting an ideal starter 
# Y = total number of Basics 
# Yi = number of ideal starters 
# NOTE; NOT SURE WHAT M, N MEAN 
# I AM GUESSING. LOOK AT ARTICLE TO CONFIRM. 
def formula_three(Y,Yi):
	M = 60 
	N = 7
	num = formula_two(M,7,Yi,1)
	den = formula_two(N,7,Y,1)
	
	return float(num / den)
	
# same values as before 
# probability starting game with a certain card in hand 
# assumed that you have at least one basic 
# idk just copying the formulas i have no idea 
# what any of this means
def formula_four(M,N,X,Y):
	
	num_sum = 0.0
	for z in range(1,N):
	
		for k in range(1,N-z+1):
			a = choose(M-X-Y,N-k-z)
			b = choose(X,k)
			c = choose(Y,z)
			num_sum += a * b * c 
			
	den_sum = 0.0
	for k in range(1,N+1):
		
		den_sum += choose(M-Y,N-k) * choose(Y,k)
		
	return float(num_sum) / float(den_sum)
	
	
	
	
			
	
	
	
	
	
	
	
	
	


	
	
	
	





