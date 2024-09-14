l1=[x for x in range(1,101)]
print(l1)
item_to_be_searched=3
l=0
r=len(l1)-1
count =0
while l<r:
    print('middle term:',l1[(l+r)//2])
    if item_to_be_searched==l1[(l+r)//2]:
        print('Item found')
        print('Count:',count)
        break
    elif item_to_be_searched<(l+r)//2:
            r=(l+r)//2-1
    else:
        l=(l+r)//2+1
    count+=1
if(l>=r):
    print('item not found')
