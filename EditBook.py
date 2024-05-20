# Nguyễn Đình Nam 20216859

import wx
import wx.adv
from Book import BookModel
import ConfigPara
from ManageAuthor import EditAuthor

class EditBook(wx.Dialog):
    def __init__(self, title, is_edit):
        wx.Dialog.__init__(self, None, title=title, size=(500, 500))
        self.panel = wx.Panel(self)

        self.is_edit = is_edit  # Xác định xem có đang chỉnh sửa sách hay không

        font = wx.Font(14, wx.FONTFAMILY_DEFAULT,
                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")
        
        lblBookID = wx.StaticText(self.panel, -1, 'Mã sách:', pos=(20, 30), size=(100, 30))
        lblBookID.SetFont(font)
        self.txtBookID = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(150, 30), size=(200, 30))
        self.txtBookID.SetFont(font)

        lblBookTitle = wx.StaticText(self.panel, -1, 'Tên sách:', pos=(20, 80), size=(100, 30))
        lblBookTitle.SetFont(font)
        self.txtBookTitle = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(150, 80), size=(200, 30))
        self.txtBookTitle.SetFont(font)

        lblYear = wx.StaticText(self.panel, -1, 'Năm sáng tác:', pos=(20, 130), size=(120, 30))
        lblYear.SetFont(font)
        self.txtYear = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(150, 130), size=(200, 30))
        self.txtYear.SetFont(font)

        lblPublisher = wx.StaticText(self.panel, -1, 'Nhà xuất bản:', pos=(20, 180), size=(120, 30))
        lblPublisher.SetFont(font)
        self.txtPublisher = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(150, 180), size=(200, 30))
        self.txtPublisher.SetFont(font)

        lblAuthorName = wx.StaticText(self.panel, -1, 'Tên tác giả:', pos=(20, 230), size=(120, 30))
        lblAuthorName.SetFont(font)
        self.txtAuthorName = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(150, 230), size=(200, 30))
        self.txtAuthorName.SetFont(font)

        lblCategory = wx.StaticText(self.panel, -1, 'Thể loại:', pos=(20, 280), size=(120, 30))
        lblCategory.SetFont(font)
        arrCategory = ('Historical', 'Documentary', ' Humanities & Social Sciences', 'Non sci-fi',
                       'For children', 'Memoir & Autobiography', 'Fantasy', 'Food & drink', 'Short story',
                       'Horror', 'Romance', 'Women', 'Sci-fi')
        self.cmbCategory = wx.ComboBox(self.panel, wx.ID_ANY, pos=(150, 280), size=(200, 30),
                                        choices=arrCategory, style=wx.CB_DROPDOWN)
        self.cmbCategory.SetFont(font)

        lblISBN = wx.StaticText(self.panel, -1, 'Số đăng ký:', pos=(20, 330), size=(120, 30))
        lblISBN.SetFont(font)
        self.txtISBN = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(150, 330), size=(200, 30))
        self.txtISBN.SetFont(font)

        if is_edit:
            # Lấy thông tin sách từ CSDL và hiển thị lên giao diện để chỉnh sửa
            if len(ConfigPara.glbBookID) > 0 :
                book = BookModel()
                row = book.getBookInf(ConfigPara.glbBookID)
                for r in row:
                    self.txtBookID.SetValue(r[0])
                    self.txtBookTitle.SetValue(r[1])
                    self.txtYear.SetValue(str(r[2]))
                    self.txtPublisher.SetValue(r[3])
                    self.txtAuthorName.SetValue(r[4])
                    self.cmbCategory.SetValue(r[5])
                    self.txtISBN.SetValue(str(r[6]))

        btnSave = wx.Button(self.panel, wx.ID_ANY, label="Lưu", pos=(20, 380), size=(150, 30))
        btnSave.SetFont(font)
        self.Bind(wx.EVT_BUTTON, self._OnButtonSaveClick, btnSave)


    def _OnButtonSaveClick(self, event):
        strBookID= self.txtBookID.GetValue()
        strBookTitle = self.txtBookTitle.GetValue()
        strYear = self.txtYear.GetValue()
        strPublisher = self.txtPublisher.GetValue()
        strAuthorName = self.txtAuthorName.GetValue()
        strCategory = self.cmbCategory.GetValue()
        strISBN = self.txtISBN.GetValue()

        if not strBookID or not strBookTitle or not strYear or not strPublisher or not strAuthorName or not strCategory or not strISBN:
            wx.MessageBox("Vui lòng nhập đủ thông tin sách!", "Lỗi", wx.OK | wx.ICON_ERROR)
            return

        try:
            pub_year = int(strYear)
        except ValueError:
            wx.MessageBox("Năm sáng tác phải là số nguyên!", "Lỗi", wx.OK | wx.ICON_ERROR)
            return
        
        if not strISBN.isdigit() or len(strISBN) != 10:
            wx.MessageBox("Số ISBN phải là số nguyên và có độ dài 10 chữ số!", "Lỗi", wx.OK | wx.ICON_ERROR)
            return

        try:
            isbn_number = int(strISBN)
        except ValueError:
            wx.MessageBox("Số ISBN phải là số nguyên và có độ dài 10 chữ số!", "Lỗi", wx.OK | wx.ICON_ERROR)
            return
    
        book = BookModel()
        if self.is_edit:
            if strBookID == ConfigPara.glbBookID:
                book.updateBook(strBookID, strBookTitle, strYear, strPublisher, strAuthorName, strCategory, strISBN)
                wx.MessageBox("Chỉnh sửa sách thành công!")
                self.EndModal(wx.ID_OK)
            else:
                wx.MessageBox("Vui lòng không sửa mã của tác giả tác giả")
        else:
            if book.checkBook(strBookID):
                wx.MessageBox("Đã tồn tại mã sách vui lòng nhập lại!")
            else:
                book.addBook(strBookID, strBookTitle, strYear, strPublisher, strAuthorName, strCategory, strISBN)
                wx.MessageBox("Thêm sách thành công!")
                self.EndModal(wx.ID_OK)
    
    
