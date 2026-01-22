"""
for i in range(1,10):
    for j in range(1,10):
        print(i * j,end = " ")
    print(f"{i}の段です。")

number = int(input("好きな数字を1つどうぞ:"))
if number % 3 == 0:
    print("foo")
else:
    print("noo")

num = int(input("好きな数字を入力してください:"))
num2 = int(input("好きな数字をもう１つ入力してください:"))
print(num + num2)

nums_str = input("2つの数字をスペースで区切って入力してください: ")
num1, num2 = map(int, nums_str.split())

print(num1 + num2)

x, y = input("2つのスペースで区切って数字を入力してください:").split()
x = int(x)
y = int(y)
print(f"{x + y}")


i = int(input("好きな数字をどうぞ:"))
j = int(input("好きな数字をもう一つどうぞ:"))
print("i =", i, ", j =", j)

i,j = j,i
print("i =", i, ", j =", j)


h = 5
for i in range(1 , h + 1):
    for j in range(i):
        print("*", end = "")
    print()

x = 0
limit = 20000

for i in range(2, limit + 1):
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            break
    else:
        x += i
print(x)


x = "" #前回の値を入れる箱
v = 1 #連続した回数を入れる箱

for i in range(10): #10回繰り返す
    j = int(input("数字を入力してください:"))
    if j == x:
        v = v + 1
        print("{}回連続".format(v))
        if v == 10:
            print("Perfect!")
    else:
        v = 1
        print("連続なし")
    x = j


x = list(map(int, input("数字を入力してください")))
for i in x:
    if i == 5:
        print("5です!!")
    else:
        print("5じゃないです")

x, y = input("2つのスペースで区切って数字を入力してください:").split()

x = int(input("1つ目の数字"))
y = int(input("2つ目の数字"))

print(f"足し算の合計{x + y}")
print(f"引き算の合計{x - y}")


for i in range(1,10):
    for j in range(1,10):
        print(f"{i}×{j}={i*j}")

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i}×{j}={i*j}")
        j = j + 1
    i = i + 1


h = int(input("好きな数字を1つどうぞ:"))

#1行目
for i in range(h):
    print("*", end = "")
print()

#2行目以降（入力された数字が1ではない場合）
if h != 1:
    for i in range(2,h):
        print("*", end="")
        for j in range(2,h):
            print(" ", end="")
        print("*")

#最終行
    for i in range(h):
        print("*", end = "")
    print()

a = 0
b = 1
while a <10000:
    print(a,end=' ')
    a,b = b,a+b
print()


x = int(input("1つ目の数字を入力してください:"))
y = int(input("2つ目の数字を入力してください:"))

if x == 1 or y == 1:
    print("False")
    
else:
    for i in range(2,x//2 +1):
        if x % i == 0:
            print("False")
            break
    else:
        for j in range(2,y//2 +1):
            if y % j == 0:
                print("False")
                break
        else:
            print("True")


def bubble_sort(data):
    if len(data) <= 1:
        return data
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
sorted_data = bubble_sort(data.copy())

print(f"{data} => {sorted_data}")
"""
def merge_sort(data):
    if len(data) <= 1:
        return data
    # データを分割
    center_idx = len(data) // 2
    left_data = data[:center_idx]
    right_data = data[center_idx:]
    # 分割したリストを渡して再帰的に関数を実行
    merge_sort(left_data)
    merge_sort(right_data)

    left_idx = right_idx = idx = 0
    # 分割したリストの左側リスト、右側リストの全要素を比較＆並べ替え
    while left_idx < len(left_data) and right_idx < len(right_data):
        if left_data[left_idx] <= right_data[right_idx]:
            data[idx] = left_data[left_idx]
            left_idx += 1
        else:
            data[idx] = right_data[right_idx]
            right_idx += 1
        idx += 1

    # 右側リストの要素が残っていればそれをすべて代入
    while right_idx < len(right_data):
        data[idx] = right_data[right_idx]
        idx += 1
        right_idx += 1

    # 左側リストの要素が残っていればそれをすべて代入      
    while left_idx < len(left_data):
        data[idx] = left_data[left_idx]
        idx += 1
        left_idx += 1

    return data

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
sorted_data = merge_sort(data.copy())

print(f"{data} => {sorted_data}")