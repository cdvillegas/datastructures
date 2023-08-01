from datastructures.minheap import MinHeap

class Sort:
	@staticmethod
	def heap_sort(arr):
		# Builds a Min Heap and repeatedly removes 
		# the smallest element
	    heap = MinHeap()
	    for item in arr:
	        heap.push(item)
	    return [heap.pop() for _ in range(len(heap))]

	@staticmethod
	def merge_sort(arr):
		# Recursively splits the array into halves, 
		# sorts them, and merges them back together
		def merge_sorted_arrays(a, b):
			res = []
			i = j = 0
			while i < len(a) and j < len(b):
				if a[i] < b[j]:
					res.append(a[i])
					i += 1
				else:
					res.append(b[j])
					j += 1
			res.extend(a[i:])
			res.extend(b[j:])
			return res
		if len(arr) < 2:
		    return arr
		else:
		    mid = len(arr) // 2
		    return merge_sorted_arrays(Sort.merge_sort(arr[:mid]), Sort.merge_sort(arr[mid:]))

	@staticmethod
	def quick_sort(arr):
		# Partitions the array and then recursively 
		# sorts the two resulting subarrays
	    def quick_sort_util(arr, lo, hi):
	        if lo < hi:
	            split = partition(arr, lo, hi)
	            quick_sort_util(arr, lo, split - 1)
	            quick_sort_util(arr, split, hi)
	    def partition(arr, lo, hi):
	        pivot = arr[hi]
	        for j in range(lo, hi):
	            if arr[j] <= pivot:
	                arr[lo], arr[j] = arr[j], arr[lo]
	                lo += 1
	        arr[lo], arr[hi] = arr[hi], arr[lo]
	        return lo
	    quick_sort_util(arr, 0, len(arr) - 1)
	    return arr

	@staticmethod
	def bubble_sort(arr):
		# Repeatedly steps through the array, compares adjacent 
		# elements and swaps them if they are in the wrong order
	    n = len(arr)
	    for i in range(n):
	        for j in range(0, n - i - 1):
	            if arr[j] > arr[j + 1]:
	                arr[j], arr[j + 1] = arr[j + 1], arr[j]
	    return arr

	@staticmethod
	def insertion_sort(arr):
		# Builds a sorted array one element at a time by comparing 
		# each element with the previous elements and inserting it 
		# into its correct position
	    for i in range(1, len(arr)):
	        key = arr[i]
	        j = i - 1
	        while j >= 0 and key < arr[j]:
	            arr[j + 1] = arr[j]
	            j -= 1
	        arr[j + 1] = key
	    return arr

	@staticmethod
	def selection_sort(arr):
		# Repeatedly selects the smallest element from the 
		# unsorted part and moves it to the beginning
	    for i in range(len(arr)):
	        min_idx = i
	        for j in range(i + 1, len(arr)):
	            if arr[min_idx] > arr[j]:
	                min_idx = j
	        arr[i], arr[min_idx] = arr[min_idx], arr[i]
	    return arr