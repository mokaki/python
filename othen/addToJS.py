#加到J尾

import json
import os




filename = 't1213.json'

with open(filename, 'r', encoding="utf-8") as f:
    data = json.load(f)
    data['if334200j'] = '請按任意024鍵繼續' # <--- 加到J尾


os.remove(filename)
with open(filename, 'a', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

os.system("pause")
