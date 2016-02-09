"""Example showing lists in defopt.

Lists are automatically converted to required flags
which accept zero or more arguments.

Code usage:
    main([1.2, 3.4], 2)

Command line usage:
    lists.py 2 --numbers 1.2 3.4
    lists.py --numbers 1.2 3.4 -- 2
"""
import defopt


@defopt.main
def main(numbers, multiplier):
    """Example function with a list argument.

    :param list[float] numbers: List of numbers to multiply
    :param float multiplier: Amount to multiply by
    """
    print([x * multiplier for x in numbers])


if __name__ == '__main__':
    defopt.run()
