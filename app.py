import click


@click.command()
@click.argument("input", type=click.File("r"), default='input.txt')
def app(input):
    """This script finds all pair summing a certain number.
    \b
    Copy stdin to stdout:
        inout - -
    """
    # Read the file assuming each line could be a different input.
    for line in input.readlines():
        numbers, target = line.split()
        try:
            # parsing strings in file into integers
            target = int(target)
            numbers = [int(char) for char in numbers.split(",")]
            print(numbers, target)
        except Exception as error:
            print(f'Error reading line: {line}')
            print(f'Please check the input is in the expected format')
        else:
            # If no parsing error, find pairs with the required sum.
            pairs = find_pairs_with_sum(numbers, target)
            print(f'All pairs suming {target}: {pairs}')


def find_pairs_with_sum(numbers, target):
    """_summary_

    Args:
        numbers (_type_): _description_
        target (_type_): _description_
    """
    complement_search = dict()
    pairs = []

    for number in numbers:
        complement_seen = complement_search.get(number)
        if number in complement_search :
            # This case means the other number making the pair was seen before.
            pairs.append((complement_seen, number))
        else:
            # save the complement in a dict, in order to find it later quickly.
            complement_search[target - number] = number

    return pairs
