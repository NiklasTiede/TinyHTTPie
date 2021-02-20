from tihttp import main

x = main.build_parser()
# print(x)

from tihttp.main import main

args = ["-H", "google.com"]
# args = ["--help"]
# x = main(args)

# print(x)
import sys

old_stdout = sys.stdout

# print(old_stdout)

from io import StringIO
import sys

# creating a context manager to capture the output in a list:
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


with Capturing() as output:
    main(args)


print(type(output))
print(output)
for e in output:
    print(e)

# ###########################

# from greet.greet import cli


# def test_greet_cli(capsys):
#     cli(["Asia/Jakarta"])
#     captured = capsys.readouterr()
#     result = captured.out
#     assert "Hello, Jakarta!" in result
