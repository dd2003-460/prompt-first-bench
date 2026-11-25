# kill-argument — 对抗式攻击-辩护审查（任务书模板）

> 来源（只读）：`aris/skills/kill-argument/SKILL.md`（wanshuiyin/Auto-claude-code-research-in-sleep）
> 移植日期：2026-11-25 · 移植者：Hermes subagent
> **执行器 = 本地 27b subagent 或 arena（跨模型族）**。原文引擎是 Codex MCP
> （`mcp__codex__codex`，model `gpt-6-astra`，reasoning `ultra`）；本模板把所有
> "怎么调模型"处替换为 `{{EXECUTOR}}`。**核心逻辑（零上下文 / 黑白名单 / 攻击轴 /
> 三分类 / verdict 由代码算而非评审自判）原样保留。**
>
> 用法：`{{EXECUTOR}}` = 一次全新上下文的模型调用（本地 qwen3.8-27b subagent，
> 或 arena 跨模型族通道）。两个线程必须是两次独立调用，绝不共享上下文
> （原文靠 "never use codex-reply" 保证，这里等价 = 两个独立会话）。
> 跨模型不变量：`{{EXECUTOR}}` 的模型族必须 ≠ 写论文的执行器模型族
> （见 `../provenance.py::assert_cross_family`）。

## 材料黑白名单

### ✅ 给什么

原文（Step 2 prompt 内）：
> "## Files to read
> - LaTeX entry: <ENTRY>
> - All section files under sections/ or wherever they live
> - Macro files (math_commands.tex, etc.)
> - Compiled PDF: <main.pdf> (if available)"

即：论文目录的 LaTeX 入口、全部 section .tex、宏文件、编译好的 PDF（如有）。
Thread 2（adjudication）额外给：**Thread 1 的 attack memo 逐字原文**。

### ❌ 不给什么

原文：
> "Read the source carefully. Do not consult any prior reviews, fix lists,
> or summaries; this must be a fresh, zero-context adversarial pass."

> "Do NOT reference prior review rounds, fix lists, or any context outside
> the current paper files."

> "Neither thread receives prior round reviews, fix lists, executor summaries,
> or improvement-loop logs."（Key Rules — Zero prior context）

## 执行 prompt

### Thread 1：攻击备忘录（~200 词，单一论点）

`{{EXECUTOR}}`（全新上下文，只读，cwd = 论文目录）：

```
You are simulating a hostile NeurIPS / ICLR / ICML reviewer for a paper.
This is a kill-argument adversarial check — your task is NOT to give a
balanced review but to construct the **single strongest argument for
rejecting this paper**.

## Files to read
- LaTeX entry: <ENTRY>
- All section files under sections/ or wherever they live
- Macro files (math_commands.tex, etc.)
- Compiled PDF: <main.pdf> (if available)

Read the source carefully. Do not consult any prior reviews, fix lists,
or summaries; this must be a fresh, zero-context adversarial pass.

## Your task
Construct the single best argument to reject this paper in approximately
200 words. Your goal is to write the worst-case rejection memo a senior
NeurIPS area chair would produce after reading the paper.

Focus on these axes (pick the most damaging combination, do not list all):
1. Theorem validity: are central theorems actually proved as stated?
2. Assumption-vs-claim mismatch: does the body silently retreat to a
   narrower object than the title/abstract advertise?
3. Missing proof obligations: is a fundamental lemma invoked but not
   proved (e.g., concentration, generic position, prefactor envelope)
   that the headline depends on?
4. Limit-order ambiguity: are limits in K/n/d/eps composed in a way the
   paper does not commit to?
5. Claim-vs-evidence gap: is the empirical/numerical evidence too narrow
   to support the breadth of the stated theorem or take-away?
6. Scope overclaim: does the title or abstract sell a result substantially
   broader than what the body proves?

## Constraints
- Approximately 200 words total (do NOT exceed 250).
- Single argument, not a list — pick the most damaging line of attack
  and develop it.
- Cite specific file:line locations or equation numbers when accusing.
- Tone: dispassionate but uncompromising. Do NOT hedge. Do NOT acknowledge
  mitigations the paper might have made elsewhere. This is the rejection
  paragraph; the defense gets the next pass.
- Do NOT reference prior review rounds, fix lists, or any context outside
  the current paper files.

Output: just the rejection memo, nothing else.
```

保存 attack memo 逐字原文（Thread 2 和报告都用它）。

### Thread 2：裁定（逐点三分类）

第二次独立 `{{EXECUTOR}}` 调用（全新上下文，**不带 Thread 1 的任何对话历史**，
只把 attack memo 作为文本输入）：

```
You are an independent area-chair adjudicator examining whether the
current paper text answers a hostile reviewer's rejection memo.
You are NOT the paper's defender — your job is to read the attack
point-by-point and rule, from the current source files alone,
whether each point stands or falls. Fresh, zero-context adjudication;
do not reference any prior reviews / fix lists.

## Paper files
[list paths same as Thread 1]

## The hostile reviewer's rejection memo (the "attack")
> <attack memo verbatim from Thread 1>

## Your task
The attack is one continuous argument, but it makes multiple distinct
rejection points that you must adjudicate separately. Decompose the
attack into its atomic rejection points (3-7 of them), then for each
point classify it:

- answered_by_current_text: the current paper source already mitigates
  this point (cite specific file:line evidence)
- partially_answered: paper has some response but not enough to refute
  the attack as written
- still_unresolved: paper has no effective response

The label `answered_by_current_text` is intentional — "fixed" implies
history of patching and biases toward optimism. You are reading the
paper as a reviewer would, with no knowledge of prior round drafts.

For each rejection point, output:
### Point P_n: <short label>
**Attack claim**: <the specific accusation, ~30 words>
**Verdict**: answered_by_current_text | partially_answered | still_unresolved
**Evidence (or lack of)**: <cite file:line, ~50 words>
**Severity if unresolved**: critical | major | minor
**If unresolved, recommended fix**: <one specific actionable sentence>

After per-point analysis, output:

## Summary
Total rejection points: N
- answered_by_current_text: X
- partially_answered: Y
- still_unresolved: Z

## Net assessment
<one short paragraph: would this paper survive a senior area-chair read
of the attack memo, given only what is in the current source? Be honest —
if Y or Z > 0 and they hit the headline, say so.>

## Top action items (in priority order, max 3)
1. ...
2. ...
3. ...

## Constraints
- Do NOT consult any prior round reviews or fix lists. Adjudication must
  be made strictly from current paper files.
- If the paper cannot refute a point, do NOT minimize — keep severity
  honest.
- If a point reflects an author-chosen position (e.g., conscious title
  scope decision), classify as `partially_answered` with a note that the
  position is intentional, AND say whether this position is sustainable
  under the attack — do NOT auto-grade as `answered_by_current_text`
  just because it is intentional.
- Be specific. No flattery, no hedging, no rationalizing on the paper's
  behalf.
```

### 可选 beast 档（多轴 fan-out，默认关）

原文 Step 2.5：6 个攻击轴各跑一次独立探针（每轴 ~120 词最强论点，xhigh 档），
最后再跑一次 commit 合成（仍必须收敛到单一 ~200 词段落，最多融合 2 轴）。
探针是取证不是 verdict。**不要 fan-out verdict，只 fan-out 喂给 verdict 的证据。**

## verdict 映射表

原文 Step 4（每个 (counts, severity) 组合必须恰好命中一行；
**verdict 由代码从逐点计数算出，绝不让 adjudicator 线程自判顶层 verdict**）：

| Verdict | reason_code | Trigger |
|---|---|---|
| `FAIL` | `unresolved_critical` | ≥1 `still_unresolved` at `critical` severity |
| `WARN` | `unresolved_major_or_minor` | ≥1 `still_unresolved` at `major` or `minor` severity (and no `critical`) |
| `WARN` | `partial_critical_or_repeated_major` | 0 `still_unresolved`, AND ≥1 `partially_answered` at `critical` or `major` |
| `PASS` | `defense_survives_with_minor_partial_only` | 0 `still_unresolved`, AND ≥1 `partially_answered`, all at `minor` severity |
| `PASS` | `defense_survives` | 0 `still_unresolved`, AND 0 `partially_answered` |
| `NOT_APPLICABLE` | `not_theory_or_scope_paper` | Paper has <2 `\begin{theorem\|lemma\|proposition\|corollary}` AND no scope / generality claims in abstract |
| `NOT_APPLICABLE` | `headline_unstable` | Title or abstract changed within the last 2 commits — re-run after headline stabilizes |
| `BLOCKED` | `paper_compile_failed` | Compiled PDF missing AND `main.tex` does not compile clean — adjudication needs source fidelity |
| `BLOCKED` | `source_files_missing` | `main.tex` not found, or no `sec/*.tex` files |
| `ERROR` | `codex_api_error` | `{{EXECUTOR}}` call failed（原文为 `mcp__codex__codex` call failed） |
| `ERROR` | `decomposition_parse_failed` | Adjudicator thread did not return parseable per-point structure |
| `ERROR` | `trace_save_failed` | Trace directory write failed |

`PASS` 要求 `still_unresolved == 0`。`still_unresolved == 0` 时，任何
`major` 及以上的 `partially_answered` 使最优 verdict 只能是 `WARN` — 永不 `PASS`。

## 输出 schema

`<paper-dir>/KILL_ARGUMENT.json`（原文 schema）：

```json
{
  "audit_skill": "kill-argument",
  "verdict": "PASS | WARN | FAIL | NOT_APPLICABLE | BLOCKED | ERROR",
  "reason_code": "<see verdict mapping above>",
  "summary": "<one-line summary, ~80 chars>",
  "audited_input_hashes": {
    "main.tex":                          "sha256:<...>",
    "sec/0.abstract.tex":                "sha256:<...>",
    "sec/<each-section>.tex":            "sha256:<...>",
    "references.bib":                    "sha256:<...>",
    "main.pdf":                          "sha256:<...>"
  },
  "trace_path": ".aris/traces/kill-argument/<date>_run<NN>/",
  "thread_id": "<defense threadId — primary; attack threadId in details>",
  "reviewer_model": "<resolved — the model that actually ran>",
  "reviewer_reasoning": "<resolved — the effort that actually ran>",
  "generated_at": "<UTC ISO-8601>",
  "details": {
    "attack_thread_id": "<threadId 1>",
    "defense_thread_id": "<threadId 2 — same as top-level thread_id>",
    "attack_memo": "<verbatim>",
    "decomposed_points": [
      {
        "id": "P_1",
        "label": "<short label>",
        "attack_claim": "<...>",
        "verdict": "answered_by_current_text | partially_answered | still_unresolved",
        "evidence": "<file:line citation>",
        "severity_if_unresolved": "critical | major | minor",
        "recommended_fix": "<...>"
      }
    ],
    "counts": {
      "answered_by_current_text": "<int>",
      "partially_answered":       "<int>",
      "still_unresolved":         "<int>"
    },
    "net_assessment": "<adjudicator memo's net assessment>",
    "top_action_items": ["...", "...", "..."]
  }
}
```

`audited_input_hashes`：论文相对路径，消费的所有 `.tex` + `references.bib` +
（如存在）编译 `main.pdf` 的 sha256。

## 关键规则（原文 Key Rules，保留）

- **每次调用全新线程。** Attack 和 Adjudication 都是独立 `{{EXECUTOR}}` 调用，
  绝不共享上下文。
- **零先前上下文。** 两个线程都不接收 prior round reviews、fix lists、
  executor summaries、improvement-loop logs。
- **攻击必须 commit。** 单一论点 ~200 词，无 "consider also" 对冲。
- **裁定者必须分类，不许淡化。** `still_unresolved` 在论文无有效回应时就是诚实答案。
- **作者有意为之的立场**（故意收窄标题范围等）：标 `partially_answered` 并注明
  intentional，同时说明该立场在攻击下是否可持续；不因 intentional 自动给
  `answered_by_current_text`。
- **verdict 由技能代码算，不由 adjudicator 判。**
- **默认 detect-only，不自动改论文文件。**

## 何时不用（原文 When NOT to Use）

- 无定理/无 scope claim 的经验论文 → 用普通 deep review。
- 标题还不稳定的早期草稿 → 先发稳定标题（否则 `NOT_APPLICABLE: headline_unstable`）。
- 实验还在跑的论文 → 等结果稳定。
