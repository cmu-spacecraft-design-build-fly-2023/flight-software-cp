# The MIT License (MIT)
#
# Copyright (c) 2017 Tony DiCola for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
`jetson_comm`
====================================================

Library for interfacing with the Jetson through UART. Also gives access
to the GPIO pins for signaling.

* Author(s): Harry Rosmann, Gordonson Yan

Implementation Notes
--------------------

TBD

"""

class JetsonComm:
    def __init__(self, uart):
        self._uart = uart

    def read(self, num_bytes):
        """Read up to num_bytes of data from the Jetson Nano directly, without parsing.
        Returns a bytearray with up to num_bytes or None if nothing was read"""
        return self._uart.read(num_bytes)

    def write(self, bytestr):
        """Write a bytestring data to the GPS directly, without parsing
        or checksums"""
        return self._uart.write(bytestr)

    @property
    def in_waiting(self):
        """Returns number of bytes available in UART read buffer"""
        return self._uart.in_waiting
    
    def readline(self):
        """Returns a newline terminated bytearray, must have timeout set for
        the underlying UART or this will block forever!"""
        return self._uart.readline()