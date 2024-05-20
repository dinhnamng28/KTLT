# Nguyễn Đình Nam 20216859

import pandas as pd
import wx
import datetime

class AuthorModel:
    def __init__(self):
        self.filePath = "D:\\Python\\python cơ bản\\Nháp thử\\Data_Authors.xlsx"


    def getAuthorList(self):
        try:
            df = pd.read_excel(self.filePath)

            # Định dạng lại ngày sinh trong chuỗi 'yy-mm-dd'
            df['birthday'] = pd.to_datetime(df['birthday']).dt.strftime('%y-%m-%d')

            return df[['au_id', 'au_name', 'birthday', 'country']].values.tolist()
        except Exception as e:
            wx.MessageBox(f"Đã xảy ra lỗi khi đọc tệp Excel: {e}", "Lỗi", wx.OK | wx.ICON_ERROR)
            return []
    

    # Lấy thông tin tác giả để chỉnh sửa
    def getAuthorInf(self, authorId):
        try:
            df = pd.read_excel(self.filePath)
            author_data = df.query(f"au_id == '{authorId}'")
            return author_data[['au_id', 'au_name', 'birthday', 'country']].values.tolist()
        except Exception as e:
            print("Đã xảy ra lỗi khi lấy thông tin tác giả:", e)
            return []


    # Tìm kiếm tác giả
    def searchAuthor(self, au_id=None, au_name=None, birthdayF=None, birthdayT=None, country=None):
        try:
            df = pd.read_excel(self.filePath)

            # Chuyển đổi cả dataframe sang chữ thường
            df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

            # Chuyển đổi từ khóa tìm kiếm sang chữ thường
            if au_id:
                au_id = au_id.lower()
            if au_name:
                au_name = au_name.lower()
            if country:
                country = country.lower()

            # Chuyển đổi kiểu dữ liệu của birthdayF và birthdayT sang datetime.datetime
            if birthdayF:
                birthdayF = datetime.datetime.strptime(birthdayF, '%Y-%m-%d')
            if birthdayT:
                birthdayT = datetime.datetime.strptime(birthdayT, '%Y-%m-%d')

            # Áp dụng các điều kiện tìm kiếm nếu các tham số không rỗng
            if au_id:
                df = df[df['au_id'].str.contains(au_id, na=False)]
            if au_name:
                df = df[df['au_name'].str.contains(au_name, na=False)]
            if birthdayF and birthdayT:
                df = df[
                    (df['birthday'] >= birthdayF) & (df['birthday'] <= birthdayT)
                ]
            if country:
                df = df[df['country'] == country]

            # Chuyển dataframe sau khi tìm kiếm về dạng danh sách tác giả
            author_list = df[['au_id', 'au_name', 'birthday', 'country']].values.tolist()

            return author_list
        except Exception as e:
            print("Đã xảy ra lỗi khi tìm kiếm tác giả:", e)
            return []


    # Kiểm tra tác giả đã tồn tại hay chưa
    def checkAuthor(self, au_id):
        try:
            df = pd.read_excel(self.filePath)
            return au_id in df['au_id'].values
        except Exception as e:
            print("Đã xảy ra lỗi khi kiểm tra mã tác giả tồn tại:", e)
            return False
        
    
    def checkAuthorUpdate(self, au_id, current_au_id):
        try:
            df = pd.read_excel(self.filePath)
            return any((df['au_id'] == au_id) & (df['au_id'] != current_au_id))
        except Exception as e:
            print("Đã xảy ra lỗi khi kiểm tra mã tác giả:", e)
            return False

    

    # Tạo mới tác giả
    def addAuthor(self, au_id, au_name, birthday, country):
        try:
            new_author_data = {
                'au_id': [au_id],
                'au_name': [au_name],
                'birthday': [birthday],
                'country': [country]
            }
            new_author_df = pd.DataFrame(new_author_data)

            # Đọc dữ liệu từ tệp Excel vào DataFrame
            df = pd.read_excel(self.filePath)

            # Thêm dữ liệu mới vào DataFrame
            df = df._append(new_author_df, ignore_index=True)

            # Ghi toàn bộ DataFrame vào tệp Excel
            df.to_excel(self.filePath, index=False)

            return True
        except Exception as e:
            print("Đã xảy ra lỗi khi thêm tác giả:", e)
            return False


    # Chỉnh sửa tác giả 
    def updateAuthor(self, au_id = None, au_name = None, birthday = None, country = None):
        try:
            df = pd.read_excel(self.filePath)
            if au_id:
                df.loc[df['au_id'] == au_id, 'au_id'] = au_id
            if au_name:
                df.loc[df['au_id'] == au_id, 'au_name'] = au_name
            if birthday:
                df.loc[df['au_id'] == au_id, 'birthday'] = birthday
            if country:
                df.loc[df['au_id'] == au_id, 'country'] = country
            
            df.to_excel(self.filePath, index=False)
            return True
        except Exception as e:
            print("Đã xảy ra lỗi khi chỉnh sửa tác giả:", e)
            return False


    # Xóa tác giả
    def deleteAuthor(self, key, column = 'au_id'):
        try:
            df = pd.read_excel(self.filePath)
            df = df[df[column] != key]
            df.to_excel(self.filePath, index=False)
            return True
        except Exception as e:
            print("Đã xảy ra lỗi khi xoá tác giả:", e)
            return False


