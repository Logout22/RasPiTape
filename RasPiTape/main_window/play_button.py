import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class PlayButton(object):
    def __init__(self):
        self.widget = Gtk.Button(label="Play")
