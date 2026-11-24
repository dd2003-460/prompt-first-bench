# Claim Inventory — workshop-draft-metacog-20261122.md (2026-11-24)

> 用途：为 18K→3.5–6K 词压缩 pass 做准备。只读分析，不改 draft。
> 来源：全文逐行读（254 行 / 122,376 字符 / ~18,085 词），承重判定基于"审稿人打这一刀是否动摇全文结论"。
> 承重 = 删了会动摇主结论/主方法；非承重 = 支撑性/背景/细节/诊断。
> 行号 = draft 内 1-indexed 行。同一承重数字多处出现时，「数字」列列出全部行号（压缩时至少保留 1 处正文可见）。
> 词数基线（压缩前，按节）：Abstract 1280 / §1 476 / §2 877 / §3 810 / §4.1 874 / §4.2 624 / §4.3 4180 / §4.4 2443 / §5 355 / §6 2709 / §7 2828 / §8 134 / §9 458。合计 ~18,085 词。

## 0. 承重数字总览（context 给定的承重集，逐一核对落点）

| 承重数字 | draft 内出现行号 | 是否已在正文 | 备注 |
|---|---|---|---|
| 断点 325 (Q6) | L9, L133, L137, L221 | 是 | 16-pt F(2,12)=7.33 p=0.008；18-pt F(2,14)=2.73 p=0.10 |
| 断点 475 (GPU) | L9, L137 | 是 | F(2,26)=2.88 p=0.074 |
| 阈值 0.3185 (cosine 0.70) | L30, L198, L199 | 是 | judge_v1 COS_THRESHOLD=0.70 口径 |
| n=3 cov 0.1304/0.2391/0.2174 (719 realized) | L40, L119, L121, L129, L133, L137, L219, L221 | 是 | 三处正文重复，压缩至少留 1 处 |
| 1.21× se (se_diff=0.0360) | L9, L40, L121, L131, L133, L137, L221 (0.0360 仅 L131) | 是 | 0.0360 只在 L131 出现一次 |
| pooled cor=0.8053 t=5.432 df=16 | L133 | 是 | 仅 L133 |
| marginal yield r1=−0.0109 r2=+0.0435 r3=+0.0326 | L137 (r2 +0.0435 另见 L9,L129) | 是 | r1/r3 只在 L137 |
| 三方 hit-set 核心 5 units {0,8,14,21,25} | L121 | 是 | 仅 L121 |
| 净增益 2 units (16 稳定, 20 r2-only) | L121 | 是 | 仅 L121 |
| merge 消融 concat=0.4129 vs merge=0.4261 | **absent** | 否 | **draft 中不存在**（0.4129/0.4261/concat/merge 均未出现） |
| 阈值梯度 0.65→0.496 / 0.70→0.3185 / 0.75→0.098 / 0.80→0.015 / 0.85→0.000 | L30, L198 | 是 | 全梯度在 L30；L198 有 0.65/0.70/0.75/0.80 四档 |
| 断点 325 (17pt tie, F(2,13)=2.934 p=0.0888) | **absent** | 否 | draft 用 16-pt F(2,12)=7.33 与 18-pt F(2,14)=2.73；无 17-pt/F(2,13)/2.934/0.0888 |

> **关键缺口**：context 列的 merge 消融 (0.4129/0.4261) 与 17-pt-tie F(2,13)=2.934 两个承重数字**不在本 draft 内**。若压缩 pass 需要保留它们，须先确认是否遗漏（可能属 supplementary 或另一文件），否则按"本 draft 无此数"处理。

## 1. 承重 claim 明细表（按节）

### Abstract (L7–L9)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| Abstract | L9 | 27B on 4×V100, no weight updates, compute constraint | 27B, 4×V100 | 是 | 实验条件，全文 scope 锚点 |
| Abstract | L9 | metacognition axis validated across 3 domains, 83 runs | 3 domains, 83 runs | 是 | 方法有效性核心声明 |
| Abstract | L9 | Q6 719 point leans still-rising at n=3 | n=3 | 是 | 主结果之一，方向性 |
| Abstract | L9 | 600–800 bin 0.1956 vs 200–400 bin 0.1522, Δ+0.0435=1.21× pooled se | 0.1956, 0.1522, +0.0435, 1.21× | 是 | 承重数字，多处重复 |
| Abstract | L9 | Q6 breakpoint bp=325, F(2,12)=7.33 p=0.008 (16-pt) | 325, F(2,12)=7.33, p=0.008 | 是 | 断点位置，承重 |
| Abstract | L9 | 18-pt scan bp=325 F(2,14)=2.73 p=0.10 ns | F(2,14)=2.73, p=0.10 | 是 | 断点弱化，承重 |
| Abstract | L9 | GPU breakpoint 475 | 475 | 是 | 断点位置，承重 |
| Abstract | L9 | 104 unique runs (83+6+15, K7 subset) | 104, 83, 6, 15 | 是 | 样本量声明 |
| Abstract | L9 | healthy gap rate 93.5% (84% incl. ambiguous) | 93.5%, 84% | 是 | Finding 1 核心 |
| Abstract | L9 | claim-field gap→search 79/64/67% vs 44/23/49% | 79/64/67, 44/23/49 | 是 | Finding 1 触发链 |
| Abstract | L9 | rework fixes 1.6–2.1% (3.7% node global / 3.1% event) | 1.6–2.1%, 3.7%, 3.1% | 是 | Finding 1 低收益核心 |
| Abstract | L9 | tree grows around 52.5% unverified (5,630/10,730) | 52.5%, 5630/10730 | 是 | 支撑 repair 失败 |
| Abstract | L9 | difficulty gradient nat 0.025<soc 0.056<gpu 0.119 | 0.025, 0.056, 0.119 | 是 | Finding 2 核心 |
| Abstract | L9 | L4 zero-convergence 0/21 strict | 0/21 | 是 | Finding 3 主 claim |
| Abstract | L9 | bare-arm 0/6 reach conclusion layer | 0/6 | 是 | capability bottleneck 证据 |
| Abstract | L9 | repetition-degeneration caught 5/5 | 5/5 | 是 | Finding 3 跨域观察 |
| Abstract | L9 | realized nodes 103–747 | 103–747 | 是 | 有效 x 轴声明 |
| Abstract | L9 | depth peak 150=0.474, plateau 0.428–0.438 | 0.474, 0.428–0.438 | 否 | 自偏轴弱信号，已 caveat |
| Abstract | L9 | control arm cor=+0.049 (t=0.18, p≈0.86) | +0.049, p≈0.86 | 是 | 证伪 peak 共享 |
| Abstract | L9 | verbosity bias cor=+0.648 p<0.01, partial +0.047 | +0.648, p<0.01, +0.047 | 是 | 机制解释 peak |
| Abstract | L9 | ANOVA F(2,12)=0.036 p≫0.05 (metacog invariance) | F(2,12)=0.036 | 是 | 预算不变性 null |
| Abstract | L9 | gap_rate 0.134/0.047/0.075 (K7 era) | 0.134/0.047/0.075 | 否 | era-scoped 细节 |
| Abstract | L9 | checkpoint: A>B 3/3 reps, vsr 0.66 vs 0.46 | 3/3, 0.66, 0.46 | 是 | Finding 4 核心 |

### §1 Introduction (L13–L23)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §1 | L17 | Qwen3-27B NVFP4 on 4×V100, no weight mod | 27B, 4×V100 | 是 | scope 锚点（与 Abstract 重复） |
| §1 | L20 | metacognition axis validated 3 domains, 83 runs | 3, 83 | 是 | 与 Abstract 重复 |
| §1 | L21 | L4 zero-convergence 0/21 at every tier | 0/21 | 是 | 与 Abstract/§4.4 重复 |

### §2 Setup (L24–L35)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §2 | L26 | gpu gold = 37-node decomposition tree | 37-node | 是 | gold 规模，方法基础 |
| §2 | L28 | budget 50/100/150/300/719, soft cap, realized overlap | 50/100/150/300/719 | 是 | 实验设计核心 |
| §2 | L28 | realized 103–423/123–314/122–392/364–415/381–747 | 103–423…381–747 | 是 | 有效 x 轴，承重 |
| §2 | L30 | cosine ≥ 0.70, bge-m3, per-unit dedup | 0.70 | 是 | 阈值口径，承重 |
| §2 | L30 | magnet rule removed (401-node 0.0 vs 316-node 0.22) | 401, 0.0, 316, 0.22 | 否 | 诊断细节 |
| §2 | L30 | 0/4 idea-2 trees share variable | 0/4 | 否 | mech 层 infeasible 细节 |
| §2 | L30 | Composite = 0.5·depth + 0.5·coverage | 0.5/0.5 | 是 | 合成口径 |
| §2 | L30 | threshold sweep 0.65→0.496/0.70→0.3185/0.75→0.098/0.80→0.015/0.85→0.000 | 0.496/0.3185/0.098/0.015/0.000 | 是 | 承重数字（阈值梯度） |
| §2 | L30 | ±0.05 window moves cov 0.18–0.22 | 0.18–0.22 | 是 | 阈值敏感性 |
| §2 | L30 | gold perturbation 10% moves cov ≤0.0215 (sd 0.0926) | 0.0215, 0.0926 | 是 | 形状稳健性 |
| §2 | L30 | cor(cov,n_nodes) 0.601→0.641 under perturbation | 0.601→0.641 | 是 | 形状稳健 |
| §2 | L32 | 60.6% of 2196 search nodes no URL | 60.6%, 2196 | 是 | retrieval 上界 caveat |
| §2 | L32 | ~20% suspected false search tags, lower bound 0.8× | 20%, 0.8× | 否 | 上界细节 |

### §3 Related work (L36–L44)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §3 | L39 | RSI: 45.6% accepts are degradations, gates→2.8% | 45.6%, 2.8% | 否 | 背景引用（arXiv:2611.10787） |
| §3 | L40 | Q6 wall-free reps cov 0.1304/0.2391/0.2174, 1.21× se | 0.1304/0.2391/0.2174, 1.21× | 是 | novelty 防御 + 承重数字 |
| §3 | L40 | GPU plateaus ~400 realized nodes | ~400 | 是 | 承重（plateau 位置） |
| §3 | L40 | Q6 rising ≤379 realized, open at n=3 | ≤379, n=3 | 是 | 跨域对比承重 |
| §3 | L41 | self-preference: 20 models, near-chance self-recognition | 20 | 否 | 背景引用 |
| §3 | L43 | snowball T-PR-17: no prior fixed-SM-checkpoint+metacog | — | 是 | novelty 防御（handoff 近邻） |

<!-- CHUNK1_END -->
