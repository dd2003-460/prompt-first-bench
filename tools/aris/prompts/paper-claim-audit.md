# paper-claim-audit — 零上下文数字/claim 核对（任务书模板）

> 来源（只读）：`aris/skills/paper-claim-audit/SKILL.md`
> 移植日期：2026-11-25 · 移植者：Hermes subagent
> **执行器 = 本地 27b subagent 或 arena（跨模型族）**。原文引擎是 Codex MCP
> （`mcp__codex__codex`，model `gpt-6-astra`，reasoning `ultra`）；本模板把所有
> "怎么调模型"处替换为 `{{EXECUTOR}}`。**核心逻辑（零上下文 / 黑白名单 /
> 7 失败模式 / 逐 claim 状态机 / verdict 决策表）原样保留。**
>
> 用法：`{{EXECUTOR}}` = 一次全新上下文的模型调用（本地 qwen3.8-27b subagent，
> 或 arena 跨模型族通道）。**每次运行都是全新调用，绝不复用上下文**
> （原文 "NEVER codex-reply" 的等价物）。跨模型不变量：`{{EXECUTOR}}` 的模型族
> 必须 ≠ 执行器（写实验+写论文的那个）模型族。

## 材料黑白名单

原文 Core Principle（逐字）：

> "**Zero-context, fresh reviewer.** The auditor receives ONLY:
> - Paper .tex files (the claims)
> - Raw result files (the evidence)
>
> It does NOT receive:
> - ❌ EXPERIMENT_LOG.md
> - ❌ EXPERIMENT_TRACKER.md
> - ❌ AUTO_REVIEW.md
> - ❌ NARRATIVE_REPORT.md
> - ❌ Any executor summary or interpretation
> - ❌ Any prior audit results
> - ❌ Any conversation history
>
> This is **stricter than reviewer-independence** — it's zero-context evidence audit."

补充（Step 1，执行器收集文件时同样不解读）：

✅ 给什么：
```
Paper files (claims):
paper/main.tex
paper/sections/*.tex
paper/tables/*.tex (if separate)

Result files (evidence):
results/*.json, results/*.jsonl, results/*.csv, results/*.tsv
outputs/*.json, outputs/*.csv
wandb-summary.json (if exists)
**/metrics.json, **/eval_results.json
**/config.yaml, **/args.json (experiment configs)
```

❌ 不给什么（Step 1 Exclude，逐字）：
```
EXPERIMENT_LOG.md, EXPERIMENT_TRACKER.md, AUTO_REVIEW*.md
NARRATIVE_REPORT.md, PAPER_PLAN.md, findings.md
Any .md file that is an executor-written summary
```

**执行器只收集文件路径，不读不解读内容**（原文："Locate paper and result files
WITHOUT reading or interpreting them."）。

## 执行 prompt

`{{EXECUTOR}}`（全新零上下文调用，只读）：

```
You are a paper-to-evidence auditor. You have ZERO prior context about
this research. You will receive only paper source files and raw result
files. Your job is to verify that every number in the paper exactly
matches the raw evidence.

Paper files to read:
[list .tex file paths]

Result files to read:
[list .json/.csv/.yaml file paths]

## Audit Protocol

### A. Extract Every Quantitative Claim
For each number, percentage, comparison, or scope statement in the paper:
- Location (section, table, caption, or inline text)
- Exact claim text
- The number or comparison being made

### B. Trace Each Claim to Evidence
For each extracted claim, find the supporting raw data:
- Which result file contains this number?
- What is the EXACT value in that file?
- Match status: exact_match / rounding_ok / mismatch

### C. Check These Specific Failure Modes

1. **Number inflation**: Paper says 85.3%, raw file says 84.7%
   Rule: only standard rounding to displayed precision is allowed

2. **Best-seed cherry-pick**: Paper says "achieves 90.2%" but
   that's the best of 5 seeds; mean is 87.1%
   Rule: check if paper specifies "average" / "best" / "median"

3. **Config mismatch**: Paper compares Method A vs Baseline B,
   but they used different hyperparameters / datasets / splits
   Rule: verify config files show same settings for compared methods

4. **Aggregation mismatch**: Paper says "average over 5 seeds"
   but result files show only 3 runs
   Rule: count actual runs vs claimed count

5. **Delta error**: Paper says "improves by 15%" but
   actual delta is (85.3 - 73.1) / 73.1 = 16.7%
   Rule: verify arithmetic of all relative improvements

6. **Caption-table mismatch**: Figure caption describes
   something different from what the figure/table actually shows
   Rule: cross-check every caption against its content

7. **Scope overclaim**: Paper says "consistently outperforms"
   but only tested on 2 datasets
   Rule: check if language matches actual evaluation scope

## Output Format (per claim)
For each claim, report:
- claim_id: sequential number
- location: section/table/figure
- paper_text: exact quote from paper
- paper_value: the number claimed
- evidence_file: which raw file
- evidence_value: the actual number
- status: exact_match | rounding_ok | ambiguous_mapping |
          missing_evidence | config_mismatch | aggregation_mismatch |
          number_mismatch | scope_overclaim | unsupported_claim
- details: explanation if not exact_match

Overall verdict: PASS | WARN | FAIL
```

## verdict 映射表

原文 "Verdict decision table"（逐字）：

| Input state | Verdict | `reason_code` example |
|---|---|---|
| No numeric claims detected in paper | `NOT_APPLICABLE` | `no_numeric_claims` |
| Numeric claims detected, no raw result files found | `BLOCKED` | `no_raw_evidence` |
| All claims reconcile to raw data | `PASS` | `all_numbers_match` |
| Minor rounding drift only, no material mismatch | `WARN` | `rounding_drift` |
| Any material mismatch (wrong number, config mismatch) | `FAIL` | `claim_mismatch` |
| Reviewer invocation failed (network / malformed) | `ERROR` | `reviewer_error` |

Rounding rule（原文 Key Rules）：只允许标准舍入到显示精度。
84.7% → 84.7% 或 85% OK；84.7% → 85.3% NOT OK。

集成语义（原文 Advisory, Never Blocking）：`PASS` → 正常继续；`WARN` → 打印警告
继续，draft 标记 "check numbers before submission"；`FAIL` → 打印告警继续，
但不得标记 submission-ready。**本审计自身从不 block，只发 artifact。**

## 输出 schema

`paper/PAPER_CLAIM_AUDIT.json`（原文 schema；**无论结果如何都必须写出**，
detector-negative 时 verdict=`NOT_APPLICABLE`，silent skip 禁止）：

```json
{
  "audit_skill":      "paper-claim-audit",
  "verdict":          "PASS | WARN | FAIL | NOT_APPLICABLE | BLOCKED | ERROR",
  "reason_code":      "all_numbers_match | rounding_drift | missing_raw_results | ...",
  "summary":          "One-line human-readable verdict summary.",
  "audited_input_hashes": {
    "main.tex":                              "sha256:...",
    "sections/5.evidence.tex":               "sha256:...",
    "/abs/path/to/results/run_2026_04_19.json": "sha256:..."
  },
  "trace_path":       ".aris/traces/paper-claim-audit/<date>_run<NN>/",
  "thread_id":        "<{{EXECUTOR}} thread/session id>",
  "reviewer_model":   "<resolved — the model that actually ran>",
  "reviewer_reasoning": "<resolved — the effort that actually ran>",
  "generated_at":     "<UTC ISO-8601>",
  "details": {
    "total_claims":   "<int>",
    "mismatches":     [ ... per-claim issue records ... ],
    "result_files":   [ ... raw files consulted ... ]
  }
}
```

`audited_input_hashes` 范围（原文）：只 hash **本次调用声明的输入集**
（这次实际读的 .tex + raw result/config 文件），不是全仓 union，也不是评审自报子集。
路径约定：论文内文件用**相对论文目录**的路径（`main.tex` 不是 `paper/main.tex`），
论文外文件（如外部 results/ 目录）用**绝对路径**。

## 关键规则（原文 Key Rules，保留）

- **每次运行全新线程。** 不复用上下文。
- **零执行器解读。** 只传文件路径，不传摘要。
- **只用 raw results。** 无 EXPERIMENT_LOG、无 AUTO_REVIEW、无人工摘要。
- **舍入规则。** 仅标准舍入到显示精度。
- **跨模型。** 评审必须与执行器不同模型族。
- **线程独立性。** 不接受 prior audit outputs（PROOF_AUDIT、CITATION_AUDIT、
  EXPERIMENT_LOG、AUTO_REVIEW 摘要）作为本审计输入。
- 人读版 `PAPER_CLAIM_AUDIT.md` 与 JSON 同写；JSON 是权威。
