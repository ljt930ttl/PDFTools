#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/28 10:52
# @Author : linjinting
# @Project : TTLRedis
# @File : logging.py
# @Software: PyCharm

from __future__ import absolute_import

import logging

default_handler = logging.StreamHandler()
default_handler.setFormatter(
    logging.Formatter("[%(asctime)s] %(levelname)s in %(name)s.%(module)s: %(message)s")
)


def has_level_handler(logger):
    """Check if there is a handler in the logging chain that will handle the
    given logger's :meth:`effective level <~logging.Logger.getEffectiveLevel>`.
    """
    level = logger.getEffectiveLevel()
    current = logger

    while current:
        if any(handler.level <= level for handler in current.handlers):
            return True
        if not current.propagate:
            break
        current = current.parent
    return False


def create_logger(name, isDebug=True):
    logger = logging.getLogger(name)

    if isDebug and not logger.level:
        logger.setLevel(logging.DEBUG)

    # if not has_level_handler(logger):
    #     logger.addHandler(default_handler)
    return logger
