from datetime import datetime,timedelta

strprice = '$27.3'

strtime0 = '2019-12-07T21:31:56.000Z'


#khai báo biến fprice và gán cho nó giá trị bằng với strprice
fprice = float(strprice.replace('$',''))

# khai báo biến dttime0 và gán cho nó giá trị của strtime0
dttime0 = datetime.strptime(strtime0,'%Y-%m-%dT%H:%M:%S.%fZ') 

# tạo biến dttime1 có giá trị bằng giá trị của dttime0 cộng thêm 1 giờ 2 phút 3 giây
dttime1 = dttime0 + timedelta(hours=1,minutes=2,seconds=3)

# Xuất 3 giá trị đã tính ra màn hình
# Xuất kiểu (type) của 3 biến trên ra màn hình

for i in range(3):
    print('{} = {}, type: {}'.format(['fprice','dttime0','dttime1'][i],
                                     [fprice,dttime0,dttime1][i],
                                     type([fprice,dttime0,dttime1][i]),))
'''
Nhận xét:
- float(strprice.replace('$','')), replace loại dấu $ thành chuỗi rỗng, để giá trị còn lại là số thực dạng chuỗi,
sau đó chuyển kiểu thành số thực: float.
- dttime0 = datetime.strptime(strtime0,'%Y-%m-%dT%H:%M:%S.%fZ'), strptime chuyển kiểu chuỗi thành datetime
theo một định dạng nhất định.
- dttime1 = dttime0 + timedelta(hours=1,minutes=2,seconds=3), timedelta thực hiện tính toán kiểu dữ liệu datetime.
'''
