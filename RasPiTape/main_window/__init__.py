#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow():
    def __init__(self):
        self.window = Gtk.Window(title="RasPiTape")
        self.setup_events()

    def setup_events(self):
        self.window.connect("destroy", Gtk.main_quit)

    def display_window(self):
        self.window.show_all()


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.display_window()
    Gtk.main()
