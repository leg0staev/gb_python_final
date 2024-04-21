import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="this is OS objects parser")
    parser.add_argument('path', metavar='P', type=str, help='enter folder path', default=None, nargs='?')
    return parser.parse_args().path
