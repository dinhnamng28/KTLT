# Nguyễn Đình Nam 20216859

import wx
import wx.adv
import wx.grid
from Author import AuthorModel
from EditAuthor import EditAuthor
import ConfigPara
from datetime import datetime

class PnlMngAuthor(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('#008080')
        arrNationality = ('Việt Nam', 'Nhật', 'Mỹ', 'Anh', 'Pháp', 'Tây Ban Nha', 'Trung Quốc', 'Ý', 'Hàn Quốc')
        
        self.font = wx.Font(14, wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")
        
        # tạo search box, các thông tin tìm kiếm, cài đặt font
        staticBox = wx.StaticBox(self, -1, "Tìm kiếm tác giả:")
        staticBox.SetFont(self.font)
        searchBox = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        
        lblAuthorID = wx.StaticText(self, -1, 'Mã tác giả:', size=(140, 30))
        lblAuthorID.SetFont(self.font)
        self.txtAuthorID = wx.TextCtrl(self, wx.ID_ANY, size=(300, 30))
        self.txtAuthorID.SetFont(self.font)
        
        lblAuthorName = wx.StaticText(self, -1, 'Tên tác giả:', size=(140, 30))
        lblAuthorName.SetFont(self.font)
        self.txtAuthorName = wx.TextCtrl(self, wx.ID_ANY, size=(300, 30))
        self.txtAuthorName.SetFont(self.font)
        
        lblBirthdayF = wx.StaticText(self, -1, 'Ngày sinh từ:', size=(140, 30))
        lblBirthdayT = wx.StaticText(self, -1, 'Ngày sinh đến:', size=(140, 30))
        lblBirthdayF.SetFont(self.font)
        lblBirthdayT.SetFont(self.font)
        self.dtmBirthdayF = wx.adv.DatePickerCtrl(self, wx.ID_ANY, style=wx.adv.DP_DROPDOWN)
        self.dtmBirthdayT = wx.adv.DatePickerCtrl(self, wx.ID_ANY, style=wx.adv.DP_DROPDOWN)
        self.dtmBirthdayF.SetFont(self.font)
        self.dtmBirthdayT.SetFont(self.font)
        
        lblNation = wx.StaticText(self, -1, 'Quốc tịch:', size=(140, 30))
        lblNation.SetFont(self.font)
        self.cmbNation = wx.ComboBox(self, wx.ID_ANY, '',
                                     choices=arrNationality, style = wx.CB_DROPDOWN)
        self.cmbNation.SetFont(self.font)
        
        self.btnSearch = wx.Button(self, label="Tìm kiếm", size=(120, 30))
        self.btnSearch.SetFont(self.font)
        
        self.btnAddNew = wx.Button(self, label="Tạo mới", size=(120, 30))
        self.btnAddNew.SetFont(self.font)

        # tạo các layout và thêm mục tìm kiếm vào layout
        layoutAuthorID = wx.BoxSizer(wx.HORIZONTAL)
        layoutAuthorID.Add(lblAuthorID)
        layoutAuthorID.Add(self.txtAuthorID)

        layoutAuthorName = wx.BoxSizer(wx.HORIZONTAL)
        layoutAuthorName.Add(lblAuthorName)
        layoutAuthorName.Add(self.txtAuthorName)

        layoutNational = wx.BoxSizer(wx.HORIZONTAL)
        layoutNational.Add(lblNation)
        layoutNational.Add(self.cmbNation)

        layoutBirthday = wx.BoxSizer(wx.HORIZONTAL)
        layoutBirthday.Add(lblBirthdayF)
        layoutBirthday.Add(self.dtmBirthdayF)
        layoutBirthday.Add(5, -1)
        layoutBirthday.Add(lblBirthdayT)
        layoutBirthday.Add(self.dtmBirthdayT)

        searchBox.Add(-1, 10)
        searchBox.Add(layoutAuthorID)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutAuthorName)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutBirthday)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutNational)
        searchBox.Add(-1, 10)
        searchBox.Add(self.btnSearch, flag=wx.ALIGN_RIGHT)
        searchBox.Add(-1, 10)
        layoutSearch = wx.BoxSizer(wx.HORIZONTAL)
        layoutSearch.Add(searchBox)
        layoutSearch.Add(20, 0)
        layoutSearch.Add(self.btnAddNew, flag = wx.ALIGN_CENTER)

        # tạo bảng hiển thị
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(100, 7)
        self.grid.SetFont(self.font)
        self.grid.SetRowLabelSize(0)

        self.grid.SetColLabelValue(0, "STT")
        self.grid.SetColSize(0, 50)
        self.grid.SetColLabelValue(1, "ID")
        self.grid.SetColSize(1, 100)
        self.grid.SetColLabelValue(2, "Tên tác giả")
        self.grid.SetColSize(2, 270)
        self.grid.SetColLabelValue(3, "Ngày sinh")
        self.grid.SetColSize(3, 120)
        self.grid.SetColLabelValue(4, "Quốc tịch")
        self.grid.SetColSize(4, 150)
        self.grid.SetColSize(5, 50)
        self.grid.SetColSize(6, 100)
        self.grid.SetLabelFont(self.font)

        # cài đặt các giá trị cho bảng
        author = AuthorModel()
        rows = author.getAuthorList()
        count = 0

        for r in rows:
            self.grid.SetCellValue(count, 0 , str(count + 1))
            self.grid.SetCellValue(count, 1,str(r[0]).upper())
            self.grid.SetCellValue(count, 2, r[1])
            if isinstance(r[2], datetime):
                self.grid.SetCellValue(count, 3, r[2].strftime('%y-%m-%d'))
            else:
                self.grid.SetCellValue(count, 3, str(r[2]))
            self.grid.SetCellValue(count, 4, str(r[3]))
            self.grid.SetCellValue(count, 5, "Edit")
            self.grid.SetCellValue(count, 6, "Delete")
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
        self.grid.SetColAttr(5, attrEdit)
        attrDelete = wx.grid.GridCellAttr()
        attrDelete.SetFont(self.font)
        attrDelete.SetBackgroundColour("#ff0000")
        attrDelete.SetTextColour("#ffffff")
        attrDelete.SetAlignment(wx.ALIGN_CENTER,wx.ALIGN_CENTER)
        self.grid.SetColAttr(6, attrDelete)

        layoutList = wx.BoxSizer(wx.VERTICAL)
        layoutList.Add(self.grid)

        # thêm các layout vào màn hình mainlayout
        mainLayout = wx.BoxSizer(wx.VERTICAL)
        mainLayout.Add(-1, 10)
        mainLayout.Add(layoutSearch)
        mainLayout.Add(-1,15)
        mainLayout.Add(layoutList)

        self.SetSizer(mainLayout)


    def UpdateGridAuthor(self, rows):
        self.grid.ClearGrid()
        count = 0
        for r in rows:
            self.grid.SetCellValue(count, 0 , str(count + 1))
            self.grid.SetCellValue(count, 1,str(r[0]).upper())
            self.grid.SetCellValue(count, 2, str(r[1]).title())
            if isinstance(r[2], datetime):
                self.grid.SetCellValue(count, 3, r[2].strftime('%y-%m-%d'))
            else:
                self.grid.SetCellValue(count, 3, str(r[2]))
            self.grid.SetCellValue(count, 4, str(r[3]).title())
            self.grid.SetCellValue(count, 5, "Edit")
            self.grid.SetCellValue(count, 6, "Delete")
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
        self.grid.SetColAttr(5, attrEdit)
        attrDelete = wx.grid.GridCellAttr()
        attrDelete.SetFont(self.font)
        attrDelete.SetBackgroundColour("#ff0000")
        attrDelete.SetTextColour("#ffffff")
        attrDelete.SetAlignment(wx.ALIGN_CENTER,wx.ALIGN_CENTER)
        self.grid.SetColAttr(6, attrDelete)


class MngAuthor(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(950,700))
        self.panel = PnlMngAuthor(self)
        self.Bind(wx.EVT_BUTTON, self._OnButtonClickSearch, self.panel.btnSearch)
        self.Bind(wx.EVT_BUTTON, self._OnButtonAddClick, self.panel.btnAddNew)
        self.panel.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self._OnGridCellClick)
        self.Show()


    # Sự kiện tìm kiếm tác giả
    def _OnButtonClickSearch(self, event):
        author = AuthorModel()
        strAuthorID = self.panel.txtAuthorID.GetValue()
        strAuthorName = self.panel.txtAuthorName.GetValue()
        dtmBirthdayF = self.panel.dtmBirthdayF.GetValue()
        strBirthdayF = f"{dtmBirthdayF.GetYear()}-{dtmBirthdayF.GetMonth()+1}-{dtmBirthdayF.GetDay()}"
        dtmBirthdayT = self.panel.dtmBirthdayT.GetValue()
        strBirthdayT = f"{dtmBirthdayT.GetYear()}-{dtmBirthdayT.GetMonth()+1}-{dtmBirthdayT.GetDay()}"
        strCountryname = self.panel.cmbNation.GetValue()

        # Tìm kiếm tác giả
        author_list = author.searchAuthor(strAuthorID, strAuthorName, strBirthdayF, strBirthdayT, strCountryname)
        rows = []
        for author in author_list:
            au_id, au_name, birthday, country = author
            if (strAuthorID and strAuthorID in au_id) or \
               (strAuthorName and strAuthorName in au_name) or \
               (strBirthdayF and strBirthdayF <= birthday <= strBirthdayT) or \
               (strCountryname and strCountryname == country):
                rows.append(author)

        self.panel.UpdateGridAuthor(rows)


    # Tạo mới hiển thị Grid sau khi thêm, sửa, xóa
    def _OnButtonClick(self, event):
        author = AuthorModel()
        # Lấy ra thông tin tác giả
        rows = author.getAuthorList()
        self.panel.UpdateGridAuthor(rows)


    # Sự kiện tạo mới tác giả
    def _OnButtonAddClick(self, event):
        s1 = EditAuthor("Thêm tác giả", False)
        result = s1.ShowModal()
        if result == wx.ID_OK:
            self._OnButtonClick(event)
        s1.Destroy()
    

    # Sự kiện chỉnh sửa và xóa tác giả
    def _OnGridCellClick(self,event):
        if event.GetCol() == 5:
            rowId = event.GetRow()
            ConfigPara.glbAuthorID = self.panel.grid.GetCellValue(rowId, 1)  
            s1 = EditAuthor("Thêm tác giả", True)
            result = s1.ShowModal()
            if result == wx.ID_OK:
                self._OnButtonClick(event)
            s1.Destroy()
        elif event.GetCol() == 6:
            rowId = event.GetRow()
            authorId = self.panel.grid.GetCellValue(rowId, 1)
            authorDel = AuthorModel()
            authorDel.deleteAuthor(authorId)
            wx.MessageBox("Xóa thành công!")
            self._OnButtonClick(event)
                

