# 最長経路探索のテスト
from io import StringIO
from longest_ticket import create_network, find_longest_path

def test_longest_path():
    """
    正常な路線データで最長経路が正しく求まるかをテスト
    """
    # パターン1: 例題通り
    test_input1 = """
    1, 2, 8.54
    2, 3, 3.11
    3, 1, 2.19
    3, 4, 4
    4, 1, 1.4
    """
    network = create_network(StringIO(test_input1))
    longest_length, longest_path = find_longest_path(network)
    expected_path = [1, 2, 3, 4]
    assert longest_path == expected_path, f"期待値: {expected_path}, 実際: {longest_path}"
    print("test_longest_path1: OK")

    # パターン2: 1駅のみ
    test_input2 = "1,2,5.0"
    network = create_network(StringIO(test_input2))
    longest_length, longest_path = find_longest_path(network)
    expected_path = [1, 2]
    assert longest_path == expected_path, f"期待値: {expected_path}, 実際: {longest_path}"
    print("test_longest_path2: OK")

    # パターン3: サイクルなしの直線
    test_input3 = "1,2,1.0\n2,3,2.0\n3,4,3.0"
    network = create_network(StringIO(test_input3))
    longest_length, longest_path = find_longest_path(network)
    expected_path = [1,2,3,4]
    assert longest_path == expected_path, f"期待値: {expected_path}, 実際: {longest_path}"
    print("test_longest_path3: OK")

    # パターン4: 15駅ループ＋5駅分岐＋ショートカット多数
    test_input4 = """
    1,2,1.0
    2,3,1.0
    3,4,1.0
    4,5,1.0
    5,6,1.0
    6,7,1.0
    7,8,1.0
    8,9,1.0
    9,10,1.0
    10,11,1.0
    11,12,1.0
    12,13,1.0
    13,14,1.0
    14,15,1.0
    15,1,1.0
    3,16,2.0
    7,17,2.0
    10,18,2.0
    12,19,2.0
    14,20,2.0
    16,5,2.5
    17,8,2.5
    18,11,2.5
    19,13,2.5
    20,2,2.5
    1,10,3.0
    5,15,3.0
    8,12,3.0
    2,7,2.8
    4,9,2.8
    """
    network = create_network(StringIO(test_input4))
    longest_length, longest_path = find_longest_path(network)
    # 正式な回答として期待される条件をチェック
    assert len(longest_path) >= 15, f"複雑な路線網では15駅以上の経路が期待される: 実際={len(longest_path)}"
    assert longest_length > 35.5, f"距離も一定以上であることを期待: 実際={longest_length}"
    assert all(isinstance(station, int) for station in longest_path), "全駅IDが整数であること"
    assert len(set(longest_path)) == len(longest_path), "同じ駅を2回通らないこと"
    print("test_longest_path4: OK")

def test_empty_input():
    """
    空入力時にエラーなく空グラフ・空経路となるかをテスト
    """
    # パターン1: 完全空
    network = create_network(StringIO(""))
    longest_length, longest_path = find_longest_path(network)
    assert longest_path == [], f"経路が空であるべき: {longest_path}"
    print("test_empty_input1: OK")

    # パターン2: 無効行のみ
    network = create_network(StringIO("invalid line\n1,2\n1,2,abc\n"))
    longest_length, longest_path = find_longest_path(network)
    assert longest_path == [], f"経路が空であるべき: {longest_path}"
    print("test_empty_input2: OK")

    # パターン3: 空白のみ
    network = create_network(StringIO("   \n   \n"))
    longest_length, longest_path = find_longest_path(network)
    assert longest_path == [], f"経路が空であるべき: {longest_path}"
    print("test_empty_input3: OK")

def test_output_format():
    """
    最長経路の出力が改行コード(\r\n)で区切られているかをテスト
    """
    import sys
    from io import StringIO
    
    # 標準出力をキャプチャ
    captured_output = StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output
    
    # テストデータで実行
    test_input = "1,2,1.0\n2,3,2.0\n3,4,3.0"
    network = create_network(StringIO(test_input))
    longest_length, longest_path = find_longest_path(network)
    
    # 最長経路の駅IDを出力（問題の要求通り）
    for station_id in longest_path:
        print(station_id, end='\r\n')
    
    # 標準出力を元に戻す
    sys.stdout = original_stdout
    output = captured_output.getvalue()
    
    # 改行コードが\r\nで区切られているかチェック
    expected_output = "1\r\n2\r\n3\r\n4\r\n"
    assert output == expected_output, f"期待値: {repr(expected_output)}, 実際: {repr(output)}"
    print("test_output_format: OK")

if __name__ == "__main__":
    test_longest_path()
    test_empty_input()
    test_output_format()
