if x<2:
    return False
for i in range(2,int(x**0.5)+1):
    if x%i==0:
        return False
return True
 
x=float(input("nhập số x"))
if kiem_tra_so_nguyen_to(x):
  print(f"{x} là số nguyên tố")
else:
  print(f"{x} không là số nguyên tố")