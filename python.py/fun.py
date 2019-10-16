# function قم بتعريف ال
# function ا تقم بإضافة أمر طباعة بداخل ال
def add_to_list( y,i):
    x=0
    z=len(y)
    while x!=z :
        y[x]+=i
        x+=1

    return y






# هذه القائمة للاختبار
list1 = [10, 5, 2, 6, 9, 11, 23]

# لا تغير أمر الطباعة
print(add_to_list(list1,2))
