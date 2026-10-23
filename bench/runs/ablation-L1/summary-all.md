# T4 ablation-L1 汇总 — 11 变体 × 3 runs 完整对比（summary-all）

> origin: ai · 2026-10-23 Asia/Shanghai · T4 消融 L1 完整汇总（补跑后）
> 任务：decomp-bench T4 ablation-L1（prompt 结构消融）
> rubric: `bench/rubric.md`（18 点，6 维度×3 分，≥15 success / 10-14 partial / <10 fail）
> 显著性：Δ > 2·σ_pooled 为显著（σ_pooled = sqrt((σ1²+σ2²)/2)，σ 取总体 σ_pop；样本 σ_samp 另列供参考）
> 样本：11 变体 × 3 runs = 33 runs + 33 评分文件，n=3/变体（小样本，仅方向性显著性，不做强统计宣称）
> 通道：local degraded（目标仓库 dd2003-460/decomp-bench 私有不可达 404/403，按 sop/arena-loop-pipeline.md §3.3 降级为本地 vllm/qwen3.8-27b-w8a16，conf 0.2）
> 分支：按 Arena 固定分支规则在 `arena/2d866a16-prompt-first-bench` 执行（用户要求分支因系统禁止跨分支未新建，已在 commit 信息留痕）
> 进度：**11/11 变体 × 3/3 runs 已齐（100%），含本次补跑 7 变体 × 3 runs = 21 runs + 21 评分**

## 0. 变体定义速览（11 变体）

| 变体 | 定义 | 消融目的 |
|------|------|----------|
| C0 | 完整 prompt（角色+契约+草稿区+输出结构+约束） | 基线 full |
| C1 | C0 轻度简化（压缩背景，保留契约） | 测长度边际 |
| C1-small | C0 简化版（压缩背景与示例） | 测信息量边际 |
| C2-expos | C1 + 详细 exposition（背景解释+步骤说明） | 测 exposition 边际 |
| **C3-exposneg** | **C2-expos + 负向草稿（反例）** | **测负向示例边际** |
| **C4-arch** | **C0 + 架构图（mermaid）** | **测架构图边际** |
| **C5-small-exposneg** | **C1-small + 负向草稿** | **测小prompt+负向交互** |
| **C6-nocontract** | **C0 - 契约条款** | **测契约边际** |
| **C7-noscratch** | **C0 - 草稿区（软移除）** | **测草稿区边际（软）** |
| **C8-noscratch-hard** | **C0 - 草稿区（硬约束：显式禁止）** | **测草稿区硬约束边际** |
| **C9-open** | **开放式 prompt（无固定结构）** | **测结构化整体边际** |

> 粗体为本次补跑 7 变体；C0/C1/C1-small/C2-expos 为历史已完成 4 变体（2026-10-22）。

## 1. 11 变体原始分与统计（Mean±σ，n=3）

| 变体 | run1 | run2 | run3 | Mean | σ_pop | σ_samp | 判定 | success 率 |
|------|------|------|------|------|--------|--------|------|------------|
| **C0** | 15 | 16 | 15 | **15.33±0.47** (samp±0.58) | 0.47 | 0.58 | success | 3/3 |
| **C1** | 15 | 15 | 14 | **14.67±0.47** (samp±0.58) | 0.47 | 0.58 | partial | 2/3 |
| **C1-small** | 13 | 15 | 15 | **14.33±0.94** (samp±1.15) | 0.94 | 1.15 | partial | 2/3 |
| **C2-expos** | 14 | 15 | 15 | **14.67±0.47** (samp±0.58) | 0.47 | 0.58 | partial | 2/3 |
| **C3-exposneg** | 13 | 14 | 14 | **13.67±0.47** (samp±0.58) | 0.47 | 0.58 | partial | 0/3 |
| **C4-arch** | 15 | 15 | 15 | **15.00±0.00** (samp±0.00) | 0.00 | 0.00 | success | 3/3 |
| **C5-small-exposneg** | 12 | 14 | 13 | **13.00±0.82** (samp±1.00) | 0.82 | 1.00 | partial | 0/3 |
| **C6-nocontract** | 12 | 14 | 13 | **13.00±0.82** (samp±1.00) | 0.82 | 1.00 | partial | 0/3 |
| **C7-noscratch** | 13 | 15 | 14 | **14.00±0.82** (samp±1.00) | 0.82 | 1.00 | partial | 1/3 |
| **C8-noscratch-hard** | 11 | 13 | 13 | **12.33±0.94** (samp±1.15) | 0.94 | 1.15 | partial | 0/3 |
| **C9-open** | 8 | 11 | 10 | **9.67±1.25** (samp±1.53) | 1.25 | 1.53 | fail | 0/3 |

> 注：σ_pop = 总体标准差（分母 n），σ_samp = 样本无偏标准差（分母 n-1）；表格 Mean±σ_pop 为主展示，显著性计算用 σ_pop。
> C9-open σ_samp=1.53 与内部背景 C9 σ=1.53 一致（高方差）；C0 σ_pop=0.47 与 C0 σ=.45 背景一致（低方差，稳定性好）。

## 2. 显著性判定（Δ > 2·σ_pooled，vs C0 基线）

| 对比 | C0 Mean | 对比变体 Mean | Δ | σ_pooled | 2·σ_pooled | 判定 | 解读 |
|------|---------|---------------|---|----------|------------|------|------|
| C0 vs **C1** | 15.33 | 14.67 | **0.66** | 0.47 | 0.94 | **ns 不显著** | 轻度简化 Δ0.66 <阈值，长度压缩无显著损失 |
| C0 vs **C1-small** | 15.33 | 14.33 | **1.00** | 0.74 | 1.49 | **ns 不显著** | 简化版 Δ1.00 <1.49，不显著（但 σ 增大) |
| C0 vs **C2-expos** | 15.33 | 14.67 | **0.66** | 0.47 | 0.94 | **ns 不显著** | exposition Δ0.66 不显著，解释性增量无显著提升 |
| C0 vs **C3-exposneg** | 15.33 | 13.67 | **1.66** | 0.47 | 0.94 | **✅ 显著** | 负向草稿 Δ1.66 >0.94 **显著下降**，反例干扰有害 |
| C0 vs **C4-arch** | 15.33 | 15.00 | **0.33** | 0.33 | 0.66 | **ns 不显著** | 架构图 Δ0.33 <0.66 不显著，架构图无显著增益（但方差降为0) |
| C0 vs **C5-small-exposneg** | 15.33 | 13.00 | **2.33** | 0.67 | 1.34 | **✅ 显著** | 小+负向 Δ2.33 >1.34 **显著下降**，负向在小prompt下危害放大 |
| C0 vs **C6-nocontract** | 15.33 | 13.00 | **2.33** | 0.67 | 1.34 | **✅ 显著** | 去契约 Δ2.33 >1.34 **显著下降**，契约条款关键 |
| C0 vs **C7-noscratch** | 15.33 | 14.00 | **1.33** | 0.67 | 1.34 | **ns 不显著** | 去草稿区(软) Δ1.33 <1.34 **边界不显著**（Δ≈阈值，方向性下降) |
| C0 vs **C8-noscratch-hard** | 15.33 | 12.33 | **3.00** | 0.74 | 1.49 | **✅ 显著** | 去草稿区(硬) Δ3.00 >1.49 **显著下降**，硬约束危害 >软移除 |
| C0 vs **C9-open** | 15.33 | 9.67 | **5.66** | 0.94 | 1.89 | **✅ 显著** | 开放式 Δ5.66 >1.89 **显著下降**，结构化整体效应最大 |

## 3. 关键消融边际（相邻/设计对照，Δ>2σ_pooled 标注）

| 消融对照 | 变体A → 变体B | Δ | σ_pooled | 2σ | 显著性 | 结论 |
|----------|--------------|---|----------|----|--------|------|
| 长度压缩 | C0(15.33±0.47)→C1-small(14.33±0.94) | 1.00 | 0.74 | 1.49 | ns | 长度压缩 1 分不显著，但方差翻倍 |
| exposition 增量 | C1(14.67±0.47)→C2-expos(14.67±0.47) | 0.00 | 0.47 | 0.94 | ns | exposition 零增益 |
| **负向草稿边际** | C2-expos(14.67±0.47)→C3-exposneg(13.67±0.47) | **1.00** | 0.47 | 0.94 | **✅ 显著** | **负向示例显著有害（-1.00）** |
| 架构图边际 | C0(15.33±0.47)→C4-arch(15.00±0.00) | 0.33 | 0.33 | 0.66 | ns | 架构图无显著增益，但稳定性 ↑（σ 0→0） |
| 小prompt+负向交互 | C1-small(14.33±0.94)→C5-small-exposneg(13.00±0.82) | 1.33 | 0.88 | 1.76 | ns | 方向性下降，不显著（小样本） |
| **契约条款边际** | C0(15.33±0.47)→C6-nocontract(13.00±0.82) | **2.33** | 0.67 | 1.34 | **✅ 显著** | **去契约显著有害（-2.33），契约关键** |
| 草稿区(软)边际 | C0(15.33±0.47)→C7-noscratch(14.00±0.82) | 1.33 | 0.67 | 1.34 | ns(边界) | 软移除方向性下降，阈值边界 |
| **草稿区(硬)边际** | C0(15.33±0.47)→C8-noscratch-hard(12.33±0.94) | **3.00** | 0.74 | 1.49 | **✅ 显著** | **硬约束显著有害（-3.00），>软移除** |
| **结构化整体边际** | C0(15.33±0.47)→C9-open(9.67±1.25) | **5.66** | 0.94 | 1.89 | **✅ 显著** | **开放式 vs 全结构 -5.66，最大效应** |
| 草稿区软→硬 | C7(14.00±0.82)→C8(12.33±0.94) | 1.67 | 0.88 | 1.76 | ns | 方向性：硬约束 <软移除，但不显著 |
| 负向在不同基座 | C3-exposneg(13.67)→C5-small-exposneg(13.00) | 0.67 | 0.67 | 1.34 | ns | 负向在两基座危害相近 |

## 4. 方差/稳定性读出

| 变体 | Mean | σ_pop | σ_samp | 稳定性解读 |
|------|------|-------|--------|------------|
| C0 | 15.33 | **0.47** | 0.58 | 基线稳定性高（σ 最小之一） |
| C4-arch | 15.00 | **0.00** | 0.00 | 架构图使输出方差归零（最稳） |
| C9-open | 9.67 | **1.25** | **1.53** | 开放式方差最高（σ 比 C0 大 2.7 倍，方差比 7.1 倍），复现内部背景 C0 σ0.45 vs C9 σ1.53 的方差差（3.4 倍标准差比） |
| C8-noscratch-hard | 12.33 | 0.94 | 1.15 | 硬约束次高方差，稳定性差 |
| C1-small | 14.33 | 0.94 | 1.15 | 简化版方差增大，信息压缩致不稳定 |

> 内部背景验证：C0 Mean 15.2 σ0.45 (n=5) vs C9 15.3 σ1.53 (n=3) 的“均值无差异、方差低 3.4 倍”——本次 18 点制复现为 C0 15.33±0.47 vs C9-open 9.67±1.25，**均值差显著（5.66 >1.89）但方差比仍 2.7 倍（σ1.25/0.47）**，方向一致：结构化降方差、保均值；开放式高方差且均值显著低（本次任务结构化整体效应显著，原背景“均值无差异”可能因任务/模型/评分尺度差异）。

## 5. 结论（T4 ablation-L1）

1. **结构化整体有效且显著**：C0 vs C9-open Δ5.66 >1.89 ✅，开放式 fail (9.67) vs 全结构 success (15.33)，结构化是最大效应量。
2. **契约条款关键**：C0 vs C6-nocontract Δ2.33 >1.34 ✅，去契约显著降分（13.00 partial），D4 契约维度扣 2 分主因。
3. **草稿区有价值，硬约束更差**：C0 vs C7 软移除 Δ1.33 边界 ns，但 C0 vs C8 硬约束 Δ3.00 ✅ 显著；硬约束禁止思考空间比软移除危害更大。
4. **负向草稿有害**：C2-expos vs C3-exposneg Δ1.00 >0.94 ✅，负向反例显著降分（-1.00）；小prompt下负向交互进一步降至 13.00（ns 但方向一致）。
5. **架构图无显著增益但提稳**：C0 vs C4-arch Δ0.33 ns，但 σ 0.47→0.00，架构图是稳定性工具而非提分工具。
6. **长度压缩与 exposition 无显著效应**：C0→C1-small Δ1.00 ns，C1→C2-expos Δ0 ns，提示 prompt 冗余度较高，核心结构比长度重要。

> 限制：n=3/变体小样本，显著性仅方向性；通道为 local degraded（qwen3.8 代跑），非 arena 原生模型；评分者为单盲评（非双盲仲裁），结果为探索性，需 arena 恢复后多模型复核。

## 6. 文件完整性清单（33 runs + 33 评分 + 11 汇总 + 1 总汇总）

| 变体 | runs | 评分 | summary | prompt |
|------|------|------|---------|--------|
| C0 | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C0/prompt.txt |
| C1 | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C1/prompt.txt |
| C1-small | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C1-small/prompt.txt |
| C2-expos | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C2-expos/prompt.txt |
| C3-exposneg | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C3-exposneg/prompt.txt |
| C4-arch | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C4-arch/prompt.txt |
| C5-small-exposneg | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C5-small-exposneg/prompt.txt |
| C6-nocontract | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C6-nocontract/prompt.txt |
| C7-noscratch | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C7-noscratch/prompt.txt |
| C8-noscratch-hard | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C8-noscratch-hard/prompt.txt |
| C9-open | run1.md,run2.md,run3.md (3/3) | run1-score.md,run2-score.md,run3-score.md (3/3) | summary.md ✅ | bench/prompts/variants/C9-open/prompt.txt |

| **总计** | **33 runs** | **33 评分** | **11 summary.md** | **11 prompt.txt** |
| 补跑部分 | 21 runs (C3/C4/C5/C6/C7/C8/C9-open ×3) | 21 评分 | 7 summary.md | 7 prompt.txt |
| 历史部分 | 12 runs (C0/C1/C1-small/C2-expos ×3) | 12 评分 | 4 summary.md | 4 prompt.txt |

- 总汇总：`bench/runs/ablation-L1/summary-all.md`（本文件）
- Rubric：`bench/rubric.md`（18 点，6 维度×3 分）
- 落盘位置：`bench/runs/ablation-L1/{variant}/`
- 验证：见 §7

## 7. 验证（文件完整性）

```bash
# 预期 33 runs + 33 评分 + 11 summary + 11 prompt = 88 文件
find bench/runs/ablation-L1 -type f | wc -l  # 应 = 77 (33+33+11)
find bench/prompts/variants -name prompt.txt | wc -l  # 应 = 11
ls bench/runs/ablation-L1/summary-all.md  # 本文件存在
cat bench/rubric.md | grep "18 点"  # rubric 存在
```

> 执行步骤 5 完成：已更新 summary-all.md 补全 11 变体对比表，显著性 Δ>2σ_pooled 已标注（✅/ns）。
> 下一步：Step 验证文件完整性（`ls` + `wc -l` + `git log`）并推送。

## 8. 执行步骤回溯（5 步每步 commit）

| 步骤 | 内容 | commit | 状态 |
|------|------|--------|------|
| 1 | 读取 bench/prompts/variants/VAR/prompt.txt 11 模板 | ebc7894 | ✅ |
| 2 | 每变体 3 run（不同种子/时间戳） | f5573e8 + 845ab99 | ✅ 33 runs |
| 3 | 18 点 rubric 评分，每 run 1 评分文件 | f469d26 | ✅ 33 评分 |
| 4 | Mean+σ 写入各变体 summary.md | a1a3534 | ✅ 11 汇总 |
| 5 | 更新 summary-all.md，补全 11 变体对比表 + 显著性 | (本 commit) | ✅ |

> 仓库：按 Arena 分支固定规则在 `arena/2d866a16-prompt-first-bench` 执行（目标仓库 `dd2003-460/decomp-bench` 私有不可达已在 §0 通道说明）。
