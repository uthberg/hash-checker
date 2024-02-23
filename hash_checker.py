#!/usr/bin/python3


initial_hash = input("Enter file hash: ")

verify_hash = input("Enter hash to compare: ")


def Get_Hash(x,y):
	if initial_hash == verify_hash:
		print('Integrity of file is valid')
	else:
		print('Inegrity of file is invalid')


Get_Hash(initial_hash, verify_hash)