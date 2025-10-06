print("RESULT OF *ARGS && **KWARGS")
#*ARGS===================================================================================================================================
# *args: non-key arguments (tuple) ------- *: Gom cac keyword thanh mot tuple
#Ex:
def total(*args):
    total = 0
    for num in args:
        total += num
    return total
print(total(1, 2, 3))

#*KWARGS================================================================================================================================
# *kwargs: keyword arguments (dictionary) ------- **: Gom cac key va value thanh dictionary
#Ex:
def displayInfo(**kwargs):
    for key in kwargs.keys():
        print(f"Key: {key}")
    for value in kwargs.values():
        print(f"Value: {value}")
    for value, key in kwargs.items():
        print(f"{key}: {value}")

displayInfo(name = "Nhat", age= 18)

# Co the ket hop *args va **kwargs lai voi nhau
def displayAnimal(*nameAnimals, **animals):
    for name in nameAnimals:
        print(name, end = "")
    for animal in animals.keys:
        print(animal) # Co the ket hop voi cac ham khac(get, ...)

#Khi tao ra mot tham so neu khong co san gia tri thi cu gan mac dinh 'None' - tranh mutable defalut

#LAMBDA==================================================================================================================================
    # Tao ham an danh (anonymous function) ----- Cu phap: lambda arguments: expression
    
#MAP=====================================================================================================================================
    # Ap dung thay doi cho tung phan tu ----- Cu phap: map(function, iterable)
    
#FILTER==================================================================================================================================
    #Loc cac phan tu trong iterable ----- Cu phao: filter(function, iterable)
    
#REDUCE==================================================================================================================================
    #Gop cac phan tu trong iterable ----- Cu phap: reduce(function, iterable, initial)
    # Muon su dung thi phai khai bao 'from functools import reduce'
    
#COMPREHENSION===========================================================================================================================
    #Tao list, set, dict tu iterable, voi dieu kien bien doi ----- Ex: [ x* x for x in range(5)]

#Ex:
from functools import reduce
nums = [2, 4, 5, 1, 4, 10]

evenNum = list(filter(lambda x: x % 2 ==0, nums))
print("RESULT REDUCE: ")
print(evenNum, end = " ")

addEachNum = list(map(lambda num: num + 5, nums))
print("\nRESULT MAP: ")
print(addEachNum, end = " ")

totalnum = reduce(lambda a, b: a*b, nums, 1)
print("\nRESULT REDUCE: ")
print(totalnum, end = " ")

#Filter su dung comprehension
filterComprehension = [num for num in nums if num % 2 == 0]
print("\n RESULT FILTER COMPREHENSION: ")
print(filterComprehension, end = " ")

#YIELD, NEXT=============================================================================================================================
    # Dung yield, next thay cho append hay comprehension -> Uu dime: Toi uu code, Tiet kiem bo nho hieu suat
                                                        # Nhuoc diem: Chi duyet qua duoc 1 lan
def multiple(nums):
    for num in nums:
        yield(num* num)
number = multiple([1, 3, 2, 4])
print("\nRESULT YIELD && NEXT: ")
print(f"\n{next(number)}")
print(f"\n{next(number)}")
print(f"\n{next(number)}")
print(f"\n{next(number)}")

def fibonaci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+ b
fibo = fibonaci()
num = [next(fibo) for _ in range(10)]
print(num, end = " ")

# DECORATOR && @TIMEIT===============================================================================================================================
    #DECORATOR (su dung 1 ham de input cho 1 ham khac) - Cu phap: @decorator: dung de dinh nghia ham
        #functools.wraps: giu nguyen thong tin cua doan code goc- tranh mat thong tin khi su dung lai
    
    #TIMEIT
        #@timeit: do time bang ham time.perf_counter()  ----- chinh xac hon time.time()

import time
import functools
def timeit(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            end = time.perf_counter() - start
            print(f"\n{fn.__name__} took {end:.4f}s")
    return wrapper
@timeit
def add1(args):
    result = 0
    for i in range(args):
        result += i
    return result
print(add1(1000))
