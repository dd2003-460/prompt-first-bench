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
  - **B1 已完成并验证（2026-11-23）**：`gold_md_to_units.py` 解析 markdown gold →
    structured units（unit_id/depth/raw/text/kind/stop_marker/share）。**Q6-Q10 全部 5 棵
    验证通过**（Q6 46 / Q7 52 / Q8 36 / Q9 34 / Q10 36 units；Q6/Q7 各有 4 个 kind=None，
    其余 0 —— 2026-11-23 重跑核验，源文档旧记 "Q7 48 / kind=None 全 0" 有误）。
    续行修复：Q8 的 leaf 标记常在节点第二行，解析器从续行补 kind+text（修复前 Q8 有 21 个
    kind=None）。Q6/Q7 各有 4 个 None 是 gold 源"合同与风险(nuisance)"分支本身无
    leaf/split 标记（gold 格式约定，非解析器 bug；coverage 层只读 text，不受影响）。
    judge_v1 的 coverage 层只读 `u["text"]`（line 149），B1 产物是其超集 →
    **Q6 coverage 跑分 = B1 产物 + judge_v1 layer_coverage，唯一改动是把硬编码的
    GOLD_UNITS 路径参数化**（已做：`judge_v1.py --gold-units`，回归验证 gpu 默认分
    0.3972 不变，Q6 注入链通 cov=0 正确跨域行为）。整条链闭合，不依赖 vLLM
    （embedding 用本地 bge-m3）。

## 分解树（正交子项）
```
general-methodology
├── A. metacog 轴跨域验证（general，成本≈0）
│   ├── A1. Q6 budget scan（5 档 × 3 reps, --question-file Q6, --qid q6）  [可立即做, 待vLLM]
│   ├── A2. Q7 budget scan（同上, Q7）                                      [待vLLM]
│   └── A3. 跨域 metacog 曲线对比（gpu vs Q6 vs Q7 的 gap_rate/ret 曲线）
├── B. quality 轴跨域验证（per-domain，成本=转换）
│   ├── B1. markdown→structured gold 转换脚本（Q6 先行）                    [✅ 完成, gold_md_to_units.py]
│   ├── B2. 转换产物人工核验（units 数/公式/bound 对齐 gold 原文）            [✅ Q6 share 全对]
│   ├── B3. Q6 quality judge 跑分（judge_v1 --gold-units 注入）              [✅ 前置完成, 待Q6 runs]
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
2. A2: Q7 budget scan
3. B3: Q6 quality 跑分 = `judge_v1.py --runs-dir <q6 runs> --gold-units <B1产物> --runs-glob "q6_budget*.json"`（前置已就绪）
4. A3+B4: 跨域曲线对比（metacog 3 域 + quality gpu vs Q6 peak 位置）→ 填 workshop §7

## 已完成（2026-11-23, 不依赖 vLLM）
- B1: `gold_md_to_units.py`（markdown→units, Q6 46 units 验证 + Q7 泛化）
- B2: Q6 share 全对（N-1=.35/N-2=.28/N-4=.18/N-5=.12/N-7=.03）
- B3 前置: `judge_v1.py --gold-units` 参数化 + 回归验证（gpu 默认 0.3972 不变, Q6 注入链通 cov=0 正确）

## B4 早期验证 (2026-11-23, Q6 r1 单点)

Q6 队列第 1 个 run (budget 50, 50 nodes) 双 gold 评分:
- 域内 (q6 gold, 46 units): cov=0.0652 (3/46 confirmed)
- 跨域 (gpu gold, 37 units): cov=0.0000 (0/37 confirmed)
- Δcov=+0.0652, 域内>跨域, gold 域特异性在 n=1 成立 (跨域 cov=0: Q6 run 未命中任何 gpu 硬件 gold unit, 符合预期)

交叉验证: 队列自动评分 (默认 gpu gold) r1 cov=0.0000 与 B4 跨域读数一致 — 队列 cov 读数对 Q6 系统性偏低是设计使然, B4 正式重评 (域内 gold) 是 cov 轴的权威读数。
B4 脚本: research/b4_cross_domain_judge.py (字段名已对齐 judge_run 实际返回, 注入验证 total=0.4135 与 gpu corpus 一致)。

## A3 早期数据点 (2026-11-23, Q6 50 档 3 run)

Q6 队列 50 档 3 run 完成 (617/833/499s), A3 自动吸收:
- Q6 50 档: gap 0.04/0.08/0.12 (均值 0.0800), metacog 0.046/0.252/0.414, judge 0.30/0.31/0.30
- GPU rep-scan 15 run: gap 均值 0.1023
- 跨域 Mann-Whitney: U=18, z=-0.533 (ns) — 域不变性在第一个 Q6 数据点成立
- 注: Q6 只有 50 档 3 run, 5 档完整曲线待队列跑完 (100/150/300/719 档)
- 队列内评分块静默失败 (python3 - 嵌套 heredoc stdin 被 SM 2>&1 影响), run 数据完好,
  q6_rescore.py 幂等补评分 (76bee01c7), 队列跑完跑一次重建 15 条

## B4 域内 cov 扩展 (2026-11-23, Q6 50 档 3 run)

Q6 50 档域内 (q6 gold, 46 units) cov: r1=0.0652(3/46) r2=0.0217(1/46) r3=0.0870(4/46), 均值 0.0580
队列自动评分 (gpu gold) cov: r1=0.0 r2=0.028 r3=0.0
域内 cov 系统性高于跨域 — gold 域特异性 n=3 再确认 (r1 单点 Δcov=+0.0652 → 3 run 均值 Δcov≈+0.03)
B4 正式重评 (全部 15 run) 待队列跑完。

## Repair 跨域数据点 (2026-11-23, Q6 50 档 3 run)

Q6 50 档 rework 修复率 (node-level, rework>0 的节点中最终 verified):
- r1: 2/17 (12%)  r2: 0/21 (0%)  r3: 0/12 (0%)  合计 2/50 = 4%
- GPU 固化版 (repair-closure-dryrun.py, 80-run corpus): 3.7% (331/8870)
- 方向一致: repair low-yield 跨域不变 (Q6 4% vs GPU 3.7%, n=3 runs/50 nodes each)
- 口径注意: Q6 50 档 n=3, 分母小; 5 档完整曲线待队列跑完
- 含义: "capability-limited 非 targeting" 诊断 (§4.1) 不是 GPU 域特异, 是 27b 定向修正能力的普遍瓶颈
