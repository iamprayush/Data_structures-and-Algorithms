# Fenwick Tree (AKA Binary Indexed Tree) implemented in Python
# Point Update - O(logn)
# Range Queries - O(logn)
# Tree construction - O(nlogn)

class Fenwick():
	def update(self, ind, val):                 # add val to the ind-th position
		while ind <= val:
			self.tree[ind-1] += x
			ind += ind & (-ind)         # righmost set bit

	def query(self, ind):                       # find the ind-th prefix sum
		ans = 0
		while ind > 0:
			ans += self.tree[ind-1]
			ind -= ind & (-ind)
		return ans

	def __init__(self, arr):
		self.n = len(arr)
		self.tree = [0 for i in range(self.n)]
		for i in range(1, self.n+1):
			self.update(i, arr[i-1])    # one based indexing
