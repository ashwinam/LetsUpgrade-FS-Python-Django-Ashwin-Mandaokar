# class int_list():
#   def __init__(self,test_list):
#     self.test_list = test_list
#   def extract_nums(self):
#     num_list =[]
#     for  x in range(0,len(self.test_list)):
#       if str(self.test_list[x]).isdigit():
#         num_list.append(int(self.test_list[x]))
#     #num_list = [x for x in self.test_list if isinstance(x, int)]
#     return num_list

# list1 = [1,2,3,"4","67","56","123","not an int", "Definitely not an int"]
# p = int_list(list1)
# integer_list = p.extract_nums()
# print(integer_list)


# Regular  methods automatically takes instance as first arugment 
# class methods automatically takes cls as first arugment 
# static methods doesn't pass anything automatically
