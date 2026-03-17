"""Extract schedule data from note.txt and output as schedule_data.json."""

import json
import re
import sys


def extract_schedule(input_file: str = "note.txt", output_file: str = "schedule_data.json") -> None:
    with open(input_file, encoding="utf-8") as f:
        content = f.read()

    match = re.search(
        r"Ni=(\[(?:[^\[\]]|\[(?:[^\[\]]|\[(?:[^\[\]]|\[[^\[\]]*\])*\])*\])*\])",
        content,
    )
    if not match:
        print("ERROR: Could not find Ni array in note.txt", file=sys.stderr)
        sys.exit(1)

    raw = match.group(1)
    # Convert JS object literal keys to quoted JSON keys
    json_str = re.sub(r"(\{|,)\s*([a-zA-Z_][a-zA-Z0-9_]*):", r'\1"\2":', raw)
    json_str = json_str.replace("undefined", "null")

    schedule = json.loads(json_str)
    print(f"Extracted {len(schedule)} items")

    stages = [
        {"id": "nanba", "name": "南霸天", "color": "#6AB344"},
        {"id": "hailong", "name": "海龍王", "color": "#7B3FA0"},
        {"id": "nvshen", "name": "女神龍", "color": "#C7237A"},
        {"id": "haibo", "name": "海波浪", "color": "#1DA0E5"},
        {"id": "kamome", "name": "卡魔麥", "color": "#E07B7B"},
        {"id": "chutou", "name": "出頭天", "color": "#D98A15"},
        {"id": "daxiong", "name": "大雄丸", "color": "#C44D4D"},
        {"id": "lanbaoshi", "name": "藍寶石", "color": "#1A3FC7"},
        {"id": "qingchun", "name": "青春夢", "color": "#F0C830"},
        {"id": "xiaogang", "name": "小港祭", "color": "#B8896B"},
        {"id": "dashu", "name": "大樹下", "color": "#4E8B3F"},
        {"id": "kids", "name": "KIDS 親子區", "color": "#FF6B6B"},
    ]

    output = {"schedule": schedule, "stages": stages}

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Written to {output_file}")


if __name__ == "__main__":
    extract_schedule()
