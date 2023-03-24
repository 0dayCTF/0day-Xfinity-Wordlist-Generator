#!/usr/bin/python
# example xfinity wifi password: fever7538harbor
import os
import sys
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(levelname)s | %(message)s')
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)


FIVE_LIST = "wordlists/5list.txt"
FIVE_LIST_BIG = "wordlists/5list-big.txt"
SIX_LIST = "wordlists/6list.txt"
SIX_LIST_BIG = "wordlists/6list-big.txt"
NUM_LIST = "wordlists/numbers.txt"
TEMP_LIST = "temp.txt"
FORWARD = "/Volumes/Data/xfinity_forward.txt"
BACKWARD = "/Volumes/Data/xfinity_backward.txt"


def open_word_list(file_name):
	with open(file_name) as f_in:
		return [item.strip() for item in f_in.readlines()]


def write_list(file_name, list_data):
	with open(file_name, 'a') as f_out:
		f_out.write('\n'.join(list_data))


def write_to_list_file(file_name, line_data):
	with open(file_name, "a") as f_out:
		f_out.write(line_data + "\n")


class XfinityWiFiPassword:
	def __init__(self):
		log.info("Xfinity WiFi Password Generator Started")
		try:
			os.remove(FORWARD)
		except FileNotFoundError:
			pass
		try:
			os.remove(BACKWARD)
		except FileNotFoundError:
			pass
		self.five_list = open_word_list(FIVE_LIST)
		# self.five_list_big = open_word_list(FIVE_LIST_BIG)
		self.six_list = open_word_list(SIX_LIST)
		# self.six_list_big = open_word_list(SIX_LIST_BIG)
		self.numbers = open_word_list(NUM_LIST)
		self.forward_list = []
		self.backward_list = []

	def add_forward(self, password):
		if sys.getsizeof(self.forward_list) >= 5000000:
			write_list(FORWARD, self.forward_list)
			self.forward_list.clear()
		self.forward_list.append(password)

	def add_backward(self, password):
		if sys.getsizeof(self.backward_list) >= 5000000:
			write_list(FORWARD, self.backward_list)
			self.backward_list.clear()
		self.backward_list.append(password)

	def forward(self):
		log.info("Creating forward passwords list")
		for word1 in self.five_list:
			for number in self.numbers:
				for word2 in self.six_list:
					self.add_forward(word1 + number + word2)

	def backward(self):
		log.info("Creating backward passwords list")
		for word1 in self.six_list:
			for number in self.numbers:
				for word2 in self.five_list:
					self.add_backward(word1 + number + word2)


if __name__ == "__main__":
	pass_gen = XfinityWiFiPassword()
	pass_gen.forward()
	pass_gen.backward()