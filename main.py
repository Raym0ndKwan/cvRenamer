#Not working

# -*- coding:utf-8 -*-
import os
import PyPDF2
import wx
import sys



class Rename_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'PDF File Rename', size=(400, 350))
        panel = wx.Panel(self, -1)

        self.Text1 = wx.StaticText(panel, label=u'Folder address ', pos=(13, 80), size=(100, 60))
        self.TextCtrl1 = wx.TextCtrl(panel, pos=(107, 80), size=(250, 25))

        self.Button1 = wx.Button(panel, -1, u'START', pos=(90, 200), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.begin_click, self.Button1)

        self.Button2 = wx.Button(panel, -1, u'CANCEL', pos=(205, 200), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.cancel_click, self.Button2)

    def begin_click(self, event):
        folder_address = self.TextCtrl1.GetValue()
        for file_name in os.listdir(folder_address):
            print(file_name)
            if file_name.lower()[-3:] == 'pdf':
                try:
                    file_name_full = folder_address + '/' + file_name
                    text_name = file_name_full[:-3] + 'txt'

                    os.system("pdftotext '%s' '%s' -enc  UTF-8 " % (file_name_full, text_name))

                    with open(text_name) as f:
                        first_line = f.readline()
                    pdf_title = first_line.strip().split()
                    pdf_title = pdf_title[0] + '.pdf'

                except:
                    pdf_title = '0_' + file_name


                try:
                    pdf_title = folder_address + '/' + pdf_title
                    os.rename(file_name_full,  pdf_title)
                    os.remove(text_name)
                    print(pdf_title)
                except:
                    pass
        self.Destroy()
        sys.exit()

    def cancel_click(self, event):
        self.Destroy()
        sys.exit()


def main():
    app = wx.App()
    win = Rename_Frame()

    win.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()