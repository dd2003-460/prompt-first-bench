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

## Metacog 轴固有变异性 (2026-11-23, cv 对比)

Q6 50 档 gap_rate: n=3 均值 0.0800 sd 0.0400 cv=0.50
GPU rep-scan: n=15 均值 0.1023 sd 0.0499 cv=0.49
→ cv 几乎相同 (0.50 vs 0.49): Q6 50 档的"大方差"不是低 budget 不稳定, 是 metacog 轴的固有变异性 (cv≈0.5 常态)
→ A3 跨域比较的 caveat 钉死: 必须用均值 (Mann-Whitney 等), 单点/单 rep 不可比; n=3 的域内 tier 均值带 cv≈0.5 的不确定性
→ 对 paper: 任何 metacog 轴的 budget 曲线 claim 都要带 rep 间 sd (skill rule 10: spread 不能藏 sd)

## 字段审计 + retrieval_rate 跨域 caveat (2026-11-23)

30 树 8767 节点字段值枚举 (无隐藏值):
- status: verified 4375 / degraded 3784 / pending 608 (3 值)
- edge_type: cartesian 7537 / quotient 1211 / stochastic 19 (3 值)
- source: knowledge 5646 / search 2864 / given 245 / derived 12 (4 值, derived 见 T-JUDGE-1 注)

**retrieval_rate 跨域 caveat**: Q6 100-r1 search 占比 14% (14/100) vs GPU rep-scan 32.7% —
Q6 (网络架构域) 的检索触发率显著低于 GPU (硬件域)。含义: retrieval_rate 不是域不变量
(与 gap_rate 不同), A3 跨域比较 retrieval_rate 时域差异是真实信号不是噪声。
Q6 50 档 3 run search 占比: 10%/40%/22% (均值 24%), 仍低于 GPU 32.7%。

## Q6 100 档 3 run 数据点 (2026-11-23)

- gap: 0.01/0.01/0.00 (均值 0.0067) vs 50 档 0.0800 — Q6 域内 gap 随 budget 降 12× (n=3/tier, suggestive; 与 GPU 域 budget-invariance 方向不同, 域间差异待 5 档全出后检验)
- cov 域内: 0.130/0.044/0.044 (均值 0.0725) vs 50 档 0.0580 — Q6 域内 cov 随 budget 升 (breadth 曲线第一个跨档信号, n=3)
- cov 跨域 (gpu gold): 0.0000 (3/3 run) — 域特异性继续成立
- repair node-level: 3/67 = 4.5% (50 档 4.0%, GPU 固化版 3.7%) — low-yield 跨档稳定
- 注: Q6 100 档 gap 极低 (0-1%) 可能是 Q6 题面特性 (网络架构域 defensive marker 少), 不是 budget 效应 — 与 GPU 域 gap~0.10 的域间差异本身是 A3 的跨域信号

## 勘误 (2026-11-23, 推翻 A3 早期"域不变性成立"结论): 检测器域偏污染跨域 gap_rate

**发现**: metacog_axis 的 DEFENSIVE_PATTERNS (8 pattern: [待核验]/不确定/未验证/待确认/
需要验证/无法确定/缺乏数据/信息不足) 对 Q6 域系统性漏检:
- Q6 50 档: 检测器命中 12, 漏掉的防御语言 (无法验证/无法确认/未能核实/无来源/未找到等) 40 → 漏检率 77%
- Q6 100 档: 检测器命中 2, 漏掉 56 → 漏检率 97%
- Q6 域实际防御措辞是"无法验证/无法确认/未能核实/缺乏来源"类, 不在检测器 8 pattern 里

**后果**:
1. A3 早期"域不变性成立" (Q6 gap 0.08 vs GPU 0.10, Mann-Whitney z=-0.533 ns) **被推翻** —
   Q6 gap_rate 是检测器漏检后的下界, 真实 gap 可能远高于 0.08; "接近"是假接近
2. "Q6 100 档 gap 骤降 12× (0.08→0.0067)" **是检测器假象**, 不是 budget 效应 —
   广谱防御语言 100 档 56 处 > 50 档 40 处, 真实 gap 可能随 budget 升不降
3. A3 跨域 gap_rate 比较**不能直接用现有检测器** — 要么给每个域建域适配的检测器,
   要么用 LLM 判防御性 (但 metacog 轴定位是 gold-free + 无 LLM, 冲突)

**对 general methodology 的影响**: D 要求"完整 general 方法论", 但 gap_rate 这个核心量
本身是 detector 域偏的 — 跨域比较前必须先解决检测器域偏, 否则 A3 的"域不变性"检验
在量层面就不成立。这是 general methodology 的一个**前置阻塞**, 不是跑完 Q6 5 档就能绕过的。

**待办**: ① 给 Q6 域补防御性 pattern (无法验证/无法确认/未能核实/缺乏来源/无来源/未找到/存疑),
重算 Q6 gap_rate 看真实值; ② 重做 A3 跨域比较 (域适配检测器); ③ 评估"无 LLM 检测器"
定位是否要放宽 (LLM 判防御性 vs 域适配 regex 的取舍)

**升级 (2026-11-23, 比 A3 跨域污染更严重): budget-invariance 非 detector-robust**
脚本: research/gap-detector-domain-bias.py (固化, 复现下表)
- 现用 8-pattern 检测器对 GPU 也漏检 ~75% (0.10→0.41), 不是只污染 Q6
- 现用下 GPU gap 随 budget 平坦 (0.093/0.097/0.109) → 论文 finding "invariance"
- 扩展下 GPU gap 随 budget **上升** (0.39/0.41/0.44) → invariance 不成立
- Q6 扩展下: 50 档 0.36 → 100 档 0.21 → 150 档 0.22 (Q6 域内 budget 效应方向与 GPU 相反)
- 扩展 pattern 命中已人工抽样验证为真防御措辞 (无法直接支持/缺乏直接来源支持/无法直接验证), 无误伤
- compute_metacog 扫 claim+evidence+corrected_claim 三字段, 与复现口径一致

**对论文的影响 (投稿级)**:
1. 核心 finding "budget-invariance" (ANOVA F=0.036) 依赖现用闭集检测器, 扩展检测器下不成立
2. 正确表述: gap_rate 是闭集 regex 的**域偏下界**, budget-invariance **非 detector-robust**
3. draft §6 必须加 limitation: "gap_rate 基于闭集防御性标记检测器 (8 pattern), 对
   未收录措辞系统性漏检 (GPU 漏检 ~75%, Q6 漏检 77-97%); budget-invariance 结论
   在扩展检测器下不成立 (gap 随 budget 升), 故 invariance 是 detector-scoped 非
   detector-robust"
4. 这其实**强化**了论文"measurement + diagnosis"定位: 发现了一个 measurement 本身
   的局限 (闭集检测器的域偏), 是元层面的诊断贡献
5. 承重数字: ANOVA F=0.036 的 invariance 现在只能标 "detector-scoped (8-pattern)"
   不能标 "confirmed invariance" — 降级为 suggestive + 带 detector caveat

**再反转 (2026-11-23, 决定性检验, 精确口径)**:
字段分布分解显示扩展检测器新增命中 **87% 在 evidence 字段 (核验/修复阶段 b/c),
只有 5% 在 claim 字段 (监控阶段 a)**。只算 claim 字段 (纯监控轴):
- 现用: 0.0896/0.0902/0.0961 (100/150/300) — 平坦
- 扩展: 0.1051/0.1062/0.1139 — **仍平坦**
- claim 字段 ANOVA: F(2,12)=0.033 (扩展) vs 0.036 (现用) — 几乎相同
**精确结论 (承重口径, 2026-11-23 第三次修正)**:
- 论文 gap_rate 是 **claim+evidence+corrected_claim 三字段混算** (compute_metacog 口径)
- 三字段混算: 现用平坦 (F=0.036), 扩展**随 budget 升** (0.39/0.41/0.44, F=1.02)
  → **pooled gap_rate 的 invariance 是 detector-scoped 的, 不 robust**
- claim 字段 (监控轴): 两检测器都平坦 (F=0.033/0.036)
  → **监控轴 invariance 是 detector-robust 的** — 这是论文可守的核心
- evidence 字段 (核验阶段): 扩展下随 budget 升 — 与 vsr budget trend 同向
- 我前两轮各错一次: 先说"不 robust" (没分解字段), 再说"robust" (把 claim 字段
  当成了论文口径) — 正确口径: pooled 不 robust, 监控轴 robust
- n=15 (5/tier) ANOVA 低功效: "平坦" = 未检出 budget 效应, 非证明 invariance
- draft §6 (ii) 已按此精确口径改写 (22-pattern, F=0.033/1.02, 字段分解)
- draft abstract + §4.3 provenance 同步补 detector-scoped 限定 (8d1d58464)

**Q6 监控轴跨域早期数据点 (2026-11-23, n=3/3/2, 低功效, 队列跑完再下结论)**:
Q6 claim 字段 (监控轴) gap_rate: 50 档 0.0733, 100 档 0.0033, 150 档 0.0167
- 现用/扩展检测器在 claim 字段完全一致 (Q6 claim 字段不含扩展 pattern)
- Q6 防御措辞主要在 evidence 字段 (pooled 扩展 0.36/0.21/0.22) — 与 GPU 字段分布同构 (87% evidence)
- Q6 监控轴水平 (0.07) 远低于 GPU (0.105/0.106/0.114), 且域内非平坦 (50→100 骤降)
- 含义: 监控轴 invariance 的跨域成立性存疑 — Q6 监控轴水平低 + 域内形状不同
- 待队列跑完 (150×3, 300×3, 719×3) 补全 Q6 全 budget 曲线再判定
- 注意: Q6 claim 字段 gap 极低可能因 Q6 题面更定量 (claim 多为数值, 防御措辞集中在
  evidence 的核验文本), 非模型监控能力差异 — 待 D 判断

**Q6 judge 轴跨 budget 早期数据点 (2026-11-23, n=3/3/2, 8/15 队列)**
- judge total: 50 档 0.305 (0.300/0.314/0.300) → 100 档 0.338 (0.400/0.314/0.300) → 150 档 0.414 (0.414/0.414)
- 单调升, 主驱动 = depth 阶梯 (0.6→0.8, 3-level step), cov 低 (0.009/0.009/0.028)
- 与 GPU K7 机械 depth 轴同向 (随 realized node count 升, 饱和于 max_depth=5)
- 含义: judge 轴的 budget 曲线跨域同形 (depth 驱动, cov 低) — 跨域不变性候选
- 待队列跑完补 300/719 档看是否饱和 (GPU 在 ~300 节点饱和)
- 评分块队列内静默失败 (python3 - heredoc stdin 被 SM 2>&1 影响), 已用 q6_rescore.py 补 8/8

**Q6 监控轴跨域不一致 (2026-11-23, n=3/3/3 补全, 重要)**
- Q6 claim 字段 gap_rate (8-pattern): 50 档 0.0733 (0.040/0.060/0.120) → 100 档 0.0033
  (0.000/0.010/0.000) → 150 档 0.0156 (0.000/0.033/0.013)
- GPU 对照 (同口径): 0.105 / 0.106 / 0.114 (平)
- 两个跨域不一致: ① Q6 水平远低于 GPU (0.07 vs 0.105) ② Q6 域内不平 (50 档后骤降)
- 含义: "监控轴 budget 不变性"目前只在 GPU 域成立, Q6 域不成立 — 跨域不变性声明
  需要降级或加域限定
- 可能机制: Q6 题面更定量 (claim 多为数值, 防御措辞集中在 evidence 字段), 50 档已
  够监控饱和 → 待 300/719 档确认 (若保持低位 = Q6 监控轴低水平非平, 跨域声明降级)
- 对 draft 影响: 监控轴不变性的跨域声明需等全曲线后决定 (降级为域内声明 / 加 Q6 例外)

**B4 域特异性 cov 分档验证 (2026-11-23, 9 run, b4_cov_only.py)**
- 域内 cov (Q6 runs × Q6 gold): 50 档 0.058 → 100 档 0.0725 → 150 档 0.087, **单调升**
- 跨域 cov (Q6 runs × GPU gold): **0.0000 全档** (Q6 对 GPU gold 零覆盖)
- diff 一致为正 (+0.058~+0.087)
- 结论: ① 域内 cov 复现 budget 响应 (升) → judge 轴 budget 响应是 general 的
  ② 跨域 cov 归零 → gold 域特异性, cov 绝对值不可跨域比
- 与 metacog 轴域偏对照: judge cov 跨域**直接归零** (彻底域特异), metacog pooled
  跨域是**水平偏移** (域偏 1.7x 但非零) — 两轴域特异性程度不同
- 注: b4_cross_domain_judge.py (完整版含 LLM depth) 超时 (bge-m3 CPU 加载慢),
  b4_cov_only.py 只算 cov 层 (机械匹配, 快) — 域特异性核心在 cov, depth 轴已用
  队列 scores 验证 (0.305→0.338→0.414)

**Finding (2) 难度梯度的字段分解 (2026-11-23, 强化论文)**
脚本: research/finding2-field-decomposition.py (固化, 复现下表)
口径: 与 finding2-difficulty-gradient-cleaned.py 完全一致 (sm-era, node.json 递归,
按 id/mtime 去重, 跳过 <20 节点, NO_UNCERTAIN 7-pattern 清洗)
| 域   | n_runs | pooled | claim  | evidence | ev%  |
|------|--------|--------|--------|----------|------|
| nat  | 21     | 0.0181 | 0.0162 | 0.0026   | 14%  |
| soc  | 26     | 0.0298 | 0.0261 | 0.0045   | 15%  |
| gpu  | 18     | 0.0999 | 0.0921 | 0.0089   | 9%   |
- claim 字段梯度 nat 0.0162 < soc 0.0261 < gpu 0.0921 **完整保持**
- claim 字段 Mann-Whitney: nat<soc z=-1.68 ns, soc<gpu z=-4.46 显著, nat<gpu z=-4.68 显著
  (与 pooled 清洗口径同构: nat<soc ns, 其余两环显著)
- evidence 字段贡献小 (9-15% of pooled)
**结论: finding (2) 难度梯度是监控轴 (claim 字段) 现象, 落在 detector-robust 的轴上**
- 与 budget-invariance 的字段分解互补: budget 效应主要在 evidence 字段 (核验阶段),
  难度效应主要在 claim 字段 (监控轴) — 两个 finding 落在不同字段, 不冲突
- 对 draft: finding (2) 可加一句 "the gradient is driven by the claim field
  (monitoring axis, 85-91% of pooled), not verification-stage text — it is
  detector-robust on the axis it measures"
- 承重脚本修复: finding2-difficulty-gradient-cleaned.py 的 ARCHIVE 路径少一层 ..
  (ZeroDivisionError), 已修 (8d1d58464 之前的 commit 待补)

**真正的新发现 (扩展检测器揭示, 监控轴之外的 budget 效应)**:
- 核验阶段防御文本 (evidence 字段) 随 budget **上升**: 0.39/0.41/0.44 (100/150/300)
- 含义: 更多 budget → 更多"来源不支持/无法验证"的核验文本 → 更多 degraded 节点
- 与 vsr budget trend (−0.47)、search ver% 随深度降 (9.4→0.0%) 同向 —
  breadth-not-depth 的又一个独立维度 (核验质量随 budget 降)
- 这其实**强化**论文: 监控轴 (a) 是 budget-invariant 的 (模型"知道自己不知道"的
  比率不随 budget 变), 但核验轴 (b/c) 随 budget 降 (更多 budget 搜到更难验证的来源)
- 对 draft: line 146 (ii) "invariance 不受影响" 结论对, 但理由要改 —
  不是"bias 跨 tier 恒定", 而是"监控轴 (claim 字段) 在扩展检测器下仍平坦 (F=0.033)";
  并加新 finding: 核验阶段文本 (evidence) 随 budget 升 (0.39→0.44), 是 breadth-not-depth
  的第 5 个独立维度

## Q6 300-r2 数据点 (2026-11-23 20:01, 队列 11/15)

- **judge 轴**: 300 档 n=2 → 0.400/0.442, mean 0.421 (depth 0.8/0.8, cov 0.0/0.083)。
  全曲线 n=3/3/3/2: 0.305→0.338→0.409→0.421 单调升, depth-step 驱动 (0.6→0.8 后饱和),
  与 GPU K7 机械 depth 轴同向。300 档 n=2, suggestive。
- **监控轴 (claim field, 8-pattern)**: 300-r2 = 0.0300 (9/300), 300 档 mean 0.0233 (n=2)。
  全曲线: 50=0.0733 → 100=0.0033 → 150=0.0156 → 300=0.0233 (n=3/3/3/2)。
  模式确认: 低水平 + 50 档后骤降, 与 GPU 0.105/0.106/0.114 (flat) 不同 →
  监控轴 budget-invariance 目前仍 GPU-only。
- 队列剩 300-r3 + 719×3 (约 2h), 完成后做全曲线 + draft §7 跨域段。
