# proof-checker — 数学证明严格验证与修复（任务书模板）

> 来源（只读）：`aris/skills/proof-checker/SKILL.md`
> 移植日期：2026-11-25 · 移植者：Hermes subagent
> **执行器 = 本地 27b subagent 或 arena（跨模型族）**。原文引擎是 Codex MCP
> （`mcp__codex__codex`，model `gpt-6-astra`，reasoning `ultra`）或 manual-review
> MCP；本模板把所有 "怎么调模型"处替换为 `{{EXECUTOR}}`。**核心逻辑
> （20 类 issue 分类 / 双轴严重度 / 8 项强制检查 / 验收门 / 反例红队 /
> 盲审）原样保留。**
>
> 用法：`{{EXECUTOR}}` = 一次全新上下文的模型调用（本地 qwen3.8-27b subagent，
> 或 arena 跨模型族通道）。跨模型不变量：`{{EXECUTOR}}` 的模型族必须 ≠
> 执行器模型族（原文：executor 是 Claude，评审路由进任何 Claude 产品会使
> 跨模型不变量作废）。
>
> 线程规则（原文）：**每次顶层调用**从全新线程开始；同一次调用内 Phase 3
> 复审轮次复用同一会话（评审需要记得之前 flag 的 gap 是否真被修复）；
> Phase 3.5 盲审例外——必须另开全新线程，不带任何先前批评。

## 材料黑白名单

原文没有显式 ✅/❌ 列表，黑白名单隐含在协议里：

✅ 给什么：
- **完整证明内容**（原文 Key Rules："**Send full content**: Don't summarize —
  send actual math for line-by-line checking."）
- Phase 0 准备的骨架工件（执行器自建，喂给评审做 checklist）：
  1. Dependency DAG（Definition/Assumption/Lemma/Theorem 节点 + "uses" 边 + 环检测）
  2. Assumption Ledger（每个定理/引理的每个假设 + 论文声称 discharge 的位置指针
     `file:line`；论文没指位置标 UNVERIFIED——注意这是"论文没给位置"，
     不是"你判数学不成立"）
  3. Typed Symbol Table（每个符号带类型签名；跨使用含义/类型不一致要 flag）
  4. Canonical Quantified Statements（每个定理用显式量词、定义域、极限顺序改写；
     改不到这么精确的标 UNCLEAR — needs disambiguation）
  5. Micro-Claim Inventory（每个非平凡步骤写成 sequent 形式的编号 micro-claim：
     Context ⊢ Goal / Rule / Side-conditions + discharge 位置指针）
  6. Limit-Order Map（每条渐近声明的极限顺序 + uniformity scope）
- 盲审（Phase 3.5）只给**修复后的 section 单独内容**，不给先前批评。

❌ 不给什么：
- 摘要/转述代替原文数学（上面 "Send full content" 的否定面）。
- 盲审线程不给任何先前 review / discussion（原文："You have NOT seen any prior
  review or discussion."）。
- 跨顶层调用不接受先前 audit outputs（PAPER_CLAIM_AUDIT、CITATION_AUDIT、
  EXPERIMENT_LOG）作为输入（原文 Thread independence）。
- 评审共识和失败的 counterexample 搜索**不能** discharge 一个 proof
  obligation（原文 Optional Lean verification 节）。

## Issue 分类学（20 类 4 组，原文逐字）

### Group A: Logic & Proof Structure

| Category | Description | Example |
|----------|-------------|---------|
| **UNJUSTIFIED_ASSERTION** | Claim stated without proof or reference | "The Hessian splits into Gram blocks" |
| **UNPROVEN_SUBCLAIM** | "Clearly" / "it follows" hides a nontrivial lemma | "By symmetry, the cross-terms vanish" without checking |
| **QUANTIFIER_ERROR** | Wrong order ∀/∃, missing "for sufficiently small κ" | "For all π, there exists ε" vs "there exists ε for all π" |
| **IMPLICATION_REVERSAL** | Uses (A⇒B) as (B⇒A), or claims equivalence with only one direction | |
| **CASE_INCOMPLETE** | Misses boundary/degenerate cases | Singular covariance, zero weight, non-unique argmin |
| **CIRCULAR_DEPENDENCY** | Lemma uses theorem that depends on it | |
| **LOGICAL_GAP** | A step is not justified by what precedes it | B=Θ(1) → β_K=0 without analyzing W |

### Group B: Analysis & Measure Theory

| Category | Description | Example |
|----------|-------------|---------|
| **ILLEGAL_INTERCHANGE** | Swaps limit/expectation/derivative/integral without DCT/MCT/Fubini | Differentiating under E without domination |
| **NONUNIFORM_CONVERGENCE** | Pointwise convergence used as uniform | sup and limit swapped |
| **MISSING_DOMINATION** | DCT cited but no dominating function given | |
| **INTEGRABILITY_GAP** | Uses E|X|^p without proving/assuming finite moments | |
| **REGULARITY_GAP** | Differentiability/Lipschitz/convexity used but not established | |
| **STOCHASTIC_MODE_CONFUSION** | Mixes a.s./in prob./in L²/in expectation | |

### Group C: Model & Parameter Tracking

| Category | Description | Example |
|----------|-------------|---------|
| **MISSING_DERIVATION** | A quantity is used but never derived from the model | Risk functional with undefined B, W |
| **HIDDEN_ASSUMPTION** | Proof silently uses a condition not in the theorem | Gaussianity assumed but not stated |
| **INSUFFICIENT_ASSUMPTION** | Hypotheses too weak for proof (counterexample exists) | Moment conditions admitting 2-point distributions |
| **DIMENSION_TRACKING** | Parameter dependence (d, n, K, ...) not explicit | d enters only through κ |
| **NORMALIZATION_MISMATCH** | Coordinate/scaling conventions inconsistent | Rescaled vs raw coordinates |
| **CONSTANT_DEPENDENCE_HIDDEN** | "C" depends on d,n,K but treated as universal | |

### Group D: Scope & Claims

| Category | Description | Example |
|----------|-------------|---------|
| **SCOPE_OVERCLAIM** | Conclusion stated more broadly than proof supports | "β_K=0" with only generic overlap |
| **REFERENCE_MISMATCH** | Cited theorem's hypotheses not verified at point of use | |

## 双轴严重度（原文逐字）

### Axis A — Proof Status（哪里错了）

| Status | Meaning |
|--------|---------|
| **INVALID** | Statement false as written (counterexample exists or contradiction) |
| **UNJUSTIFIED** | Could be true, but current proof does not establish it |
| **UNDERSTATED** | True only after strengthening assumptions |
| **OVERSTATED** | True only after weakening conclusion / adding qualifiers |
| **UNCLEAR** | Ambiguous notation / definition drift (not wrong per se) |

### Axis B — Impact（坏多少）

| Impact | Meaning |
|--------|---------|
| **GLOBAL** | Breaks main theorem or core dependency chain |
| **LOCAL** | Affects a side result but not the main theorem |
| **COSMETIC** | Exposition only |

### Severity Labels（导出）

| Label | Definition |
|-------|------------|
| **FATAL** | INVALID + GLOBAL |
| **CRITICAL** | (INVALID + LOCAL) or (UNJUSTIFIED + GLOBAL) |
| **MAJOR** | (UNJUSTIFIED + LOCAL) or (UNDERSTATED/OVERSTATED + GLOBAL) |
| **MINOR** | Clarity / notation / dimension bookkeeping that doesn't change claims |

## 常用定理旁路条件 checklist（原文逐字）

证明用到下列任一定理时，要求显式验证**全部**列出条件：

| Theorem | Required Conditions |
|---------|-------------------|
| **DCT** (Dominated Convergence) | Pointwise a.e. convergence + integrable dominating function |
| **MCT** (Monotone Convergence) | Monotone increasing + non-negative |
| **Fubini/Tonelli** | Product measurability + integrability (Fubini) or non-negative (Tonelli) |
| **Leibniz integral rule** | Continuity of integrand + dominating function for derivative |
| **Implicit Function Theorem** | Continuous differentiability + non-singular Jacobian |
| **Taylor with remainder** | Sufficient differentiability + remainder form (Lagrange/integral) |
| **Jensen's inequality** | Convexity of function + integrability |
| **Cauchy-Schwarz** | Correct inner product space + integrability of both factors |
| **Weyl/Davis-Kahan** | Symmetry/Hermiticity + perturbation bound conditions |
| **Analytic continuation** | Domain connectivity + identity theorem conditions |
| **WLOG reduction** | Invariance under claimed symmetry + reduction is reversible |

## 验收门（原文 Acceptance Gate，客观判据取代主观打分）

证明通过当且仅当**全部**满足：
1. Zero open FATAL or CRITICAL issues
2. Every theorem/lemma has: (i) explicit hypotheses, (ii) proof with all
   interchanges justified, (iii) every application discharges hypotheses in
   the ledger
3. All big-O/Θ/o statements have declared parameter dependence and
   uniformity scope
4. Counterexample pass executed on all key lemmas (log candidates even if
   none found)

MAX_REVIEW_ROUNDS = 3（Phase 2-3 循环上限）。

## 执行 prompt

### Phase 1：首审

`{{EXECUTOR}}`（全新线程，ultra 档），提交**完整证明内容** + 下面 checklist
（原文 "Use this exact prompt for both backends"，逐字）：

```
You are performing a rigorous mathematical proof review. For EVERY theorem,
lemma, and proposition, check ALL of the following:

## MANDATORY CHECKS

A. DEFINITIONS: List any symbol whose meaning is ambiguous or changes.
B. HYPOTHESIS DISCHARGE: For each lemma/theorem APPLICATION (not statement),
   list each hypothesis and whether it was verified, with location.
C. INEQUALITY AUDIT: For each inequality chain, verify direction, missing
   absolute values, missing conditions (convexity, PSD, integrability).
D. INTERCHANGE AUDIT: Flag every limit/derivative/expectation/integral
   interchange. State which theorem justifies it (DCT/MCT/Fubini/Leibniz)
   and which conditions are verified/missing.
E. PROBABILITY MODE: Track whether claims are a.s./in prob./in expectation/
   w.h.p. Ensure transitions are justified.
F. UNIFORMITY & CONSTANTS: For every O(·), o(·), Θ(·), ≲, state whether
   it is uniform over all parameters. List hidden parameter dependence.
G. EDGE/DEGENERATE CASES: Attempt to break each key lemma with a 1D,
   low-rank, or extreme-parameter construction.
H. DEPENDENCY CONSISTENCY: Detect cycles or forward references to unproven
   results.

## OUTPUT FORMAT (per issue)
For each issue found, provide:
- id: sequential number
- status: INVALID / UNJUSTIFIED / UNDERSTATED / OVERSTATED / UNCLEAR
- impact: GLOBAL / LOCAL / COSMETIC
- category: [from taxonomy]
- location: section/equation/line
- statement: what the proof claims
- why_invalid: why this is wrong or unjustified
- counterexample: YES (describe) / NO / CANDIDATE (describe attempt)
- affects: which downstream results break if this is wrong
- minimal_fix: how to fix it

[FULL PROOF CONTENT HERE]
```

解析成结构化 issue 列表，写入 `PROOF_AUDIT.md`。

### Phase 1.5：反例红队（执行器自己做）

对每个 CRITICAL/MAJOR issue，以及每个引入以下内容的 key lemma：
新不等式界 / identifiability-uniqueness claim / curvature-PSD-strong
convexity 断言 / uniform-in-parameter claim / 收敛模式升级
（pointwise→uniform, in prob→w.h.p.），系统性尝试构造反例：

| Strategy | Description |
|----------|-------------|
| **Dimensional collapse** | Set d=1 or 2, K=2, n small |
| **Degeneracy** | Singular covariance, tiny weight, overlapping means, identical components |
| **Extremal distributions** | Two-point ±a, bounded non-subGaussian, heavy tails |
| **Adversarial parameter scaling** | Pick parameters making neglected terms dominate |
| **Numeric falsification** | Translate lemma to a function, brute-force optimize over small domain |

**规则**：只有代数验证通过才标 "counterexample found"，否则记
"candidate counterexample — needs verification"。所有尝试（成败）都记入
`PROOF_AUDIT.md`。

### Phase 2：修复（执行器做）

按严重度排序（FATAL → CRITICAL → MAJOR → MINOR）逐个修。每个 issue 显式
选一种策略：ADD_DERIVATION / STRENGTHEN_ASSUMPTION / WEAKEN_CLAIM /
ADD_REFERENCE。修复要有完整数学推导（不是 claim），LaTeX 编译通过
（`pdflatex -interaction=nonstopmode <file>.tex` 查 Error/Warning/undefined），
并按原文 Fix 记录格式写入 PROOF_AUDIT.md（Issue / Severity / Status /
Impact / Fix strategy / Location / BEFORE / WHY WRONG / AFTER / KEY EQUATION /
PROOF OBLIGATIONS ADDED / DOWNSTREAM EFFECTS）。

### Phase 3：复审

同一次顶层调用内**复用 Phase 1 的会话**（`{{EXECUTOR}}` 的 reply 通道），
带上修复摘要，请求同样的 mandatory checklist。检查验收门；未满足则重复
Phase 2-3（至多 MAX_REVIEW_ROUNDS = 3）。

### Phase 3.5：全局闭合 + 独立盲审

全局闭合检查（执行器做）：statement-conclusion match / 所有 obligation
discharged / case 分析覆盖边界退化情形 / 归纳正确性 / 每个 WLOG 都有
lossless 证明的 micro-claim / 无静默强化假设。

**FATAL/CRITICAL 修复的独立二次评审**：把**修复后的 section 单独内容**
（不展示先前批评）提交给**全新线程**的 `{{EXECUTOR}}`（原文盲审 prompt，逐字）：

```
Blind review of the following proof section. You have NOT seen any prior
review or discussion. Check every step for correctness, hidden assumptions,
illegal interchanges, and counterexamples.
[FIXED SECTION ONLY]
```

盲审发现新问题 → 回到 Phase 2。回归检查：DAG 无新环 / 被改结果的下游
lemma 跑反例套件 / assumption-delta 报告。

### Phase 3.9：不可恢复协议

MAX_REVIEW_ROUNDS 用尽仍未过验收门 → 输出 **Proof Unrecoverable Report**：
1. 无法解决的阻塞 FATAL/CRITICAL issue 最小集
2. 分级 salvage 选项：(a) weaken claim, (b) strengthen assumptions,
   (c) add missing lemmas, (d) restructure argument
3. 哪些部分大概率仍可复用
4. 给作者的下一步建议

**不得静默宣布成功。** 报告必须诚实。

## verdict 映射表

原文 "Verdict decision table"（逐字）：

| Input state | Verdict | `reason_code` example |
|---|---|---|
| No theorems / lemmas / proofs in paper | `NOT_APPLICABLE` | `no_theorems` |
| Theorems present but referenced files unreadable | `BLOCKED` | `source_unreadable` |
| All proof obligations discharged, no gaps | `PASS` | `all_proofs_complete` |
| Only MINOR issues (notation / exposition) | `WARN` | `minor_gaps` |
| Any FATAL or CRITICAL issue (logic gap, wrong claim) | `FAIL` | `critical_gap` |
| Reviewer invocation failed (network / malformed) | `ERROR` | `reviewer_error` |

> MAJOR issues alone map to `WARN` or `FAIL` at the reviewer's discretion
> and must carry an explicit justification in `summary` + `details.issues`.

**本技能自身从不 block**；是否 block 由上层（原文 paper-writing Phase 6 +
verifier）按 `assurance` 级别决定。

## 输出 schema

`PROOF_AUDIT.json`（原文 schema，**无论有无定理都必须写出**；无
`\begin{theorem|lemma|proof}` 时 verdict=`NOT_APPLICABLE`，silent skip 禁止）：

```json
{
  "audit_skill":      "proof-checker",
  "verdict":          "PASS | WARN | FAIL | NOT_APPLICABLE | BLOCKED | ERROR",
  "reason_code":      "all_proofs_complete | minor_gaps | critical_gap | no_theorems | ...",
  "summary":          "One-line human-readable verdict summary.",
  "audited_input_hashes": {
    "main.tex":                 "sha256:...",
    "sections/4.theory.tex":    "sha256:..."
  },
  "trace_path":       ".aris/traces/proof-checker/<date>_run<NN>/",
  "thread_id":        "<{{EXECUTOR}} thread/session id>",
  "reviewer_model":   "<resolved — the model that actually ran>",
  "reviewer_reasoning": "<resolved — the effort that actually ran>",
  "generated_at":     "<UTC ISO-8601>",
  "details": {
    "theorems_audited": "<int>",
    "issues": [ { "id": "T1-H3", "severity": "FATAL|CRITICAL|MAJOR|MINOR",
                  "category": "quantifier|domination|...",
                  "location": "sections/4.theory.tex:L182",
                  "note": "..." }, ... ]
  }
}
```

`audited_input_hashes` 范围：只 hash 本次实际评审的 theorem-bearing .tex 文件
（不是全仓 union，不是评审自报子集）。路径约定：论文内文件用相对论文目录
路径（无 `paper/` 前缀），论文外文件用绝对路径。

可选扩展字段（原文 opt-in，默认省略）：
- `--deep-fix` → `details.deep_fix_plans[]`（per issue：corrected_statement /
  changed_equations / downstream_labels / minimal_tex_patch_plan /
  closure_tests / algebra_sanity）+ `details.deep_fix_status: "ok"|"unavailable"`。
  失败时 `deep_fix_status="unavailable"` + `deep_fix_plans=[]`，下游必须视同
  字段不存在，不 block。**绝不**往 `details.issues` 加 deep-fix-only 类别。
- `--restatement-check` → `details.restatement_drift[]`（per drift：label /
  canonical_location / restatement_location / drift_type ∈
  conditional_loss|scope_change|quantifier_loss|regime_envelope_change|
  constant_change|variable_rename / canonical_excerpt / restatement_excerpt /
  severity / note）+ `details.restatement_check_status: "ok"|"unavailable"`。
  drift 不改变 `details.issues` 也不改变顶层 verdict 决策规则。

状态持久化 `PROOF_CHECK_STATE.json`（原文 Phase 5 schema）：

```json
{
  "status": "completed",
  "rounds": 2,
  "threadId": "...",
  "fatal_fixed": 0,
  "critical_fixed": 3,
  "major_fixed": 2,
  "minor_fixed": 1,
  "counterexamples_found": 1,
  "counterexample_candidates": 2,
  "acceptance_gate": "PASS",
  "timestamp": "..."
}
```

## 关键规则（原文 Key Rules，保留）

数学严谨性：
- **Never accept a proof step on faith**。"Clearly" / "it follows" /
  "by standard arguments" 是红旗——每个必须 spawn 一个 micro-claim。
- **Hypothesis discharge**：每次 APPLIED 引理时，在该点验证其**每个**假设。
- **Interchange discipline**：每次 limit/expectation/derivative/integral 交换
  必须引用定理（DCT/MCT/Fubini/Leibniz）并验证条件。
- **Uniformity discipline**：每个 O(·)/Θ(·) 必须声明对哪些参数 uniform。
- **Quantifier discipline**：查 ∀/∃ 顺序。"For sufficiently small κ" 必须说明
  κ₀ 依赖谁。
- **Counterexample-first**：修 gap 前先试图打破它。
- **WLOG prohibition**：每个 "without loss of generality" 必须有显式 micro-claim
  证明 reduction。No free WLOGs。
- **No silent assumption strengthening**：加条件的修复必须传播到定理陈述。

跨模型协议：
- **执行器分析，评审批评**：执行器读证明、组织问题、实施修复；外部评审给
  对抗式审查。
- **评审推理档位始终 ultra**（deep-audit 档），能力降级链只能在显式能力错误
  时步进，且永不低于 xhigh。
- **Send full content**：不摘要，送实际数学供逐行检查。
- **单次顶层调用内保留线程**（Phase 3 复审用 reply 通道，评审需要记得
  之前的 issue）；跨顶层调用永远新线程。Phase 3.5 盲审是单次运行内的刻意
  例外：必须新线程。

修复质量：最小修复（只修坏的）/ 完整推导 / 显式 scope 决策标签 / 每次修复后
编译。

Scope 诚实：不过度声明 / "proven" 与 "assumed" 分开 / 开放问题列出不隐藏。

线程独立性（原文）：每次顶层调用全新线程；跨调用不接受先前 audit outputs
（PAPER_CLAIM_AUDIT、CITATION_AUDIT、EXPERIMENT_LOG）作为输入。
