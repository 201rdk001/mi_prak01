# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d-dirty)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Krustiņi un apļi", pos = wx.DefaultPosition, size = wx.Size( 640,240 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 640,240 ), wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Punkti" ), wx.VERTICAL )

        bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Aplis:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer71.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.circle_points_label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.circle_points_label.Wrap( -1 )

        bSizer71.Add( self.circle_points_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer71.Add( ( 10, 0), 1, 0, 5 )

        self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Gājiens:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer71.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.active_player_label = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.active_player_label.Enable( False )

        bSizer71.Add( self.active_player_label, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer71.Add( ( 60, 0), 1, 0, 5 )

        self.m_staticText21 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Krusts:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer71.Add( self.m_staticText21, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.cross_points_label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cross_points_label.Wrap( -1 )

        bSizer71.Add( self.cross_points_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        sbSizer1.Add( bSizer71, 1, wx.EXPAND, 5 )


        bSizer1.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )

        self.game_field_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC|wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        game_field = wx.BoxSizer( wx.HORIZONTAL )


        bSizer3.Add( game_field, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.game_field_panel.SetSizer( bSizer3 )
        self.game_field_panel.Layout()
        bSizer3.Fit( self.game_field_panel )
        bSizer1.Add( self.game_field_panel, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.perform_move_button = wx.Button( self, wx.ID_ANY, u"Izpildīt gājienu", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.perform_move_button.SetDefault()
        bSizer2.Add( self.perform_move_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.new_game_button = wx.Button( self, wx.ID_ANY, u"Sākt jaunu spēli", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.new_game_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.perform_move_button.Bind( wx.EVT_BUTTON, self.on_perform_move_clicked )
        self.new_game_button.Bind( wx.EVT_BUTTON, self.on_new_game_clicked )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_perform_move_clicked( self, event ):
        event.Skip()

    def on_new_game_clicked( self, event ):
        event.Skip()


###########################################################################
## Class GameStartDialog
###########################################################################

class GameStartDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Spēles uzstādījumi", pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.Size( 300,300 ), wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Spēles garums:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.length_num_box = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 15, 25, 15 )
        bSizer3.Add( self.length_num_box, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )

        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Spēlēt ar" ), wx.HORIZONTAL )

        gSizer2 = wx.GridSizer( 1, 2, 0, 0 )

        self.circle_radio_btn = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Apļiem", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.circle_radio_btn.SetValue( True )
        gSizer2.Add( self.circle_radio_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.cross_radio_btn = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Krustiem", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.cross_radio_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        sbSizer3.Add( gSizer2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( sbSizer3, 1, wx.ALL|wx.EXPAND, 5 )

        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Datora algoritms" ), wx.HORIZONTAL )

        gSizer4 = wx.GridSizer( 1, 2, 0, 0 )

        self.minimax_radio_btn = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Minimaksa", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.minimax_radio_btn.SetValue( True )
        gSizer4.Add( self.minimax_radio_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.alfabeta_radio_btn = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Alfa-beta", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer4.Add( self.alfabeta_radio_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        sbSizer5.Add( gSizer4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer2.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )

        self.start_game_button = wx.Button( self, wx.ID_ANY, u"Sākt spēli", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.start_game_button, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.start_game_button.Bind( wx.EVT_BUTTON, self.on_start_game_clicked )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_start_game_clicked( self, event ):
        event.Skip()


###########################################################################
## Class GameOverDialog
###########################################################################

class GameOverDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Spēles beigas!", pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.Size( 300,150 ), wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )


        bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Uzvarēja :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText4.Wrap( -1 )

        bSizer4.Add( self.m_staticText4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Zaudēja :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )

        bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Sākt jaunu spēli", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.on_new_game_clicked )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_new_game_clicked( self, event ):
        event.Skip()


