# %%
import pandas as pd
import json
import os
import re

all_data = []
for x in os.listdir("./res/"):
    filepath = f"./res/{x}"
    s = open(filepath).read().strip()
    if not s:
        continue
    try:
        a = json.loads(s)
        print(a["content"], file=open(filepath+"-decode.txt", "w"))
        for line in a["content"].strip().split("\n"):
            line_lst = re.sub("》 *\||》", "|", line).split("|")
            if len(line_lst) >= 3:
                line_lst[0] = re.sub(
                    r"\d*[．\.] *", "",
                    re.sub("《", "", line_lst[0].strip())
                ).strip()
                line_lst = [x.strip() for x in line_lst]
                print(line_lst)
                all_data.append(line_lst[:3])
    except:
        pass

df = pd.DataFrame(all_data, columns=["书名", "书名（英文）", "作者"])
print(df.shape)
df["书名"].value_counts().to_csv("value_counts.tsv", sep="\t")
df.to_csv("collection.tsv", sep="\t", index=False)

# %%

# for s in ["50. 《心理测试与行为评估》", '1. 人类简史 ']:
#     print(re.sub(
#         r"\d*[．\.] *", "",
#         re.sub("[《》]", "", s.strip())
#     ))

# %%

