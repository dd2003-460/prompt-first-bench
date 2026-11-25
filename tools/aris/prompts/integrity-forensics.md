# integrity-forensics — 论文诚信取证（任务书模板）

> 来源（只读）：`aris/skills/integrity-forensics/SKILL.md`
> 移植日期：2026-11-25 · 移植者：Hermes subagent
> **执行器 = 本地 27b subagent 或 arena（跨模型族）**。
>
> ⚠️ **本 skill 与其他 5 个不同**：它不是纯 prompt 模板，而是一个
> **thin launcher**——pin 住上游 Anti-Autoresearch 仓库（SHA 固定
> `b47af6f983b38347b6d2110379e266400597cf66`），委托上游 sweep 原样执行，
> 再把 verdict 翻译成 ARIS 政策词汇。上游 sweep 内部的 9 维 auditor 是
> GPT 族模型（`gpt-6-astra` + `xhigh`，上游自己的设计决定，launcher
> 不暴露任何 reviewer knob）。
>
> **移植适配点（只改"怎么调模型"的部分）**：
> - 上游 sweep 内部的 auditor 调用（Codex MCP）→ `{{EXECUTOR}}`
>   （本地 27b subagent 或 arena 跨模型族）。
> - 上游仓库需要 git clone + 联网验证 pin（`git fetch` + `eval/run_eval.py`
>   eval gate）——**纯离线环境下该 bootstrap 步骤无法执行**，见文末
>   [不确定] 标注。
> - ARIS 侧的确定性 gate（`forensics_gate.py`，verdict→policy 翻译 +
>   obligations ledger）是纯本地代码，**原样可用**，不需要模型。

## 材料黑白名单

原文没有显式 ✅/❌ 列表，黑白名单由上游 sweep 的契约定义：

✅ 给什么：
- 审计目标：`[paper-dir | pdf | arxiv-id]`（绝对路径指给上游）
- 上游 sweep 自己构建 span-anchored evidence ledger（46 patterns × 8
  families，确定性 GRIM/GRIMMER/statcheck 核心）——材料收集是上游契约，
  launcher 不插手
- gate 阶段（ARIS 侧）给：`report.json`（上游 sweep 产出）+ paper 目录
  （`.tex`/`.bib`/`.sty`/`.cls`/figures/PDF 用于 paper_fingerprint）+
  `--anti-ar-commit` + `--executor-model`

❌ 不给什么：
- 不重写、不软化、不重映射上游输出（原文 Step 1，逐字）：
  > "**Never rewrite, soften, or re-map its outputs** (`report.json` +
  > `REPORT.md`, verdict ∈ CLEAN_GIVEN_EVIDENCE / SOFT_FLAGS / HARD_FLAGS /
  > REVIEW_UNAVAILABLE)."
- 不改上游的 fresh-thread-per-dimension / 串行执行 / 模型 pin（原文 Step 1
  规则 2）。
- 观测级别（L0/L1/L2）由上游从现有 artifacts 推导——**不承诺 L2**
  （原文 Step 1）。
- gate 不信任存储的 token：决策永远从 sha-verified 的归档 report
  （`last_report.json`）+ 活动 ledger **重算**（原文 Step 2）。

## 执行 prompt（三步流程）

### Step 0 — Bootstrap pin（幂等）

原文 bash 块：clone 上游到 `~/.aris/anti-autoresearch`，checkout 固定 SHA
`b47af6f983b38347b6d2110379e266400597cf66`，`reset --hard` + `clean -ffdx`
强制 pristine 树（本地篡改不得存活），然后一次性 eval gate 验证
（`python3 eval/run_eval.py`：8 类注入缺陷 100% recall + 零 clean false
positive），marker 落在 clone 之外
（`${CLONE_DIR}.aris_eval_ok_<SHA>`）。

> **移植注**：此步需要 git clone + `git fetch`（联网）。纯离线环境无法执行
> 首次 bootstrap；已有验证过的本地 pin 副本时可离线跑（原文："a cached,
> validated pin works offline"）。见文末 [不确定]。

### Step 1 — Delegate：上游 sweep 原样执行

打开并从头到尾跟随 `$CLONE_DIR/workflows/anti-autoresearch/SKILL.md`。
launcher 只加两条包装规则（原文 Step 1，逐字）：

1. **cwd.** 上游 skill 用 `git rev-parse --show-toplevel` 自定位。所有上游
   bash 块先 `cd "$CLONE_DIR"`（永远是 cd，不是只 export ROOT），论文用
   **绝对路径**引用。
2. **Codex calls carry `approval-policy: never` + `sandbox: read-only`**
   （会话卫生；上游已规定 fresh-thread-per-dimension、串行执行、自己的模型
   pin——不改它们）。

**移植适配**：上游 auditor 的 Codex 调用 → `{{EXECUTOR}}`（本地 27b
subagent 或 arena 跨模型族），保持 fresh-thread-per-dimension + 串行 +
只读。其余——evidence ledger、coverage.json 状态机、9 个 auditor 维度、
refutation pass、确定性 summary——全是上游契约，原样执行。

### Step 2 — Typed gate + obligations（ARIS 侧，纯本地代码）

```bash
python3 "$GATE_HELPER" evaluate --report "$PAPER_DIR/report.json" --paper-dir "$PAPER_DIR" \
    --anti-ar-commit "$ANTI_AR_COMMIT" --executor-model "<this pipeline's executor>"
# exit 0 = WARN / NO_NEW_BLOCKER · exit 1 = BLOCK
```

（`GATE_HELPER` = `forensics_gate.py`，ARIS tools/ 里有，本次未随 4 脚本移植；
如需 gate 功能另行 copy。verdict→policy 翻译不重标 verdict。）

### Step 3 — Fix what it found（obligations，不是 polish loop）

每个 OPEN obligation 必须 DISPOSITIONED——修复或显式 waive。`waive` 是
一等公民预期结果（"模型提了这个，我判它错"是正常处置，不是最后手段）。
按报告列 `Anchored` / `Observability` / `FP-risk` / `Surface` / `Ext-check`
权衡。真实问题的修复路由（原文表）：

| Finding family | Repair route |
|---|---|
| A — numeric self-consistency | 从 RESULT FILES 重算（/paper-claim-audit 证据链）；修数字不修句子 |
| D — experiment integrity | 回 /experiment-audit / 重跑 |
| E — citations | /citation-audit KEEP/FIX/REPLACE 机制 |
| G — proof & derivation | /proof-checker 的 fix loop |
| B / C / H — scope, baselines, eval design | 科学层面：喂给 /auto-review-loop 作 reviewer INPUT 或给人 |
| AIS / advisory (zero-weight) | 仅作 /auto-paper-improvement-loop 的可选上下文；永不 gate |

关闭每个 obligation 用类型化 + 哈希 receipt（`resolve` 带 `--fix-type`
corrected-from-results|claim-narrowed|claim-withdrawn|citation-replaced +
`--evidence` + `--verified-by` human:/checker:/cross-family-review:；或
`waive` 仅人签）。

Ledger 机械强制的规则（原文，`tests/test_forensics_gate.py`）：
- **append-only** — 重跑 sweep 只能开 obligation，不能关；
- 后来报告里*消失*的 finding 保持 OPEN 并加 `UNRESOLVED_DISAPPEARANCE`
  ——改写 span 不是修复；
- `claim-withdrawn` 是诚实修复（删掉不支持的 claim 是合法解决——以删除 diff
  为证据）；
- **waiver 不是 resolution**：人批准、永久记录、原始 finding 快照不可变；
- 执行器的 `fix_type` 标签是 receipt 不是 verdict——critical 的关闭需要
  family checker、全新跨族 review 或人；
- receipts **重验不记忆**：之后每次 gate 都要证据文件仍存在且哈希与关闭时
  记录一致——关闭后改证据会重新打开 BLOCK；
- `resolve`/`waive`（同 `update`）**作废 standing `gate.json`**——Step 3 结尾
  必须重跑 sweep + `evaluate`。

**The One Forbidden Loop（原文，逐字）**：
> **Never run "edit → re-sweep → repeat until CLEAN".** That objective
> function teaches the editor to defeat the detector — deleting an anchored
> span kills a flag faster than fixing the number, and the result is a paper
> laundered against its own audit. The re-run after fixes exists to confirm
> the DISCREPANCY is gone (and to catch new ones); the obligations ledger —
> not the verdict — decides whether the gate opens.

## verdict 映射表

原文 Step 2 表（上游 verdict → ARIS policy，逐字）：

| upstream verdict | policy |
|---|---|
| `HARD_FLAGS` | **BLOCK** — 某个 auditor 提出了 critical 的东西，摆在你面前等你读；绝不是"机器发现了欺诈" |
| `REVIEW_UNAVAILABLE` | **BLOCK** — 不完整 sweep 不能放行论文 |
| `SOFT_FLAGS` | **WARN** — 人工处置。也要读 never-ran 列表：上游只在"否则会 clean"时把不完整折进 verdict，所以 WARN 可能压在一个 verdict-bearing 维度根本没跑的 sweep 上。`evaluate` 和 `fresh` 都会打印那些维度 |
| `CLEAN_GIVEN_EVIDENCE` | **NO_NEW_BLOCKER** — *永不*叫 PASS 或 accepted：意思是"手头证据里没找到 flag"，不是无罪释放 |
| anything else | **BLOCK** (fail closed) |

外加（原文）：任何 OPEN critical obligation → BLOCK；任何 OPEN obligation →
至少 WARN；closed-without-receipt 或 unknown-status 的 ledger 条目 → BLOCK
（手改 `"status": "RESOLVED"` 打不开 gate）。

`fresh` 命令（下游 preflight 一条命令）：
`python3 "$GATE_HELPER" fresh --paper-dir "$PAPER_DIR" --anti-ar-commit "$ANTI_AR_COMMIT"`
——exit 0 ⟺ gate 在当前 pin 产生 ∧ gate 存在 ∧ gate 之后论文没变 ∧ gate 与
当前 obligations ledger 匹配 ∧ 从 sha-verified 归档 report + 活动 ledger
**重算**的决策是 pass-capable（`WARN` / `NO_NEW_BLOCKER`）。其余一律 exit 1：
重跑 sweep + `evaluate`。

## 输出 schema

原文没有单一 JSON schema 字段定义——产物是三个 artifact（原文 Review tracing
节，逐字）：

- `gate.json`（`.aris/forensics/`）：pin `anti_ar_commit` + report/ledger
  hashes + paper-text fingerprint（sha over 论文的编译输入**和**交付物——
  `.tex`/`.bib`/`.sty`/`.cls`/figures/PDF）
- `obligations.json`（`.aris/forensics/`）：append-only ledger
- `last_report.json`（`.aris/forensics/`）：folded report 的 sha-verified
  归档，`fresh` 从它重算

上游 sweep 自身的产物（launcher 不改写）：`report.json` + `REPORT.md`，
verdict ∈ `CLEAN_GIVEN_EVIDENCE | SOFT_FLAGS | HARD_FLAGS | REVIEW_UNAVAILABLE`。

## 信任边界（原文 Trust boundary，保留）

- **Computed**（gate 机械强制）：verdict→policy 映射、append-only ledger
  生命周期、sha 绑定（report ↔ ledger ↔ archive）、receipt 重哈希、paper
  fingerprint、pin/version 匹配、重算决策（`fresh` 永不信任存储 token）。
- **Protocol**（指令级，刻意）：sweep 确实在 pin 住的 clone 上针对这篇论文
  跑了。gate 抬高门槛——结构性地板（report 必须命名 adjudicator 并带
  coverage map）、stale-report mtime 守卫——到此为止。report 和 paper 之间
  **刻意没有**密码学绑定：这是研究工作流 gate 不是 provenance 系统；诚实的
  说法是恶意执行器可以递一个 stale report。`human:` / `checker:` /
  `cross-family-review:` 标签是问责不是认证：假标签是显式的、永久的假记录。
- **Out of scope**：有 shell 权限、能一致改写 `.aris/` artifacts 的一方拥有
  owner 权力（可以直接删目录）。gate 防的是马虎/走捷径的执行器和诚实的
  crash/race/resume——不防机器 owner。

## 跨族标注（原文）

上游 auditor 是 GPT 族：对 **Claude 执行器**，findings 带 `cross-family`
proposal provenance；对 **Codex 执行器**是 `same-family`。无论如何这个 gate
只抬 flag——没有 acceptance 可授予，所以这个区别是信息性的，不是漏洞。

**移植注**：对本地 qwen3.8-27b 执行器 + `{{EXECUTOR}}` 跨族评审，provenance
应为 `cross-family`（qwen ≠ gpt）。

## [不确定] 移植缺口

1. **Step 0 bootstrap 需联网**（git clone/fetch + eval gate 验证）。纯离线
   跑不了首次 bootstrap；需要 D 在有网时机跑一次 bootstrap，之后 pin 副本
   可离线复用（原文支持 cached validated pin 离线跑）。
2. **上游仓库本身未 clone**：ARIS 仓库里只有 launcher，Anti-Autoresearch
   （46 patterns / 9 维 auditor 的实际实现）在 `wanshuiyin/Anti-Autoresearch`，
   不在本地。本模板只提取了 launcher 契约 + gate 映射；上游 sweep 的
   逐维度 auditor prompt 未落盘（在上游仓库里）。
3. **`forensics_gate.py` 未随 C1 移植**（任务只列了 4 脚本 + 2 依赖）。
   gate 功能需要它时再 copy（32KB，纯本地代码）。
