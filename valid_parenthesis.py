"""
Given a string s containing only the characters (, ), {, }, [, ], determine if the input string is valid.
An input string is valid if open brackets are closed by the same type of brackets and in the correct order.
"""


class ValidParenthesis:
    def __init__(self, string):
        self.string = string

    def check_validity(self):
        stack = []
        for char in self.string:
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            else:
                if not stack or char != stack.pop():
                    return False
        return True

    def print_statement(self):
        result = self.check_validity()
        if result:
            print(f"The string '{self.string}' is valid.")
        else:
            print(f"The string '{self.string}' is not valid.")


def main():
    test_string = "({[]afasf})"
    validator = ValidParenthesis(test_string)
    validator.print_statement()


if __name__ == "__main__":
    main()
