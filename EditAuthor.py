# Nguyễn Đình Nam 20216859

import wx
import wx.adv
from Author import AuthorModel
import datetime as dt
import ConfigPara

class EditAuthor(wx.Dialog):
    def __init__(self, title, is_edit):
        wx.Dialog.__init__(self, None, title=title, size=(450, 400))
        self.panel = wx.Panel(self)

        self.is_edit = is_edit

        self.font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")

        # Tạo search box, các thông tin tìm kiếm, cài đặt font
        lblAuthorID = wx.StaticText(self.panel, -1, 'ID tác giả:', pos=(20, 20), size=(140, 30))
        lblAuthorID.SetFont(self.font)
        self.txtAuthorID = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(170, 20), size=(200, 30))
        self.txtAuthorID.SetFont(self.font)

        lblAuthorName = wx.StaticText(self.panel, -1, 'Tên tác giả:', pos=(20, 70), size=(140, 30))
        lblAuthorName.SetFont(self.font)
        self.txtAuthorName = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(170, 70), size=(200, 30))
        self.txtAuthorName.SetFont(self.font)

        lblBirthday = wx.StaticText(self.panel, -1, 'Ngày sinh:', pos=(20, 120), size=(140, 30))
        lblBirthday.SetFont(self.font)
        self.dtmBirthday = wx.adv.DatePickerCtrl(self.panel, wx.ID_ANY, pos=(170, 120), size=(200, 30), style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        self.dtmBirthday.SetFont(self.font)


        lblNation = wx.StaticText(self.panel, -1, 'Quốc tịch:', pos=(20, 170), size=(140, 30))
        lblNation.SetFont(self.font)
        arrNationality = ('Việt Nam', 'Nhật', 'Mỹ', 'Anh', 'Pháp', 'Tây Ban Nha', 'Trung Quốc', 'Ý', 'Hàn Quốc')
        self.cmbNation = wx.ComboBox(self.panel, wx.ID_ANY, pos=(170, 170), size=(200, 30), choices=arrNationality, style=wx.CB_DROPDOWN)
        self.cmbNation.SetFont(self.font)

        # Nếu tác giả tồn tại lấy ra thông tin tác giả
        if self.is_edit:
            if len(ConfigPara.glbAuthorID) > 0:
                author = AuthorModel()
                row = author.getAuthorInf(ConfigPara.glbAuthorID)
                if row:
                    for r in row:
                        self.txtAuthorID.SetValue(str(r[0]))
                        self.txtAuthorName.SetValue(str(r[1]))

                        if isinstance(r[2], dt.datetime):
                            wx_datetime = wx.DateTime.FromDMY(r[2].day, r[2].month - 1, r[2].year)
                            self.dtmBirthday.SetValue(wx_datetime)
                        else:
                            self.dtmBirthday.SetValue(str(r[2]))

                        self.cmbNation.SetValue(str(r[3]))
                else:
                    wx.MessageBox("Mã tác giả không tồn tại!", "Lỗi", wx.OK | wx.ICON_ERROR)
                            
        btnSave = wx.Button(self.panel, label="Lưu thông tin", pos=(20, 220), size=(350, 30))
        btnSave.SetFont(self.font)
        self.Bind(wx.EVT_BUTTON, self._OnButtonSaveClick, btnSave)


    def _OnButtonSaveClick(self, event):
        strAuthorID = self.txtAuthorID.GetValue()
        strAuthorName = self.txtAuthorName.GetValue()
        selected_date = self.dtmBirthday.GetValue()
        date = dt.datetime(selected_date.GetYear(), selected_date.GetMonth() + 1, selected_date.GetDay())
        strBirthday = date.strftime('%Y-%m-%d')
        strCountryname = self.cmbNation.GetValue()

        if not strAuthorName or not strBirthday or not strCountryname:
            wx.MessageBox("Vui lòng nhập đủ thông tin tác giả!", "Lỗi", wx.OK | wx.ICON_ERROR)
            return

        author = AuthorModel()

        if self.is_edit:
            if strAuthorID == ConfigPara.glbAuthorID:
                author.updateAuthor(strAuthorID, strAuthorName,str(strBirthday), strCountryname)
                wx.MessageBox("Chỉnh tác giả thành công!")
                self.EndModal(wx.ID_OK)
                
            else:
                wx.MessageBox("Vui lòng không chỉnh sửa mã tác giả!")
        else:
            if author.checkAuthor(strAuthorID):
                wx.MessageBox("Đã tồn tại mã tác giả!")
            else:
                author.addAuthor(strAuthorID, strAuthorName, str(strBirthday), strCountryname)
                wx.MessageBox("Thêm mới tác giả thành công!")
                self.EndModal(wx.ID_OK)
    

