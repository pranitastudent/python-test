# from byotest import *
# usd_coins = [100, 50, 25, 10, 5, 1]
# euro_coins = [100, 50, 20, 10, 5, 2, 1]


# def get_change(amount, coins=euro_coins):
#     """
#     Takes the payment amount and returns the change
#     `amount` the amount of money that we need to provide change for
#     Returns a list of coin values
#     """
#     change = []
#     for coin in coins:
#         while coin <= amount:
#             amount -= coin
#             change.append(coin)

#     return change


# #  Write our tests for our code
# test_are_equal(get_change(0), [])
# test_are_equal(get_change(1), [1])
# test_are_equal(get_change(2), [2])
# test_are_equal(get_change(5), [5])
# test_are_equal(get_change(10), [10])
# test_are_equal(get_change(20), [20])
# test_are_equal(get_change(50), [50])
# test_are_equal(get_change(100), [100])
# test_are_equal(get_change(3), [2, 1])
# test_are_equal(get_change(7), [5, 2])
# test_are_equal(get_change(9), [5, 2, 2])
# test_are_equal(get_change(35, usd_coins), [25,10])


# print("All tests pass!")



# Challenge on change into a dictionary , the machine should have 20 of each coin denomination

from byotest import *
usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
eur_coins = {200: 20, 100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}


def get_change(amount, coins=euro_coins):
    """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    Returns a list of coin values
    """
    for demonination in sorted(coins.keys(), reverse=True):
        while demonination <= amount and coins[denomination] > 0:
            amount -= demonination
            coins[denomination] -= 1
            change.append(demonination)
    
    if amount != 0:
        raise Exception("Insufficient coins to give change.")

    return change



# Write our tests for our code
test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])
test_are_equal(get_change(5, {2: 1, 1: 4}), [2, 1, 1, 1])
test_exception_was_raised(get_change, (5, {2: 1, 1: 2}),
    "Insufficient coins to give change.")

print("All tests pass!")


def test_are_equal(actual, expected):
    """
    Test that two values are equal. Raises AssertionError if both values are
    not equal.
    `actual` is the actual value produced
    `expected` is the value that was supposed to be produced
    """
    assert expected == actual, "Expected {0}, got {1}".format(
        expected, actual)


def test_not_equal(a, b):
    """
    Test that two values are not equal. Raises AssertionError if both values
    are not equal.
    `a` is the actual value produced
    `b` is the value that was supposed to be produced
    """
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    """
    Check to ensure that a given collection contains a given value. Raises
    AssertionError if `item` is not in `collection`
    `collection` is the collection to be tested
    `item` is the item that is being searched for
    """
    assert item in collection, "{0} does not contain {1}".format(
        collection, item)


def test_not_in(collection, item):
    """
    Check to ensure that a given collection does not contain a given value.
    Raises AssertionError if the `item` is found in `collection`
    `collection` is the collection in question
    `item` is the thing that we want to check for
    """
    assert item not in collection, "{0} is not in {1}".format(
        item, collection)


def test_between(upper_limit, lower_limit, actual):
    """
    Check to ensure that a number is between two other numbers. Raises
    AssertionError if the number is not between the other two numbers
    """
    assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)


def test_exception_was_raised(func, args, message):
    """
    Test that an error gets thrown inside of a given function. Raises
    AssertionError if the error message was different from the expected
    message
    `func` is a reference to the function that is to be called
    `args` is a tuple containing the arguments that are to be provided to
        `func`
    `message` is the string that is expected to be output by the error once
        it's thrown
    """
    try:
        # Call the function and unpack the `args` tuple by using `*`. This
        # will unpack each of the items from the `args` tuple to pass 
        # them into the function as arguments
        func(*args)

        # Execution will cease at this point if the error was successfully
        # thrown, and will move onto the `except` block. If the
        # function was successfully executed without throwing an error, we'll
        # raise an AssertionError here to inform the developer that the
        # function didn't throw an error as expected
        assert False, "Exception was not raised"
    except Exception as e:
        # The message that was thrown will be stored in the exception
        # instance as the first item in the list of `args`. This will allow us
        # to check to see if the message that was thrown is the same as the
        # message that the developer was expecting 
assert e.args[0] == message, "The message that was provided did not match the message thrown"