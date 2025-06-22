#write.py
import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))

file_name = "data.json"
file_path = os.path.join(current_path, file_name)

print("値を入力してJSONファイルを更新します。終了するには 'exit' と入力してください。")

while True:
    user_input = input("新しい値を入力: ")
    if user_input.lower() == "exit":
        print("終了します。")
        break

    try:
        new_value = int(user_input)
    except ValueError:
        print("数値を入力してください。")
        continue

    data = {}
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
    except json.JSONDecodeError:
        print(f"{file_path} は正しいJSON形式ではありません。データを初期化します。")

    data["value"] = new_value

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"{file_path} に値を更新しました: {new_value}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")