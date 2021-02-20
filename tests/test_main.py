import pytest
import os


# parser = build_parser(['tihttp', 'google.com'])
# print(parser)

# x = print(os.system("python --version"))
# print(x)

# def test_parser():
#     parser = build_parser(['-l', '-m'])
#     assert parser == 'a'


import os
import sys
from subprocess import getstatusoutput, getoutput
from src.tihttp.main import main

# prg = "./hello.py"

# prg = "./src/tihttp/main.py"
# # --------------------------------------------------
# def test_exists():
#     assert os.path.isfile(prg)


def test_myoutput(capsys):  # or use "capfd" for fd-level
    # print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"


def test_greet_cli(capsys):
    cli(["Asia/Jakarta"])
    captured = capsys.readouterr()
    result = captured.out
    assert "Hello, Jakarta!" in result


def test_google_header(capsys):
    main(["-H", "google.com"])
    captured = capsys.readouterr()
    result = captured.out
    assert "Hello, Jakarta!" in result


# --------------------------------------------------
# def test_usage():
#     for flag in ["-h", "--help"]:
#         rv, out = getstatusoutput(f"{prg} {flag}")
#         assert rv == 0
#         assert out.lower().startswith("usage")


# # --------------------------------------------------
# def test_default():
#     out = getoutput(prg)
#     assert out.strip() == "Hello, World!"


# #  --------------------------------------------------
# def test_input():
#     for val in ["Universe", "Multiverse"]:
#         for option in ["-n", "--name"]:
#             rv, out = getstatusoutput(f"{prg} {option} {val}")
#             assert rv == 0
#             assert out.strip() == f"Hello, {val}!"
