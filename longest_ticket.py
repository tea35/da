# 最長片道きっぷの旅
# 入力処理

def read_input():
    import sys
    import re
    graph = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = re.split(r'\s*,\s*', line)
        if len(parts) != 3:
            continue
        start_id, end_id, dist = parts
        start_id = int(start_id)
        end_id = int(end_id)
        dist = float(dist)
        if start_id not in graph:
            graph[start_id] = []
        graph[start_id].append((end_id, dist))
    return graph

if __name__ == "__main__":
    graph = read_input()
    print(graph)  # デバッグ用: 入力が正しくパースされているか確認
