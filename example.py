#課題1
print("hello world")


#課題2
def greet():
    print("こんにちは")

greet()


#課題3
def print_name(name):
    print(f"私の名前は{name}です")

#fは文字列に変数の値を埋め込むときに使う

print_name("じゅん")


#課題4
def get_greet():
    return "おはようございます"

message = get_greet()
print(message)


#課題5
def add(a,b):
    return a + b

result = add(4,5)
print(result)