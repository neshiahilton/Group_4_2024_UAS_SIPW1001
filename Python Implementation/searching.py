class Searching:
    def linear_search(self, arr, target):
        """
        Linear Search Algorithm
        :param arr: List of elements
        :param target: Element to search
        :return: Index of the target if found, else -1
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def binary_search(self, arr, target):
        """
        Binary Search Algorithm
        :param arr: Sorted list of elements
        :param target: Element to search
        :return: Index of the target if found, else -1
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Testing
if __name__ == "__main__":
    searching = Searching()

    # Testing Linear Search
    arr = [10, 20, 30, 40, 50]
    target = 30
    print(f"Linear Search: Target {target} found at index:", searching.linear_search(arr, target))

    # Testing Binary Search
    sorted_arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    print(f"Binary Search: Target {target} found at index:", searching.binary_search(sorted_arr, target))

    # Additional Tests
    print(f"Linear Search (not found): Target 100 found at index:", searching.linear_search(arr, 100))
    print(f"Binary Search (not found): Target 2 found at index:", searching.binary_search(sorted_arr, 2))
