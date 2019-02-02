#!/usr/bin/env python3
from RasPiTape.main_window.next_button import NextButton
from RasPiTape.main_window.pause_button import PauseButton
from RasPiTape.main_window.prev_button import PrevButton
from RasPiTape.main_window.record_button import RecordButton
from RasPiTape.main_window.play_button import PlayButton
from RasPiTape.main_window.stop_button import StopButton

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(object):
    def __init__(self):
        self.window = Gtk.Window(title="RasPiTape")

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.window.add(self.grid)

        self.file_list_store = Gtk.ListStore(str, float)
        self.file_list_store.append(["test.wav", 2.15])
        self.file_list_view = Gtk.TreeView.new_with_model(self.file_list_store)
        self.file_list_view.append_column(Gtk.TreeViewColumn("File Name", Gtk.CellRendererText(), text=0))
        self.file_list_view.append_column(Gtk.TreeViewColumn("Length", Gtk.CellRendererText(), text=1))

        self.record_button = RecordButton()
        self.play_button = PlayButton()
        self.prev_button = PrevButton()
        self.next_button = NextButton()
        self.stop_button = StopButton()
        self.pause_button = PauseButton()

        self.arrange_ui_elements()
        self.setup_events()

    def arrange_ui_elements(self):
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)

        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(self.record_button.widget, self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.play_button.widget, self.record_button.widget, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.prev_button.widget, self.play_button.widget, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.next_button.widget, self.prev_button.widget, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.stop_button.widget, self.next_button.widget, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.pause_button.widget, self.stop_button.widget, Gtk.PositionType.RIGHT, 1, 1)

        self.scrollable_treelist.add(self.file_list_view)

    def setup_events(self):
        self.window.connect("destroy", Gtk.main_quit)

    def display_window(self):
        self.window.show_all()


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.display_window()
    Gtk.main()
