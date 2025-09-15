import sys
from io import StringIO
from longest_ticket import read_input

def test_read_input():
    test_input = """
    1, 2, 8.54
    2, 3, 3.11
    3, 1, 2.19
    3, 4, 4
    4, 1, 1.4
    """
    sys.stdin = StringIO(test_input)
    graph = read_input()
    sys.stdin = sys.__stdin__  # 元に戻す
    expected = {
        1: [(2, 8.54)],
        2: [(3, 3.11)],
        3: [(1, 2.19), (4, 4.0)],
        4: [(1, 1.4)]
    }
    assert graph == expected, f"期待値: {expected}, 実際: {graph}"
    print("test_read_input: OK")

if __name__ == "__main__":
    test_read_input()
