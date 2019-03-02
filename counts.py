# def count_upper_case(message):
#     count = 0
#     for c in message:
#         if c.isupper():
#             count += 1
#     return count

# # Return zero as they are no uppercase characters
# assert count_upper_case("") ==0, "Empty String"  
# assert count_upper_case("A") ==1, "One uppercase"
# assert count_upper_case("b") ==0, "One lower case"
# assert count_upper_case("£$%") ==0, "special characters"

# print("All the tests passed")

def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") ==0, "Empty String"  
assert count_upper_case("A") ==0, "One uppercase"
assert count_upper_case("b") ==0, "One lower case"
assert count_upper_case("£$%") ==0, "special characters"


print("All the tests passed")
