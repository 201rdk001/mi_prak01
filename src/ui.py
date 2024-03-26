import wx
import ui_generated
import game

class MainWindow(ui_generated.MainWindow):
    def __init__(self, parent):
        ui_generated.MainWindow.__init__(self, parent)

        self.player_type = "O"
        self.active_button = None
        self.game_complete = True
        self.Show()

        self.game_over_dialog = GameOverDialog(self)
        self.start_dialog = GameStartDialog(self)
        self.start_dialog.Show()

    def button_index(self, button):
        return self.game_field_panel.GetChildren().index(button)

    def get_button(self, index):
        return self.game_field_panel.GetChildren()[index]

    def init_game_field(self, state):
        game_field = self.game_field_panel.GetSizer().GetChildren()[0].Sizer
        game_field.Clear(True)

        for character in state:
            button = wx.ToggleButton(
                self.game_field_panel,
                label=character,
                pos=wx.DefaultPosition,
                size=(24, 24),
                style=wx.BORDER_NONE)

            button.Bind(wx.EVT_TOGGLEBUTTON, self.on_game_field_button_clicked)
            game_field.Add(button, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.game_field_panel.Layout()
        self.game_complete = False

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

            if self.player_type != button.Label:
                button.Value = True
                button.GetNextSibling().Value = True
                self.active_button = button
        else:
            if button == self.active_button:
                button.GetNextSibling().Value = False
            else:
                self.active_button.Value = False

    def on_perform_move_clicked(self, event):
        if self.game_complete:
            return

        button = self.active_button

        if button and button.Value:
            button.GetNextSibling().Destroy()
            button.Label = self.player_type
            button.Value = False

            if self.player_type == "O":
                self.player_type = "X"
            else:
                self.player_type = "O"

            self.active_button = None
            self.game_field_panel.Layout()

        if self.is_game_complete():
            self.on_game_completed()

    def on_new_game_clicked(self, event):
        self.start_dialog.Show()


    def is_game_complete(self):
        buttons = self.game_field_panel.GetChildren()
        count = len(buttons)

        if count <= 1:
            return True

        for i in range(count - 1):
            if buttons[i].Label != self.player_type:
                return False

        return True

    def on_game_completed(self):
        self.game_complete = True
        # Game completion code here
        self.game_over_dialog.ShowModal()

class GameStartDialog(ui_generated.GameStartDialog):
    def get_selected_player_type(self):
        if self.circle_radio_btn.Value:
            return game.GameAlgorithm.MINIMAX

        return game.GameAlgorithm.ALFABETA

    def get_selected_algorithm(self):
        if self.minimax_radio_btn.Value:
            return game.PlayerType.CIRCLE

        return game.PlayerType.CROSS

    def on_start_game_clicked(self, event):
        game.set_settings(
            int(self.length_num_box.Value),
            self.get_selected_player_type(),
            self.get_selected_algorithm())

        self.Parent.init_game_field(game.temp_get_game_state())
        self.Hide()
        event.Skip()

class GameOverDialog(ui_generated.GameOverDialog):
    def __init__(self, parent):
        ui_generated.GameOverDialog.__init__(self, parent)

    def on_new_game_clicked(self, event):
        self.Hide()
        self.Parent.start_dialog.Show()
        event.Skip()
