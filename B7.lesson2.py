#B2:Viết chương trình đọc nội dung của một tập tin văn bản cho trước. Tên tập tin do người dùng chỉ định. Trong tập tin có nhiều dòng chữ.
def doc_fide():
    with open('abc.txt', mode='r',encoding='utf-8') as f:
        f = open("abc.txt","a")
        f.write("I Love You Very Much")
        f.write("I am here.Where are You?")
if __name__ == "__main__":
    doc_fide()
    print(doc_fide())