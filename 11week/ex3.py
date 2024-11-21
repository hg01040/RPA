import qrcode 


a = input("이름을 입력하시오 : ")
b = input("학번을 입력하시오 : ")
c = input("전공을 입력하시오 : ")

my_info_data = a, b, c
qr_img = qrcode.make(my_info_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)