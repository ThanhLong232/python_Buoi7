#bt5:Viết chương trình xóa toàn bộ tập tin trong một thư mục có sẵn. Lưu ý, không xóa thư mực
import os

def clean_folder(dirname):
    for file in os.listdir(dirname):
        os.remove(os.path.join(dirname, file))
    print(f'Foder {dirname} was cleaned')

if __name__ == "__main__":
    clean_folder('folder4')