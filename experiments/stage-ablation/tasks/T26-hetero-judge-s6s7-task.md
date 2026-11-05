# T26: S6/S7 Prompt-Style Arms — Hetero-Judge (Arena Agent Mode)

## 强制段

你是 LMArena agent，本任务只涉及 **prompt-first-bench / arena/4a614e63-prompt-first-bench** 分支。忽略历史中其他仓库的消息。

先 `git pull` 当前分支。严格按以下步骤执行，产出落盘到指定路径。通道故障报告 Lead，不得静默跳过。

完成后回执必须含 repo URL + branch + commit_sha。

## 【目标】

用你的模型（GPT/Claude 级）作为**异源 judge**，对 S6（模糊启发式 prompt）和 S7（混合 prompt）臂的 30 个 run 做 M1/M4 评分。这是本地 27B 同族自评的交叉验证——成璐硬规则：judge 必须 ≥ 被评模型或走 arena，禁用 7B 等小模型。

## 【背景】

- S6 = 模糊启发式 prompt（~300 chars，"第一性原理/因素分解/找矛盾"，无流程步骤）
- S7 = 混合 prompt（~2.6k chars，S5 阶段结构 + 关键节点注入模糊启发）
- 本地 27B 同族 judge 结果：S6 total=0.462, S7 total=0.559
- 需要异源 judge 确认这些分数是否可靠（同源 judge 有 self-bias 风险）
- 数据打包在 `experiments/stage-ablation/arena-judge-s6s7-pack.json`（30 runs + 5 gold files，463KB）

## 【SOP 索引】

- `experiments/stage-ablation/score.py` — 评分逻辑（M1-M6 定义 + judge prompt 模板）
- `experiments/stage-ablation/gold/Q{1-5}.md` — Gold 锚点
- `experiments/stage-ablation/scoring-v4-m7.md` — 现有评分口径说明

## 【实验设计】

### 评分维度（只需判 M1 和 M4，M2/M3/M5/M6 是规则计算不需要 LLM）

**M1 事实准确率**（权重 0.25，Q5 降为 0.125）：
- 对照 gold 锚点和模型输出，逐条判定可判定断言（有具体数字/规格/结论）
- 每条标 match / mismatch / undecidable
- M1 = matched / total_decidable
- 规则：模糊表述（"可能""大概""据我所知"）不算可判定断言，跳过

**M4 缺口覆盖率**（权重 0.20）：
- 对照 gold 中列出的关键缺口/不确定性，判断模型是否主动识别
- "不确定/需要查证/查不到/未解决/无法核实"算识别
- 表格/列表显式列出"不确定性因素/局限/待验证项"也算识别
- 通篇断言零处承认局限 = 未识别
- M4 = gaps_identified / gaps_in_gold

### 变体表

| Arm | Qid | Reps | 需判 run 数 |
|-----|-----|------|-----------|
| S6  | Q1-Q5 | ×3   | 15        |
| S7  | Q1-Q5 | ×3   | 15        |
| **合计** | | | **30**    |

### 验收标准

- 30/30 run 全部有 M1 + M4 分数
- 每个 run 的 JSON 输出含 `assertions[]`（M1）和 `gaps`（M4）明细
- 产出文件可被 `python3 -c "import json; d=json.load(open('...')); print(len(d))"` 验证
- 与本地 27B 分数的差异分析（per-arm per-question Δ 表）

## 【失败降级】

- 如果某个 run 的输出文本为空或 <100 chars → M1=M4=0，note="empty output"
- 如果 gold 文件中某题没有明确缺口列表 → M4 按"该题 gold 中所有标注为'缺口/不确定/待验证'的条目"计数
- 如果 30 run 中 >5 个无法解析 → 停止，报告 Lead，不要继续

## 【交付物】

1. `experiments/stage-ablation/runs/hetero-judge-s6s7-results.json` — 30 run 的完整评分
   格式：`[{"arm":"S6","qid":"Q1","rep":1,"M1":0.87,"M4":1.0,"m1_assertions":[...],"m4_gaps":{"identified":[...],"missed":[...]}, "notes":"..."}, ...]`
2. `experiments/stage-ablation/runs/receipt-t26-hetero-judge.md` — 回执（含 per-arm per-question 分数表 + 与本地 27B 的差异分析 + 你用的模型名）

## 【给 Lead 的备注】

- 本任务是 T23-v2 hetero-judge 的延伸（T23-v2 判了 S0-S5，本次判 S6/S7）
- 边界：不重新判 S0-S5（已有 T23-v2 结果），只判 S6/S7
- 下一步：Lead 合并异源+同源双判结果，更新 T17 final report 的 S6/S7 分数