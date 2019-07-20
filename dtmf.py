#!/usr/bin/env python

import pygtk
pygtk.require('2.0')

import gtk
import pygame, pygame.sndarray
import numpy

sample_rate = 44100

class MyProgram:
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
    pygame.mixer.init(sample_rate, channels = 1)
    self.sound1 = pygame.sndarray.make_sound(self.sine_wave(self.dtmf_tones_row[0], 4096))
    self.sound2 = pygame.sndarray.make_sound(self.sine_wave(self.dtmf_tones_col[0], 4096))
    app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#    app_window.set_size_request(500, 350)
#    app_window.set_border_width(10)
    app_window.set_title("DTMF dialer")
    app_window.connect("delete_event", lambda w,e: gtk.main_quit())

    table_layout = gtk.Table(rows=4, columns=4, homogeneous=True)

    button_one_data = ("1", 0, 0)
    button_one = gtk.Button("1")
    button_one.connect("pressed", self.button_pressed, button_one_data)
    button_one.connect("released", self.button_released, button_one_data)
    button_one.show()
    table_layout.attach(button_one, 0, 1, 0, 1, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_two = gtk.Button("2")
    button_two_data = ("2", 1, 0)
    button_two.connect("pressed", self.button_pressed, button_two_data)
    button_two.connect("released", self.button_released, button_two_data)
    button_two.show()
    table_layout.attach(button_two, 1, 2, 0, 1, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_three = gtk.Button("3")
    button_three_data = ("3", 2, 0)
    button_three.connect("pressed", self.button_pressed, button_three_data)
    button_three.connect("released", self.button_released, button_three_data)
    button_three.show()
    table_layout.attach(button_three, 2, 3, 0, 1, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_a = gtk.Button("A")
    button_a_data = ("A", 3, 0)
    button_a.connect("pressed", self.button_pressed, button_a_data)
    button_a.connect("released", self.button_released, button_a_data)
    button_a.show()
    table_layout.attach(button_a, 3, 4, 0, 1, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)


    button_four = gtk.Button("4")
    button_four_data = ("4", 0, 1)
    button_four.connect("pressed", self.button_pressed, button_four_data)
    button_four.connect("released", self.button_released, button_four_data)
    button_four.show()
    table_layout.attach(button_four, 0, 1, 1, 2, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_five = gtk.Button("5")
    button_five_data = ("5", 1, 1)
    button_five.connect("pressed", self.button_pressed, button_five_data)
    button_five.connect("released", self.button_released, button_five_data)
    button_five.show()
    table_layout.attach(button_five, 1, 2, 1, 2, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_six = gtk.Button("6")
    button_six_data = ("6", 2, 1)
    button_six.connect("pressed", self.button_pressed, button_six_data)
    button_six.connect("released", self.button_released, button_six_data)
    button_six.show()
    table_layout.attach(button_six, 2, 3, 1, 2, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_b = gtk.Button("B")
    button_b_data = ("B", 3, 1)
    button_b.connect("pressed", self.button_pressed, button_b_data)
    button_b.connect("released", self.button_released, button_b_data)
    button_b.show()
    table_layout.attach(button_b, 3, 4, 1, 2, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)


    button_seven = gtk.Button("7")
    button_seven_data = ("7", 0, 2)
    button_seven.connect("pressed", self.button_pressed, button_seven_data)
    button_seven.connect("released", self.button_released, button_seven_data)
    button_seven.show()
    table_layout.attach(button_seven, 0, 1, 2, 3, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_eight = gtk.Button("8")
    button_eight_data = ("8", 1, 2)
    button_eight.connect("pressed", self.button_pressed, button_eight_data)
    button_eight.connect("released", self.button_released, button_eight_data)
    button_eight.show()
    table_layout.attach(button_eight, 1, 2, 2, 3, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_nine = gtk.Button("9")
    button_nine_data = ("9", 2, 2)
    button_nine.connect("pressed", self.button_pressed, button_nine_data)
    button_nine.connect("released", self.button_released, button_nine_data)
    button_nine.show()
    table_layout.attach(button_nine, 2, 3, 2, 3, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_c = gtk.Button("C")
    button_c_data = ("C", 3, 2)
    button_c.connect("pressed", self.button_pressed, button_c_data)
    button_c.connect("released", self.button_released, button_c_data)
    button_c.show()
    table_layout.attach(button_c, 3, 4, 2, 3, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)


    button_star = gtk.Button("*")
    button_star_data = ("*", 0, 3)
    button_star.connect("pressed", self.button_pressed, button_star_data)
    button_star.connect("released", self.button_released, button_star_data)
    button_star.show()
    table_layout.attach(button_star, 0, 1, 3, 4, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_zero = gtk.Button("0")
    button_zero_data = ("0", 1, 3)
    button_zero.connect("pressed", self.button_pressed, button_zero_data)
    button_zero.connect("released", self.button_released, button_zero_data)
    button_zero.show()
    table_layout.attach(button_zero, 1, 2, 3, 4, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_hash = gtk.Button("#")
    button_hash_data = ("#", 2, 3)
    button_hash.connect("pressed", self.button_pressed, button_hash_data)
    button_hash.connect("released", self.button_released, button_hash_data)
    button_hash.show()
    table_layout.attach(button_hash, 2, 3, 3, 4, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    button_d = gtk.Button("D")
    button_d_data = ("D", 3, 3)
    button_d.connect("pressed", self.button_pressed, button_d_data)
    button_d.connect("released", self.button_released, button_d_data)
    button_d.show()
    table_layout.attach(button_d, 3, 4, 3, 4, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 0, 0)

    table_layout.show()
    app_window.add(table_layout)
    app_window.show()
    return

  def button_pressed(self, widget, data):
    print("Button '%s' pressed." % data[0])
    self.sound1.stop()
    self.sound2.stop()
    self.sound1 = pygame.sndarray.make_sound(self.sine_wave(self.dtmf_tones_row[data[1]], 4096))
    self.sound2 = pygame.sndarray.make_sound(self.sine_wave(self.dtmf_tones_col[data[2]], 4096))
    self.sound1.play(-1)
    self.sound2.play(-1)

  def button_released(self, widget, data):
    print("Button '%s' released." % data[0])
    self.sound1.stop()
    self.sound2.stop()

  def sine_wave(self, hz, peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    return numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)


def main():
  gtk.main()
  return 0

if __name__ == "__main__":
  MyProgram()
  main()
