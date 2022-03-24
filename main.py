#!/usr/bin/env python3
import argparse
from turtle import st
import rich
from rich import console


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url", dest="url", type=str, required=True)
