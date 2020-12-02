"""
Python 3.7.9
Author: Adam Turner <turner.adch@gmail.com>
Note: I was following the tutorial at https://www.programiz.com/python-programming/closure
"""


def main():

    def print_msg(msg):
        """Outer enclosing function."""

        def printer():
            """Nested function."""
            print(msg)
            return None

        return printer

    # function closure
    # output: "Hello"
    print_hello = print_msg("Hello")
    print_hello()

    # output: "Hello"
    del print_msg
    print_hello()
    
    return None


if __name__ == "__main__":
    main()
