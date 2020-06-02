#!/usr/bin/python3


"""
This module creates a new MyList Class
"""


class MyList(list):
	"""My List class

	Arguments:
		list --
	"""
	def print_sorted(self):
		print(sorted(self))
