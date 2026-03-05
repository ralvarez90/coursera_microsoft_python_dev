#!/usr/bin/env python3
import argparse
import os

parse = argparse.ArgumentParser()

parse.add_argument('--path', help='The path to list files from.')
args = parse.parse_args()

if args.path:
    for item in os.listdir(args.path):
        print(f'- {item}')
else:
    for item in os.listdir('.'):
        print(f'- {item}')
