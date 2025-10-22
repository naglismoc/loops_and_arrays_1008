import random
import time

number = 20
#          0  1  2   3   4   5
numbers = [1, 5, 20, 40, 80, 50] #viso 6 elementai <-- cia yra list

print(numbers)
print('ilgis', len(numbers))
print(numbers[0])
print(numbers[5])

numbers[0] = 20
print(numbers)
numbers.append(100)
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.index(20))
numbers.reverse()
numbers.insert(2,12)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.sort()
print(numbers)
#            0               1           2        3
vardai = ['Žygimantas','Gabrielius','Jokūbas','Vilius',]


print(vardai)
print(vardai[1])


arr2d = [
    [1,4,10],
    [3,5,8],
    [1,2,3],
    [5,10,5,7,"Žygimantas"],
    "17"
]
print(arr2d)
print(arr2d[2] )
print(arr2d[2][1] )
arr2d[2].append(13)
print(arr2d)
arr2d[0].extend([3,13,14])
print(arr2d)

vardai = [
      ['Žygimantas',10],
      ['Gabrielius', 8],
      ['Jokūbas',    9],
      ['Vilius',    10]
    ]
print(vardai)

#             0  1  2  3  4  5  6  7  8  9 INDEXAI
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##################### PIRMAS PARAMETRAS INCLUSSIVE, JĮ IMA, ANTRAS EXCLUSIVE, JO NEIMA,  IMA IKI JO ###################
############################# Multidimensiniuose masyvuose galioja tos pačios taisyklės################################
# my_numbers[pradžia:galas:žingsnis]
print(my_numbers) # atspausdina viską
print(my_numbers[6]) # atspausdina vieną elementą
print(my_numbers[0:4]) #nuo iki
print(my_numbers[4:8])
print(my_numbers[7:]) #nuo iki galo
print(my_numbers[:4]) #nuo pradzios iki nurodytos pozicijos (exclusive, jos neima, IKI jos)
print(my_numbers[-2]) #antra pozicija nuo galo
print(my_numbers[-5:]) #nuo 5 pozicijos nuo galo iki pat galo
print(my_numbers[:-5]) #nuo pradzios iki 5 pozicijos nuo galo
print(my_numbers[2:-5]) #nuo 2 pozicijos iki 5tos nuo galo
print(my_numbers[-6:-2]) #nuo 6 nuo galo iki 2 nuo galo
print(my_numbers[-8:4]) #teoriskai veikia, neapsikraukit =D
print(my_numbers[:]) #paima viska nuo pradzios iki galo, lygiai taip kaip kaip ir neirasius nieko
print(my_numbers[::2]) #visa imtis, kas antras elementas
print(my_numbers[::3]) #visa imtis, kas trecias elementas
print(my_numbers[1::2]) #visa imtis NUO 1o indexo iki galo, kas antras elementas
print(my_numbers[3:7:2]) #nuo 3 indexo iki 7 exclusive, kas antas elementas
print(my_numbers[2:-2:2]) #nuo antro iki antro nuo galo, kas antras elementas
print(my_numbers[::-1]) #visi elementai nuo galo (panaudojau minusini zingsni)
print(my_numbers[::-2]) #visi elementai, kas antas elementas, nuo galo
print(my_numbers[5::-2]) #NUO 5to elemento kas antras elementas atbulai
print(my_numbers[8:3:-2]) #nuo 8tos pozicijos, iki 3cios, kas anatras elementas atbulai
print(my_numbers[-2:2:-2]) #nuo antro nuo galo iki antro nuo nuo pradzios, kas antras elementas atbulai

imtis = range(0,10)
print(imtis)

for i in range(0,10):
    print(i)
print('po ciklo')


vardai = ['Žygimantas','Gabrielius','Jokūbas','Vilius',]

for vardas in vardai:
    print(vardas)
print("-----------")
numbers = [3, 30, 40, 5, 3]
for skaicius in numbers:
    print(skaicius)
print("-----------")
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print("-----------")

for i in range(4):
    print(i)
print("-----------")
for i in range(4,9):
    print(i)
print("-----------")
for i in range(1000000,1000005):
    print(i)
print("-----------")

dariaus_skaiciai = [3,5,7,8,9]

for i in range(5,10):
    print(f'range skaicius {i}, my_numbers[{i}] reiksme yra {my_numbers[i]}')
print("-----------")

for i in dariaus_skaiciai:
    print(f'range skaicius {i}, my_numbers[{i}] reiksme yra {my_numbers[i]}')
print("-----------")

arr = []
for i in arr:
    print(i)
print("-----------")

for i in range(len(vardai)):
    print(f'range skaicius {i}, my_numbers[{i}] reiksme yra {vardai[i]}')
print("-----------")

for indeksas, vardas in enumerate(vardai):
    print(f'indeksas {indeksas}, reiksme {vardas}')
data = []
for row in data:
    print(row['author_id'],row['first_name'],row['last_name'])


names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Elizabeth",
    "Frederick", "Gabriella", "Henry", "Isabella", "Jacob",
    "Katherine", "Liam", "Madeline", "Nathaniel", "Olivia",
    "Patrick", "Quinn", "Rebecca", "Samuel", "Theresa",
    "Ulysses", "Victoria", "William", "Xavier", "Yvonne",
    "Zachary", "Abigail", "Brandon", "Cassandra", "Derek",
    "Emily", "Francis", "Grace", "Hannah", "Ian",
    "Julia", "Kevin", "Laura", "Michael", "Natalie",
    "Oscar", "Penelope", "Quincy", "Rachel", "Stephen",
    "Tracy", "Uma", "Vincent", "Wendy", "Yosef"
]
# select name from names where length(name) <= 3;
for name in names:
    if len(name) <= 3:
        print(name)

for i, name in enumerate(names):
    if i % 2 == 0:
        print(name)

numbers = [3,30,40,5,300]
# numbers.sort()
print(numbers)
count = 0
for num in numbers:
    for i in range(len(numbers) -1):
        count += 1
        if numbers[i] < numbers[i + 1]:
            temp = numbers[i + 1]
            numbers[i + 1] = numbers[i]
            numbers[i] = temp
print(numbers)
print(count)
print("---------------")

count = 0
for a in range(len(numbers)):  #numbers[1]
    for i in range(a, len(numbers) -1):
        count += 1
        if numbers[i] < numbers[a]:
            temp = numbers[a]
            numbers[a] = numbers[i]
            numbers[i] = temp
    print(numbers)
print(count)
# numbers.sort()

arr2d = [
    [1, 4, 10],
    [3, 5, 8],
    [1, 2, 3],
    [5, 10, 5]
]

print(arr2d)

sum = 0
count = 0

for row in arr2d:
    for number in row:
        sum += number
        count += 1
print(sum, count)
print(sum / count)
print("---------------")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print("---------------")

for i in range(10):
    if i == 4:
        break
    print(i)
print("---------------")
while True:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        break
    print("metam kauliuka dar karta")
print("---------------")
should_roll_dice = True
while should_roll_dice:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        should_roll_dice = False
    print("metam kauliuka dar karta")
print("---------------")
start_time = time.time()
count = 0
times = 100
for i in range(times):
    while True:
        count +=1
        dice = random.randint(1, 6)
        # print(dice)
        if dice == 6:
            break
print(f'kauliuka meteme {count} kartu. tikimybe isridenti 6-ta yra {times / count}')
end_time = time.time()
print(f'skaiciavimai truko {end_time - start_time}')

for y in range(1, 11):
    for x in range(1,11):
        print(x * y, end=" ")
    print()
print("---------------")

for y in range(1, 11):
    row = ""
    for x in range(1,11):
        row += str(x * y) + " "
    print(row)