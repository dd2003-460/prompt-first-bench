# 任务：rubric-v3 pilot 矩阵 run（arena 执行 · 固定会话）

## 背景
DRAFT-rubric-v3-v2.md 已完成 batch1+batch2 全部修订（main @ r162），状态 = pilot-ready。本任务是 §3.1「pilot → 定维度」两步走的第一步：**跑出 pilot 双判数据**，用于 (a) judge 条目层 κ 首验（U-K1 γ 语义）、(b) 8×8 维度相关矩阵（R-05 合并规则输入）、(c) MDE 反推 n_pairs（R-11）。

## 输入材料（都在本目录 pilot-matrix/）
- `prompt-V0-baseline.txt` — 基线题面（无 D1/D2 段；sha256_16 见 manifest.json）
- `prompt-V1-full.txt` — V1 基准变体（含 D1 候选集构造规则 + D2 边界类型声明）
- `prompt-V1-align.txt` — V1 纯结构对照（D1 按 §4.2 三处差异改写：无默认先验字样/无数量义务/三问全候选适用）
- `manifest.json` — 冻结 diff 登记（D1/D2 sha256_16 + 各变体 sha256_16 + B10 口径注记）

**B10 口径**：共用题面不含 D3 矛盾预算段（未注册口径，§3.2 D3 行规定）。

## 你要做的

### Step 1: 跑 9 个 run（3 变体 × 3 次独立 run）
对每个变体 prompt 文件，做 **3 次完全独立的 run**（fresh context，不复用前一次搜索记忆，不读其他 run 的产出）。每次 run 完整执行题面要求（拆树 + 找瓶颈 + 矛盾清单 + 黑盒标注），产出保存为：
`runs/{variant}/run{1,2,3}.md`

**独立性要求**：
- 每次 run 从零开始调研，不许参考同变体的其他 run
- 三次 run 之间可以有自然的时间差，但内容上必须独立
- 如果某次 run 中途失败，重跑该 run，不许拿部分结果凑数

### Step 2: 落盘 run 元数据
每个 run 完成后记录到 `runs/meta.json`：
```json
{
  "runs": [
    {
      "variant": "V0-baseline",
      "run_id": "V0-baseline/run1",
      "started_at": "ISO8601",
      "ended_at": "ISO8601",
      "search_count": <整数>,
      "output_file": "runs/V0-baseline/run1.md",
      "output_sha256_16": "<16位>",
      "notes": ""
    }
  ]
}
```

### Step 3: 自检
- 9 个 run 文件都存在且非空
- 每个 run 包含：拆解树（有层级结构）、瓶颈判断（指名哪一支+为什么）、矛盾清单（或显式"无"+查过≥2独立来源的证明）、黑盒标注（如有）
- meta.json 9 条记录齐全
- 输出 `selfcheck.json`: {"all_runs_present": true, "all_have_tree": true, "all_have_bottleneck": true, "all_have_contradiction_section": true, "meta_complete": true}

## 约束
- 所有产出在 `bench/rubric-v3/ablation/pilot-matrix/runs/` 下
- 不修改 prompt 文件、manifest.json、DRAFT 文档
- 单次 run 内可以多次搜索，但跨 run 禁止共享搜索结果（独立性）
- 某个 run 确实搜不到关键数据时，按题面要求标黑盒给区间，不许编数字

## 回执（Lead 核验门禁 · 必须）
完成后回执必须含：repo URL（https://github.com/dd2003-460/prompt-first-bench.git）+ branch（你当时 checkout 的分支全名）+ commit_sha（push 后的 tip）。回执没指纹 = Lead 不验收。
