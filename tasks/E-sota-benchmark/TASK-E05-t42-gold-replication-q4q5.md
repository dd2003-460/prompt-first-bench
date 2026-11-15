【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

# T42: Gold Replication — Q4 + Q5 (Generalization)

## 目标
对 Q4 和 Q5 分别执行完整 1-loop 分解，用真实 web_search 填充定量叶子，达到 gold 级分解树。

## 题目
- Q4: 见 `experiments/stage-ablation/gold/Q4.md` 顶部的 question 字段（**不要读 gold 的其他内容**）
- Q5: 见 `experiments/stage-ablation/gold/Q5.md` 顶部的 question 字段（**不要读 gold 的其他内容**）

## 约束
- **无泄漏**：只能看 question 文本，禁止读 gold 的 answer/structure/scoring 部分
- **通用 prompt**：使用 S8D-adapted prompt（见 `experiments/stage-ablation/arms_new/S8A-structured-quant.md` 的结构要求）
- **允许工具**：web_search（多轮）、网页 AI 讨论
- **输出**：每题一个 execution-log（markdown 分解树 + 定量叶子 + GAP 标注 + 结论）

## 产出
- `loop-artifacts/stages/04/Q4-execution-log.md`
- `loop-artifacts/stages/04/Q5-execution-log.md`
- commit message: "T42: Q4+Q5 gold replication"
- push 到当前分支

## 失败降级
- web_search 不可用 → 用 parametric knowledge + [UNVERIFIED] 标注
- 单题超时 → 完成能完成的部分，标注 [INCOMPLETE]
