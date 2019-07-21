#!/usr/bin/env python

import pygtk
pygtk.require('2.0')

import gtk
import pygame, pygame.sndarray
import numpy

sample_rate = 44100
tone_ms = 200

class DTMFDialer:
  dtmf_tones_row = (1209, 1336, 1477, 1633)
  dtmf_tones_col = (697, 770, 852, 941)

  def add_button(self, table, name, col, row):
    button_data = (name, col, row)
    button = gtk.Button(name)
    button.connect("pressed", self.button_pressed, button_data)
    button.connect("released", self.button_released, button_data)
    button.show()
    table.attach(button, col, col + 1, row, row + 1, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

  def __init__(self):
    pygame.mixer.pre_init(sample_rate, channels = 1, buffer = 1024)
    pygame.init()
    pygame.mixer.set_num_channels(3)
    pygame.mixer.set_reserved(2)
    self.sounds_row = [pygame.sndarray.make_sound(self.sine_wave(self.dtmf_tones_row[x], 4096)) for x in range(4)]
    self.sounds_col = [pygame.sndarray.make_sound(self.sine_wave(self.dtmf_tones_col[x], 4096)) for x in range(4)]
    app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#    app_window.set_size_request(500, 350)
#    app_window.set_border_width(10)
    app_window.set_title("DTMF dialer")
    app_window.connect("delete_event", lambda w,e: gtk.main_quit())

    table_layout = gtk.Table(rows = 4, columns = 4, homogeneous = True)

    self.add_button(table_layout, "1", 0, 0)
    self.add_button(table_layout, "2", 1, 0)
    self.add_button(table_layout, "3", 2, 0)
    self.add_button(table_layout, "A", 3, 0)

    self.add_button(table_layout, "4", 0, 1)
    self.add_button(table_layout, "5", 1, 1)
    self.add_button(table_layout, "6", 2, 1)
    self.add_button(table_layout, "B", 3, 1)

    self.add_button(table_layout, "7", 0, 2)
    self.add_button(table_layout, "8", 1, 2)
    self.add_button(table_layout, "9", 2, 2)
    self.add_button(table_layout, "C", 3, 2)

    self.add_button(table_layout, "*", 0, 3)
    self.add_button(table_layout, "0", 1, 3)
    self.add_button(table_layout, "#", 2, 3)
    self.add_button(table_layout, "D", 3, 3)

    table_layout.show()
    app_window.add(table_layout)
    app_window.show()
    return

  def __del__(self): 
    pygame.mixer.quit()

  def button_pressed(self, widget, data):
    print("Button '%s' pressed." % data[0])
    pygame.mixer.Channel(1).play(self.sounds_col[data[2]], -1)
    pygame.mixer.Channel(0).play(self.sounds_row[data[1]], -1)

  def button_released(self, widget, data):
    print("Button '%s' released." % data[0])
    pygame.mixer.Channel(0).stop()
    pygame.mixer.Channel(1).stop()

  def sine_wave(self, freq, gain, delay = tone_ms):
    length = sample_rate / float(freq)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = gain * numpy.sin(xvalues)
    n_samples = int(delay / float(1000) * sample_rate) / int(length) * int(length)
    return numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)

def main():
  gtk.main()
  return 0

if __name__ == "__main__":
  DTMFDialer()
  main()
