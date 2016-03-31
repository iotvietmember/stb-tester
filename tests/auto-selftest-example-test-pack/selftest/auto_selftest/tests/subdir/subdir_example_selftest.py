#!/usr/bin/env python
# coding=utf-8
"""
This file contains regression tests automatically generated by
``stbt auto-selftest``. These tests are intended to capture the
behaviour of Frame Objects (and other helper functions that operate on
a video-frame). Commit this file to git, re-run ``stbt auto-selftest``
whenever you make a change to your Frame Objects, and use ``git diff``
to see how your changes affect the behaviour of the Frame Object.

NOTE: THE OUTPUT OF THE DOCTESTS BELOW IS NOT NECESSARILY "CORRECT" --
it merely documents the behaviour at the time that
``stbt auto-selftest`` was run.
"""
# pylint: disable=line-too-long

import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '../../../../tests/subdir'))

from subdir_example import *  # isort:skip pylint: disable=wildcard-import, import-error

_FRAME_CACHE = {}


def f(name):
    img = _FRAME_CACHE.get(name)
    if img is None:
        import cv2
        filename = os.path.join(os.path.dirname(__file__),
                                '../../../screenshots', name)
        img = cv2.imread(filename)
        assert img is not None, "Failed to load %s" % filename
        _FRAME_CACHE[name] = img
    return img


def auto_selftest_Truth():
    r"""
    >>> Truth(frame=f("frame-object-with-dialog-different-background.png"))
    Truth(is_visible=True)
    >>> Truth(frame=f("frame-object-with-dialog.png"))
    Truth(is_visible=True)
    >>> Truth(frame=f("frame-object-with-dialog2.png"))
    Truth(is_visible=True)
    >>> Truth(frame=f("frame-object-without-dialog-different-background.png"))
    Truth(is_visible=True)
    >>> Truth(frame=f("frame-object-without-dialog.png"))
    Truth(is_visible=True)
    """
    pass