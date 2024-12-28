class Sorting:
    def bubble_sort(self, arr):
        """
        Bubble Sort Algorithm
        :param arr: List of numbers to sort
        :return: Sorted list
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def merge_sort(self, arr):
        """
        Merge Sort Algorithm
        :param arr: List of numbers to sort
        :return: Sorted list
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def quick_sort(self, arr):
        """
        Quick Sort Algorithm
        :param arr: List of numbers to sort
        :return: Sorted list
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)


# Testing
if __name__ == "__main__":
    sorting = Sorting()

    # Testing Bubble Sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)
    print("Bubble Sorted Array:", sorting.bubble_sort(arr[:]))

    # Testing Merge Sort
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original Array:", arr)
    print("Merge Sorted Array:", sorting.merge_sort(arr[:]))

    # Testing Quick Sort
    arr = [10, 7, 8, 9, 1, 5]
    print("Original Array:", arr)
    print("Quick Sorted Array:", sorting.quick_sort(arr[:]))
