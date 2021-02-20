# from subprocess import getstatusoutput, getoutput
from src.tihttp.main import main


# prg = "./src/tihttp/main.py"

# # --------------------------------------------------
# def test_exists():
#     assert os.path.isfile(prg)


# def test_myoutput(capsys):  # or use "capfd" for fd-level
#     # print("hello")
#     sys.stderr.write("world\n")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
#     assert captured.err == "world\n"
#     print("next")
#     captured = capsys.readouterr()
#     assert captured.out == "next\n"


def test_api_body(capsys):
    main(["-B", "http://jsonplaceholder.typicode.com/todos?userId=1"])
    captured = capsys.readouterr()
    result = captured.out
    with open("tests/jsonplaceholder.json", "r") as f:
        output = f.read()
    assert result == output


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
