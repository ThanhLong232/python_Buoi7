#Bài 4:Viết chương trình ghi một danh sách sinh viên lên tập tin sau đó đọc lại vào một danh sách khác. Kiểm tra hai danh sách có giống nhau không.

#Thông tin sinh viên bao gồm:

#-	Mã SV

#-	Họ tên

#-	Năm sinh

#-	Giới tính

#-	Điểm Toán

#-	Điểm Lý

#-	Điểm Hóa

def ghi_fide(a):
    with open('sinhvien.txt', mode='w',encoding='utf-8') as f:
        f.write(a)

def nhap_1_sv():
    sinhvien = ''
    mssv = input("Nhập Mã Số: ")
    hoten = input("Nhập Họ Tên: ")
    namsinh = int(input("Nhập Năm Sinh: "))
    gioitinh = input("Nhập Giới Tính: ")
    diemtoan = float(input("Nhập Điểm Toán: "))
    diemly = float(input("Nhập Điểm Lý: "))
    diemhoa = float(input("Nhập Điểm Hóa: "))
    
    sinhvien += f'Mã Số: {mssv}\n'
    sinhvien += f'Họ Tên: {hoten}\n'
    sinhvien += f'Năm Sinh: {namsinh}\n'
    sinhvien += f'Giới Tính: {gioitinh}\n'
    sinhvien += f'Điểm Toán: {diemtoan}\n'
    sinhvien += f'Điểm Lý: {diemly}\n'
    sinhvien += f'Điểm Hóa: {diemhoa}\n'
    return sinhvien
def nhap_ds_sv(n):
    a =''
    for i in range(n):
        print(f"Nhập thong tin sinh vien thứ {i+1}: ")
        a += nhap_1_sv()
    return a

if __name__ == "__main__":
    n = int(input("Nhập số lượng sinh viên: "))
    kq = nhap_ds_sv(n)
    ghi_fide(kq)


