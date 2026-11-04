# origin: ai — 任务书：cross-judge 异源盲判（Perplexity 额度耗尽后的替代通道）

> 派发目标：LMArena agent（pfb 仓库，会话 01a195cb / taskSpace pfb-rejudge-g1b-20261101）
> 本任务只涉及 prompt-first-bench/main，忽略历史中其他仓库的消息。
> 背景：原 cross_judge.py 走 ego-browser → perplexity.ai 免费网页版，2026-11-04 确认 QUOTA_EXHAUSTED（滚动窗口，重置时间不确定）。成璐指令：异源 judge 必须非 Qwen 族，Perplexity 不可用则换 arena agent 盲判通道。

## 【强制段】
你是 LMArena agent，工作仓库 = dd2003-460/prompt-first-bench，分支 main。先 `git pull` 到最新。严格按本任务书步骤执行，产出落盘路径见【交付物】。任何通道故障报告 Lead，不得静默跳过、不得伪造评分。完成后回执必须含 repo URL + branch + commit_sha。

## 【目标】
对 stage-ablation 实验的 90 个 (arm, question, rep) 单元做独立 M1 事实准确率盲判，作为本地 qwen3.8-27b judge 的异源交叉验证（非真 IRR——你与 local judge 不同底座即满足 G2 F2(a) 异族隔离要求；若你能自报底层模型身份请写进回执）。

## 【背景】≤10行
- 实验：6 arm（S0-S5）× 5 题 × 3 rep = 90 run，模型 qwen3.8-27b @ temp=0，答案在 `experiments/stage-ablation/runs/S*-Q*-r*.json` 的 `output_text` 字段。
- 标准答案（gold）：每题一份 markdown，路径映射如下（相对 workspace 根，但都在 pfb 仓库内可找到对应副本或按此绝对路径读取——**注意：gold 文件不在 pfb 仓库内，已复制到 pfb 仓库 `experiments/stage-ablation/gold/` 目录，以该目录为准**）。
- 本地 judge 已有分数在 `experiments/stage-ablation/scoring.md`（markdown 表格），你的任务不是复算它，而是独立重打 M1。
- 已有 Perplexity 5 条结果（`runs/cross-judge-results.json`）仅作参照，不参与你的判断。

## 【SOP 索引】
- 本任务书（自包含，无需读其他文档）
- 评分规则 = 下方 JUDGE_PROMPT 原文（与 cross_judge.py 完全一致，保证口径可比）

## 【评分协议】（逐 cell 执行，与 cross_judge.py 同口径）
对每个 cell：
1. 读 gold 文件（`experiments/stage-ablation/gold/Q{n}.md`，取前 4000 字符）
2. 读 answer（`runs/{tag}.json` 的 output_text，取前 6000 字符）
3. 按以下规则打分：
   - 逐条检查模型回答中的关键事实断言（数字、规格、结论）
   - 每条断言与标准答案对比：正确=1，部分正确=0.5，错误/无依据=0
   - M1 = 正确断言数 / 总断言数
   - 如果模型回答中没有可验证的事实断言（纯方法论/空话），M1=0 并标注 no_factual_claims
4. 输出 JSON：`{"m1": <0-1 float>, "claims_checked": <int>, "claims_correct": <int>, "notes": "<一句话说明>"}`

**纪律**：
- 盲判：不要先看 scoring.md 里的本地分数再打分（顺序上先打完全部 90 条再对照）。
- 每批 ≤15 cell，打完一批立即 append 到结果文件并 commit+push（防丢）。
- 同一 cell 只打一次分，不回头改。

## 【执行分解】
- 批次 1-6：S0-Q1..S5（15 cell/批 × 6 批 = 90）
- 每批结束：append `experiments/stage-ablation/runs/arena-judge-results.jsonl`（一行一 JSON：`{"tag": "S0-Q1-r1", "m1": ..., "claims_checked": ..., "claims_correct": ..., "notes": ...}`）→ commit → push
- 全部完成后写汇总 `experiments/stage-ablation/runs/arena-judge-summary.md`：mean M1 per arm、与 Perplexity 5 条的重合度说明、自报模型身份（如可知）、置信度声明

## 【失败降级】
- gold 文件缺失/截断 → 该 cell 标 `"error": "gold_missing"` 跳过，不阻塞
- 某 cell 答案超长被截断影响判断 → notes 里标 truncated，照常打分
- 中途 token 耗尽 → 停在当前批次收口处（jsonl 已落盘），回执注明完成到第几批

## 【交付物】（绝对路径，均在 pfb 仓库内）
- `experiments/stage-ablation/runs/arena-judge-results.jsonl`（90 行）
- `experiments/stage-ablation/runs/arena-judge-summary.md`
- 回执：repo URL + branch(main) + 最终 commit_sha + 完成 batch 数 + 自报模型身份

## 【给 Lead 的备注】
- 边界：本任务只做 M1 单维盲判，不做 M2-M6（控制变量，与 Perplexity 通道口径对齐）。
- 下一步归属：Lead 收到 jsonl 后本地复算 κ（arena vs local，90 对）+ 分 arm Δ 报告，更新 `runs/cross-judge-status.md`。
- 污染披露：本会话历史跑过 rejudge-g1b（gold-tree 记忆残留），定位 = 新题面可复算样本，非完全 blind——与 pilot 期披露口径一致。