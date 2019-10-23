from heap import Heap

# Sorts array l using a min heap
def heap_sort(arr):
	heap = Heap()
	for item in arr:
		heap.push(item)

	return [heap.pop() for _ in range(len(heap))]

def merge_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		mid = (len(arr) + 1) // 2
		return merge_sorted_arrays(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

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
	if i < len(a): res.extend(a[i:])
	if j < len(b): res.extend(b[j:])

	return res

# Quick sort that pivots around first item
# Assume on every partion, everything to the
# left of split is less than pivot, and 
# Everything to the right is greater
def quick_sort(arr):
	def quick_sort_util(arr,lo,hi):
		if lo < hi: 
			split = partition(arr, lo, hi)
			quick_sort_util(arr, lo, split - 1)
			quick_sort_util(arr, split + 1, hi)
		return arr
	return quick_sort_util(arr, 0, len(arr) - 1)

def partition(arr, lo, hi): 
	pivot = arr[hi]
	for j in range(lo, hi): 
		if arr[j] <= pivot: 
			arr[lo], arr[j] = arr[j], arr[lo] 
			lo += 1
	arr[lo], arr[hi] = arr[hi], arr[lo] 
	return lo


if __name__ == '__main__':
	print(quick_sort([5, 4, 3, 2, 1]))