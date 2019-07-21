#!/usr/bin/env python

import pygtk
pygtk.require('2.0')

import gtk
import pygame, pygame.sndarray
import numpy

sample_rate = 44100

class DTMFDialer:
  dtmf_tones_row = [1209, 1336, 1477, 1633]
  dtmf_tones_col = [697, 770, 852, 941]

  def add_button(self, table, name, col, row):
    button_data = (name, col, row)
    button = gtk.Button(name)
    button.connect("pressed", self.button_pressed, button_data)
    button.connect("released", self.button_released, button_data)
    button.show()
    table.attach(button, col, col + 1, row, row + 1, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

  def gen_dtmf_tone(self, y, x):
    f1 = self.dtmf_tones_row[x]
    f2 = self.dtmf_tones_col[y]
    l1 = sample_rate / float(f1)
    l2 = sample_rate / float(f2)

    s1 = self.sine_wave(f1, 4096, int(round(l1)) * int(round(l2)))
    s2 = self.sine_wave(f2, 4096, int(round(l1)) * int(round(l2)))
    return pygame.sndarray.make_sound((s1 + s2) / 2)

  def __init__(self):
    pygame.mixer.pre_init(sample_rate, channels = 1, buffer = 512)
    pygame.init()
    self.sounds = [[self.gen_dtmf_tone(y, x) for x in range(4)] for y in range(4)]
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
    pygame.mixer.Channel(0).play(self.sounds[data[2]][data[1]], -1)
    print("Button '%s' pressed." % data[0])

  def button_released(self, widget, data):
    pygame.mixer.Channel(0).stop()
    print("Button '%s' released." % data[0])

  def sine_wave(self, freq, gain, samples = sample_rate):
    length = sample_rate / float(freq)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(round(length))) * omega
    onecycle = gain * numpy.sin(xvalues)
    return numpy.resize(onecycle, (samples,)).astype(numpy.int16)

def main():
  gtk.main()
  return 0

if __name__ == "__main__":
  DTMFDialer()
  main()
