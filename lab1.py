def snippet_1(n):
    total = 0
    for i in range(n):
        total = total + 1
    return total

# Độ phức tạp: O(n)
# Giải thích: vòng for chạy n lần, mỗi lần chạy 1 phép cộng

def snippet_2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

# Độ phức tạp: O(n^2)
# Giải thích: vòng ngoài i chạy n lần, vòng trong j cũng chạy n lần => thực hiện lệnh count+=1 =  n*n = n^2

def snippet_3(n):
    steps = 0
    while n > 0:
        n = n // 2
        steps += 1
    return steps

# Độ phức tạp: O(logn)
# Giải thích: Mỗi lần lặp, n bị chia đôi đến khi n <= 1 là log2(n)

def constant_work():
    x=1
    y=2
    z=x+y
    return z
def snippet_4(n):
    for i in range(n):
        constant_work()

# Độ phức tạp: O(n)
# Giải thích: Hàm constant_work() là O(1), còn hàm snippet_4(n) có vòng for lặp lại n lần, mỗi lần gọi hàm constant_work()

def snippet_5(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total

# Độ phức tạp: O(n^2)
# Giải thích: Tổng số lần lặp = n(n-1)/2 bỏ qua hằng số thì ta được n^2

def snippet_6(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
        k = k * 2
    return total

# Độ phức tạp: (nlogn)
# Giải thích: mỗi lần lặp k*2 nên số lần vòng lặp while chạy là log2n, 
# trong vòng while có vòng for chạy n lần -> tổng số lần thực hiện lệnh total+=1 là n*log2n = nlogn

def snippet_7(arr):
    count = 0
    for x in arr:
        if x in arr:
            count += 1
    return count

# Độ phức tạp: O(n)
# Giải thích: Vòng for chạy qua tất cả phần tử của mảng arr, nếu arr có n phần tử thì vòng for sẽ chạy n lần -> độ phức tạp là O(n)
# Mỗi lần chạy vòng for, điều kiện if x in arr để kiểm tra xem phần tử x có tồn tại không nhưng vì arr là một mảng có n phần tử nên việc
# kiểm tra x trong arr sẽ mất O(n) thời gian -> tổng thời gian thực hiện sẽ là O(n) * O(n) = O(n^2)

def snippet_8(arr):
    s=set(arr)
    count = 0
    for x in arr:
        if x in s:
            count += 1
    return count

# Độ phức tạp: O(n)
# Giải thích: Việc tạo set s từ arr mất O(n) thời gian, sau đó vòng for chạy qua tất cả phần tử của mảng arr, nếu arr có n phần tử thì vòng for sẽ chạy n lần -> độ phức tạp là O(n)
# Mỗi lần chạy vòng for, điều kiện if x in s để kiểm tra xem phần tử x có tồn tại không nhưng vì s là một set nên việc kiểm tra x trong s sẽ mất O(1) thời gian -> tổng thời gian thực hiện sẽ là O(n) + O(n) * O(1) = O(n)

def two_sum_quadratic(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None

# Độ phức tạp: O(n^2)
# Giải thích: Vòng for ngoài chạy n lần, vòng for trong chạy n-i lần, tổng số lần thực hiện lệnh if arr[i] + arr[j] == target là n(n-1)/2 bỏ qua hằng số thì ta được n^2

def two_sum_linear(arr, target):
    seen = set()
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (arr.index(complement), i)
        seen.add(num)
    return None

# Độ phức tạp: O(n)
# Giải thích: Vòng for chạy n lần, mỗi lần kiểm tra nếu complement có trong seen mất O(1) thời gian, tổng thời gian thực hiện là O(n) * O(1) = O(n)
import time
import random

arr = list(range(100000))
random.shuffle(arr)
target = arr[123] + arr[9876]
start = time.time()
print(two_sum_quadratic(arr, target))
print("O(n^2) time:", time.time() - start)

arr = list(range(100000))
random.shuffle(arr)
target = arr[123] + arr[9876]
start = time.time()
print(two_sum_linear(arr, target))
print("O(n) time:", time.time() - start)