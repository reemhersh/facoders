s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]



x=input("Enter student's name")
y=0

if(x==s1[0]):

    for no in s1[1:] :
        y+=no
    print( s1[0] +' '+str(y))

elif(x==s2[0]):
    for no in s2[1:] :
        y+=no
    print( s2[0] +' '+str(y))

elif(x==s3[0]):
    for no in s3[1:] :
        y+=no
    print( s3[0] +' '+str(y))

else :
    print("Students is not recorded 0")
