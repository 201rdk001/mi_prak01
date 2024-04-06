import wx
import ui_generated
import game
import time
import threading

class MainWindow(ui_generated.MainWindow):
    def __init__(self, parent):
        ui_generated.MainWindow.__init__(self, parent)
        self.game_over_dialog = GameOverDialog(self)
        self.start_dialog = GameStartDialog(self)
        self.Show()
        self.start_dialog.Show()

        self.game = None
        self.chosen_player = None
        self.active_button = None
        #gājiens button
        self.m_toggleBtn1.SetLabel('O')
        #punktus pielikt
        self.game = game.Game(
            int(self.start_dialog.length_num_box.Value),
            self.start_dialog.get_selected_algorithm())
        self.m_staticText3.SetLabel(str(self.game.cross_points))    #krusts
        self.m_staticText6.SetLabel(str(self.game.circle_points))    #aplis

    def button_index(self, button):
        return self.game_field_panel.GetChildren().index(button)

    def get_button(self, index):
        return self.game_field_panel.GetChildren()[index]

    def init_game(self):
        self.chosen_player = self.start_dialog.get_selected_player()
        self.game = game.Game(
            int(self.start_dialog.length_num_box.Value),
            self.start_dialog.get_selected_algorithm())

        game_field = self.game_field_panel.GetSizer().GetChildren()[0].Sizer
        game_field.Clear(True)

        for character in self.game.state:
            button = wx.ToggleButton(
                self.game_field_panel,
                label=character,
                pos=wx.DefaultPosition,
                size=(24, 24),
                style=wx.BORDER_NONE)

            button.Bind(wx.EVT_TOGGLEBUTTON, self.on_game_field_button_clicked)
            game_field.Add(button, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.game_field_panel.Layout()

    def on_game_field_button_clicked(self, event):
        button = event.EventObject

        if not button.GetNextSibling():
            button.Value = False
            return

        if button.Value:
            if self.active_button:
                self.active_button.Value = False
                self.active_button.GetNextSibling().Value = False

            button.Value = False

            if self.game.player != button.Label:
                button.Value = True
                button.GetNextSibling().Value = True
                self.active_button = button
        else:
            if button == self.active_button:
                button.GetNextSibling().Value = False
            else:
                self.active_button.Value = False

    def on_perform_move_clicked(self, event):
        
        if self.game.has_ended:
            return

        button = self.active_button

        if button and button.Value:
            button.GetNextSibling().Destroy()
            button.Label = self.game.player
            button.Value = False
            self.game_field_panel.Layout()

            self.active_button = None
            self.game.execute_move(self.button_index(button))
            #nomainīt, kuram gājiens
            self.m_toggleBtn1.SetLabel(game.get_opponent(self.start_dialog.get_selected_player()))
            #punktus pielikt
            self.game = game.Game(
            int(self.start_dialog.length_num_box.Value),
            self.start_dialog.get_selected_algorithm())
            self.m_staticText3.SetLabel(str(self.game.cross_points))    #krusts
            self.m_staticText6.SetLabel(str(self.game.circle_points))    #aplis
            if self.game.has_ended:
                self.on_game_completed()

        
    def perform_computer_move(self,event):
        
        if self.game.has_ended:
            return
        
        button = self.get_button(self.game.generate_computer_move())
        #iezime pogas
        button.BackgroundColour = (252, 140, 71) 
        button.GetNextSibling().BackgroundColour = (252, 140, 71)
        #gaida 3sek pirms izdzēš
        #timer = threading.Timer(3.0, button.GetNextSibling().Destroy())
        #timer.start()
        #button.BackgroundColour = button.GetNextSibling().BackgroundColour
        button.GetNextSibling().Destroy()
        button.Label = self.game.player
        button.style=wx.BORDER_NONE
        self.game_field_panel.Layout()
        self.game.execute_move(self.button_index(button))
        #nomainīt, kuram gājiens
        self.m_toggleBtn1.SetLabel(self.start_dialog.get_selected_player())
        #punktus pielikt
        self.game = game.Game(
            int(self.start_dialog.length_num_box.Value),
            self.start_dialog.get_selected_algorithm())
        self.m_staticText3.SetLabel(str(self.game.cross_points))    #krusts
        self.m_staticText6.SetLabel(str(self.game.circle_points))    #aplis
        if self.game.has_ended:
            self.on_game_completed()

    def on_new_game_clicked(self, event):
        self.start_dialog.Show()

    def on_game_completed(self):
        # Game completion code here
        self.game_over_dialog.ShowModal()

class GameStartDialog(ui_generated.GameStartDialog):
    def get_selected_player(self):
        return 'O' if self.circle_radio_btn.Value else 'X'

    def get_selected_algorithm(self):
        return 'minimax' if self.minimax_radio_btn.Value else 'alfabeta'

    def on_start_game_clicked(self, event):
        self.Parent.init_game()
        self.Hide()
        event.Skip()

class GameOverDialog(ui_generated.GameOverDialog):
    def __init__(self, parent):
        ui_generated.GameOverDialog.__init__(self, parent)
        self.start_dialog = GameStartDialog(self)
        self.m_staticText4.SetLabel("Uzvarēja: "+ str(game.get_opponent(game.get_opponent(game.Game.get_winner))))
        self.m_staticText3.SetLabel("Zaudēja: "+str(game.get_opponent(game.Game.get_winner)))
    def on_new_game_clicked(self, event):
        self.Hide()
        self.Parent.start_dialog.Show()
        event.Skip()
