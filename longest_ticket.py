import sys
import re
import collections

def create_network(input_stream=None) -> dict:
    """
    標準入力から路線データを読み込み、
    始点IDをキーとした隣接リスト（辞書型）として返す。
    無効な行（型変換失敗や要素数不足）はスキップ。
    """
    if input_stream is None:
        input_stream = sys.stdin
    
    network = collections.defaultdict(list)
    for line in input_stream:
        line = line.strip()
        if not line:
            continue
        parts = re.split(r'\s*,\s*', line)
        if len(parts) != 3:
            continue
        start_id, end_id, dist = parts
        try:
            start_id = int(start_id)
            end_id = int(end_id)
            dist = float(dist)
        except ValueError:
            continue  # 無効な行はスキップ
        network[start_id].append((end_id, dist))
    return dict(network)

def find_longest_path(network: dict) -> tuple:
    """
    構築済みのネットワーク辞書を使って、最長の単純パスを見つける。

    Args:
        network (dict): 隣接リスト形式のグラフ（ネットワーク辞書）。

    Returns:
        tuple: (最長経路の長さ, 最長経路のリスト)
    """
    max_length = 0.0
    max_path = []

    def dfs(current_node: int, path: list, current_length: float):
        """
        深さ優先探索（DFS）で最長経路を探索する再帰関数。
        """
        nonlocal max_length, max_path
        
        # 現在の経路がこれまでの最長よりも長ければ更新
        if current_length > max_length:
            max_length = current_length
            max_path = path[:]

        # 現在の駅から接続されているすべての駅について探索
        for neighbor, weight in network.get(current_node, []):
            if neighbor not in path:  # 同じ駅を2回通らない
                path.append(neighbor)
                dfs(neighbor, path, current_length + weight)
                path.pop()  # バックトラッキング

    # グラフに存在するすべてのノードを取得して始点候補にする
    all_nodes = set(network.keys())
    for destinations in network.values():
        for dest, _ in destinations:
            all_nodes.add(dest)

    # 全ての駅を始点としてDFSを開始
    for start_node in sorted(list(all_nodes)):
        dfs(start_node, [start_node], 0.0)

    return max_length, max_path

def solve_longest_ticket():
    """
    最長片道きっぷの旅のメイン処理。
    入力データを読み込み、最長経路を探索して結果を出力する。
    """
    # 1. 標準入力からネットワーク辞書を作成
    network = create_network()
    
    # 2. 作成したネットワークを使って最長経路を探索
    longest_length, longest_path = find_longest_path(network)
    
    # 3. 最長経路の駅IDを順に標準出力（改行コード\r\n区切り）
    for station_id in longest_path:
        print(station_id, end='\r\n')

if __name__ == "__main__":
    solve_longest_ticket()
