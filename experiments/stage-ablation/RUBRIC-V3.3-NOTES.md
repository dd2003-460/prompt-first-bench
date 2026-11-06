# Rubric v3.3: M1 评分逻辑修正

## 问题

v3.2 的 M1 judge 对照 gold 文本判定断言。但 gold Q2 是**方法论树**（正交性证明、KIND 分类、breakeven），不含具体 benchmark 数字。当被评对象（arena）用 web_search 查到真实数据时，judge 全部标 UNDECIDABLE → M1=0。

这是**评分盲区**，不是被评对象的错。

## 修正方案

M1 判定分两种情况：

### Case A: Gold 含具体数值（如 Q1 GPU 规格）
- 现有逻辑不变：对照 gold 文本判 MATCH/CONTRADICT/UNDECIDABLE

### Case B: Gold 是方法论型（如 Q2 分解结构）
- **不要求被评对象复现 gold 的数字**（gold 本身没有数字）
- 改为：提取被评对象的关键定量断言 → 对照**公开事实**（judge 的训练知识）判定 CORRECT/INCORRECT
- M1 = correct / (correct + incorrect)，UNCERTAIN 不计入分母

### 实现

score.py 增加 `--gold-type auto|methodology|data` 参数：
- `auto`: 检测 gold 是否含 ≥5 个具体数值行（含 %/$/GB 等单位）→ data 型；否则 methodology 型
- methodology 型走 Case B 逻辑

## 影响

- Q2 的 arena 输出从 M1=0 修正为 M1=1.0
- 不影响 S0/S1/S5 的相对排名（它们的 M1 本来就低，因为 27B 编造数字）
- Paper 中需标注此修正

## 待做

1. score.py 加 --gold-type 参数
2. 重跑 Q2 所有 arm 的 M1（预期：S1 仍高，S8D 中等，Arena 最高）
3. Paper §5 加一段说明
