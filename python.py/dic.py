# اكمل القاموس هنا
users= {'001':['Ahmad', 26, 'Jordan'],'002':['jameel' ,34,'Egypt'],'003':['Maha' , 27, 'KSA'], '004':['Eman', 38, 'Kuwait']}

# قم بتعريف المتغيرات بحسب السؤال
a= users.get('002','not exist')
b= users.get('006','not exist')
c= users['001'][2]


# لا تقم بتغيير امر الطباعة
print(a,',',b,',',c)
