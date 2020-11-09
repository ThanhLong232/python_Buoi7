#BT3: Viết chương trình đọc một danh sách các số được ghi trong một tập tin văn bản, với mỗi số cách nhau bằng dấu khoảng trắng. Hiển thị danh sách ra màn hình và tính tổng các số đó.
def doc_fide():
    with open('abc.txt', mode='r',encoding='utf-8') as f:
        a = f.read()
        print(a)
        b = a.split(" ")
        return b
def tinh_tong(a):
    tong = 0
    for item in a:
        tong = tong + float(item)
    return tong
if __name__ == "__main__":
    a = doc_fide()
    print(a)
    kq = tinh_tong(a)
    print(kq)
#f = open("abc.txt","w+")
#f.write("1 2 3 4 5.5 6.5")

