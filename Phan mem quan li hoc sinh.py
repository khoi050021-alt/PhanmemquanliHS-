HS=[['Khoi',10,10],
    ['Nghia',9,9],
    ['Tung',8,8],
    ['Hai',7,7],
    ['Tuan',6,6],
    ['Duc',5,5],
    ['Binh',4,4],
    ['Long',3,3],
    ['Dong',2,2],
    ['Van',1,1]]
a=int(input('Diem mon toan la: '))
for i in range(1,10):
    if(HS[i][1]>=a):
        print("Hoc sinh co diem toan cao hon",a,"la",HS[i][0])

for i in range(1,10):
    TB=(HS[i][1]+HS[1][2])/2
    HS[i].append(TB)
    if (HS[i][3]>=8):
        print("Hoc sinh co diem trung binh cong >=8 la",HS[i][0])