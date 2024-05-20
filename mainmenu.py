# Nguyễn Đình Nam 20216859

import wx
from ManageAuthor import MngAuthor
from ManageBook import MngBook

class PnlMenu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('#008080')
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")

        # Tạo các ô chức năng của thư viện
        lblLibTitle = wx.StaticText(self, -1 , 'Quản lý thư viện')
        lblLibTitle.SetFont(font)
        lblLibTitle.SetForegroundColour("#192f60")
        lblLibTitle.SetBackgroundColour("#ffffff")
        btnFont = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")
        self.btnBookMng = wx.Button(self, wx.ID_ANY, 'Quản lý sách',size=(290, 60))
        self.btnBookMng.SetFont(btnFont)
        self.btnAuthMng = wx.Button(self, wx.ID_ANY, 'Quản lý tác giả', size=(290, 60))
        self.btnAuthMng.SetFont(btnFont)

        btnLayout = wx.GridSizer(rows=1, cols=2, gap=(0, 0))
        btnLayout.Add(self.btnBookMng)
        btnLayout.Add(self.btnAuthMng)
        
        # Thêm các layout vào mainlayout
        mainLayout = wx.BoxSizer(wx.VERTICAL)
        mainLayout.Add(-1, 10)
        mainLayout.Add(lblLibTitle, flag = wx.ALIGN_CENTER, border = 10)
        mainLayout.Add(-1, 10)
        mainLayout.Add(btnLayout, flag=wx.ALIGN_CENTER, border=10)
        mainLayout.Add(-1, 5)
        self.SetSizer(mainLayout)


class MainMenu(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(700,250))
        self.panel = PnlMenu(self)
        self.Bind(wx.EVT_BUTTON, self._OnClickAuthor, self.panel.btnAuthMng)
        self.Bind(wx.EVT_BUTTON, self._OnClickBook, self.panel.btnBookMng)
        self.Show()

    # Sự kiện click vào ô tác giả
    def _OnClickAuthor(self, event):
        s1 = MngAuthor("Tác giả")
        s1.Show()

    # Sự kiện click vào ô sách
    def _OnClickBook(self, event):
       s1 = MngBook("Sách")
       s1.Show()
    


