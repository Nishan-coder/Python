l1 = [x for x in range(1, 101)]
print(l1)
item_to_be_searched = int(input('Enter the number to be searched: '))
l = 0
r = len(l1) - 1
count = 0

while l <= r:
    mid = (l + r) // 2
    print('Middle term:', l1[mid])
    
    if item_to_be_searched == l1[mid]:
        print('Item found at index:', mid)
        print('Count:', count)
        break
    elif item_to_be_searched < l1[mid]:
        r = mid - 1
    else:
        l = mid + 1
    
    count += 1

if l > r:
    print('Item not found')
    print('Count:', count)
