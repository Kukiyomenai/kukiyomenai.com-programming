#read.py
import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))

file_name = "data.json"
file_path = os.path.join(current_path, file_name)

print("エンターを押すとJSONファイルの値を確認します。終了するには 'exit' と入力してください。")

while True:
    user_input = input("エンターキーを入力")
    if user_input.lower() == "exit":
        print("終了します。")
        break

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            value = data.get("value")
            print(f"value: {value}")
    except FileNotFoundError:
        print(f"{file_path} が見つかりませんでした。")
    except json.JSONDecodeError:
        print(f"{file_path} は正しいJSON形式ではありません。")