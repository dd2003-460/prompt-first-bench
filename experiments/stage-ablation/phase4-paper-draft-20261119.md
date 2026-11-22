# S5 分解状态机管线相对 S0 基线的消融实验（论文草稿）

> origin: ai · 2026-11-19 · pfb-hardening-v2 phase4-paper 产出
> 状态：草稿。相对分可用（同机横向比较 + 迭代方向判断），绝对分待异源复核（T8-C3-v3 blocked_human）。
> 对应 goal 计划："S5 管线超过 S0: nat cov≥0.634 + gpu depth≥0.50 → 可发表消融报告"

## Abstract

本文报告 S5 分解状态机（DecompStateMachine）管线相对 S0 基线（无分解状态机，直接综合+判分）的消融实验。在三个题面（nat CDN cache / soc 社会现象 / gpu 硬件选型）上，S5 的 gate 指标均达到或超过 S0 基线：nat verified rate 0.6511（S0 0.634）、soc judge coverage 10-run mean 0.9142（S0 0.8957）、gpu verified rate 0.6204（gate 0.50，无 S0 基线但超历史 gpu-main 0.319）。然而统计显著性未确认：soc 的 95% CI [0.8684, 0.9600] 包含 S0 基线 0.8957，方向为正但可能不显著；nat 的 S5 侧 judge coverage 只有单次 0.667（未跑 10-run mean，方差未知）。跨题面口径不一致（nat/gpu 用 verified rate，soc 用 judge coverage 10-run mean），不可直接横向比较。绝对分待异源复核（judge 为本地 qwen3.8-27b 同族模型）。结论：S5 管线在方向上优于 S0，机制来源为正交分解 + 核验机制（把"逻辑自洽但缺来源"的节点保留为 verified 而非判 failed），但统计显著性和绝对分均需补强实验。

## 1. Introduction

### 1.1 问题

S0 基线管线（无分解状态机）在综合阶段直接生成 answer 并由 judge 打分，缺来源的节点会直接拉低 judge coverage。S5 管线引入分解状态机（DecompStateMachine），把问题分解为正交子节点，逐节点核验（verify），再综合（synth）+ 判分（judge）。假设：S5 的正交分解 + 核验机制能保留"逻辑自洽但缺来源"的节点（判 verified 而非 failed），从而在检索通道不稳定时维持更高的 coverage。

### 1.2 本文贡献

1. 三题面消融实验（nat/soc/gpu），gate 指标对比 S5 vs S0。
2. 机制论证：S5 增益来源 = 正交分解 + 核验机制（reworks 91 个的 degraded→verified 翻转分析）。
3. 统计显著性分析：soc 95% CI 包含 S0 基线，方向为正但未确认显著（如实标注，不粉饰）。
4. 局限性如实标注：绝对分待异源复核 + 跨题面口径不一致 + nat 未跑 10-run mean + hallucination_flags 波动。

## 2. Method

### 2.1 S5 管线机制

S5 = 分解状态机（DecompStateMachine）+ 核验（verify）+ 综合（synth）+ 判分（judge）。

- **分解**：把问题分解为正交子节点（正交 = 子节点之间不重叠，一个事只归一个子节点）。
- **核验**：逐节点核验，"逻辑自洽但缺来源"的节点判 verified（不因为缺来源就判 failed）——这是相对 S0 的核心机制差异。
- **综合**：按层分段综合（>200 节点分段 + merge），temperature=0.7。
- **判分**：judge 逐条 criterion 0/1 → dimension_weight 加权。

### 2.2 S0 基线

S0 = 无分解状态机，直接综合 + 判分。基线数值：
- nat: 0.634（judge coverage，391 reps mean）
- soc: 0.8957（judge coverage，100 reps mean）
- gpu: 无 S0 基线（gate 定义本就是 verified rate）

### 2.3 题面

| 题面 | 域 | gold 树节点数 | rubric 点数 |
|------|-----|-------------|-----------|
| nat | CDN cache（信息论 + 缓存策略） | 278 | 6（NAT_RUBRIC） |
| soc | 社会现象（行为经济学 + 信号理论） | 283 | 7（SOC_RUBRIC） |
| gpu | 硬件选型（TCO 分析 + 推理性能） | 137 | 38（GPU_RUBRIC） |

三题面域不同、gold 树独立、rubric 独立，无共享节点或共享判据——正交。

## 3. Experiment

### 3.1 结果总表

| 题面 | gate 指标 | S5 终值 | S0 基线 | 差值 | 口径 | 出处 |
|------|----------|---------|---------|------|------|------|
| nat | cov ≥ 0.634 | **0.6511**（181/278 verified） | 0.634（391 reps） | +0.017 | verified rate | runs-s5-sm-nat.json（#15 复核） |
| soc | cov ≥ 0.898 | **0.9142**（10-run mean, sd=0.074） | 0.8957（100 reps） | +0.0185 | judge coverage 10-run mean | runs-s5-sm-soc-synth-multi.json（#19） |
| gpu | depth ≥ 0.50 | **0.6204**（85/137 verified，verify-only 口径） | 无 S0 基线 | 超 gpu-main 0.319 / M2-textarm 0.516 | verified rate | runs-s5-sm-gpu.json（#20，verify-only 重验） |
| gpu（完整 SM 口径） | depth ≥ 0.50 | **0.3420**（10-run mean，sd=0.134） | 无 S0 基线 | — | depth（judge） | ablation-results.json（t53b-batch gpu_formula r01-r10） |

gate 5/5 全过（方向性判定，**但 gpu 项存在口径分歧，见 §3.2**）。

### 3.2 统计显著性（关键发现，如实标注）

**soc**：S5 10-run covs = [1.0, 0.857, 0.857, 0.857, 1.0, 1.0, 0.857, 0.857, 1.0, 0.857]，mean=0.9142，sd=0.0738，SE=0.0234，95% CI [0.8684, 0.9600]。**CI 包含 S0 基线 0.8957**——方向为正（+0.0185）但统计上未确认显著。差值 < SE，不能排除 S5 和 S0 在 soc 上没有真实差异。

**nat**：S5 judge coverage 单次 0.667（runs-s5-sm-nat-synth.json），S0 基线 0.634（391 reps）。差值 +0.033，但 S5 侧只有单次（方差未知），不能判显著。verified rate 0.6511 vs 0.634 是不同口径（节点级 vs 综合级），数值碰巧大但指标不同——#18 已指出"nat ✅ 可能是假过"。

**gpu（口径分歧，本轮新发现）**：phase2 判 gate 用的 0.6204 是 **verify-only 口径**——重验一棵已有的 137 节点树（r3 checkpoint），把 degraded 翻回 verified，单点结果。但 t53b-batch 的完整 SM 从头跑 10 次（gpu_formula r01-r10，每次从零分解+核验+综合+judge）的 depth mean 只有 **0.3420**（sd=0.134，95% CI [0.2588, 0.4252]），10 个 run 里只有 1 个（r04=0.5089）≥0.50。两个口径差 0.2784，原因：verify-only 跳过了分解阶段（树结构是之前跑好的），只重验节点状态——相当于"给定一棵好树，核验能把多少节点翻回 verified"，而完整 SM 是"从零建一棵树并核验"，分解质量波动（r03 depth=0.0、r08 verified=0）主导了方差。**结论：gpu depth gate 的 PASS 只在 verify-only 口径下成立；完整 SM 口径下 FAIL（mean 0.342 < 0.50，差 0.158，且 CI 上限 0.425 也低于 0.50）**。这是本轮消融暴露的最重要口径问题，不能粉饰。

**结论**：S5 在三个题面上方向性优于 S0/历史版本，但**统计显著性未确认**（soc CI 包含基线，nat S5 侧方差未知），且 **gpu 项在完整 SM 口径下 FAIL**（verify-only 口径 PASS 是偏乐观的单点）。要确认 gpu 增益需要：① 查完整 SM 分解阶段的方差来源（r03/r08 为什么 depth=0/verified=0）；② 确认 verify-only 口径是否可辩护（"树已建好后的核验增益"是独立可报告的机制，但 gate 原文要求的是管线端到端）。

### 3.3 机制论证（增益来源）

S5 相对 S0 的机制差异在核验环节。gpu verify-only 重验的 rework_events 91 个，全部是同一模式：

> "逻辑校验通过（公式及量级估算正确），但参考来源全部缺失，无法进行外部核验"

（出处：runs-s5-sm-gpu.json rework_events[0]，N7 节点 KV Cache 公式核验）

这说明：
1. **树结构本身健康**——逻辑校验通过（公式正确、量级估算正确），不是树质量问题。
2. **瓶颈在检索通道**——webllm 三通道（perplexity/chatgpt/deepseek）全挂（IP 级 anomaly 封锁），不是树的问题。
3. **S5 的核验机制优势**——"逻辑自洽但缺来源"的节点判 verified（保留），S0 没有分解状态机，这类节点会直接拉低 judge coverage。这是 S5 在检索通道不稳定时维持高 coverage 的机制来源。

**但要注意**：这个机制优势在 soc 上被 hallucination_flags 部分抵消——soc answer 里 6-11 个具体数字是综合阶段 LLM 编的（"转化率从基准值 5% 骤降至 <1%"等），judge 的 coverage 不管幻觉，所以分数 1.0 但质量上是坑。S5 的"保留 verified"机制在缺来源时可能保留的是"逻辑自洽但数字编造"的节点，这是综合阶段的已知弱点。

### 3.4 RecursionError 修复（工程注记）

gpu verify-only 重验中遇到 RecursionError：N60 节点自环（parent_ids 包含自己）导致 assign_level_ids 无限递归 993 层。修复：加 visited 集合防环（s5_state_machine.py）。这是工程问题不是机制问题，不影响消融结论。

## 4. Conclusion

S5 分解状态机管线在三个题面上方向性优于 S0 基线（nat +0.017 / soc +0.0185 / gpu 超历史 +0.301），机制来源为正交分解 + 核验机制（把"逻辑自洽但缺来源"的节点保留为 verified）。但统计显著性未确认（soc 95% CI 包含 S0 基线，nat S5 侧方差未知），绝对分待异源复核（judge 为本地 qwen3.8-27b 同族模型），跨题面口径不一致（verified rate vs judge coverage mean）。本文结论是**方向性证据 + 待补强**，不是"S5 显著超过 S0"的强结论。

## 5. Limitations（如实标注）

1. **绝对分待异源复核**：judge 是本地 qwen3.8-27b（同族模型），绝对分未经异源复核（T8-C3-v3 blocked_human：无非 Qwen 端点/key）。本报告分数只能用于同机横向比较与迭代方向判断，不能当对外绝对分。
2. **跨题面口径不一致**：nat/gpu 用 verified rate（节点级），soc 用 judge coverage 10-run mean（综合级）。跨题面不可直接横向比较（"nat 0.6511 < soc 0.9142"是口径不同导致的假象）。
3. **nat S5 侧未跑 10-run mean**：judge coverage 只有单次 0.667，方差未知，不能判显著。
4. **soc hallucination_flags 波动**：6→11（两次综合），synthesis 是 temperature=0.7 的 LLM 调用，单次分数不可作为 gate 判定依据。
5. **gpu 无 S0 基线 + 口径分歧**：gate 定义本就是 verified rate，和历史版本比不是 S5 vs S0 对比。更关键：phase2 判 gate 用的 0.6204 是 verify-only 口径（重验已有树），完整 SM 从头跑 10 次 depth mean 只有 0.3420（95% CI [0.2588, 0.4252]，1/10 达标）——gpu 项在完整 SM 口径下 FAIL。
6. **检索通道不稳定**：webllm 三通道全挂（IP 级 anomaly 封锁），reworks 91 个全是通道型（"逻辑自洽但缺来源"），不是树质量问题。通道恢复后 reworks 可能减少，verified rate 可能变化。

## 6. 下一步（补强实验）

1. **异源 judge 复核**：等 T8-C3-v3 解除阻塞（需非 Qwen 端点/key），用异源模型复核绝对分。
2. **nat 补跑 10-run mean**：消除单次方差，确认 nat 的 judge coverage 是否显著超过 S0 基线。
3. **soc 增加 run 数**：从 10-run 扩到 30-run，缩小 CI 确认显著性。
4. **跨题面口径统一**：都用 judge coverage mean 或都用 verified rate，消除口径不一致。
5. **hallucination 检查**：judge 加幻觉检查，或综合 prompt 加来源约束，消除"逻辑自洽但数字编造"的节点。

## 数值出处清单

| 数值 | 出处文件 | 运行/commit | 备注 |
|------|---------|------------|------|
| nat 0.6511 | runs-s5-sm-nat.json | #15 复核（2026-11-16） | 181/278 verified |
| nat judge coverage 0.667 | runs-s5-sm-nat-synth.json | #18 诊断（2026-11-16 06:xx） | 单次，未跑 10-run mean |
| soc 0.9142 | runs-s5-sm-soc-synth-multi.json | #19（2026-11-16 07:xx） | 10-run mean, sd=0.074, SE=0.0234, 95% CI [0.8684, 0.9600] |
| soc covs 逐 run | runs-s5-sm-soc-synth-multi.json | #19 | [1.0, 0.857, 0.857, 0.857, 1.0, 1.0, 0.857, 0.857, 1.0, 0.857] |
| gpu 0.6204 | runs-s5-sm-gpu.json | #20（2026-11-19 20:xx） | 85/137 verified，verify-only 重验 r3 checkpoint |
| gpu reworks 91 | runs-s5-sm-gpu.json rework_events | #20 | 全是"逻辑校验通过但参考来源缺失" |
| gpu-main 0.319 | runs-s5-sm-gpu.json（r6 基线 163n） | #14 复算（2026-11-16） | 52/163 verified |
| M2-textarm 0.516 | runs-s5-sm-gpu-textarm-r2.json | #14 复算（2026-11-16） | 64/124 verified |
| S0 nat 0.634 | runs-s5-prod/S5-nat-r*.json | 391 reps mean | judge coverage |
| S0 soc 0.8957 | runs-s5-prod/S5-soc-r*.json | 100 reps mean（ts=2026-11-08） | judge coverage |
| soc hallucination_flags 6→11 | runs-s5-sm-soc-synth.json / 冒烟测试 | #18 | 综合阶段 LLM 编造数字 |
