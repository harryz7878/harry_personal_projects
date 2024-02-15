# #case one 
# res+[i] meant res made a copy of itself and passed the copy to the resursive call
# def test(i,res):
#     if i >3:
#         return
    
#     print(f'res the reursive call took in for iteration {i}:{res}')
#     test(i+1,res+[i])
#     print(f'res the recursive call give out for iteration {i}:{res}')
# test(0,[])


#case two  - use this method, the neetcode way, all the questions are solved this way
def test(i,res):
    if i >3:
        return
    print(f'res the reursive call took in for iteration {i}:{res}')
    res.append(i)
    test(i+1,res)
    print(f'res the recursive call give out for iteration {i}:{res}')

test(0,[])

# from gpt
# The difference between the two methods in your code examples lies in how they handle the res list when making recursive calls.

# Case One: Using res+[i]
# Mechanism: In this method, res+[i] creates a new list by concatenating res with [i]. This does not modify the original res list but creates a new list with an additional element i.
# Behavior in Recursion: Each recursive call gets a copy of res with the new element added. Changes made to res in deeper levels of recursion do not affect the res in the upper levels.
# Result: The print statements before and after the recursive call show the same res for each iteration, as the modifications in deeper recursive calls do not affect the upper levels.
# Case Two: Using res.append(i)
# Mechanism: In this method, res.append(i) modifies the original res list by adding i to its end.
# Behavior in Recursion: Each recursive call modifies the same res list. Changes made in deeper levels of recursion are reflected in the upper levels because they all reference the same list.
# Result: The print statements before and after the recursive call show the progressive building of res across iterations. The list grows with each deeper level of recursion, and these changes are visible when the recursion unwinds.
# Summary
# Case One: Creates a new list for each recursive call, thus preserving the state of res across different levels of recursion.
# Case Two: Modifies the same list across all recursive calls, reflecting changes across all levels of recursion.
# The choice between these two methods depends on the desired behavior in your recursive algorithm. The first method is useful when you need to preserve the state of a list at each level of recursion, while the second is used when you want changes to persist across all levels.

