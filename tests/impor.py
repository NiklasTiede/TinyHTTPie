# from pprint import pprint
# import sys

# import sys

# sys.path.append("..")

# # from src import tihttp


# # sys.path.append('../src')
# pprint(sys.modules)

# from src.tihttp.main import build_parser

# parser = build_parser()
# print(parser)
# import os
# os.cwd()
# print(os.cwd())

# sys.path.append("")
############

# from src.tihttp import main

# x = main.build_parser()
# print(x)

from src.tihttp.main import main

args = ["-H", "google.com"]
main(args)
