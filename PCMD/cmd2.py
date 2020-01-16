__author__ = "Burgess Zheng"
# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Command
"""
import os


class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        print(self)
        self()

    def __call__(self):
        print('renaming {} to {}'.format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print('renaming {} to {}'.format(self.dest, self.src))
        os.rename(self.dest, self.src)


if __name__ == "__main__":

    command_stack = []

    # commands are just pushed into the command stack
    command_stack.append(MoveFileCommand('foo.txt', 'foo.txt'))
    print(type(command_stack[0]).__name__)
    command_stack.append(MoveFileCommand('bar.txt', 'bar1.txt'))
    print(type(command_stack[1]).__name__)

    # they can be executed later on
    for cmd in command_stack:
        cmd.execute()

    # and can also be undone at will
    for cmd in reversed(command_stack):
        cmd.undo()
