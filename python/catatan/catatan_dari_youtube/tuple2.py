import sys
import timeit

#perbedaan ukuran data
data_list = [1,2,3,4,"kocheng","anjim","wiskas",False,3,14]
data_tuple =(1,2,3,4,"kocheng","anjim","wiskas",False,3,14)

ukuran_data_list = sys.getsizeof(data_list) #getsizeof gunannya untuk mengecek ukuran sebuah data
ukuran_data_tuple = sys.getsizeof(data_tuple)

print("besar data list",ukuran_data_list)
print("besar data tuple",ukuran_data_tuple)

#perbedaan waktu proses
data_list = timeit.timeit(stmt="[1,2,3,4,5,6,6,5,7,7,8]",number=29023)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,6,5,7,7,8)",number=29023)

print("waktu proses list: ",data_list)
print("waktu proses tuple: ",data_tuple)
