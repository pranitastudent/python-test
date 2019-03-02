# def is_even(number):
#     return number % 2 == 0

# def even_number_of_evens(numbers):
    
#     evens = sum([1 for n in numbers if is_even(n)])
#     return False if evens == 0 else is_even(evens)
    
    
    
    
# ## Testing using own framework



    
    
# ## idiopathic functions    
    
#     # evens = 0
#     # for n in numbers:
#     #     if  is_even(n):
#     #         evens += 1
            
#     #     if  evens == 0:
#     #         return False
#     #     else:    
#     #         return is_even(evens)    
    
    
#  # Our set of test cases
# assert even_number_of_evens([]) == False, "No numbers"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2]) == False, "One even numbers"
# assert even_number_of_evens([1,3,9]) == False, "Three odd numbers"


# print("All tests passed!")



def even_number_of_evens(numbers):



    if not numbers: return False



    evens = 0

    if len(numbers) > 1:

        for n in numbers:

            if not n % 2:

                evens += 1

    

    if len(numbers) == evens:

        return True

    return False      

    

    

 # Our set of test cases

assert even_number_of_evens([]) == False #"No numbers"

assert even_number_of_evens([2]) == False #"One even numbers"

assert even_number_of_evens([1,3,9]) == False #"Three odd numbers"

assert even_number_of_evens([2, 4]) == True #"Two even numbers"



print("All tests passed!")