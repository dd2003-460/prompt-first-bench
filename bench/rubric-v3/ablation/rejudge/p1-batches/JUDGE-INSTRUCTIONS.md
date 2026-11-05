# P1 层 judge 指令（RV3G6-o3-claim-rejudge · P1 98 cell）

## 任务
对 packet 中每个 `--- CELL runN/N-x ---` 段，盲判该 run 产出是否包含 [B2 claim] 描述的实质内容。

## 判定规则（与 P0 层 rules-frozen.json 同源 o3-claim-rejudge-rules-v1）
1. h_claim=1 当且仅当 run 产出包含该 claim 描述的实质内容（语义等价即算，判实质不判术语）
2. 必须引一句 run 原文真实存在的句子作 evidence_quote（≤60字符，必须是 run 全文的连续子串——机判 in 检查，带省略号/格式改写 = 违例）；h_claim=0 填 "none"
3. 不确定时保守判 0
4. 「方向内嵌说明」列是 no 的典型情形参考：错误方向的覆盖不算命中

## 输出格式（严格 JSON 数组，无其他文字）
```json
[{"cell_id":"run1/N-0","h_claim":0,"evidence_quote":"none"}, ...]
```
- cell_id 用 `runN/N-x` 格式（与 packet 中一致）
- 必须覆盖 packet 全部 cell，一个不少
- 只输出 JSON 数组本身

## 输入边界（blind-packet 白名单，协议 §2.2）
你只能看到：B1 run 全文 + B2 claim 文本 + B3 node ID。
不得假设你知道 hit-matrix 现值、gold-tree 全文、prior 估计——这些不在你的输入里，也不应影响判断。
