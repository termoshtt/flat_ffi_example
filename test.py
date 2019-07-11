#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import flat_cpp


def test_cpp_binding():
    a = flat_cpp.new_zero(3)
    assert (a == numpy.zeros(3)).all()
