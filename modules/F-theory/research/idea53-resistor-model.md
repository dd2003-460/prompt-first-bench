#53 电阻瓶颈模型 (树状 2x2) — 一行结论

5090: flip_br=0.399 H_br=0.362 flip_within=0.191 | T5000: flip_br=0.181 H_br=0.656 flip_within=0.290 | 4090: flip_br=0.495 H_br=0.041 flip_within=0.112 | A100: flip_br=0.487 H_br=0.084 flip_within=0.114

flat归零=True 段级复现1D=True → 成立(深层节点决定哪条支是瓶颈: flip_br 全>0, H_br 全>0, flat归零, 段级复现1D)
