#Bt1:Viết chương trình tạo một tập tin văn bản với tên và nội dung do người dùng chỉ định.
def doc_fide():
    with open('abc.txt', mode='r',encoding='utf-8') as f:
        f = open("abc.txt","w")
        f.write("Hello World")
if __name__ == "__main__":
    doc_fide()
    print(doc_fide())