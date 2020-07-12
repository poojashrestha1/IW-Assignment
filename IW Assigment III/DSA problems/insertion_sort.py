#Insertion Sort 

def insertion(my_list): 

	for i in range(len(my_list)): 
		value = my_list[i] 
		j = i-1
		while j >= 0 and value < my_list[j]: 
				my_list[j+1] = my_list[j] 
				j -= 1
		my_list[j+1] = value 


my_list = [5,8,2,1,9]
print("Original: ", my_list)
insertion(my_list)
print (f"Sorted array is: {my_list}") 
