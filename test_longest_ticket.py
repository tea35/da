from io import StringIO
from longest_ticket import create_network

def test_create_network():
    """
    正常な入力データが正しくパースされるかをテスト
    """
    # パターン1: 通常
    test_input1 = """
    1, 2, 8.54
    2, 3, 3.11
    3, 1, 2.19
    3, 4, 4
    4, 1, 1.4
    """
    graph = create_network(StringIO(test_input1))
    expected = {
        1: [(2, 8.54)],
        2: [(3, 3.11)],
        3: [(1, 2.19), (4, 4.0)],
        4: [(1, 1.4)]
    }
    assert graph == expected, f"期待値: {expected}, 実際: {graph}"
    print("test_create_network1: OK")

    # パターン2: 1駅のみ
    test_input2 = "1, 2, 5.0"
    graph = create_network(StringIO(test_input2))
    expected = {1: [(2, 5.0)]}
    assert graph == expected, f"期待値: {expected}, 実際: {graph}"
    print("test_create_network2: OK")

    # パターン3: 空白や余分なスペース
    test_input3 = " 1 , 2 , 10.0  \n 2,3, 2.5 "
    graph = create_network(StringIO(test_input3))
    expected = {1: [(2, 10.0)], 2: [(3, 2.5)]}
    assert graph == expected, f"期待値: {expected}, 実際: {graph}"
    print("test_create_network3: OK")

    # パターン4: \r\n改行コード対応テスト
    test_input4 = "1,2,8.54\r\n2,3,3.11\r\n3,4,4.0\r\n"
    graph = create_network(StringIO(test_input4))
    expected = {1: [(2, 8.54)], 2: [(3, 3.11)], 3: [(4, 4.0)]}
    assert graph == expected, f"期待値: {expected}, 実際: {graph}"
    print("test_create_network4: OK")

def test_invalid_input():
    """
    無効な入力（要素数不足・型変換失敗）が無視されるかをテスト
    """
    # パターン1: 無効行のみ
    test_input1 = "invalid line\n1,2\n1,2,abc\n"
    graph = create_network(StringIO(test_input1))
    assert graph == {}, f"無効入力は無視されるべき: {graph}"
    print("test_invalid_input1: OK")

    # パターン2: 有効と無効混在
    test_input2 = "1,2,3.0\n1,2,abc\n2,3,4.0"
    graph = create_network(StringIO(test_input2))
    expected = {1: [(2, 3.0)], 2: [(3, 4.0)]}
    assert graph == expected, f"期待値: {expected}, 実際: {graph}"
    print("test_invalid_input2: OK")

    # パターン3: 空入力
    test_input3 = ""
    graph = create_network(StringIO(test_input3))
    assert graph == {}, f"空入力は空グラフであるべき: {graph}"
    print("test_invalid_input3: OK")

if __name__ == "__main__":
    test_create_network()
    test_invalid_input()
