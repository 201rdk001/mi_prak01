"""Example module providing the user interface for the game."""

import wx
import ui

if __name__ == '__main__':
    app = wx.App()
    window = ui.MainWindow(None)
    window.Show(True)

    dialog = ui.GameStartDialog(window)
    dialog.Show()
    app.MainLoop()