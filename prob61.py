pp = 999
def numbers(func):
    i = 1
    ans = []
    while True:
        k = func(i)
        i = i +1
        if k <= pp:
            continue
        if k > pp*10+9:
            break
        ans.append(k)
    return ans

def traingle():
    return numbers(lambda x: (x*(x+1))/2)

def square():
    return numbers(lambda x: (x*x))

def pent():
    return numbers(lambda x: (x*(3*x-1))/2)

def hex():
    return numbers(lambda x: (x*(2*x-1)))

def hept():
    return numbers(lambda x: (x*(5*x-3))/2)

def oct():
    return numbers(lambda x: (x*(3*x-2)))

start_list = [traingle(), square(), pent(), hex(), hept(), oct()]
hash_list_first = []

for i in range(6):
    hash_dict = {}
    for k in start_list[i]:
        key = k/100
        if key in hash_dict:
            hash_dict[key].append(k)
        else:
            hash_dict[key] = [k]
    hash_list_first.append(hash_dict)

all_possible = [0,1,2,3,4,5]

from collections import deque

queue = deque() ## current_path, traced_elements, now_element
for num in start_list[0]:
    queue.append([[0], [num], num])

while len(queue) > 0:
    popped_element = queue.popleft()
    # print popped_element
    [current_path, traced_elements, now_element] = popped_element
    if len(current_path) == 6:
        if traced_elements[-1]%100 == traced_elements[0]/100:
            print traced_elements, sum(traced_elements)
    next_possible = list(set(all_possible) - set(current_path)) 
    for k in next_possible:
        key = now_element%100
        if key in hash_list_first[k]:
            for element in hash_list_first[k][key]:
                queue.append([current_path[:] + [k], traced_elements[:] +[element], element])