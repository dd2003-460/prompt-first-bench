# TASK-T4b — T1-T5 模板最小 pilot（before/after，本地 27b）

> origin: ai · 2026-11-26 · 触发：arena review 修改建议 #3（"加最小 T1-T5 pilot：5 prompt×1 模型 before/after"）——同时解 TMLR 可投性与 LLM-origin 嫌疑
> 性质：最小可行性 pilot，n=1/cell，不做统计显著性声明（论文里会如实这么写）。零成本（本地 vLLM）。

## [背景]
论文 `tasks/think-mechanism-paper/draft/paper.tex` 的贡献之一是 5 个可注入思考模板 T1-T5（定义见 `projects/AI-计算科学/D1-persona-align/memory/general-thinking-template-20261124.md` 第 30-40 行，模板正文如下，照抄进 system prompt）：

```
T1 Cost model: when you solve a concrete problem or are asked "is X optimal?", write down the cost model (what cost is computed, under what premises) and a unified form; verify the original solution is a special case. If you cannot derive it, name the missing premise.
T2 Unified coverage: when facing several seemingly unrelated methods/systems, find one formula or analogy that covers all of them (compression ratio / info gain per cost / channel bandwidth), and write the degeneration conditions of each.
T3 Quantitative landing: when giving a qualitative conclusion, immediately quantify it into a testable number (success-rate formula / bandwidth lower bound / expected number of tests). If you cannot quantify, mark "needs measurement" and design the cheapest probe.
T4 Analogy audit: when borrowing a historical case/analogy/prior, check condition gaps delta and conclusion sensitivity s_k dimension by dimension; if sensitive and mismatched, do not borrow; attach an epsilon*uniform floor against confident errors.
T5 Criterion bottleneck: when a framework takes shape, find the "criterion bottleneck" — the step in the loop lacking cheap reliable ground truth; that step is the real bottleneck, not the architecture. Prefer "closing the world" (synthetic domains / executable verification) as the fix.
```

## [实验设计]
- 端点：`http://127.0.0.1:8787/v1/chat/completions`，model=`qwen3.8-27b-mtp`（已确认存在）
- 条件 A（baseline）：system prompt = ""（或 "You are a helpful assistant."），user = prompt 原文
- 条件 B（treatment）：system prompt = "Follow these five thinking disciplines in your answer:\n" + 上面 T1-T5 全文，user = 同一 prompt 原文
- 参数：temperature=0.7, max_tokens=1500, 每格 1 次调用（n=1，如实声明）
- 5 个 prompt（每个自然触发一个模板）：
  1. P1 (T1): "Is binary search the fastest way to find an element in a sorted array of N items? What is the cost model behind your answer, and under what premises does it hold?"
  2. P2 (T2): "Compare gradient descent, Newton's method, and evolutionary strategies as optimizers. Is there a single formula or analogy that covers all three, and under what conditions does each degenerate?"
  3. P3 (T3): "People say large language models generalize better with more data. Turn this qualitative claim into a testable quantitative prediction, or state exactly what measurement is needed and design the cheapest probe."
  4. P4 (T4): "Someone suggests borrowing the lesson from TCP congestion control (slow start) to design LLM agent retry policies. Audit this analogy dimension by dimension before accepting it."
  5. P5 (T5): "We are building an automated research pipeline: idea generation -> literature search -> experiment -> judge. Which step is the true bottleneck, and what is the cheapest way to make the system verifiable?"
- 共 10 次 API 调用。串行执行，每次之间 sleep 1s。失败重试 2 次，仍失败记 status=error 不编造。

## [机械审计 rubric]（0/1 计分，判据必须机械可查——关键词/结构存在性，不靠主观印象）
每个 run 按对应模板打分（P1→T1, P2→T2, P3→T3, P4→T4, P5→T5）：
- T1: 含显式代价模型（公式或逐项代价清单）+ 前提陈述 + 原解=特例 的验证句。三项全有=1，否则 0
- T2: 含单一公式/类比覆盖 ≥2 个方法 + 每个方法的退化条件。两项全有=1，否则 0
- T3: 含可检验数（带单位的数/公式/期望值）或显式 "needs measurement" + 最便宜探针设计。二选一满足=1，否则 0
- T4: 含逐维条件差检查（≥3 个维度逐项列）+ 借/不借的结论。两项全有=1，否则 0
- T5: 含指明哪一步缺廉价 ground truth + 闭合对策（合成域/可执行验证/预注册）。两项全有=1，否则 0
- 附加记录（不计分）：每个 run 的 output tokens 数、是否出现 "needs measurement"/"cheapest probe"/"special case" 等标志词（grep 计数）

## [交付]（全部落盘 `tasks/think-mechanism-paper/pilot/`）
1. `runs.json` — 10 个 run 的原始输出（prompt id / condition / full text / tokens / latency / status）
2. `audit-rubric.md` — 上面的 rubric 原文
3. `results.md` — 表：prompt × 条件 × 模板分（0/1）+ 每条件合计 + 标志词计数；最后一节：局限性声明（n=1/cell、单模型、无统计检验、分数是机械 checklist 非质量分）
4. 不要修改 paper.tex（那是 T4a 的事）

## [验收（Lead 对照检查）]
- 10 个 run 全在 runs.json（允许 ≤1 个 status=error，须如实记录）
- results.md 表完整（5×2 格子全有分）
- 原始输出未截断（每个 run 的 finish_reason 记录在案）
- 无编造：Lead 抽 2 个 run 比对 runs.json 与 API 原始返回

## [防截断协议（27b 输出上限教训）]
- 每完成一个 run 立即 append 到 runs.json（增量写，不攒着）
- results.md 最后写
- 推理从简：这是执行任务不是研究任务，不展开思考链

## [回执]
完成后回执：runs 成功数/10 + 每条件合计分 + 三个文件路径 + 每个 run 的 finish_reason 分布。
