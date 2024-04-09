import threading
import wx
import ui_generated
import game

class MainWindow(ui_generated.MainWindow):
    def __init__(self, parent):
        ui_generated.MainWindow.__init__(self, parent)
        self.game_over_dialog = GameOverDialog(self)
        self.start_dialog = GameStartDialog(self)

        self.game = None
        self.chosen_player = None
        self.active_button = None

        self.Show()
        self.start_dialog.ShowModal()

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

        if self.chosen_player != 'O':
            self.game_field_panel.Disable()
            self.perform_move_button.Disable()
            self.new_game_button.Disable()
            self.game_field_panel.Update()
            threading.Thread(target=self.perform_computer_move, daemon=True).start()

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
            return True

        if self.game.player != self.chosen_player:
            self.game_field_panel.Disable()
            self.perform_move_button.Disable()
            self.new_game_button.Disable()
            self.game_field_panel.Update()
            threading.Thread(target=self.perform_computer_move, daemon=True).start()
        else:
            self.game_field_panel.Enable()
            self.perform_move_button.Enable()
            self.new_game_button.Enable()

        return False

    def perform_person_move(self):
        if self.active_button and self.active_button.Value:
            self.perform_move(self.active_button)
            self.active_button = None

    def perform_computer_move(self):
        index = self.game.generate_computer_move()
        wx.CallAfter(self.start_computer_move_animation, index)

    def start_computer_move_animation(self, index):
        button: wx.ToggleButton = self.get_button(index)
        # Highlight buttons
        button.BackgroundColour = (128, 191, 255)
        button.GetNextSibling().BackgroundColour = (128, 191, 255)
        # Wait 1.5 seconds before completing move
        wx.CallLater(1500, self.end_computer_move_animation, button)

    def end_computer_move_animation(self, button):
        button.BackgroundColour = wx.NullColour
        ended = self.perform_move(button)
        self.active_button = None

        if ended:
            self.game_field_panel.Disable()
            self.perform_move_button.Disable()
            self.new_game_button.Disable()
            self.game_field_panel.Update()
            return

        self.game_field_panel.Enable()
        self.perform_move_button.Enable()
        self.new_game_button.Enable()

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
        self.start_dialog.ShowModal()

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
        self.Parent.start_dialog.ShowModal()
        event.Skip()
