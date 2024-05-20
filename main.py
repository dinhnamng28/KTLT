# Nguyễn Đình Nam 20216859

from mainmenu import MainMenu
import wx

if __name__ == '__main__':
    app = wx.App(redirect = True)
    s1 = MainMenu("Main Menu")
    s1.Show()
    app.MainLoop()