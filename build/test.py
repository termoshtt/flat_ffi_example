#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import flatbuffers
import flat_cpp
from Electic import FooBar


def test_cpp_binding():
    a = flat_cpp.new_zero(3)
    assert (a == numpy.zeros(3)).all()


def test_flatbuffers():
    builder = flatbuffers.Builder(0)
    say = builder.CreateString("Madoka kawaii")

    FooBar.FooBarStart(builder)
    FooBar.FooBarAddHeight(builder, 150)
    FooBar.FooBarAddSay(builder, say)
    off = FooBar.FooBarEnd(builder)
    builder.Finish(off)

    buf = builder.Output()
    foobar = FooBar.FooBar.GetRootAsFooBar(buf, 0)

    assert foobar.Height() == 150
    assert foobar.Say() == b"Madoka kawaii"
