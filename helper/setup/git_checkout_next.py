#!/usr/bin/python
import sys
import utils.mojo_utils as mojo_utils


def main(argv):
    mojo_utils.git_checkout_next_all()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
