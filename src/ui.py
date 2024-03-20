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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,240 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 640,240 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Sākt jaunu spēli", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn1, 0, 0, 5 )

		self.m_toggleBtn2 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn2, 0, 0, 5 )

		self.m_toggleBtn3 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn3, 0, 0, 5 )

		self.m_toggleBtn4 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn4, 0, 0, 5 )

		self.m_toggleBtn5 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn5, 0, 0, 5 )

		self.m_toggleBtn6 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn6, 0, 0, 5 )

		self.m_toggleBtn7 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn7, 0, 0, 5 )

		self.m_toggleBtn8 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn8, 0, 0, 5 )

		self.m_toggleBtn9 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn9, 0, 0, 5 )

		self.m_toggleBtn10 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn10, 0, 0, 5 )

		self.m_toggleBtn11 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn11, 0, 0, 5 )

		self.m_toggleBtn12 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn12, 0, 0, 5 )

		self.m_toggleBtn13 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn13, 0, 0, 5 )

		self.m_toggleBtn14 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn14, 0, 0, 5 )

		self.m_toggleBtn15 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn15, 0, 0, 5 )

		self.m_toggleBtn16 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn16, 0, 0, 5 )

		self.m_toggleBtn17 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn17, 0, 0, 5 )

		self.m_toggleBtn18 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn18, 0, 0, 5 )

		self.m_toggleBtn19 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn19, 0, 0, 5 )

		self.m_toggleBtn20 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn20, 0, 0, 5 )

		self.m_toggleBtn21 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn21, 0, 0, 5 )

		self.m_toggleBtn22 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn22, 0, 0, 5 )

		self.m_toggleBtn23 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn23, 0, 0, 5 )

		self.m_toggleBtn24 = wx.ToggleButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn24, 0, 0, 5 )

		self.m_toggleBtn25 = wx.ToggleButton( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 24,24 ), wx.BORDER_NONE )
		bSizer6.Add( self.m_toggleBtn25, 0, 0, 5 )


		bSizer4.Add( bSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer4.Add( bSizer7, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class GameStartDialog
###########################################################################

class GameStartDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 350,350 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 350,350 ), wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Spēles garums:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Spēlēt ar" ), wx.HORIZONTAL )

		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )

		self.m_radioBtn5 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Apļiem", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_radioBtn5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_radioBtn6 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Krustiem", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_radioBtn6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer3.Add( gSizer2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( sbSizer3, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Spēlēt pret" ), wx.HORIZONTAL )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_radioBtn7 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Cilvēku", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_radioBtn7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_radioBtn8 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Datoru", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_radioBtn8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer4.Add( gSizer3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( sbSizer4, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Datora algoritms" ), wx.HORIZONTAL )

		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )

		self.m_radioBtn9 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Minimaksa", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_radioBtn9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_radioBtn10 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Alfa-beta", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_radioBtn10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer5.Add( gSizer4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer2.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Sākt spēli", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


