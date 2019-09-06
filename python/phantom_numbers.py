#
# phantom_numbers.py
#
# Phantom Numbers File No. 1 of Release 0.1.0
#
# This library is suitable for Python 2 and Python 3.
#
# MIT License
#
# Copyright (c) 2019 Adrian Gjerstad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# This file uses the tab stop value "    " (Space * 4)
#

import math

class PhantomInteger:
    def __init__(self, bytes_=[3, 232]):
        if not isinstance(bytes_, list):
            raise TypeError("The value entered was not of type list.")

        if len(bytes_) == 0:
            bytes_ = [0]

        bytes_.reverse()
        self.bytes = bytes_

    def __repr__(self):
        result = ""
        tmp = self.bytes.copy()
        for i in range(len(self.bytes)):
            result += str(tmp[i] % 10)
            for j in range(i, len(self.bytes)):
                tmp[j] = math.floor(tmp[j]/10)

        print(result)
        return result
