x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# tipe data boolean
#contoh 1
print(10 > 9)
print(10 == 9)
print(10 < 9) 
#contoh 2
a = 200
b = 330
if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

#contoh 3
katakasar = ['anj*ng','asu','b*ngsa*t','ba*i']
if 'anj*ng' in katakasar:
    print('yaaa anj*ng adalah kata kasar dan tidak boleh diucapkan sembarangan')


if 5 != 10: # tanda seru itu bisa diartikan sebagai tidak jadi ini adalah 5 "tidak sama" dengan 10. tanda sama dengan bisa diganti dengan tanda lain sepeerti lebih dari(>) /kurang dari(<)
  print("5 dan 10 tidak sama")
else:
    print('sama kok')

print('10 > 9',10 > 9)
print('10 == 9',10 == 9)
print('10 < 9',10 < 9)
print('bool("abc")',bool("abc"))
print('bool(0)',bool(0))

