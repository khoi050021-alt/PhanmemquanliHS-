k=d=e=0
for i in range (1,11):
    a=input('Nhap ten hoc sinh: ')
    x=float(input('Nhap diem khoa hoc: '))
    y=float(input('Nhap diem xa hoi: '))
    z=float(input('Nhap diem ky nang mem: '))
    s = (x+y+z)/3
    print('Diem trung binh cua',a,'la: ',s)
    if(s>=8):
        print(a,'xuat sac that')
    elif(s>=5.5) and (s<=7.9):
        d+=1
        print(a,'lam tot lam')
    else:
        e+=1
        print(a,'co len')
    print('_'*10)
print('Co tong cong',k,'HSG')
print('Co tong cong',d,'HSK')
print('Co tong cong',e,'HSTB')