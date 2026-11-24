# Claim Inventory — workshop-draft-metacog-20261122.md (2026-11-24)

> 用途：为 18K→3.5–6K 词压缩 pass 做准备。只读分析，不改 draft。
> 来源：全文逐行读（254 行 / 122,376 字符 / ~18,085 词），承重判定基于"审稿人打这一刀是否动摇全文结论"。
> 承重 = 删了会动摇主结论/主方法；非承重 = 支撑性/背景/细节/诊断。
> 行号 = draft 内 1-indexed 行。同一承重数字多处出现时，「数字」列列出全部行号（压缩时至少保留 1 处正文可见）。
> 词数基线（压缩前，按节）：Abstract 1280 / §1 476 / §2 877 / §3 810 / §4.1 874 / §4.2 624 / §4.3 4180 / §4.4 2443 / §5 355 / §6 2709 / §7 2828 / §8 134 / §9 458。合计 ~18,085 词。

## 0. 承重数字总览（context 给定的承重集，逐一核对落点）

| 承重数字 | draft 内出现行号 | 是否已在正文 | 备注 |
|---|---|---|---|
| 断点 325 (Q6) | L9, L133, L137, L222 | 是 | 16-pt F(2,12)=7.33 p=0.008；18-pt F(2,14)=2.73 p=0.10 |
| 断点 475 (GPU) | L9, L137 | 是 | F(2,26)=2.88 p=0.074 |
| 阈值 0.3185 (cosine 0.70) | L30, L198, L199 | 是 | judge_v1 COS_THRESHOLD=0.70 口径 |
| n=3 cov 0.1304/0.2391/0.2174 (719 realized) | L40, L119, L121, L129, L133, L137, L220, L222 | 是 | 三处正文重复，压缩至少留 1 处 |
| 1.21× se (se_diff=0.0360) | L9, L40, L121, L131, L133, L137, L222 (0.0360 仅 L131) | 是 | 0.0360 只在 L131 出现一次 |
| pooled cor=0.8053 t=5.432 df=16 | L133 | 是 | 仅 L133 |
| marginal yield r1=−0.0109 r2=+0.0435 r3=+0.0326 | L137 (r2 +0.0435 另见 L9,L129) | 是 | r1/r3 只在 L137 |
| 三方 hit-set 核心 5 units {0,8,14,21,25} | L121 | 是 | 仅 L121 |
| 净增益 2 units (16 稳定, 20 r2-only) | L121 | 是 | 仅 L121 |
| merge 消融 concat=0.4129 vs merge=0.4261 | **absent** | 否 | **draft 中不存在**（0.4129/0.4261/concat/merge 均未出现） |
| 阈值梯度 0.65→0.496 / 0.70→0.3185 / 0.75→0.098 / 0.80→0.015 / 0.85→0.000 | L30, L198 | 是 | 全梯度在 L30；L198 有 0.65/0.70/0.75/0.80 四档 |
| 断点 325 (17pt tie, F(2,13)=2.934 p=0.0888) | **absent** | 否 | draft 用 16-pt F(2,12)=7.33 与 18-pt F(2,14)=2.73；无 17-pt/F(2,13)/2.934/0.0888 |

> **关键缺口**：context 列的 merge 消融 (0.4129/0.4261) 与 17-pt-tie F(2,13)=2.934 两个承重数字**不在本 draft 内**。若压缩 pass 需要保留它们，须先确认是否遗漏（可能属 supplementary 或另一文件），否则按"本 draft 无此数"处理。
>
> **行号核验（2026-11-24，来源 ① grep 当前 draft）**：§7 区行号因 draft 当日修订有漂移——原 §0 引用的 L219/L221 已失效（L221 现为空行），实际数据落在 **L220**（"From per-domain foundation" 段，含 n=3 cov）与 **L222**（Data note 段，含 0.1304/0.2391/0.2174、1.21×、325）。本表已按当前行号修正。merge 0.4129/0.4261 与 17-pt F(2,13)=2.934 经 grep 确认**确实 absent**（F(2,13)/2.934/0.0888 全文无匹配；L129 的 "17pt" 仅指 17-point snapshot 文件名，非断点）。
>
> **§4 压缩热点（2026-11-24 核验）**：§4 共 84 条 claim，**无真重复行**（每行一条独立 claim；同 token 命中多为"同一巨型段多 claim"或"不同数共享 token"，如 0.047 gap_rate≠0.047 partial-cor、0.008 p≠0.008 spread）。压缩 pass 优先处理 claim 密度最高的源行：**L51（8 claim，rework 机制段）与 L137（8 claim，breakpoint/plateau 段）** 各占 §4 词数大头，其次 L101/L105/L177（各 4）。这些行的 claim 都承重、不可删，但可在 draft 正文合并表述（inventory 保留逐条锚点供回溯）。

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

### §4.1 Monitoring is present; repair is low-yield (L47–L65)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §4.1 | L49 | healthy_gap_rate mean 0.938 (0.667–1.0); 93.5% unverifiable not contradicted (84% incl. ambiguous) | 0.938, 93.5%, 84% | 是 | Finding 1 核心（监控健康） |
| §4.1 | L51 | rework loop fixes only 1.6–2.1% of reworked nodes (36/2298 budget-scan, 61/2919 era-matched) | 1.6–2.1%, 36/2298, 61/2919 | 是 | Finding 1 低收益核心 |
| §4.1 | L51 | event-level dry-run 80-run corpus: no_source 4.0% / value_mismatch 2.4% / other 2.8% / global 3.1% (10,702 attempts) | 4.0%, 2.4%, 2.8%, 3.1%, 10702 | 是 | 低收益分解，承重 |
| §4.1 | L51 | node-level (rework_count>0) fix rate 3.7% (331/8870) | 3.7%, 331/8870 | 是 | 承重数字（8,870 节点） |
| §4.1 | L51 | no_source fix rate higher than value_mismatch → mis-targeting hypothesis rejected | 4.0% > 2.4% | 是 | 机制判断，承重 |
| §4.1 | L51 | directed-fix path structurally unreachable, never executed (0/8,870 node-level rework events) | 0/8870 | 是 | 瓶颈定位，承重 |
| §4.1 | L51 | Q6 batch: 72.6% of 621 reworked nodes carry substantively different corrected_claim | 72.6%, 621 | 是 | 证伪"模型不改claim" |
| §4.1 | L51 | rework_count=1 for all 8,870 reworked nodes (621 Q6 / 139 Q7); pool holds only current round | 8870, 621, 139 | 是 | 单次尝试设计，承重 |
| §4.1 | L51 | repair overwrites claim only when re-verification returns verified (L821); else sits in corrected_claim unscored | L821 | 否 | 测量缺口细节 |
| §4.1 | L53 | **Claim**: metacognitive breakpoint is the repair loop, not monitoring; loop is mark→retrieve→classify | 3.1% global | 是 | §4.1 主 claim |
| §4.1 | L55-61 | two gap mechanisms: search-source vs knowledge-source (GPU 331/235/89 27%, nat 89/41/45 51%, soc 299/162/135 45%) | 331/235/89, 89/41/45, 299/162/135 | 否 | 机制细分，支撑 |
| §4.1 | L63 | knowledge-source gaps 27–51% of all gap nodes, all 3 domains; 47–59% carry search_query vs 18–40% non-gap | 27–51%, 47–59%, 18–40% | 否 | within-source (a)→(b) 细节 |
| §4.1 | L65 | claim-field gap→search trigger: 79/64/67% (GPU/NAT/SOC) vs 44/23/49% non-gap (z=+12.47/+9.40/+7.23, all p<0.001) | 79/64/67, 44/23/49 | 是 | Finding 1 触发链核心 |
| §4.1 | L65 | within-source (a)→(b) effect +12 to +30 pp; trigger is a gradient not binary | +12 to +30 pp | 否 | 梯度细化 |
| §4.1 | L65 | [待核验] tag is the trigger: tagged 66%/60% vs untagged 14%/0% (z=+3.63/+3.52; pooled 59% vs 44%, z=+2.96) | 66%/60%, 14%/0%, 59% vs 44% | 否 | prompt-elicitation 证据 |
### §4.2 Gap marking is difficulty-calibrated (L67–L81)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §4.2 | L73-75 | era-matched gap_rate rises with difficulty: nat 0.0254 < soc 0.0562 < gpu 0.1193 (raw) | 0.0254, 0.0562, 0.1193 | 是 | Finding 2 核心梯度 |
| §4.2 | L73-75 | cleaned gap_rate: nat 0.0181 < soc 0.0298 < gpu 0.0999 (n=21/26/18) | 0.0181, 0.0298, 0.0999 | 是 | 清洗后梯度（主口径） |
| §4.2 | L79 | Kruskal–Wallis H=37.8, p<0.0001 (raw detector) | H=37.8, p<0.0001 | 是 | 显著性核心 |
| §4.2 | L79 | nat<soc step drops to ns under cleaned detector (z=−1.82); robust core is gpu end | z=−1.82 | 是 | 梯度稳健性边界 |
| §4.2 | L79 | field decomposition: gradient carried by claim field (nat 0.0162 < soc 0.0261 < gpu 0.0921); evidence field only 9–15% | 0.0162, 0.0261, 0.0921 | 是 | 监控轴定位，承重 |
| §4.2 | L79 | correction: gpu 0.1193 (n=19) not 0.1469 — 0.1469 not reproducible from current corpus | 0.1193, 0.1469 | 否 | 数据修正记录 |
| §4.2 | L81 | within soc, gap_rate correlates with node count (ρ=0.488, p=0.010) — part may be budget effect | ρ=0.488, p=0.010 | 否 | 边界 caveat |
| §4.2 | L81 | K7 budget scan gap_rate non-monotonic (50→0.064, 100→0.134, 150→0.047, 300→0.075, 719→0.081) | 0.064/0.134/0.047/0.075/0.081 | 否 | 预算效应独立于难度 |
### §4.3 Budget–quality is flat-to-weakly-non-monotonic (L83–L155)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §4.3 | L89-93 | depth score by nominal tier: 50→0.3842, 100→0.4352, 150→0.4743, 300→0.4275, 719→0.4376 | 0.3842/0.4352/0.4743/0.4275/0.4376 | 是 | 150 peak 主表 |
| §4.3 | L97-101 | depth values from LLM rubric judge (judge_v2_depth), same-model self-bias; not mechanical judge_v1 | judge_v2_depth | 是 | provenance 关键（自偏轴） |
| §4.3 | L101 | mechanical judge_v1 depth = 3-level step (30 trees: 12@0.6, 16@0.8, 2@1.0); no nominal-tier discrimination at n=3 | 12/16/2, 0.667 | 否 | 机械轴细节 |
| §4.3 | L101 | rep-scan (n=8/tier): tier means 0.625/0.725/0.800 at 100/150/300, 719=0.933; depth~n_nodes r=+0.944, n=30 | 0.625/0.725/0.800, 0.933, r=+0.944 | 是 | 机械深度承重 |
| §4.3 | L101 | mechanical depth saturates at max_depth=5 (~n=665); extra budget buys nodes not depth steps | ~n=665 | 是 | breadth-vs-depth 承重 |
| §4.3 | L101 | control arm: LLM answer-depth vs mechanical tree-depth cor=+0.049 (t=0.18, p≈0.86); flat 0.431/0.430/0.441 | +0.049, p≈0.86 | 是 | 证伪 peak 共享 |
| §4.3 | L105 | verbosity bias: LLM depth vs answer length cor=+0.648 (t=+3.07, df=13, p<0.01); partial +0.641 | +0.648, p<0.01 | 是 | 机制解释 peak |
| §4.3 | L105 | LLM↔budget vanishes controlling length (partial +0.047 vs raw +0.135) | +0.047, +0.135 | 是 | 机制解释 peak |
| §4.3 | L105 | 150-tier "peak" (0.474/0.518) coincides with two longest answers (24770/24197 chars) | 0.474/0.518, 24770/24197 | 否 | verbosity 细节 |
| §4.3 | L105 | robustness: Spearman ρ=+0.681 (p=0.005); dropping 2 longest/shortest leaves r≈+0.64–0.67 | ρ=+0.681, p=0.005 | 否 | 稳健性细节 |
| §4.3 | L109 | coverage rise-to-plateau: 0.259/0.264/0.278/0.358/0.352 at 50/100/150/300/719 | 0.259/0.264/0.278/0.358/0.352 | 是 | 机械轴主曲线 |
| §4.3 | L111 | pooling provenance: 300=(0.426×3+0.317×5)/8=0.358; K7-only 0.426, rep-scan-only 0.317 | 0.426, 0.317, 0.358 | 否 | pooling 细节 |
| §4.3 | L113 | cor(cov, n_nodes)=+0.602 (t=+2.72, df=13, p≈0.019); re-verified r=+0.601, t=+2.71 | +0.602, p≈0.019 | 是 | 承重（size-confounded） |
| §4.3 | L113 | K7 bookkeep off-by-one: bookkeep rN matches archive r(N+1); per-run n_nodes misaligned | off-by-one | 否 | 数据修正记录 |
| §4.3 | L117 | Q6 coverage different shape: 0.058/0.073/0.087/0.138/0.167 at 50/100/150/300/719; still rising at 719 (Δ=+0.029) | 0.058/0.073/0.087/0.138/0.167 | 是 | 跨域对比承重 |
| §4.3 | L117 | Q6 719 tier wall-bound (realized 197/351/379, max_depth=4); lexical-novelty 0.889–0.909, frontier 54–94 nodes | 197/351/379, 0.889–0.909 | 否 | wall-bound 细节 |
| §4.3 | L119 | wall-free 719 batch (n=3/3): cov 0.1304 (r1), 0.2391 (r2), 0.2174 (r3); r1 below 0.167, r2/r3 above 0.1957 | 0.1304, 0.2391, 0.2174 | 是 | 承重数字（n=3 cov） |
| §4.3 | L121 | spread 0.109 = 3.3× orig batch sd (0.033); 719 magnitude open at n=3, leans rising (2/3 above max) | 0.109, 3.3×, 0.033 | 是 | n=3 开放声明 |
| §4.3 | L121 | hit-set control: r1 (6 units) strict subset of orig-r2 (9 units); r1∩r2=5/6, r3∩r2=9/10, r3∩r1=5/6 | 6/9, 5/6, 9/10 | 否 | 机制 hit-set 细节 |
| §4.3 | L121 | three wall-free reps share 5-unit three-way core {0,8,14,21,25}, pairwise overlap 5–9 | {0,8,14,21,25} | 是 | 三方 hit-set 核心（承重） |
| §4.3 | L121 | net gain beyond orig union = 2 units (static-request price, self-built fixed cost); only former stable (r2+r3), latter r2-only → cov reversal is unit-level run-to-run exchange, not systematic depth effect | 2 units, r2-only | 是 | 净增益机制（承重，防过度解读 719 reversal） |
| §4.3 | L125 | cross-domain confound: GPU pre-clamp (soft cap) vs Q6 post-clamp (hard cap), max_depth 5 vs 4 | pre-clamp, post-clamp | 否 | 跨域 confound caveat |
| §4.3 | L129 | 600–800-node bin mean 0.1956 (n=3) above 200–400-node bin 0.1522 by +0.0435 | 0.1956, 0.1522, +0.0435 | 是 | 承重数字（bin 对比） |
| §4.3 | L131 | +0.0435 = 1.21× pooled se (0.0360); marginally resolvable at n=3, not conventionally significant | 1.21×, 0.0360 | 是 | 承重（se 倍数） |
| §4.3 | L133 | pooled cor(cov, realized)=+0.805 (18 pts, t=5.43, df=16); 600–800 bin n=3 sd 0.0575 | +0.805, t=5.43, 0.0575 | 是 | 承重（pooled cor） |
| §4.3 | L133 | GPU plateau (30-tree bins 0-200:0.250 / 200-400:0.325 / 400-600:0.361 / 600-800:0.361) as n=30 reference | 0.250/0.325/0.361/0.361 | 是 | GPU plateau 参考 |
| §4.3 | L137 | pre-computation falsified by r2 (0.2391 outside 0.1304–0.1957 range, 1.3× sd above max) | 0.2391, 1.3× | 否 | 预计算证伪记录 |
| §4.3 | L137 | stopping state universal: high novelty (0.86–0.958), non-empty frontier (24–252), low_gain_streak=0 at every stop | 0.86–0.958, 24–252 | 否 | 停止态细节 |
| §4.3 | L137 | marginal coverage yield declines past ~400 nodes; 200–400 bin yield GPU +0.0748 / Q6 +0.0739 per 200 nodes | +0.0748, +0.0739 | 是 | 承重（marginal yield） |
| §4.3 | L137 | breakpoint scan: Q6 F(2,12)=7.33 p=0.008 (16-pt) → F(2,14)=2.73 p=0.10 (18-pt); GPU F(2,26)=2.88 p=0.074; optima 475 (GPU)/325 (Q6) | 7.33, 0.008, 2.73, 0.10, 2.88, 0.074, 475, 325 | 是 | 断点位置承重（核心） |
| §4.3 | L137 | 400–600 bin yield halves (GPU +0.0363/200, Δ/se=1.12×); 600–800 bin GPU 0.0000/200; Q6 r1 −0.0109, r2 +0.0435, r3 +0.0326 | +0.0363, 0.0000, −0.0109, +0.0435, +0.0326 | 是 | marginal yield 承重（r1/r2/r3） |
| §4.3 | L137 | plateau = slope collapse not flat top; robust claim is direction (yield declines past ~400), not sharpness | slope collapse | 是 | 主 claim 措辞 |
| §4.3 | L137 | breadth-without-depth scoped to marginal high-budget regime (past ~400: novelty high, marginal cov ~0) | past ~400 | 是 | headline 定位 |
| §4.3 | L137 | GPU final-round gain vs total coverage cor=+0.505 (t=+3.09, df=28, p<0.01); pooled −0.299 = Simpson's paradox | +0.505, p<0.01, −0.299 | 否 | 机制细节 |
| §4.3 | L141-145 | gap_rate 0.099/0.100/0.107 across 100/150/300; between-tier spread 0.008 = 6.5× smaller than within-group sd 0.054 | 0.099/0.100/0.107, 0.008, 6.5×, 0.054 | 是 | 预算不变性核心 |
| §4.3 | L145 | ANOVA F(2,12)=0.036 (p≫0.05); cleaned detector F(2,12)=0.003 (closer to zero) | F(2,12)=0.036, 0.003 | 是 | 预算不变性 null 承重 |
| §4.3 | L149 | detector-scoped: pooled invariance holds under 8/7-pattern but not 22-pattern (rises 0.39/0.41/0.44, F=1.02); claim-field flat (F=0.033) | 0.39/0.41/0.44, F=1.02, 0.033 | 否 | detector-scoped caveat |
| §4.3 | L153 | provenance: rep-scan pre-clamp (soft cap); gap_rate vs realized cor=−0.034 (t=−0.12, ns); invariance holds vs realized compute | −0.034, t=−0.12 | 否 | provenance caveat |
| §4.3 | L153 | metacog total flat-to-mildly-declining (0.246/0.247/0.232); retrieval_rate blind to channel outages (r7: 97 tags, 3 URLs) | 0.246/0.247/0.232 | 否 | 测量盲点细节 |
| §4.3 | L155 | 150 "peak" = 0.9 run-sd above plateau (0.041 vs sd 0.046) — suggestive not significant at n=3; dropping 300-r3 (0.3516) moves 300 to 0.465 | 0.9 run-sd, 0.041, 0.046, 0.3516 | 是 | 150 peak 稳健性 |
| §4.3 | L155 | breadth-vs-depth split: GPU 103–747 realized nodes, mechanical depth rises 0.625→0.800 then holds; agent spreads sideways not down spine | 103–747, 0.625→0.800 | 是 | breadth claim 承重 |
### §4.4 Failure modes and continuity (per-layer anatomy) (L157–L185)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §4.4 | L163-167 | per-layer status 30 trees (8,767 nodes): L1 162 / L2 855 / L3 2759 / L4 4230 / L5 761; ver% 6.8/42.6/48.1/52.7/58.2% | 8767, 162/855/2759/4230/761 | 否 | 解剖表，支撑 |
| §4.4 | L169 | knowledge share rises with depth (52% L2 → 68% L4); ver% differs by source ~20× (knowledge 74.4% / search 3.2%) | 52%→68%, 74.4%, 3.2% | 是 | source-mix confound 核心 |
| §4.4 | L174 | obs 1: verification rate source-determined not depth-determined; standardized ver% flat (42.6/41.0/41.9/42.3%) | 42.6/41.0/41.9/42.3% | 是 | 深度非验证悬崖 |
| §4.4 | L174 | search-node ver% declines with depth (9.4/4.6/0.9/0.0% L2→L5); deeper retrieved claims verify less | 9.4/4.6/0.9/0.0% | 是 | 真实深度效应（检索通道） |
| §4.4 | L175 | obs 2: L4 conclusion layer absent in 12/30 trees; absence budget-dependent (50→2/3, 100→7/8, 150→3/8, 300→0/8, 719→0/3) | 12/30, 2/3/7/8/3/8/0/8/0/3 | 是 | 结论层缺失承重 |
| §4.4 | L175 | once L4 grows (18 trees), all 18/18 have ≥1 verified L4 node; chain break is depth not verification | 18/18 | 是 | 机制定位（depth 非 verification） |
| §4.4 | L176 | obs 3: loop continuous not cumulative; rework does not repair 45.5% failing nodes (9,984/21,945, 160-tree corpus) | 45.5%, 9984/21945 | 是 | 非累积承重 |
| §4.4 | L176 | metacognitive loop = filter (mark+retrieve+classify), not repair cycle (mark→fix→re-verify) | filter not repair | 是 | 主 claim 措辞 |
| §4.4 | L177 | obs 4: 0/15 final recommendations match gold winner (4× RTX 3090/W4/n=2); "3090×4" never appears (0/15) | 0/15, 3090×4 | 是 | L4 zero-convergence 核心 |
| §4.4 | L177 | "3090" alone in 15/15 runs; final recommendation line 2/15 (as 2× or single, never 4-card winner) | 15/15, 2/15 | 是 | 知道候选不 commit |
| §4.4 | L177 | zero-convergence holds at every budget tier; budget buys more nodes not more stable answer | every tier | 是 | Finding 3 主 claim |
| §4.4 | L177 | idea-2 arm (n=6): strict winner commits 0/6, loose "3090 in conclusion" 0/6; "3090" in 4/6 full-text (candidate not conclusion) | 0/6, 0/6, 4/6 | 是 | 跨数据集验证 |
| §4.4 | L179 | bare-arm control (n=6, SM off): 0/6 reach L4 (max_depth 2–3; 5 at depth 3, 1 at depth 2) | 0/6, 2–3 | 是 | capability bottleneck 证据 |
| §4.4 | L179 | bare gpu run recommends 1× RTX 5090, 3090 only as 2× fallback → 0/1 gold commit; breakage not SM artifact | 0/1 | 是 | 证伪 prompt artifact |
| §4.4 | L179 | SM value = makes breakage measurable (per-node status, rework events, evidence), not prevents it | measurable | 否 | 价值定位 |
| §4.4 | L181 | cross-domain degeneration (T-PUB-1, n=35): Q04 2/5 runs deterministic loop (390-char ×45, ×90); detector 5/5 correct | 2/5, 390×45, 5/5 | 是 | 跨域退化观察（承重） |
| §4.4 | L181 | degeneration Q04-specific (2/35; zero on other 6 questions); triggered by multi-subquestion + ambiguity | 2/35 | 否 | 触发条件细节 |
| §4.4 | L183 | predicted fix: no_source (4.0%) outperforms value_mismatch (2.4%); falsifiable branch = path reachability not targeting | 4.0%, 2.4% | 是 | 修复预测承重 |
| §4.4 | L185 | obs 5: self-report calibrated in direction weak in strength; verified 0.78 (n=9 ns), degraded 0.56 (n=191), pending 0.55 (n=20) | 0.78, 0.56, 0.55 | 否 | 校准细节 |
| §4.4 | L185 | 56% of degraded-marked nodes still have claimed number on cited page; under-claiming not over-claiming | 56% | 否 | 校准方向细节 |
<!-- CHUNK2_S4_END -->
