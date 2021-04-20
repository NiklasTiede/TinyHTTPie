import tihttp

def test_api_body(capsys):
    tihttp.main(["-B", "http://jsonplaceholder.typicode.com/todos?userId=1"])
    captured = capsys.readouterr()
    result = captured.out
    with open("tests/jsonplaceholder.json", "r") as f:
        output = f.read()
    assert result == output
