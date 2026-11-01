# 任务：rubric-v3 正式实验矩阵 run（arena 执行 · 固定会话）

## 背景
DRAFT-rubric-v3-v2.md §3.1「pilot → 定维度」两步走。pilot（3 变体 × 3 run + 双判 κ）已收口，R-05 合并处置裁定落定（选项 c：维持分开报只标共线风险，确认性主维 O3+O1 不变）。本任务 = **第二步：完整 7 变体矩阵**，产出消融归因数据。

## 输入材料（都在 bench/rubric-v3/ablation/formal-matrix/）
- `prompt-V0-baseline.txt` — 基线题面（无 D1/D2 段）
- `prompt-V1-full.txt` — V1 基准（含 D1 候选集构造规则 + D2 边界类型声明）
- `prompt-V1-align.txt` — V1 纯结构对照（D1 用 §4.2 改写版）
- `prompt-V2-nocoverage.txt` — V1 精确删 D1（隔离 O1 的 prompt 归因）
- `prompt-V3-noboundary.txt` — V1 精确删 D2（隔离 P4 的 prompt 归因）
- `prompt-V-sham.txt` — V1 的 D1 替换为等长中性格式规范段（控制长度/格式效应）
- `prompt-V3-sham.txt` — V1 的 D2 替换为等长中性引用格式段
- `manifest.json` — 冻结 diff 登记（每变体 sha256_16，开跑前逐文件核对）

**B10 口径**：共用题面不含 D3 矛盾预算段（未注册口径，§3.2 D3 行规定）。

## 你要做的

### Step 1: 跑 21 个 run（7 变体 × 3 次独立 run）
对每个变体的 prompt 文件做 **3 次完全独立的 run**（fresh context，不复用前一次搜索记忆，不读其他 run 的产出）。每次 run 完整执行题面要求（拆树 + 找瓶颈 + 矛盾清单 + 黑盒标注），产出保存为：
`runs/{variant}/run{1,2,3}.md`（variant = 文件名去掉 prompt- 前缀和 .txt 后缀，如 V0-baseline、V1-full）

**独立性要求**：
- 每次 run 从零开始调研，不许参考同变体的其他 run
- 跨变体同样禁止共享搜索结果——V2 的 run 不得知道 V1 的 run 查过什么
- 如果某次 run 中途失败，重跑该 run，不许拿部分结果凑数

### Step 2: 落盘 run 元数据
每个 run 完成后记录到 `runs/meta.json`（schema 同 pilot：variant/run_id/started_at/ended_at/search_count/output_file/output_sha256_16/notes），21 条齐全。

### Step 3: 自检
- 21 个 run 文件都存在且非空
- 每个 run 包含：拆解树（有层级结构）、瓶颈判断（指名哪一支+为什么）、矛盾清单（或显式"无"+查过≥2独立来源的证明）、黑盒标注（如有）
- meta.json 21 条记录齐全
- 输出 `selfcheck.json`: {"all_runs_present": true, "n_runs": 21, "all_have_tree": true, "all_have_bottleneck": true, "all_have_contradiction_section": true, "meta_complete": true}

## 约束
- 所有产出在 `bench/rubric-v3/ablation/formal-matrix/runs/` 下
- 不修改 prompt 文件、manifest.json、DRAFT 文档、o3-claim-list.md
- 单次 run 内可以多次搜索，但跨 run 禁止共享搜索结果（独立性）
- 某个 run 确实搜不到关键数据时，按题面要求标黑盒给区间，不许编数字
- 21 run 量大，建议按变体分批推进；每完成一个变体的 3 run 就把该批 meta 增量写盘（防中断丢工作）

## 回执（Lead 核验门禁 · 必须）
完成后回执必须含：repo URL（https://github.com/dd2003-460/prompt-first-bench.git）+ branch（你当时 checkout 的分支全名）+ commit_sha（push 后的 tip）。回执没指纹 = Lead 不验收。
