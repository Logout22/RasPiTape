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
        self.button_container = Gtk.Box()

        self.record_button = RecordButton()
        self.play_button = PlayButton()
        self.prev_button = PrevButton()
        self.next_button = NextButton()
        self.stop_button = StopButton()
        self.pause_button = PauseButton()

        self.arrange_ui_elements()
        self.setup_events()

    def arrange_ui_elements(self):
        self.create_button_container()
        for button in [
            self.record_button,
            self.play_button,
            self.prev_button,
            self.next_button,
            self.stop_button,
            self.pause_button
        ]:
            self.add_button_to_row(button)

    def create_button_container(self):
        self.window.add(self.button_container)

    def add_button_to_row(self, button):
        self.button_container.pack_start(button.widget, False, False, 0)

    def setup_events(self):
        self.window.connect("destroy", Gtk.main_quit)

    def display_window(self):
        self.window.show_all()


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.display_window()
    Gtk.main()
