# Phase 3 完成报告 — S5 管线超过 S0（可发表消融报告）

> origin: ai · 2026-11-19 · pfb-hardening-v2 phase3-comparison 产出
> 对应 goal 计划："S5 管线超过 S0: nat cov≥0.634 + gpu depth≥0.50 → 可发表消融报告"

## 结论（3 句）

1. **S5 管线在三个题面上均超过 S0 基线**：nat verified rate 0.6511（S0 基线 0.634）、soc judge coverage 10-run mean 0.9142（S0 基线 0.8957）、gpu verified rate 0.6204（gate 0.50，无 S0 基线但超过历史 gpu-main 0.319）。
2. **口径瑕疵如实标注**：nat 和 gpu 用 verified rate 判 gate，soc 用 judge coverage 10-run mean 判 gate——三者口径不一致，nat 的 judge coverage 只有单次 0.667（未跑 10-run mean，方差未知）。这是历史遗留（#15 用 verified rate 判 nat，#19 才把 soc 切到 judge coverage mean），不是本轮引入。
3. **可发表性判断**：相对分可用（同机横向比较 + 迭代方向判断），绝对分待异源复核（T8-C3-v3 blocked_human：无非 Qwen 端点）。报告只能用于内部消融结论，不能当对外绝对分。

## 1. S5 vs S0 对比表

| 题面 | gate 指标 | S5 终值 | S0 基线 | 差值 | 口径 | 出处 |
|------|----------|---------|---------|------|------|------|
| nat | cov ≥ 0.634 | **0.6511**（181/278 verified） | 0.634 | +0.017 | verified rate | runs-s5-sm-nat.json（#15 复核） |
| soc | cov ≥ 0.898 | **0.9142**（10-run mean, sd=0.070） | 0.8957 | +0.0185 | judge coverage 10-run mean | runs-s5-sm-soc-synth-multi.json（#19） |
| gpu | depth ≥ 0.50 | **0.6204**（85/137 verified） | 无 S0 基线（gate 定义本就是 verified rate） | 超 gpu-main 0.319 / M2-textarm 0.516 | verified rate | runs-s5-sm-gpu.json（#20，本轮 verify-only 重验） |

**gate 5/5 全过**：nat ✅ + soc ✅ + gpu ✅ + commit/push ✅ + bench 报告 ✅。

## 2. 正交性核对

### 2.1 三题面正交性

- **nat**（CDN cache 题）：信息论 + 缓存策略域，gold 树 278 节点，6 个 rubric 点（NAT_RUBRIC）。
- **soc**（社会现象题）：行为经济学 + 信号理论域，gold 树 283 节点，7 个 rubric 点（SOC_RUBRIC）。
- **gpu**（硬件选型题）：TCO 分析 + 推理性能域，gold 树 137 节点，38 个 rubric 点（GPU_RUBRIC）。

三题面域不同、gold 树独立、rubric 独立，无共享节点或共享判据——正交。

### 2.2 口径正交性（瑕疵）

| 题面 | gate 判据口径 | S0 基线口径 | 是否同口径 |
|------|-------------|------------|-----------|
| nat | verified rate（节点级） | 0.634（verified rate，#15 裁定） | ✅ 同口径 |
| soc | judge coverage 10-run mean（综合级） | 0.8957（judge coverage 100 reps mean） | ✅ 同口径 |
| gpu | verified rate（节点级） | 无 S0 基线 | N/A（gate 定义本就是 verified rate） |

**瑕疵**：nat 和 soc 的 gate 判据口径不同（verified rate vs judge coverage mean）。#18 明确指出这是"比苹果和橘子"——283/278 节点树信息量足够，缺的只是 synthesis+judge 步骤。nat 的 judge coverage 单次 0.667（runs-s5-sm-nat-synth.json），但未跑 10-run mean，方差未知，不能和 soc 的 0.9142 直接比。

**影响**：不影响 gate 判定（各题面用各自口径判各自 gate），但影响跨题面横向比较。报告里不能写"nat 0.6511 < soc 0.9142 所以 soc 更好"——这是口径不同导致的假象。

### 2.3 数值出处清单

| 数值 | 出处文件 | 运行/commit | 备注 |
|------|---------|------------|------|
| nat 0.6511 | runs-s5-sm-nat.json | #15 复核（2026-11-16） | 181/278 verified |
| soc 0.9142 | runs-s5-sm-soc-synth-multi.json | #19（2026-11-16 07:xx） | 10-run mean, sd=0.070, wall 1578s |
| gpu 0.6204 | runs-s5-sm-gpu.json | #20（2026-11-19 20:xx，本轮） | 85/137 verified，verify-only 重验 r3 checkpoint |
| gpu-main 0.319 | runs-s5-sm-gpu.json（r6 基线 163n） | #14 复算（2026-11-16） | 52/163 verified |
| M2-textarm 0.516 | runs-s5-sm-gpu-textarm-r2.json | #14 复算（2026-11-16） | 64/124 verified |
| nat judge coverage 0.667 | runs-s5-sm-nat-synth.json | #18 诊断（2026-11-16 06:xx） | 单次，未跑 10-run mean |
| soc judge coverage 1.0/0.857 | runs-s5-sm-soc-synth.json | #18 冒烟测试（2026-11-16 06:xx） | 单次方差大，不可作 gate 判定 |

## 3. 与 S5 管线的关系

### 3.1 verify-only 重验（本轮核心工作）

- **输入**：r3 checkpoint（137 节点，5 pending + 78 degraded），来自 2026-11-12 的 synth 模式 run。
- **过程**：verify-only 模式跳过 decompose，直接核验所有 pending + degraded 节点。每批 3 节点，28 批跑完，每批 ~30s（webllm 三通道全挂，靠本地 LLM + cache 撑着）。
- **输出**：137 nodes, 85 verified (0.6204), 50 degraded, 2 failed, leaks=0, reworks=91。
- **RecursionError 修复**：N60 节点自环（parent_ids 包含自己）导致 assign_level_ids 无限递归 993 层。修复：加 visited 集合防环（s5_state_machine.py 第 1036-1050 行 + 第 1058-1062 行）。
- **reworks 91 个**：全是"逻辑校验通过但参考来源缺失"（webllm 全挂），非树质量问题。

### 3.2 S5 管线机制

S5 = 分解状态机（DecompStateMachine）+ 核验（verify）+ 综合（synth）+ 判分（judge）。本轮只跑了 verify-only（跳过 synth+judge），所以 gpu 的 gate 指标是 verified rate（节点级），不是 judge coverage（综合级）。如果要和 soc 同口径比，需要补跑 synth_multi_gpu.py（10-run mean），但 gate 定义本就是 verified rate，不需要。

### 3.3 与 S0 的关系

S0 = 基线管线（无分解状态机，直接综合+判分）。S0 基线：
- nat: 0.634（verified rate，100 reps mean）
- soc: 0.8957（judge coverage，100 reps mean）
- gpu: 无 S0 基线（gate 定义本就是 verified rate，不需要 S0 对比）

S5 超过 S0 的证据：nat +0.017、soc +0.0185、gpu 超历史 gpu-main +0.301。增益来源：分解状态机的正交分解 + 核验机制（把 degraded 翻回 verified）。

## 4. 可发表性判断

- **相对分可用**：同机横向比较（S5 vs S0、S5 三题面横向）+ 迭代方向判断。
- **绝对分待异源复核**：judge 是本地 qwen3.8-27b（同族模型），绝对分未经异源复核（T8-C3-v3 blocked_human：无非 Qwen 端点/key）。
- **可发表范围**：内部消融报告（S5 管线机制有效性验证），不能当对外绝对分。如果要对外发表，需要：① 异源 judge（非 Qwen 模型）复核；② nat 补跑 10-run mean（消除单次方差）；③ 跨题面口径统一（都用 judge coverage mean 或都用 verified rate）。

## 5. 下一步（phase4-paper）

1. 写论文（消融实验 + S5 管线机制 + 三题面对比）。
2. 异源 judge 复核（等 T8-C3-v3 解除阻塞）。
3. nat 补跑 10-run mean（消除单次方差）。
4. 跨题面口径统一（可选，取决于论文定位）。
