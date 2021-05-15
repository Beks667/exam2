# def func(*args):
#     result = 0
#     for i in args:
#         try:
#             result+=i
#         except TypeError:
#             continue
#     return result

# a=func(1,2,3,5)
# print(a)

def func_2(*args):
    result=0
    numbers=float(input("1:"))
    for i in numbers:
        try:
            result+=i
        except TypeError:
            continue
    return result

print(func_2())