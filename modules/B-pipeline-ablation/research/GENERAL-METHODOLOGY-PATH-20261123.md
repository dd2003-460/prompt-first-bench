# General 方法论路径：分解树 + 缺口 + 验收（2026-11-23）

## 背景
D 2026-11-23 纠正："gpu题目的机械判定只能证明这方面没有llm judge的问题，
除非产出完整的general的方法论，否则只能是论文的基础工作。"
→ workshop 已重框为两轴框架（metacog 轴 general + quality 轴 per-domain）。
本文件把"general 方法论"从 §7 prose 固化成可执行规划。

## 两轴各自的 general 化成本（已核验，非猜）

### 轴1：metacognition 轴（gold-free，纯 node 字段）
- **general 化成本 ≈ 0**：`metacog_axis.py` 只读 node 字段（status/source/claim），
  不依赖任何 gold。换题面 = 换 `--question-file` + `--qid`，pipeline 端到端复用。
- 已验证：83 runs 跨 3 域（gpu 34 / CDN 22 / 二手定价 27）。
- **缺口**：无。可直接跑 Q6-Q10 任意题的 budget scan。

### 轴2：quality 轴（gold-conditioned，机械 judge）
- **general 化成本 = per-domain 转换**（核验 judge_v1.py + gold-Q6.md 得出）：
  - judge_v1 吃 **structured gold**：`gold-gpu-units.json`（36 单元, text 供 embedding）
    + `gold-gpu-formulas.json`（36 单元, kind/sympy/ref/bound）。
  - Q6-Q10 的 gold 是 **markdown**（`bench/rubric-v3/ablation/gold-Q6.md` 等, 41 节点）。
  - **转换可分两层（核验 gold-Q6.md 后修正，2026-11-23）**：
    - **units.json（coverage 层用）≈ 可自动**：Q6 gold 与 GPU gold 同构
      （N-id / depth / SHARE / leaf 标记 / 数值+单位行），解析器可机械提取
      unit_id/depth/raw/text。coverage 层只吃 text 做 embedding cosine，够用。
    - **formulas.json（L1 物理层用）= 人工标注**：`sympy`（符号式）/`ref`（参考值）/
      `bound`（约束）是域特定量（GPU 是物理约束，Q6 是经济参数），不可从 markdown
      机械提取，需人工或半自动（LLM 辅助 + 人工核验）标注。
  - **结论**：Q6 的 coverage 轴跑分 = 写解析器（机械）；L1 物理层 = 人工标注成本。
    先跑 coverage 轴即可验证"曲线形状跨域成立"，L1 层可后置。

## 分解树（正交子项）
```
general-methodology
├── A. metacog 轴跨域验证（general，成本≈0）
│   ├── A1. Q6 budget scan（5 档 × 3 reps, --question-file Q6, --qid q6）  [可立即做, 待vLLM]
│   ├── A2. Q7 budget scan（同上, Q7）                                      [待vLLM]
│   └── A3. 跨域 metacog 曲线对比（gpu vs Q6 vs Q7 的 gap_rate/ret 曲线）
├── B. quality 轴跨域验证（per-domain，成本=转换）
│   ├── B1. markdown→structured gold 转换脚本（Q6 先行）                    [未写]
│   ├── B2. 转换产物人工核验（units 数/公式/bound 对齐 gold 原文）
│   ├── B3. Q6 quality judge 跑分（judge_v1 换 gold 文件）                  [待B1+B2]
│   └── B4. 跨域 budget-quality 曲线对比（gpu vs Q6 的 peak 位置）
└── C. capability 轴（独立 general 化, 7b/27b/70b）                          [未启动, 需换模型]
```

## 验收（机器可查）
- A 完成：`runs_budget_scan/q6_budget{50,100,150,300,719}_r{1,2,3}.json` 15 个 +
  跨域 metacog 曲线图（3 域 gap_rate/ret vs budget）。
- B 完成：`gold-q6-units.json` + `gold-q6-formulas.json` + Q6 quality 分数 +
  跨域 budget-quality 曲线（peak 位置对比）。
- 口径：metacog 轴 gold-free（node 字段）；quality 轴 per-domain（structured gold）；
  两轴分开报，不混算。

## 依赖 / 阻塞
- **vLLM 被 A-r3 + rep_scan 队列占着**（~11h）→ A1/A2 要等 vLLM 释放。
- B1 转换脚本不依赖 vLLM，**现在就能写**（纯文本转换）。
- C capability 轴需换 7b/70b 模型，当前只有 27b，**阻塞**。

## 下一步（vLLM 释放后）
1. A1: Q6 budget scan（复用 budget_scan_batch.sh, 改 QID + --question-file）
2. B1: 写 markdown→structured gold 转换脚本（Q6 先行）
3. A2+B3: Q7 scan + Q6 quality 跑分
4. A3+B4: 跨域曲线对比 → 填 workshop §7
