# experiment-audit — 实验完整性审计（任务书模板）

> 来源（只读）：`aris/skills/experiment-audit/SKILL.md`
> 移植日期：2026-11-25 · 移植者：Hermes subagent
> **执行器 = 本地 27b subagent 或 arena（跨模型族）**。原文引擎是 Codex MCP
> （`mcp__codex__codex`，model `gpt-6-astra`，reasoning `ultra`）或 manual-review
> MCP；本模板把所有 "怎么调模型"处替换为 `{{EXECUTOR}}`。**核心逻辑
> （执行器只收路径 / 评审独立判完整性 / A-F 六项检查 / 4 类欺诈模式）原样保留。**
>
> 用法：`{{EXECUTOR}}` = 一次全新上下文的模型调用（本地 qwen3.8-27b subagent，
> 或 arena 跨模型族通道）。跨模型不变量：`{{EXECUTOR}}` 的模型族必须 ≠
> 执行器模型族。

## 材料黑白名单

原文 Core Principle（逐字）：

> "**The executor collects file paths. The external reviewer backend reads code
> and judges integrity. The executor does NOT participate in integrity judgment.**"

> "**DO NOT summarize, interpret, or explain any file content.** Only collect paths."

✅ 给什么（Step 1 扫描清单，逐字）：
```
Scan project directory for:
1. Evaluation scripts:    *eval*.py, *metric*.py, *test*.py, *benchmark*.py
2. Result files:          *.json, *.csv in results/, outputs/, logs/
3. Ground truth paths:    look in eval scripts for data loading (dataset paths, GT references)
4. Experiment tracker:    EXPERIMENT_TRACKER.md, EXPERIMENT_LOG.md
5. Paper claims:          NARRATIVE_REPORT.md, paper/sections/*.tex, PAPER_PLAN.md
6. Config files:          *.yaml, *.toml, *.json configs with metric definitions
```

注意：与 paper-claim-audit 相反，本审计**给** tracker/claims 文件（评审判
"claim vs 实际"一致性），但执行器仍然只收集路径、不解读内容。

❌ 不给什么：任何执行器对文件内容的摘要/解读/解释（上面两条引文即禁令）。
评审直接自己读全部文件。

## 执行 prompt

`{{EXECUTOR}}`（全新上下文，只读，cwd = 项目目录）。原文 "Use this exact prompt
for both backends"（逐字）：

```
You are an experiment integrity auditor. Start from the assumption that the
evaluation is compromised somewhere — your job is to find where. Be
adversarial. Trust nothing the author tells you — verify everything
yourself. Read ALL files listed below and check for the following fraud
patterns.

Files to read:
- Evaluation scripts: [list paths]
- Result files: [list paths]
- Experiment tracker: [list paths]
- Paper claims: [list paths]
- Config files: [list paths]

## Audit Checklist

### A. Ground Truth Provenance
For each evaluation script:
1. Where does "ground truth" / "reference" / "target" come from?
2. Is it loaded from the DATASET, or generated/derived from MODEL OUTPUTS?
3. If derived: is it explicitly labeled as proxy evaluation?
4. Are official eval scripts used when available for this benchmark?
FAIL if: GT is derived from model outputs without explicit proxy labeling.

### B. Score Normalization
For each metric computation:
1. Is any metric divided by max/min/mean of the model's OWN output?
2. Are raw scores reported alongside any normalized scores?
3. Are any scores suspiciously close to 1.0 or 100%?
FAIL if: Normalization denominator comes from prediction statistics.

### C. Result File Existence
For each claim in the paper/narrative:
1. Does the referenced result file actually exist?
2. Does the claimed metric key exist in that file?
3. Does the claimed NUMBER match what's in the file?
4. Is the experiment tracker status DONE (not TODO/IN_PROGRESS)?
FAIL if: Claimed results reference nonexistent files or mismatched numbers.

### D. Dead Code Detection
For each metric function defined in eval scripts:
1. Is it actually CALLED in any evaluation pipeline?
2. Does its output appear in any result file?
WARN if: Metric functions exist but are never called.

### E. Scope Assessment
1. How many scenes/datasets/configurations were actually tested?
2. How many seeds/runs per configuration?
3. Does the paper use words like "comprehensive", "extensive", "robust"?
4. Is the actual scope sufficient for those claims?
WARN if: Scope language exceeds actual evidence.

### F. Evaluation Type Classification
Classify each evaluation as:
- real_gt: uses dataset-provided ground truth
- synthetic_proxy: uses model-generated reference
- self_supervised_proxy: no GT by design
- simulation_only: simulated environment
- human_eval: human judges

## Output Format

For each check (A-F), report:
- Status: PASS | WARN | FAIL
- Evidence: exact file:line references
- Details: what specifically was found

Overall verdict: PASS | WARN | FAIL

Be thorough. Read every eval script line by line.
```

## verdict 映射表

原文没有单独的 (counts→verdict) 代码表——verdict 直接由评审按检查项状态给出
（每项 PASS/WARN/FAIL + overall PASS/WARN/FAIL），FAIL 触发条件写在每个检查项
末尾（"FAIL if: ..." / "WARN if: ..."，见上 prompt A-E）。

集成语义（原文，逐字）：

> "**Never blocks the pipeline.** Even on FAIL, the pipeline continues — but
> claims carry visible integrity tags."

- `PASS` → continue normally
- `WARN` → print ⚠️ warning, continue, tag claims as `[INTEGRITY: WARN]`
- `FAIL` → print 🔴 alert, continue, tag claims as `[INTEGRITY CONCERN]`

下游消费（原文）：
- `/result-to-claim`：读 `integrity_status`，`fail` 时 verdict 显示降级为
  `"yes [INTEGRITY CONCERN]"`；无 audit 时标 `"provisional — no integrity audit"`。
- `/paper-write`：`integrity_status == "fail"` 时给受影响 claim 加脚注
  "Note: integrity audit flagged concerns with this evaluation"。

## 输出 schema

`EXPERIMENT_AUDIT.json`（原文 schema，逐字）：

```json
{
  "date": "2026-04-10",
  "auditor": "external-reviewer-ultra",
  "overall_verdict": "warn",
  "integrity_status": "warn",
  "checks": {
    "gt_provenance": {"status": "pass", "details": "..."},
    "score_normalization": {"status": "warn", "details": "..."},
    "result_existence": {"status": "pass", "details": "..."},
    "dead_code": {"status": "pass", "details": "..."},
    "scope": {"status": "warn", "details": "..."},
    "eval_type": "real_gt"
  },
  "claims": [
    {"id": "C1", "impact": "supported"},
    {"id": "C2", "impact": "needs_qualifier"}
  ]
}
```

人读版 `EXPERIMENT_AUDIT.md` 同写（含 Overall Verdict / Integrity Status /
Checks A-F / Action Items / Claim Impact 各节）。

## 关键规则（原文 Key Rules，保留）

- **评审独立性**：执行器收路径，评审判。句号。
- **永不 block**：大声警告，不停管线。
- **File-as-switch**：没有 EXPERIMENT_AUDIT.md = 技能没跑过 = 对既有行为零影响。
- **跨模型**：评审必须与执行器不同模型族。
- **诚实面对局限**：审计抓常见模式，不抓所有可能的欺诈。是安全网不是保证。

动机（原文 Acknowledgements）：社区报告的完整性事故（#57、#131）——执行器 agent
造 fake ground truth、自归一化分数。
