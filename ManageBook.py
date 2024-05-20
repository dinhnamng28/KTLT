# Nguyễn Đình Nam 20216859

import wx
import wx.adv
import wx.grid
from Book import BookModel
from EditBook import EditBook
import pandas as pd
import ConfigPara

class PnlMngBook(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('#008080')
        arrCategory = ('Historical', 'Documentary', ' Humanities & Social Sciences', 'Non sci-fi'
                    , 'For children', 'Memoir & Autobiography', 'Fantasy', 'Food & drink', 'Short story'
                    , 'Horor', 'Romance', 'Women', 'Sci-fi')
        self.font = wx.Font(14, wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")
        
        # tạo search box, các thông tin tìm kiếm, cài đặt font
        staticBox = wx.StaticBox(self, -1, "Tìm kiếm sách:")
        staticBox.SetFont(self.font)
        searchBox = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

        lblBookID = wx.StaticText(self, -1, 'Mã sách:', size = (140, 30))
        lblBookID.SetFont(self.font)
        self.txtBookID = wx.TextCtrl(self, wx.ID_ANY, size = (250, 30))
        self.txtBookID.SetFont(self.font)
        
        lblBookTitle = wx.StaticText(self, -1, 'Tên sách:', size = (140, 30))
        lblBookTitle.SetFont(self.font)
        self.txtBookTitle = wx.TextCtrl(self, wx.ID_ANY, size = (250, 30))
        self.txtBookTitle.SetFont(self.font)

        lblAuthorName = wx.StaticText(self, -1, 'Tên tác giả:', size = (140, 30))
        lblAuthorName.SetFont(self.font)
        self.txtAuthorName = wx.TextCtrl(self, wx.ID_ANY, size = (250, 30))
        self.txtAuthorName.SetFont(self.font)

        lblPubliser = wx.StaticText(self, -1, 'Nhà xuất bản:', size = (140, 30))
        lblPubliser.SetFont(self.font)
        self.txtPubliser = wx.TextCtrl(self, wx.ID_ANY, size = (250, 30))
        self.txtPubliser.SetFont(self.font)

        lblCategory = wx.StaticText(self, -1, 'Thể loại:', size = (150, 30))
        lblCategory.SetFont(self.font)
        self.cmbCategory = wx.ComboBox(self, wx.ID_ANY, size = (100, 30),
                                       choices = arrCategory, style = wx.CB_DROPDOWN)
        self.cmbCategory.SetFont(self.font)
        
        lblISBN = wx.StaticText(self, -1, 'Số đăng ký:', size = (150, 30))
        lblISBN.SetFont(self.font)
        self.txtISBN = wx.TextCtrl(self, wx.ID_ANY, size = (150, 30))
        self.txtISBN.SetFont(self.font)

        lblYearF = wx.StaticText(self, -1, 'Từ:', size = (100, 30))
        lblYearT = wx.StaticText(self, -1, 'Đến:', size = (100, 30))
        lblYearF.SetFont(self.font)
        lblYearT.SetFont(self.font)
        self.dtmYearF = wx.TextCtrl(self, wx.ID_ANY, size = (80, 30))
        self.dtmYearT = wx.TextCtrl(self, wx.ID_ANY, size = (80, 30))
        self.dtmYearF.SetFont(self.font)
        self.dtmYearT.SetFont(self.font)

        self.btnSearch = wx.Button(self, label="Tìm kiếm", size = (120, 30))
        self.btnSearch.SetFont(self.font)
        self.btnAddNew = wx.Button(self, label="Tạo mới", size = (120, 30))
        self.btnAddNew.SetFont(self.font)
        self.btnSortISBN = wx.Button(self, label="Xếp theo số ISBN", size = (200, 30))
        self.btnSortISBN.SetFont(self.font)
        self.btnSortPub = wx.Button(self, label = "Xếp theo NXB", size = (150, 30))
        self.btnSortPub.SetFont(self.font)
        self.btnExport = wx.Button(self, label = "Xuất file", size = (150, 30))
        self.btnExport.SetFont(self.font)

        # tạo các layout và thêm mục tìm kiếm vào layout
        layoutBook = wx.BoxSizer(wx.HORIZONTAL)
        layoutBook.Add(lblBookID)
        layoutBook.Add(self.txtBookID)
        layoutBook.Add(30,-1)
        layoutBook.Add(lblBookTitle)
        layoutBook.Add(self.txtBookTitle)
        layoutBook.Add(30,-1)
        layoutBook.Add(lblCategory)
        layoutBook.Add(self.cmbCategory)

        layoutAuPub = wx.BoxSizer(wx.HORIZONTAL)
        layoutAuPub.Add(lblAuthorName)
        layoutAuPub.Add(10,-1)
        layoutAuPub.Add(self.txtAuthorName)
        layoutAuPub.Add(10,-1)
        layoutAuPub.Add(lblPubliser)
        layoutAuPub.Add(10,-1)
        layoutAuPub.Add(self.txtPubliser)

        layoutISBN = wx.BoxSizer(wx.HORIZONTAL)
        layoutISBN.Add(lblISBN)
        layoutISBN.Add(10, -1)
        layoutISBN.Add(self.txtISBN)

        layoutYear = wx.BoxSizer(wx.HORIZONTAL)
        layoutYear.Add(lblYearF)
        layoutYear.Add(self.dtmYearF)
        layoutYear.Add(20, -1)
        layoutYear.Add(lblYearT)
        layoutYear.Add(self.dtmYearT)

        searchBox.Add(-1, 10)
        searchBox.Add(layoutBook)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutAuPub)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutISBN)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutYear)
        searchBox.Add(-1, 10)

        buttonLayout = wx.BoxSizer(wx.HORIZONTAL)
        buttonLayout.Add(self.btnSearch, flag=wx.ALIGN_CENTER)
        buttonLayout.AddSpacer(50)
        buttonLayout.Add(self.btnAddNew, flag=wx.ALIGN_CENTER)
        buttonLayout.AddSpacer(50)
        buttonLayout.Add(self.btnSortISBN, flag=wx.ALIGN_CENTER)
        buttonLayout.AddSpacer(50)
        buttonLayout.Add(self.btnSortPub, flag=wx.ALIGN_CENTER)
        buttonLayout.AddSpacer(50)
        buttonLayout.Add(self.btnExport, flag=wx.ALIGN_CENTER)
        searchBox.Add(buttonLayout)

        layoutSearch = wx.BoxSizer(wx.HORIZONTAL)
        layoutSearch.Add(searchBox)
        layoutSearch.Add(20, 0)

        # tạo bảng hiển thị
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(100, 10)
        self.grid.SetFont(self.font)
        self.grid.SetRowLabelSize(0)
        self.grid.SetColLabelValue(0, "STT")
        self.grid.SetColSize(0, 50)
        self.grid.SetColLabelValue(1, "ID")
        self.grid.SetColSize(1, 150)
        self.grid.SetColLabelValue(2, "Tên sách")
        self.grid.SetColSize(2, 270)
        self.grid.SetColLabelValue(3, "Năm sáng tác")
        self.grid.SetColSize(3, 150)
        self.grid.SetColLabelValue(4, "Nhà xuất bản")
        self.grid.SetColSize(4, 130)
        self.grid.SetColLabelValue(5, "Tác giả")
        self.grid.SetColSize(5, 200)
        self.grid.SetColLabelValue(6, "Thể loại")
        self.grid.SetColSize(6, 100)
        self.grid.SetColLabelValue(7, "Số đăng ký")
        self.grid.SetColSize(7,150)
        self.grid.SetColSize(8, 50)
        self.grid.SetColSize(9, 100)
        self.grid.SetLabelFont(self.font)

        # Cài đặt các giá trị cho bảng
        book = BookModel()
        rows = book.getBookList()
        count = 0

        for r in rows:
            self.grid.SetCellValue(count, 0 , str(count + 1))
            self.grid.SetCellValue(count, 1, str(r[0]))
            self.grid.SetCellValue(count, 2, str(r[1]))
            self.grid.SetCellValue(count, 3, str(r[2]))
            self.grid.SetCellValue(count, 4, str(r[3]))
            self.grid.SetCellValue(count, 5, str(r[4]))
            self.grid.SetCellValue(count, 6, str(r[5]))
            self.grid.SetCellValue(count, 7, str(r[6]))
            self.grid.SetCellValue(count, 8, "Edit")
            self.grid.SetCellValue(count, 9, "Delete")
            attr = wx.grid.GridCellAttr()
            attr.SetFont(self.font)
            self.grid.SetRowAttr(count, attr)
            self.grid.SetRowSize(count, 35)
            count = count + 1

        attrEdit = wx.grid.GridCellAttr()
        attrEdit.SetFont(self.font)
        attrEdit.SetBackgroundColour("#006e54")
        attrEdit.SetTextColour("#ffffff")
        attrEdit.SetAlignment(wx.ALIGN_CENTER,wx.ALIGN_CENTER)
        self.grid.SetColAttr(8, attrEdit)
        attrDelete = wx.grid.GridCellAttr()
        attrDelete.SetFont(self.font)
        attrDelete.SetBackgroundColour("#ff0000")
        attrDelete.SetTextColour("#ffffff")
        attrDelete.SetAlignment(wx.ALIGN_CENTER,wx.ALIGN_CENTER)
        self.grid.SetColAttr(9, attrDelete)

        layoutList = wx.BoxSizer(wx.VERTICAL)
        layoutList.Add(self.grid)

        mainLayout = wx.BoxSizer(wx.VERTICAL)
        mainLayout.Add(-1, 20)
        mainLayout.Add(layoutSearch)
        mainLayout.Add(-1,15)
        mainLayout.Add(layoutList)
        self.SetSizer(mainLayout)


    def UpdateGrid(self, rows):
        self.grid.ClearGrid()
        count = 0
        for r in rows:
            self.grid.SetCellValue(count, 0 , str(count + 1))
            self.grid.SetCellValue(count, 1, str(r[0]).upper())
            self.grid.SetCellValue(count, 2, str(r[1]).title())
            self.grid.SetCellValue(count, 3, str(r[2]))
            self.grid.SetCellValue(count, 4, str(r[3]).title())
            self.grid.SetCellValue(count, 5, str(r[4]).title())
            self.grid.SetCellValue(count, 6, str(r[5]).title())
            self.grid.SetCellValue(count, 7, str(r[6]))
            self.grid.SetCellValue(count, 8, "Edit")
            self.grid.SetCellValue(count, 9, "Delete")
            attr = wx.grid.GridCellAttr()
            attr.SetFont(self.font)
            self.grid.SetRowAttr(count, attr)
            self.grid.SetRowSize(count, 35)
            count = count + 1

        attrEdit = wx.grid.GridCellAttr()
        attrEdit.SetFont(self.font)
        attrEdit.SetBackgroundColour("#006e54")
        attrEdit.SetTextColour("#ffffff")
        attrEdit.SetAlignment(wx.ALIGN_CENTER,wx.ALIGN_CENTER)
        self.grid.SetColAttr(8, attrEdit)
        attrDelete = wx.grid.GridCellAttr()
        attrDelete.SetFont(self.font)
        attrDelete.SetBackgroundColour("#ff0000")
        attrDelete.SetTextColour("#ffffff")
        attrDelete.SetAlignment(wx.ALIGN_CENTER,wx.ALIGN_CENTER)
        self.grid.SetColAttr(9, attrDelete)


class MngBook(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(1350,700))
        self.panel = PnlMngBook(self)
        self.Bind(wx.EVT_BUTTON, self._OnButtonClickSearch, self.panel.btnSearch)
        self.Bind(wx.EVT_BUTTON, self._OnButtonAddClickBook, self.panel.btnAddNew)
        self.Bind(wx.EVT_BUTTON, self._OnButtonSortClick1, self.panel.btnSortISBN)
        self.Bind(wx.EVT_BUTTON, self._OnButtonSortClick2, self.panel.btnSortPub)
        self.Bind(wx.EVT_BUTTON, self._OnButtonExportClick, self.panel.btnExport)
        self.panel.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self._OnGridCellClickBook)
        self.Show()


    # Sự kiện tìm kiếm sách
    def _OnButtonClickSearch(self, event):
        # Lấy thông tin sách
        book = BookModel()
        strBookID = self.panel.txtBookID.GetValue()
        strBookTitle = self.panel.txtBookTitle.GetValue()
        strYearF = self.panel.dtmYearF.GetValue()
        strYearT = self.panel.dtmYearT.GetValue()
        strPublisher = self.panel.txtPubliser.GetValue()
        strAuthorname = self.panel.txtAuthorName.GetValue()
        strCategory = self.panel.cmbCategory.GetValue()
        strISBN = self.panel.txtISBN.GetValue()
        
        book_list = book.searchBook(strBookID, strBookTitle, strYearF, strYearT, strPublisher, strAuthorname, strCategory, strISBN)
        rows = []
        for book_info in book_list:
            rows.append(book_info)

        # Hiển thị tìm kiếm
        self.panel.UpdateGrid(rows)


    # Hiện thị thông tin trên Grid sau khi thêm, sửa, xóa
    def _OnButtonClickBook(self, event):
        # Lấy thông tin sách
        book = BookModel()
        # Hiển thị tìm kiếm
        rows = book.getBookList()
        self.panel.UpdateGrid(rows)


    # Sự kiện tạo mới sách
    def _OnButtonAddClickBook(self, event):
        s1 = EditBook("Thêm sách", False)
        result = s1.ShowModal()
        if result == wx.ID_OK:
            self._OnButtonClickBook(event)
        s1.Destroy()


    # Sự kiện chỉnh sửa và xóa sách 8: sửa sách, 9: xóa sách
    def _OnGridCellClickBook(self,event):
        if event.GetCol() == 8:
            rowId = event.GetRow()
            ConfigPara.glbBookID = self.panel.grid.GetCellValue(rowId, 1)
            s1 = EditBook("Sửa sách", True)
            result = s1.ShowModal()
            if result == wx.ID_OK:
                self._OnButtonClickBook(event)
            s1.Destroy()

        elif event.GetCol() == 9:
            rowId = event.GetRow()
            bookId = self.panel.grid.GetCellValue(rowId, 1)
            bookDel = BookModel()
            bookDel.deleteBook(bookId)
            wx.MessageBox("Xóa thành công!")
            self._OnButtonClickBook(event)


    # Sự kiện sắp xếp theo số ISBN
    def _OnButtonSortClick1(self, event):
        book = BookModel()
        self.panel.grid.ClearGrid()
        sorted_books_by_isbn = book.sortISBN()  # Lấy danh sách sách đã được sắp xếp theo ISBN
        self.panel.UpdateGrid(sorted_books_by_isbn)


    # Sự kiện sắp xếp theo NXB 
    def _OnButtonSortClick2(self, event):
        book = BookModel()
        self.panel.grid.ClearGrid()
        sorted_books_by_pub = book.sortPub()  # Lấy danh sách sách đã được sắp xếp theo NXB
        self.panel.UpdateGrid(sorted_books_by_pub)


    # Sự kiện xuất file
    def _OnButtonExportClick(self, event):
        book = BookModel()
        rows = book.getBookList()

        # Chuyển dữ liệu thành DataFrame của pandas
        df = pd.DataFrame(rows, columns=['ID', 'Tên sách', 'Năm sáng tác', 'Nhà xuất bản', 'Tác giả', 'Thể loại', 'Số đăng ký'])

        # Hiển thị hộp thoại để chọn vị trí và tên file
        file_dialog = wx.FileDialog(self, "Lưu file Excel", wildcard=".xlsx", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if file_dialog.ShowModal() == wx.ID_CANCEL:
            return

        # Lấy đường dẫn và tên file đã chọn
        file_path = file_dialog.GetPath()
        file_dialog.Destroy()
        df.to_excel(file_path, index=False)

        wx.MessageBox("Dữ liệu đã được xuất ra file Excel thành công!")



