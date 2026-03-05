#!/usr/bin/env python3
import argparse

# Create argument parser instances
parse = argparse.ArgumentParser()

# Add and get optional argument
parse.add_argument('--name', help='The name of the person to greet.')
args = parse.parse_args()

# Show results
if args.name:
    print(f'Hello, my name is {args.name}.')
else:
    print(f'Hello there!')
