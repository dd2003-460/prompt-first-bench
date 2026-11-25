# TASK-T4b Pilot Results — T1-T5 模板 before/after（本地 27b）

> origin: ai · 2026-11-26 · 自动生成自 runs.json + scores.json（机械 rubric，见 audit-rubric.md）
> 注：本文件为 2026-11-26 00:47 树重写后的重跑产物（首轮输出已丢失，详见 audit-rubric.md 重跑说明）。

## 设置

- 端点 `http://127.0.0.1:8787/v1/chat/completions`，model=`qwen3.8-27b-mtp`
- 条件 A（baseline）：system = "You are a helpful assistant."；条件 B（treatment）：system = "Follow these five thinking disciplines in your answer:" + T1-T5 全文
- temperature=0.7, max_tokens=1500, n=1/cell, 串行执行间隔 1s

## 得分表（0/1 机械 rubric）

| prompt | 模板 | A baseline | B treatment | B−A |
|--------|------|-----------|-------------|-----|
| P1 | T1 | **0** (length, 1500 tok) | **1** (length, 1500 tok) | 1 |
| P2 | T2 | **1** (length, 1500 tok) | **1** (length, 1500 tok) | 0 |
| P3 | T3 | **1** (length, 1500 tok) | **1** (length, 1500 tok) | 0 |
| P4 | T4 | **1** (length, 1500 tok) | **1** (length, 1500 tok) | 0 |
| P5 | T5 | **0** (stop, 1458 tok) | **1** (length, 1500 tok) | 1 |
| **合计** | | **3/5** | **5/5** | |

## 逐 run 明细

| run | status | finish_reason | completion_tokens | latency_s | score | 机械判据命中 |
|-----|--------|---------------|-------------------|-----------|-------|--------------|
| P1-A | ok | length | 1500 | 13.079 | 0 | cost_model=✓; premises=✓; special_case=✗ |
| P1-B | ok | length | 1500 | 12.608 | 1 | cost_model=✓; premises=✓; special_case=✓ |
| P2-A | ok | length | 1500 | 9.208 | 1 | unified_formula=✓; degeneration_conditions=✓ |
| P2-B | ok | length | 1500 | 9.823 | 1 | unified_formula=✓; degeneration_conditions=✓ |
| P3-A | ok | length | 1500 | 9.99 | 1 | quantitative_number=✓; needs_measurement=✗; probe_design=✓ |
| P3-B | ok | length | 1500 | 9.684 | 1 | quantitative_number=✓; needs_measurement=✗; probe_design=✗ |
| P4-A | ok | length | 1500 | 9.08 | 1 | dimensions_listed=✓; borrow_conclusion=✓ |
| P4-B | ok | length | 1500 | 9.945 | 1 | dimensions_listed=✓; borrow_conclusion=✓ |
| P5-A | ok | stop | 1458 | 10.034 | 0 | step_with_ground_truth_gap=✗; closing_fix=✓ |
| P5-B | ok | length | 1500 | 10.08 | 1 | step_with_ground_truth_gap=✓; closing_fix=✓ |

## 标志词计数（不计分，grep 大小写不敏感）

| 标志词 | A 合计 | B 合计 |
|--------|--------|--------|
| `needs measurement` | 0 | 0 |
| `cheapest probe` | 0 | 0 |
| `special case` | 0 | 0 |
| `需要测量` | 0 | 0 |
| `最便宜的探针` | 0 | 0 |
| `特例` | 0 | 1 |

## 解读（初步方向性观察，供 T4a M7 使用；非统计结论）

- 模板注入（B）相对 baseline（A）的增量出现在 **P1（T1 特例验证）与 P5（T5 指明缺 ground truth 的步骤）**：这两项的 prompt 原文未点名目标结构，只有模板注入补齐；P2/P3/P4 的 prompt 原文已点名目标结构（"single formula" / "testable quantitative prediction" / "dimension by dimension"），baseline 亦满分，模板无增量。
- 因此本表测量的是**模板对 prompt 未诱导维度的补齐效果**，不是模板的普遍增益；B−A 差值含截断窗口位置成分（B 的 system prompt 更长→输出更长→撞 1500 上限，模板短语更易落在窗口内）。
- 详细机制分析与两条可检验预言见 `mechanism-note.md`（非交付物，供 T4a/Lead 参考）。

## 局限性声明

1. **n=1/cell**：每格仅 1 次调用，无统计显著性声明（论文中如实这么写）。
2. **单模型**：仅 qwen3.8-27b-mtp（本地 vLLM），结论不外推到其他模型/规模。
3. **无统计检验**：5 个二值分不构成可检验的差异；B−A 仅作方向性观察。
4. **分数是机械 checklist 非质量分**：0/1 由关键词/结构存在性判定（见 audit-rubric.md 的正则组），不衡量答案质量、正确性或推理深度；命中关键词≠真正执行了对应思考纪律。
5. **采样噪声**：temperature=0.7，单次采样结果含随机性；finish_reason=length 的 run 输出可能被 max_tokens=1500 截断（截断本身如实记录在 runs.json）。
6. **截断影响（重要）**：所有 run max_tokens=1500，9/10 finish_reason=length（输出在 1500 token 处截断），rubric 是对截断后文本打分；两条件相同上限，对照受控公平，但"结构存在性"检查受截断影响（写到一半可能丢后续结构项）。

## 文件清单

- `runs.json` — 10 个 run 原始输出（prompt id / condition / full text / tokens / latency / status / finish_reason）
- `raw/<run_id>.json` — 每次调用的 API 原始返回（未编造核验用）
- `audit-rubric.md` — rubric 原文 + 机械实现说明 + 重跑说明
- `scores.json` — 逐 run 判据命中明细（本表的数据源）
