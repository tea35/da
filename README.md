# 最長片道きっぷの旅

## 概要

駅と駅を結ぶ鉄道路線網において、同じ駅を 2 回通らずに最も長い距離を旅する経路（最長片道きっぷ）を求めるプログラムです。

## ファイル構成

- longest_ticket.py : 本体プログラム（入力処理・探索・出力）
- test_longest_ticket.py : 入力処理のテスト（正常系・異常系・境界系）
- test_longest_ticket_path.py : 最長経路探索のテスト（正常系・空・異常系）

## 使い方

標準入力から路線データを与えて実行します。

### 入力例

```
1, 2, 8.54
2, 3, 3.11
3, 1, 2.19
3, 4, 4
4, 1, 1.4
```

### 実行例

```sh
python3 longest_ticket.py < input.txt
```

最長経路となる駅 ID が順に出力されます。

## テスト方法

各種テストは以下で実行できます。

```sh
python3 test_longest_ticket.py
python3 test_longest_ticket_path.py
```

すべてのテストが OK となれば正しく動作しています。
