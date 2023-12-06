# -*- coding: utf-8 -*-
"""
@author: 
"""

import time

original_list = list(range(1,1000001))
auxiliar_list = list(range(1,1000001, 2)) #we want remove this elemento 
# Begin
start_time = time.perf_counter()

#your code here----------------------------------
new_list=[]



#------------------------------------------------

# Fin
end_time = time.perf_counter()
# execution Time
execution_time = end_time - start_time
print(f"The execution time was: {execution_time:.5f} seconds.")


#Test--------------------------------------------------
assert new_list[:5] == [2, 4, 6, 8, 10], "the first values are not expected"
assert execution_time <= 1.0, "The execution took more than 1 second"