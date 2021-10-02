num_1 = int(input("first integer : "))
num_2 = int(input("second integer : "))
bool_1 = num_1 > num_2
bool_2 = num_1 < num_2
bool_3 = num_1 >= num_2
bool_4 = num_1 <= num_2

print("%d >%d --- 1"%(num_1,num_2) if bool_1 else "%d > %d --- 0"%(num_1,num_2))
print("%d < %d --- 1"%(num_1,num_2) if bool_2 else "%d < %d --- 0"%(num_1,num_2))
print("%d >= %d --- 1"%(num_1,num_2) if bool_3 else "%d >= %d --- 0"%(num_1,num_2))
print("%d <= %d --- 1"%(num_1,num_2) if bool_4 else "%d <= %d --- 0"%(num_1,num_2))