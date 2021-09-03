# Str tasks

# 1
str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
print(len(str))

# 2
str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
elifba="abcçdeəfghijklmnopqrstuvxyzw"
for herf in elifba:
  say = str.count(herf)
  if say > 1:
    print (herf,say)

# 3
str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# 4
str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
saitler=set("aıoueəiöüAIOUEƏİÖÜ")

saitsay=0
samitsay=0

for i in str:
    if i in saitler:
        saitsay=saitsay+1
    elif ((i>='a' and i<='z')) or ((i>='A' and i<='Z')):
        samitsay=samitsay+1

print(samitsay)
print(saitsay)

# 5
string='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
print(string[0:len(string)-2])

# 6
str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
string='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
string2=string.split(",")
print(string2)

# 7
string='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
if 'yox' in string:
    print("Tapıldı")
else:
    print("Təəssüf ki, tapılmadı")



# Num tasks

# 1
nums=[1,2,3,6,7,8,23,78,34,12]
print(sum(nums))

# 2
nums=[1,2,3,6,7,8,23,78,34,12]
numbers=sorted(nums, reverse=True)
print(numbers)

# 3
nums=[1,2,3,6,7,8,23,78,34,12]
print(max(nums))

# 4
nums=[1,2,3,6,7,8,23,78,34,12]
kvadrat=[num ** 2 for num in nums]
print(kvadrat)

# 5
nums=[1,2,3,6,7,8,23,78,34,12]
cem=0

for num in nums:
    if num % 2 != 0:
       print(num," ")
    
       cem+=num
print(cem)

# 6
nums=[1,2,3,6,7,8,23,78,34,12]
for num in nums:
    if num==3:
        print(num)

# 7
nums=[1,2,3,6,7,8,23,78,34,12]
tekler=[]
for i in nums :
    if i % 2!=0:
        tekler.append(i)
        print(tekler)