import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class StopButton(object):
    def __init__(self):
        self.widget = Gtk.Button(label="Stop")
