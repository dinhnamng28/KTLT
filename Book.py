# Nguyễn Đình Nam 20216859

import pandas as pd
import wx

class BookModel:
    def __init__(self):
        self.filePath = "D:\\Python\\python cơ bản\\Nháp thử\\Data_Book.xlsx"


    # Lấy danh sách sách
    def getBookList(self):
        try:
            df = pd.read_excel(self.filePath)

            return df[['book_id', 'title', 'pub_year', 'pub_name', 'au_name', 'category', 'isbn_number']].values.tolist()
        except Exception as e:
            wx.MessageBox(f"Đã xảy ra lỗi khi đọc tệp Excel: {e}", "Lỗi", wx.OK | wx.ICON_ERROR)
            return []
    

    # Lấy thông tin sách để chỉnh sửa
    def getBookInf(self, bookID):
        try:
            df = pd.read_excel(self.filePath)
            book_data = df.query(f"book_id == '{bookID}'")
            return book_data[['book_id', 'title', 'pub_year', 'pub_name', 'au_name', 'category', 'isbn_number']].values.tolist()
        except Exception as e:
            print("Đã xảy ra lỗi khi lấy thông tin sách:", e)
            return []


    # Tìm kiếm sách
    def searchBook(self, book_id=None, title=None, pub_yearF=None, pub_yearT=None, pub_name=None, au_name=None, category=None, isbn_number=None):
        try:
            df = pd.read_excel(self.filePath)

            # Chuyển chuỗi tìm kiếm và dữ liệu trong dataframe về cùng một dạng (chữ thường)
            if book_id:
                book_id = book_id.lower()
                df['book_id'] = df['book_id'].apply(lambda x: x.lower())
            if title:
                title = title.lower()
                df['title'] = df['title'].apply(lambda x: x.lower())
            if pub_name:
                pub_name = pub_name.lower()
                df['pub_name'] = df['pub_name'].apply(lambda x: x.lower())
            if au_name:
                au_name = au_name.lower()
                df['au_name'] = df['au_name'].apply(lambda x: x.lower())
            if category:
                category = category.lower()
                df['category'] = df['category'].apply(lambda x: x.lower())
            if isbn_number:
                isbn_number = isbn_number.lower()
                df['isbn_number'] = df['isbn_number'].apply(lambda x: x.lower())

            # Áp dụng các điều kiện tìm kiếm nếu các tham số không rỗng
            if book_id:
                df = df[df['book_id'].str.contains(book_id, na=False)]
            if title:
                df = df[df['title'].str.contains(title, na=False)]
            if pub_yearF and pub_yearT:
                df = df[(df['pub_year'] >= pub_yearF) & (df['pub_year'] <= pub_yearT)]
            if pub_name:
                df = df[df['pub_name'].str.contains(pub_name, na=False)]
            if au_name:
                df = df[df['au_name'].str.contains(au_name, na=False)]
            if category:
                df = df[df['category'].str.contains(category, na=False)]
            if isbn_number:
                df = df[df['isbn_number'].str.contains(isbn_number, na=False)]

            return df[['book_id', 'title', 'pub_year', 'pub_name', 'au_name', 'category', 'isbn_number']].values.tolist()
        except Exception as e:
            print("Đã xảy ra lỗi khi tìm kiếm sách:", e)
            return []



    # Kiểm tra sách đã tồn tại hay chưa
    def checkBook(self, book_id):
        try:
            df = pd.read_excel(self.filePath)
            return book_id in df['book_id'].values
        except Exception as e:
            print("Đã xảy ra lỗi khi kiểm tra mã sách tồn tại:", e)
            return False
    

    # Tạo mới sách
    def addBook(self, book_id, title, pub_year, pub_name, au_name, category, isbn_number):
        try:
            new_book_data = {
                'book_id': [book_id],
                'title': [title],
                'pub_year': [pub_year],
                'pub_name': [pub_name],
                'au_name': [au_name],
                'category': [category],
                'isbn_number': [isbn_number]
            }
            new_book_df = pd.DataFrame(new_book_data)

            # Đọc dữ liệu từ tệp Excel vào DataFrame
            df = pd.read_excel(self.filePath)

            # Thêm dữ liệu mới vào DataFrame
            df = df._append(new_book_df, ignore_index=True)

            # Ghi toàn bộ DataFrame vào tệp Excel
            df.to_excel(self.filePath, index=False)

            return True
        except Exception as e:
            print("Đã xảy ra lỗi khi thêm sách:", e)
            return False


    # Chỉnh sửa sách
    def updateBook(self, book_id=None, title=None, pub_year=None, pub_name=None, au_name=None, category=None, isbn_number=None):
        try:
            df = pd.read_excel(self.filePath)

            if book_id is not None:
                df.loc[df['book_id'] == book_id, 'book_id'] = book_id
            if title is not None:
                df.loc[df['book_id'] == book_id, 'title'] = title
            if pub_year is not None:
                df.loc[df['book_id'] == book_id, 'pub_year'] = pub_year
            if pub_name is not None:
                df.loc[df['book_id'] == book_id, 'pub_name'] = pub_name
            if au_name is not None:
                df.loc[df['book_id'] == book_id, 'au_name'] = au_name
            if category is not None:
                df.loc[df['book_id'] == book_id, 'category'] = category
            if isbn_number is not None:
                df.loc[df['book_id'] == book_id, 'isbn_number'] = isbn_number

            df.to_excel(self.filePath, index=False)
            return True
        except Exception as e:
            print("Đã xảy ra lỗi khi chỉnh sửa sách:", e)
            return False


    # Xóa sách
    def deleteBook(self, key, column='book_id'):
        try:
            df = pd.read_excel(self.filePath)
            df = df[df[column] != key]
            df.to_excel(self.filePath, index=False)
            return True
        except Exception as e:
            print("Đã xảy ra lỗi khi xoá sách:", e)
            return False


    # Sắp xếp theo số ISBN
    def sortISBN(self):
        try:
            # Đọc dữ liệu từ tệp Excel vào dataframe
            df = pd.read_excel(self.filePath)

            # Sắp xếp dataframe theo cột 'isbn_number' và chuyển dataframe đã sắp xếp thành danh sách
            sorted_df = df.sort_values(by='isbn_number')
            sorted_books_list = sorted_df[['book_id', 'title', 'pub_year', 'pub_name', 'au_name', 'category', 'isbn_number']].values.tolist()

            return sorted_books_list
        except Exception as e:
            print("Đã xảy ra lỗi khi đọc tệp Excel hoặc sắp xếp sách:", e)
            return []
    

    # Sắp xếp theo NXB
    def sortPub(self):
        try:
            df = pd.read_excel(self.filePath)

            # Sắp xếp dataframe theo cột 'pub_name' và chuyển dataframe đã sắp xếp thành danh sách
            sorted_df = df.sort_values(by='pub_name')
            sorted_books_list = sorted_df[['book_id', 'title', 'pub_year', 'pub_name', 'au_name', 'category', 'isbn_number']].values.tolist()

            return sorted_books_list
        except Exception as e:
            print("Đã xảy ra lỗi khi đọc tệp Excel hoặc sắp xếp sách:", e)
            return []


 