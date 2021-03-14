def mergesort(list):
    if len(list)>1:
        mid_ele=len(list)//2
        list_left=list[:mid_ele]
        list_right=list[mid_ele:]
        mergesort(list_left)
        mergesort(list_right)
        i=0
        j=0
        k=0
        while i<len(list_left) and j<len(list_right):
            if list_left[i]<list_right[j]:
                list[k]=list_left[i]
                i=i+1
                k=k+1
            else:
                list[k]=list_right[j]
                j=j+1
                k=k+1
        while i<len(list_left):
              list[k]=list_left[i]
              i=i+1
              k=k+1
        while j<len(list_right):
              list[k]=list_right[j]
              j=j+1
              k=k+1
              
list=[]
num=int(input("Enter the number of elements"))
for n in range(0,num):
    ele=int(input("Enter the elements"))
    list.append(ele)
mergesort(list)
print("The sorted order is");
print(list);
