class Arrays:
    def kadanes_algorithm(self, nums):
        """
        Kadane's Algorithm to find the maximum subarray sum
        :param nums: List of integers
        :return: Maximum sum
        """
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

    def kmp_algorithm(self, text, pattern):
        """
        Knuth-Morris-Pratt (KMP) Algorithm for pattern matching
        :param text: The main text
        :param pattern: The pattern to find
        :return: Starting index of the pattern in text, -1 if not found
        """
        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
            return lps

        lps = compute_lps(pattern)
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def floyd_cycle_detection(self, head):
        """
        Floyd's Cycle Detection Algorithm
        :param head: Head of the linked list
        :return: True if a cycle is detected, False otherwise
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Testing
if __name__ == "__main__":
    arrays = Arrays()

    # Testing Kadane's Algorithm
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print("Maximum Subarray Sum (Kadane's):", arrays.kadanes_algorithm(nums))

    # Testing KMP Algorithm
    text = "ababcabcabababd"
    pattern = "ababd"
    print(f"Pattern '{pattern}' found at index:", arrays.kmp_algorithm(text, pattern))

    # Testing Floyd's Cycle Detection
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    # Create linked list with a cycle
    head = Node(1)
    second = Node(2)
    third = Node(3)
    head.next = second
    second.next = third
    third.next = second  # Create cycle

    print("Cycle detected in linked list:", arrays.floyd_cycle_detection(head))
