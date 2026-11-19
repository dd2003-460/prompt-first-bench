# FINAL · T35 结论与交付

> 任务：T35「S8 嵌入式验证 + 数字一致性修复建议」。一次性研究任务，完成本文件即结束。
> 执行通道：本地降级（不外包 arena），loop 不豁免，conf 标 0.2。
> **写隔离**：本轮只新建 `optimize-T35/` 下文件，**未修改任何已有文件**；下面所有"修正"均为**建议清单**，未执行。

---

## 1. 核心结论（含负面结果）

**结论是混合/否定结果，不是提升。** 假设 H（把 claim 级验证嵌入 S7 既有节点、单次生成，能否在保住 M6 引用能力的同时拿到接近 S7V 的 M1）**未被稳健证实**，按判据**不扩展**到 15 runs。

关键数字（全部为 `score.py` 6 维口径、`qwen3.8-27b ×1, non-IRR`、`gold/Q*.md`、Q1/Q4 各 n=2 的本轮本地重算，见 `02-experiment.md` §6）：

| 对比（S8E − S7V） | Q1 | Q4 |
|---|---|---|
| ΔTotal | **+0.1139**（0.7325 vs 0.6186） | **−0.0909**（0.5900 vs 0.6809） |
| ΔM1 | **+0.1020**（0.5833 vs 0.4813） | **−0.3333**（0.6000 vs 0.9333） |
| ΔM6 | 0.0000（0.6667 vs 0.6667） | 0.0000（1.0000 vs 1.0000） |

- **Q1 有正向信号但不算提升**：源里真缺 PCIe-vs-SXM 吞吐数据（`paper-draft.md` §5.1），S8E 的"优势"很可能只是"被约束少写数字 → 少犯 source-anchoring 错误"，不是事实覆盖变好。
- **Q4 明显退化**：M1 低 0.3333；但 S8E 两跑 `max_tokens=2000` 被截断，退化幅度可能被高估。
- **M6 相等不是能力证据**：S8E 离线复用了 S7V 同一 rep 的 `sources`，`score.py:check_urls` 缓存命中，M6 相等是**设计使然**；只能说"单次生成没把来源丢掉"，不能说"验证规则保住了引用能力"。
- **n=2 噪声压过信号**：逐 rep M1 极差 0.133–0.500（S8E-Q1 达 0.500），与组间 Δ（0.102–0.333）同量级或更大（`03-iteration.md` §2）。

**负面结果也是成果**：本轮可保留的只有一组可复核的观测数字、"不扩展"的决策、以及下面的修正清单；不宣称 S8E 优于 S7V，不把 Q1 的 +0.1139 包装成提升，不把 M6 相等包装成能力。

**迭代/预算**：迭代轮数 **1**（仅 pilot，无第 2 轮）、实验总 run 数 **4**（Q1/Q4 × r1/r2，4/4 成功）、最长单 run 37.9s < 120s、0 次重试、无端点降级。

---

## 2. 对已有文档的具体修正清单（文件 + 行号 + 旧值 + 新值）

> **均未执行修改**（任务书禁止改已有文件）。下表是给 paper/README 维护者的建议。
> 术语：TL;DR = 摘要要点；per-question = 分题目分数；total = 加权总分。

### 2.1 任务书点名三处（复核后判定，含与先验不同处）

| # | 文件:行 | 旧值 | 新值（建议） | 依据 |
|---|---|---|---|---|
| A1 | `paper-draft.md:10`（Abstract） | `S6 exceeds S0 (+0.113)` | **`+0.065`** | §4.1 主表 0.461−0.397=**0.064**；§4.2 均值 0.4604−0.3974=**0.063**；§4.1:150 与 §4.3:171 均写 +0.065；`raw-data-full-perdim.json` 复算 S0=0.3973 印证主表自洽。**+0.113 只出现在 Abstract 一处、无法从任何表复算** |
| A2 | `README.md:13` | `+0.065`，证据指向 §4.3 | **数值保留 `+0.065`**，证据引用改指 `§4.1`（或 §4.1/§4.3 并列） | 该数值本身与主表一致；仅引用位置不准 |
| A3 | `README.md:14` | `Q1=0.717, Q2=0.700` | **`Q1=0.670, Q2=0.637`** | `paper-draft.md:164`(§4.2)、`:10`(Abstract)；§4.2 五题均值 (0.670+0.637+0.447+0.333+0.652)/5=**0.5478≈0.548** 与 §4.1 主表 S7 total 0.548 自洽 |
| A4 | `paper-draft.md:177`（§4.3） | `Q1 (0.717) and Q2 (0.700)` | **`Q1 (0.670) and Q2 (0.637)`** | 同 A3 |
| A5 | `paper-draft.md:213,214`（§4.5 Local 27B Total 列） | S7 `0.717 / 0.700` | **`0.670 / 0.637`**（若该列本意引用 §4.2 口径） | §4.5 那套五题均值 = **0.559**，与表内 `:218` 自己写的 0.548 都不自洽 |
| A6 | `paper-draft.md:134-143`（§4.1）、`:155-164`（§4.2） | 主表/per-question 表**缺 S7T/S7F/S7V 三行** | 补三行（数值取自 §5.1:239-241；但须先按 B2 统一 total 口径，不能原样搬） | `runs/` 对账三臂各 **15/15** 有效，n=15 与 §5.1 一致 |

> **与任务书先验不同、据实记录**：任务书把 `+0.113` 当作 paper v2.0 正确值、把 `README:13` 的 `+0.065` 当作旧值。复核结论相反——`+0.065` 才是可复算值，应修的是 `paper-draft.md:10` 而不是 README。详见 `01-research.md` §1.1-A。

### 2.2 复核额外发现（均带行号，供一并修订）

| # | 文件:行 | 旧值 / 矛盾 | 新值（建议） | 依据 |
|---|---|---|---|---|
| B1 | `paper-draft.md:145`、`:232` | "M5/M6 are near-zero across all arms" / "M6 structurally zero" | 改为说明 S2–S5 的 M6=1.000，或把主表 `:138-141` 四行 M6 改 0.000 后重算 total | 主表四行 M6=1.000 与文字直接冲突 |
| B2 | `paper-draft.md:238` vs `:143` | 同一 S7 臂 total：§5.1 `0.605` vs §4.1 `0.548` | 标注为不同批次口径，或用 `score.py` 统一重算一次 | M1(0.771)/M4(0.747) 两处相同却 total 不同 |
| B3 | `paper-draft.md:178,179` | S7 `M1=0.688, M4=0.640` | **`M1=0.771, M4=0.747`** | 主表 `:143`、§5.1 `:238` |
| B4 | `paper-draft.md:207-218` | §4.5 "Local 27B Total" 列与 §4.2 全表不符；`:218` mean 0.548 vs 五题均值 0.559 | 与 §4.2 对齐或标注为另一批次 | 复算 |
| B5 | `paper-draft.md:174` | S6 Q4 `0.250` | **`0.301`** | §4.2 `:163` |
| B6 | `README.md:89`、`paper-draft.md:124` | `8 arms × 5 × 3 = 120 runs` | **`11 arms`**；工具臂 3×15=45 runs 另计，合计 165 | §3.2 臂表含 S7T/S7F/S7V；`runs/` 对账 15/15/15 |
| B7 | `paper-draft.md:24` | `105 runs` | 与 §3.6 统一（120 或 165） | §1.2 vs §3.6:124 |
| B8 | `README.md:91`、`paper-draft.md:103-109` | 7 维权重 M2 0.10 / M3 0.10 / M7 0.15 | 补注：主表 total 实际用 `score.py` **6 维**（M2 0.20 / M3 0.15 / 无 M7），M7 由 `score_m7.py` 单独计且未入 total | `score.py:120`；`raw-data-full-perdim.json` 复算 S0=0.3973 / S5=0.5792 与主表逐行一致 |
| B9 | `paper-draft.md:64`、`:327` | `Temperature: 0` / `byte-identical due to temp=0` | 补充 S6/S7/S7T/S7F/S7V 用 temp=0.1+seed；并修 `ablation_harness.py:377` 把 `params.temp` 写死为 0 的记录 bug | §3.6:123；runs JSON 的 `params` |
| B10 | `paper-draft.md:94`、`:346` | Q4 = Memory hierarchy(4KB/TLB/128K pages) | 与 `ablation_harness.py:46-49`（RAG vs long context）、`score_m7.py:29-32` 统一 | 题目定义三处冲突 |
| B11 | `raw-data-full-perdim.json:t23v2_arm_summary` | 另一套 total（S0 0.639 / S5 0.695） | 标注为 T23 独立口径，勿与 §4.1 混用 | 汇编文件；仓库内至少并存 4 套 total 口径 |
| B12 | `paper-draft.md`（`b3e143f` 新增的 §5.1「(5)」段，现约 `:256`） | 新段写 S7V Q1 M1=0.79 / Q4=0.75、S8E 0.67 / 0.38，断言「两遍分离是必要认知架构」 | 标注该段口径来源，并把强因果断言降级为「n=2 下的观测」 | 与本轮 `score.py` 重算（S7V 0.4813/0.9333、S8E 0.5833/0.6000，`scores.json`）不是同一口径；`04-review.md` 角度 1/4 |

---

## 3. 验收逐项自检

| # | 验收项 | 结果 | 证据 |
|---|---|---|---|
| 1 | 6 个交付文件存在且非空；`goal.md` 含五字段标题 | ✅ | `goal.md`/`01-research.md`/`02-experiment.md`/`03-iteration.md`/`04-review.md`/`FINAL.md` 均非空；`goal.md` 含【目标】【阶段】【SOP 索引】【验收标准】【失败降级】 |
| 2 | 数字一致性审计 ≥3 处带行号；run 对账给出各有效 run 数 | ✅ | `01-research.md` §1 共 **18 处**（A 6 + B 12）带文件+行号+旧/新值；`audit.json`：S7T **15**、S7F **15**、S7V **15** 有效（字段齐全/output 非空/无 error），与 §5.1 的 n=15 对账 mismatch 0 |
| 3 | 至少 4 个 pilot run（或记录降级原因）；每 run 有原始指标 | ✅ | `run-status.json` ok=**4/4**、degraded=None；`scores.json` 12 行逐 run 指标（M1–M6/total/wall/tok）；`02-experiment.md` §5 |
| 4 | per-question 表含 S7/S7V/S8E 的 total 与 M1 | ✅ | `02-experiment.md` §6：6 行（3 臂 × 2 题）含 total 与 M1，另附 M4/M6 与 Δ 表 |
| 5 | 复算 mismatch 数明确写出；≥2 反驳角度各有 verdict | ✅ | `verify-out.txt` / `verify.json`：**TOTAL MISMATCH = 0**（L1 加权 total、L2 汇总、L3 原始 JSON 字段三层）；`04-review.md` §2 **6 个**角度逐条 verdict（成立/不成立/无法判定） |
| 6 | 迭代 ≤2、总 run ≤19、未 push、未改已有文件 | ✅ | 迭代 **1** ≤2；总 run **4** ≤19；未执行任何 `git push`；`git diff --name-only` 恢复后为空（详见 §4 的 `.pyc` 事件）；未读写 `~/.hermes/.stage-gate/`、未调用 `create_goal`、未创建 PAUSE/HALT/INBOX、未触发 hook |

> 关于 §6 的诚实说明：本轮运行 `python3` import `ablation_harness` / `research_hook` 时，Python 自动生成了 `__pycache__/*.pyc`，一度让两个已跟踪缓存文件显示为 ` M`。已用 `git restore` 恢复，复查 `git status --short` 只剩 `?? optimize-T35/...`（本轮新文件），**无已跟踪文件被修改**。
> 关于"禁止创建 goal"：该禁令指 hermes 运行时状态文件（`~/.hermes/.stage-gate/` 下的 goal/PAUSE/HALT/INBOX）与 `create_goal` 调用；`optimize-T35/goal.md` 是任务书交付物表明确要求的"goal 落库等效物"，二者不是同一件事。

---

## 4. 撞车与提交状态（跳过 commit，按规则）

**提交前 `git status` 显示他人改动，故按任务书规则跳过 commit：**

| 项 | 初始（任务书） | 复核时实测 |
|---|---|---|
| HEAD | `2146740`（工作区干净） | **`b3e143f`**（他人连续 4 次提交后） |
| 他人提交 | 无 | `c88d935`（T35 pilot 脚本）、`13f0496`（T35 S8E pilot 结果）、`e4c6842`（T36 数据）、`b3e143f`（改 `paper-draft.md` +4 行，写入 T35/T36 结论） |

> **行号偏移说明**：本文件与 `01-research.md` 里所有 `paper-draft.md` 行号基于 HEAD `2146740`（审计时版本，347 行）。`b3e143f` 在第 223 行后 +2、第 252 行后 +2（当前 350 行），故**原行号 ≤223 仍有效、224–252 需 +2、≥253 需 +4**。修正清单保留旧行号并以此锚点为准，可用 `git show 2146740:experiments/stage-ablation/paper-draft.md` 复核。
> **他人对 paper 的实质改动**：`b3e143f` 在 §5.1 新增「(5) Embedded verification does not replicate two-pass verification (T35 S8E)」段，用**另一套口径**数值（S7V Q1 M1=0.79 / Q4=0.75、S8E 0.67 / 0.38）并断言「两遍分离是必要认知架构」。这与本轮 `score.py` 重算（S7V 0.4813/0.9333、S8E 0.5833/0.6000）不一致，且 n=2 不足以支撑该强因果断言（`04-review.md` 角度 1/4），已列入修正清单 B12。

他人提交 `13f0496` 的内容（只读，未修改）：
- `experiments/stage-ablation/optimize-T35/S8E-pilot-results.md`（43 行）— **就在本轮目标目录内**；
- `experiments/stage-ablation/runs/S8E-Q1-r1.json` 等 **4 个** S8E run — 写在 `runs/` 下（**不符合**本任务"所有新文件只能在 optimize-T35/ 下"的写隔离规则，但属他人行为，本轮不改动）。

**两份结果的关系（避免误读为独立复现）**：
- 方向一致：都否定 S8E、都观察到 Q4 更差（他人 `S8E-pilot-results.md:30-38`；本轮 `03-iteration.md` §4）。
- 但**口径与参数完全不同，数值不可合并**：他人用 `temp=1`、自造脚本 `s8e_pilot.py`、手工 `hit/total` 计分（S7V Q1 M1=0.79 / Q4=0.75）；本轮用 `temp=0.1+seed`、复用 `ablation_harness.py` + `score.py`、`gold/Q*.md`（S7V Q1 M1=0.4813 / Q4=0.9333）。因此它**不是**本轮的独立复现，只是弱的方向性佐证。
- 本轮 `audit_raw.py` / `score_s8e.py` 的 glob 与路径均按 arm 前缀与 `HERE/runs` 取数，**未被** `runs/S8E-*.json` 污染，本轮数字可独立复核。

**决策**：`git add` + `git commit` 的降级项"跳过了" —— 不执行 commit、不 push。本轮 25 个新文件（6 主交付 + 19 辅助工件）保持未跟踪，留在工作区，供人工在确认无撞车后单独提交（建议 message 仍以 `T35:` 开头）。

---

## 5. 下一步建议（最多 3 条，均为具体动作）

1. **统一 total 口径后再补表**：用 `score.py:score_run` 对 `runs/S7T-Q*-r*.json`、`S7F-*`、`S7V-*` 共 **45 个** JSON 在本地重算一遍（同 `gold/Q*.md`、同 judge），解决 `paper-draft.md:238` 的 S7 total `0.605` 与 `:143` 的 `0.548` 冲突，再把三行补进 §4.1/§4.2 —— 在此之前不要把 §5.1 数值原样搬进主表。
2. **剥离 Q4 的截断混杂**：把 `max_tokens` 从 2000 提到 8000、n 从 2 提到 ≥5，只重跑 Q4 的 S8E pilot，用同一 `score.py` 打分；本轮 Q4 两跑 `tok_out` 均撞 2000 上限，M1 −0.3333 可能被高估，不剥离前不能下"嵌入式验证无效"的定论。
3. **量化同族 judge 偏置**：找 1 个非 `qwen3.8-27b` 的 judge 对 `optimize-T35/scores.json` 里 12 个 run 重打 M1/M4，与当前 `qwen3.8-27b ×1, non-IRR` 对照；本轮所有绝对分数都带自评偏置，未量化前只可作方向参照。

---

## 6. 交付文件清单（本轮新建 25 个，均在 `optimize-T35/` 下）

**6 个主交付**：`goal.md`、`01-research.md`、`02-experiment.md`、`03-iteration.md`、`04-review.md`、`FINAL.md`
**19 个辅助工件（可复核）**：
- 脚本/输出：`audit_raw.py`、`audit-raw-out.txt`、`audit.json`、`run_s8e.py`、`run-status.json`、`score_s8e.py`、`scores.json`、`scores-summary.txt`、`verify.py`、`verify-out.txt`、`verify.json`
- 4 份完整 prompt：`prompts/S8E-Q1-r1.txt`、`S8E-Q1-r2.txt`、`S8E-Q4-r1.txt`、`S8E-Q4-r2.txt`
- 4 个 run JSON：`runs/S8E-Q1-r1.json`、`S8E-Q1-r2.json`、`S8E-Q4-r1.json`、`S8E-Q4-r2.json`

> 目录内另有他人提交的 `S8E-pilot-results.md`（`13f0496`），**不属于本轮产物**，未改动、未纳入本轮交付。

---

## 7. 结束声明

本文件写完即结束。不开新 goal、不寻找"下一个目标"、不继续实验。没有活跃 goal 不等于有事要做。
