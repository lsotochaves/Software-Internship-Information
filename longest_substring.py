class FindLongest:
    def __init__(self, s):
        self.s = s
        self.max_string = 0

    def find_longest(self):
        # Dictionary storing the last index where each character was seen
        seen_dict = {}
        # Left boundary of the sliding window
        left = 0

        # Iterate through the string using right as the window's right boundary
        for right, value in enumerate(self.s):
            # If the character repeats, move left forward if needed
            if value in seen_dict:
                left = max(left, seen_dict[value] + 1)

            # Update last seen index of the current character
            seen_dict[value] = right

            # Length of the current window without duplicates
            current_length = right - left + 1

            # Update the maximum length found so far
            self.max_string = max(self.max_string, current_length)

        # Return the longest length found
        return self.max_string


def main():
    # Test cases in the form: (input_string, expected_result)
    test_cases = [
        ("", 0),  # empty string
        ("a", 1),  # single character
        ("aaaa", 1),  # all characters the same
        ("abcabcbb", 3),  # repeating pattern
        ("bbbbb", 1),  # repeated single character
        ("pwwkew", 3),  # non-adjacent repeat
        ("abba", 2),  # left pointer must not move backwards
        ("abacdbd", 4),  # mixed repeats
        ("abcdef", 6),  # all characters unique
        ("dvdf", 3),  # overlapping window
    ]

    # Run each test case and compare expected vs obtained result
    for s, expected in test_cases:
        test_object = FindLongest(s)
        obtained = test_object.find_longest()

        # Simple pass/fail indicator
        status = "PASS" if obtained == expected else "FAIL"

        print(f"String: '{s}' | Expected: {expected} | Obtained: {obtained} | {status}")


if __name__ == "__main__":
    main()
