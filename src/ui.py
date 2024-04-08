import wx
import ui_generated
import game

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

    def button_index(self, button):
        return self.game_field_panel.GetChildren().index(button)

    def get_button(self, index):
        return self.game_field_panel.GetChildren()[index]

    def init_game(self):
        self.chosen_player = self.start_dialog.get_selected_player()
        self.game = game.Game(
            int(self.start_dialog.length_num_box.Value),
            self.start_dialog.get_selected_algorithm())

        # Initalize labels
        self.active_player_label.SetLabel(str(self.game.player))
        self.circle_points_label.SetLabel(str(self.game.circle_points)) # Circle
        self.cross_points_label.SetLabel(str(self.game.cross_points))   # Cross

        game_field = self.game_field_panel.GetSizer().GetChildren()[0].Sizer
        game_field.Clear(True)

        for character in self.game.state:
            button = wx.ToggleButton(
                self.game_field_panel,
                label=character,
                pos=wx.DefaultPosition,
                size=(24, 24),
                style=wx.BORDER_DEFAULT)

            button.Bind(wx.EVT_TOGGLEBUTTON, self.on_game_field_button_clicked)
            game_field.Add(button, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.game_field_panel.Layout()

        if (self.chosen_player != 'O'):
            self.perform_computer_move()

    def perform_move(self, button):
        if self.game.has_ended:
            return

        button.GetNextSibling().Destroy()
        button.Label = self.game.player
        button.Value = False
        self.game_field_panel.Layout()

        self.game.execute_move(self.button_index(button))
        self.active_player_label.SetLabel(str(self.game.player))
        self.circle_points_label.SetLabel(str(self.game.circle_points)) # Circle
        self.cross_points_label.SetLabel(str(self.game.cross_points))   # Cross

        if self.game.has_ended:
            self.on_game_completed()
        elif self.game.player != self.chosen_player:
            self.perform_computer_move()

    def perform_person_move(self):
        if self.active_button and self.active_button.Value:
            self.perform_move(self.active_button)
            self.active_button = None

    def perform_computer_move(self):
        self.perform_move_button.Disable()

        index = self.game.generate_computer_move()
        button: wx.ToggleButton = self.get_button(index)
        # Highlight buttons
        button.BackgroundColour = (179, 217, 255)
        button.GetNextSibling().BackgroundColour = (179, 217, 255)
        # Wait 1.5 seconds before completing move
        wx.CallLater(1500, self.perform_computer_move_delayed, button)

    def perform_computer_move_delayed(self, button):
        button.BackgroundColour = wx.NullColour
        self.perform_move(button)
        self.perform_move_button.Enable()
        self.active_button = None

    def on_game_field_button_clicked(self, event):
        button: wx.ToggleButton = event.EventObject

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
        self.perform_person_move()

    def on_new_game_clicked(self, event):
        self.start_dialog.Show()

    def on_game_completed(self):
        self.active_player_label.SetLabel(str(self.game.player))
        self.circle_points_label.SetLabel(str(self.game.circle_points)) # Circle
        self.cross_points_label.SetLabel(str(self.game.cross_points))   # Cross

        self.game_over_dialog.set_winner(self.game)
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

    def set_winner(self, game):
        if game.get_winner() =='O':
            self.m_staticText4.SetLabel("Uzvarēja: O")
            self.m_staticText3.SetLabel("Zaudēja: X")
        elif game.get_winner() =='X':
            self.m_staticText4.SetLabel("Uzvarēja: X")
            self.m_staticText3.SetLabel("Zaudēja: O")
        else:
            self.m_staticText4.SetLabel("Neizšķirts")
            self.m_staticText3.SetLabel(" ")

    def on_new_game_clicked(self, event):
        self.Hide()
        self.Parent.start_dialog.Show()
        event.Skip()
