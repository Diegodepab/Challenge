# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:14:47 2023

@author: DiegoDePablo
"""


import time

original_list = list(range(1,10000))
auxiliar_list = list(range(1,10001, 2)) #we want remove this elements
# Begin
start_time = time.perf_counter()
#your code here
#----------------------------------
new_list=[]
new_list=[element for element in original_list
          if element not in auxiliar_list]
#----------------------------------
# Fin
end_time = time.perf_counter()
# execution Time
execution_time = end_time - start_time
print(f"The execution time was: {execution_time:.5f} seconds.")


#Test--------------------------------------------------
assert new_list[:5] == [2, 4, 6, 8, 10], "the first values are not expected"
assert execution_time <= 1.0, "The execution took more than 1 second"
#Why not use .remove?
#https://wiki.python.org/moin/TimeComplexity 