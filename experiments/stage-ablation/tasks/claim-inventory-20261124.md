# Claim Inventory — workshop-draft-metacog-20261122.md (2026-11-24)

> 用途：为 18K→3.5–6K 词压缩 pass 做准备。只读分析，不改 draft。
> 来源：全文逐行读（254 行 / 122,376 字符 / ~18,085 词），承重判定基于"审稿人打这一刀是否动摇全文结论"。
> 承重 = 删了会动摇主结论/主方法；非承重 = 支撑性/背景/细节/诊断。
> 行号 = draft 内 1-indexed 行。同一承重数字多处出现时，「数字」列列出全部行号（压缩时至少保留 1 处正文可见）。
> 词数基线（压缩前，按节）：Abstract 1280 / §1 476 / §2 877 / §3 810 / §4.1 874 / §4.2 624 / §4.3 4180 / §4.4 2443 / §5 355 / §6 2709 / §7 2828 / §8 134 / §9 458。合计 ~18,085 词。
> **覆盖状态（2026-11-24 补全）**：明细表已覆盖 Abstract→§9 全部节，共 **194 条 claim**（Abstract 23 / §1 3 / §2 13 / §3 6 / §4.1 15 / §4.2 8 / §4.3 41 / §4.4 20 / §5 10 / §6 26 / §7 20 / §8 4 / §9 5），其中 **承重 141 条**（Abstract–§4 95 / §5 9 / §6 17 / §7 16 / §8 1 / §9 3）。§0 为独立的承重数字 cross-reference，不计入明细 194。

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
### §5 Implications (L187–L192)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §5 | L189 | directed-fix path structurally unreachable: 0/8,870 node-level rework events across 80-run corpus | 0/8,870 | 是 | 路径可达性承重 |
| §5 | L189 | single-attempt design: rework_count=1 for all 8,870 reworked nodes; every node gets exactly one repair attempt | 8,870, count=1 | 是 | 单尝试设计约束承重 |
| §5 | L189 | 72.6% of Q6 reworked nodes produce substantively different corrected_claim, but angle path never rewrites node claim (only claim-writing path L821 in unreachable branch) | 72.6%, L821 | 是 | 修复未落地承重 |
| §5 | L189 | 85.3% of Q6 reworked nodes end in degraded terminal state | 85.3% | 是 | 终端态承重 |
| §5 | L189 | 2.4% value_mismatch = blind-re-search baseline not ceiling; no_source 4.0% retained; single-attempt fix 3.7% baseline | 2.4%, 4.0%, 3.7% | 是 | 修复预测基线承重 |
| §5 | L189 | two orthogonal changes separately testable (path reachability vs attempt count); greedy gates misclassify 45.6% of accepts | 45.6% | 否 | 实验设计细节 |
| §5 | L190 | mechanical frozen judge feasible & necessary for harness ablation; LLM judges inject family bias + non-determinism | — | 是 | 评估方法 claim |
| §5 | L191 | more budget buys breadth + modest saturating depth: tier means 0.625/0.725/0.800 (100/150/300), 0.933 (719), r=+0.944 n=30, saturates max_depth=5 (~n=665) | 0.625/0.725/0.800, 0.933, r=+0.944, ~n=665 | 是 | 预算-广度承重 |
| §5 | L191 | L4 conclusion layer does not converge to gold winner at any tier (0/21); warning against "just give it more budget" | 0/21 | 是 | 主 claim 承重 |
| §5 | L192 | checkpoint reuse trades coverage (composite A>B 3/3) for metacognitive precision (gap marking 3/3 higher on resume arm) + vsr 0.66 vs 0.46 (r3 excluded) | 3/3, 0.66 vs 0.46 | 是 | checkpoint 权衡承重 |
### §6 Limitations (L194–L213)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §6 | L196 | quality axis gold-conditioned: each domain needs own frozen reference tree; general = method + gold-free metacog axis, not quality scores | 3 domains | 是 | 核心 scope limit |
| §6 | L197 | "mechanical" = deterministic scoring not designer-free: gold tree is designer artifact (origin: ai, 2026-11-22 rebuild, original lost) | origin: ai | 是 | 参考树偏差承重 |
| §6 | L197 | reference harder than model output: mean coverage ~0.32, spread 0.11–0.56; self-transcription would sit ~1.0 (not self-copy) | 0.32, 0.11–0.56 | 否 | 偏差缓解 (i) |
| §6 | L197 | cross-domain near-zero coverage: Q6 vs GPU gold ≤8% every tier vs 6–13% in-domain; leakage check 0 hits; same-family 27B prior NOT controlled | ≤8%, 6–13%, 0 hits | 是 | 参考树 question-specific 承重 |
| §6 | L198 | no independent gold cross-check: perturbation (drop 10% units, 5 seeds) moves mean cov ≤0.0215 (< 1× sd 0.0926); cor 0.601→0.641 | 0.0215, 0.0926, 0.601→0.641 | 否 | 构造敏感性细节 |
| §6 | L198 | threshold sweep: 0.70→0.3185, 0.65→0.496, 0.80→~0.015 (0.85→0.000) = 30× swing over 0.15 window; 0.70 manually calibrated | 0.3185/0.496/0.015, 30× | 是 | 阈值自由度承重 |
| §6 | L198 | shape cor(cov,n_nodes) 0.802/0.601/0.388/0.132 at 0.65/0.70/0.75/0.80; low-budget rise detectable only ≤0.70; plateau sub-noise at all | 0.802/0.601/0.388/0.132 | 是 | 形状 threshold-scoped 承重 |
| §6 | L199 | embedding-model robustness: shape robust (cor 0.601 bge-m3 vs 0.692 MiniLM); levels model-sensitive (0.3185 vs 0.1963, per-tree 0.553) | 0.601/0.692, 0.3185/0.1963 | 是 | 嵌入模型自由度承重 |
| §6 | L200 | judge scores output tree not acquisition process; provenance blind spot; source-anchored verification only partial (URL-retained subset) | — | 是 | 测量盲点承重 |
| §6 | L201 | single model 27B; no capability curve (7b/27b/70b planned not run); scoped to "open-weight ~27B" | 27B | 否 | 模型单一 caveat |
| §6 | L202 | self-judge bias: depth axis same-family; r=0.861 with older LLM-judge cov axis; heterogeneous re-judging blocked (no API key) | r=0.861 | 否 | 自偏轴细节 |
| §6 | L203 | n=3/budget at 50/719, n=8/tier at 100/150/300; depth gradient 0.625/0.725/0.800 era-consistent; 300 saturates (sd=0, 8/8@0.8); 50/719 95% CI ±0.29 | 0.625/0.725/0.800, ±0.29 | 是 | 样本量承重 |
| §6 | L203 | power analysis: ANOVA F(2,12)=0.036, per-tier 0.099/0.100/0.108, pooled sd 0.085; power to detect large effect (f=0.40)=21.5%, medium (f=0.25)=11.0% → severely underpowered | F=0.036, 21.5%, 11.0% | 是 | 功效不足承重（防过度解读 null） |
| §6 | L204 | mech layer diagnostic-only: 0/4 idea-2 trees share any variable (orthogonal quantity spaces); numeric self-consistency lives in L1 physical layer | 0/4 | 否 | 机械层限制 |
| §6 | L205 | one question family (gpu) for gold; other 2 domains metacog-only; five out-of-domain gold trees Q6–Q10 ready for next scans | Q6–Q10 | 否 | 单问题族 caveat |
| §6 | L206 | construct mismatch: question 32K floor + search own candidates vs gold 64K fixed + fixed set (3090/M2Ultra/L40S/A100/V100/TPU); all 20 trees take 32K; coverage partially confounded | 32K vs 64K, 20 trees | 是 | 构造错配 confound 承重 |
| §6 | L207 | provenance retention gap: 60.6% search-tagged nodes (1330/2196) no stored URL; retention 0–100% across runs (pipeline not model) | 60.6%, 1330/2196 | 是 | URL 保留缺口承重 |
| §6 | L208 | retrieval-channel silent outage: 70–90% source-empty; idea-2 r3 A-r3 90%/B-r3 70% vs 2%/36% healthy; whitelist log dozens→0–8; r3 vsr excluded | 90%/70% vs 2%/36% | 是 | 通道静默故障承重 |
| §6 | L209 | detector domain bias: soc 42% hits = mathematical "uncertainty" concept vs GPU 15%; soc gap_rate inflated ~1.7×; cross-domain levels not comparable | 42% vs 15%, ~1.7× | 是 | 检测器域偏承重 |
| §6 | L209 | 8-pattern pooled flat F(2,12)=0.036 but 22-pattern rises 0.39/0.41/0.44 (F=1.02); monitoring axis flat under both (0.090/0.090/0.096; 0.105/0.106/0.114; F=0.033) → invariance detector-scoped | F=0.036, 0.39/0.41/0.44, F=0.033 | 是 | 不变性 detector-scoped 承重 |
| §6 | L209 | node-level coupling survives cleaning: search-source 71.0% vs 27.7% (GPU); z +16.24/+8.13/+11.73 all p<0.001 | 71.0% vs 27.7%, z all p<0.001 | 否 | 耦合稳健性细节 |
| §6 | L210 | gap marker prompt-elicited not spontaneous (prompts.py:78,312): 82% GPU / 72% nat / 51% soc of hits are instructed tag; gap_rate measures elicited not spontaneous monitoring | 82%/72%/51% | 是 | prompt-elicited 承重 |
| §6 | L211 | workshop scope: measurement + diagnosis paper not fix; repair-loop fix designed + predicted not yet run | — | 否 | scope 定位 |
| §6 | L212 | single-attempt rework = harness design choice not model limit: rework_count=1 for all 8,870 (621 Q6/139 Q7); max_rework=2 never exercised (structural ceiling) | 8,870, 621/139, count=1 | 是 | 单尝试设计约束承重 |
| §6 | L212 | 72.6% Q6 reworked produce different corrected_claim but angle path never rewrites claim (L821 unreachable); node ends degraded (85.3%) | 72.6%, L821, 85.3% | 是 | 修复未落地 + 终端态承重 |
| §6 | L213 | executor continuity (meta): agent itself continuity-bound (passively triggered); goal state-machine records where to resume not drives resumption | — | 否 | 执行者连续性 caveat |
### §7 Future work (L215–L222)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §7 | L217 | structural stop-criterion axis (L2): agent over-expands 50 vs 24 (2.08:1), near-orthogonal to depth score (r=−0.23); not yet in composite | 50/24, 2.08:1, r=−0.23 | 是 | 新诊断轴承重 |
| §7 | L218 | tree-level conditional information gain for bottleneck localization; components mature but tree-level combo unclaimed (closest 2611.24733 zero overlap) | 2611.24733 | 否 | 后续方向 + novelty |
| §7 | L219 | replication (5 added reps/tier at 100/150/300, n=3→8) settles mechanical curve not LLM-depth peak; 7b/70b capability curve planned | n=3→8 | 否 | 复制 + 能力轴 |
| §7 | L220 | general-methodology needs 2–3 more domains; 5 frozen gold trees exist (Q6–Q10, 41-node, 2026-11-07); converter validated (Q6 46/Q7 52/Q8 36/Q9 34/Q10 36 units) | Q6–Q10, 46/52/36/34/36 | 是 | 泛化路径 + 资产承重 |
| §7 | L220 | Q6 budget scan complete (15/15); in-domain coverage rises with budget: 0.058/0.073/0.087/0.130/0.167 at 50/100/150/300/719 (300 cache-suppressed sd=0) | 0.058/0.073/0.087/0.130/0.167 | 是 | 跨域曲线承重 |
| §7 | L222 | rep-isolated rerun: metacog sd 0.0673 (300) / 0.0648 (719) vs cache-shared 0.0304 / 0.0290 → ~2.2× spread; first behavioral evidence cache-sharing suppresses rep variance | 0.0673/0.0648 vs 0.0304/0.0290, ~2.2× | 是 | 缓存抑制方差承重 |
| §7 | L222 | 300-tier rerun: r1 depth-ceiling (252 nodes) vs r2/r3 budget-cap (300); 719 rerun all depth-ceiling-bound (349/277/392, max_depth=4) → does not test 719 budget cleanly | 252/300, 349/277/392 | 否 | 停止机制 confound 细节 |
| §7 | L220 | cross-domain coverage near-zero: Q6 runs scored against GPU gold 0.009/0.009/0.019/0.046 (same tiers), 0–3 of 36 gold units ≤8% → validates gold-conditionality scope limit | 0.009/0.019/0.046, ≤8% | 是 | 跨域近零承重（gold 条件性） |
| §7 | L220 | Q6 719 tier: 3 reps realized 197/351/379 nodes → coverage 0.130/0.174/0.196; realized node count explains within-719 spread (197≈300-tier level) | 197/351/379, 0.130/0.174/0.196 | 是 | realized 节点数解释承重 |
| §7 | L222 | GPU 719 tier: coverage does NOT rise with realized node count (381→0.333, 665→0.417, 747→0.306; most-nodes rep lowest) → plateau not a depth-wall artifact | 381/665/747, 0.333/0.417/0.306 | 是 | plateau 非深度墙承重 |
| §7 | L222 | GPU nominal budget axis contaminated: realized node counts overlap across tiers (nominal-50 r1=423 > nominal-300 r1=364; 300 spans 364–415; 719 spans 381–747) | 423/364, 364–415, 381–747 | 是 | x 轴污染 confound 承重 |
| §7 | L222 | re-binning 30 GPU trees by REALIZED node count: cor(cov,realized)=+0.563 (t=+3.60, df=28); plateau at ~400 realized nodes not nominal ~300 (bins 0.250/0.325/0.361/0.361) | +0.563, t=+3.60, ~400 | 是 | realized 轴主结果承重 |
| §7 | L222 | plateau-segment caveat: flat top rests on top 2 bins only (n=3+n=2=5); bin means 0.361/0.361 gap 0.0000 vs noise floor sd≈0.078 → flatness is low-n shape statement, cor carries the rise | n=5, 0.361/0.361, sd≈0.078 | 是 | plateau 弱半承重（防过度解读） |
| §7 | L222 | GPU batch uniformly truncated: all 15 K7 trees final_state=rework, gain 0.86–0.92, non-empty frontier 24–252, max_level≤5 → none converged naturally | 0.86–0.92, 24–252 | 否 | 截断态细节 |
| §7 | L222 | era confound (checked 2026-11-24, commit 47a8543cd): GPU K7 + rep-scan = pre-clamp (soft cap), Q6 original + rerun = post-clamp (hard cap); cross-domain contrast compares different regimes + max_depth 5 vs 4 | 47a8543cd, 5 vs 4 | 是 | era confound 承重 |
| §7 | L220 | within-tier rep variance large: at budget 100 the 3 reps score 0.130/0.044/0.044; a budget-100 rep (0.130) exceeds every budget-150 rep → realized node count not a clean monotonic predictor across all 15 runs | 0.130/0.044/0.044 | 是 | 曲线解读 confound 承重 |
| §7 | L220 | in-domain composite = 0.5·tree-depth + 0.5·coverage (both mechanical); post-300 rise carried entirely by coverage — tree-depth saturates 0.800 from 150 tier (Δdepth=0 across 719 reps; Q6 gold max depth 3 vs GPU 5) → curve purely coverage-driven | 0.5/0.5, 0.800, depth 3 vs 5 | 是 | 覆盖驱动主结果承重 |
| §7 | L220 | cross-domain residual = fixed set of 5 generic hardware-cost units (purchase amortization/power/electricity/failure/feasibility); none of 8 cache/hit-rate units ever match → domain specificity strong but not binary; raw-markdown gold → exactly zero, enriched gold → ≤8% | 5 units, 8 cache units | 是 | 跨域特异性 nuance 承重 |
| §7 | L220 | monitoring-axis invariance does NOT transfer to Q6: claim-field gap rate 0.073/0.003/0.016/0.026 at 50/100/150/300 (719 reps 0.000/0.029/0.005), low + non-flat after 50, vs GPU flat 0.105/0.106/0.114 → invariance currently a GPU-domain-only result | 0.073/0.003/0.016/0.026, 0.105/0.106/0.114 | 是 | 不变性不跨域承重（关键负结果） |
| §7 | L220 | repair low-yield DOES transfer: Q6 32/621 = 5.2% (same frozen metric as GPU 3.7% = 331/8870, §4.1) → "low-yield repair tail" not a GPU-domain artifact (n=15) | 32/621=5.2%, 3.7%=331/8870 | 是 | 修复低收益跨域承重 |
### §8 Data & code (L224–L226)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §8 | L226 | all metrics deterministic functions of saved run JSONs; judge code + calibration + metacog axis + 15-run scan in repo (paths in supplementary-index) | 15-run | 是 | 可复现性 claim |
| §8 | L226 | source-anchored verification = source_verify.py (strict 20-char-window number+unit co-occurrence, no LLM); calibration = calibration_check.py | 20-char | 否 | 验证层方法细节 |
| §8 | L226 | gold converter gold_md_to_units.py verified on all 5 out-of-domain trees; judge gold-injection regression-checked GPU default 0.3972 | 0.3972 | 否 | 回归检查细节 |
| §8 | L226 | degeneration detector (repeated-block + no-answer-block) validated 5/5 on Q04, full-corpus 2/35 degenerate | 5/5, 2/35 | 否 | 退化检测细节 |

### §9 References (L228–L250) + draft notes (L255)

| 节 | 行号 | claim 摘要 (≤30 词) | 数字 | 承重? | 理由 (≤15 词) |
|---|---|---|---|---|---|
| §9 | L230–L250 | reference list: 21 refs (no load-bearing numbers; citations only) | 21 refs | 否 | 参考文献结构 |
| §9 | L241/L242/L248 | self-preference-bias cluster supports judge-bias claim: Panickssery 2404.13076, Pombal 2604.06996, Yang 2604.22891 | 3 refs | 是 | 支撑 judge-bias 承重 claim |
| §9 | L243 | metacognitive myopia ref (Scholten 2408.05568) supports metacog-axis framing | 2408.05568 | 否 | 框架支撑 |
| §9 | L255 | deadline verified 2026-11-23 (ICML 2027 workshop; main abstract 2027-01-14 / full 2027-01-22 AoE; conf 2027-08-02~04 San Diego; workshop CFP not yet published) | 2027-01-14/22, 08-02~04 | 是 | venue/deadline 承重 |
| §9 | L255 | Idea 2 r1–r3 data note: A>B composite 3/3 (cov-driven); B-arm gap rate 0.14 vs 0.06; vsr B 0.66 vs A 0.46 (r1–r2, r3 excluded) | 3/3, 0.14/0.06, 0.66/0.46 | 是 | checkpoint 数据 note 承重 |
<!-- CHUNK3_END -->
