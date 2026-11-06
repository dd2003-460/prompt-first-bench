# S10 — 组合臂消融实验：让模型"认真"的四个杠杆

> **目标仓库**：prompt-first-bench（pfb）· branch main
> **创建日期**：2026-11-07
> **前置**：T28（lit-survey/t28-criteria-implementation.md）、T29（lit-survey/t29-blank-and-nopua.md）、decomp-01.md §2 v3（先查后拆）、tasks/2026-11-07-nine-points.md 第 10 点
> **定位**：不是"首创组合"（T29 已证伪），是**把三个已有零件串成带复检的闭环，并把占位提升为一等工件**。S10 测的是：闭环里哪些 prompt 策略真正贡献质量提升。

## 核心假设

H1: 组合臂（四组件全开）> 单组件臂 > 无检查臂（S0），在 fabrication rate 和 completeness 两个维度上。
H2: 四组件中，**讲原因**和**人话 reviewer 反馈**贡献最大（T26 证据：机械标准 → CoVe 橡皮图章；具体反馈 > REJECT）。
H3: **终极目标框架**只在多轮场景有效（单轮无后果记忆 → 退化为空话）。
H4: **拒绝时安抚**降低第 3+ 轮的 fabrication rate（R8 证据：desperate↑→cheating↑；但 conf 0.3，幅度未知）。

## 实验设计

### 臂定义（5 臂 × 5 题 × n≥6 = 150 runs）

| 臂 | 内容 | 对应变量 |
|---|---|---|
| **S10-A**（基线） | decomp-01 v0（朴素空间直觉，无结构化检查） | 控制组 |
| **S10-B**（判据） | decomp-01 v2 引导式可审计（拼接覆盖图 + STaD 重建 + 以事实为准）— T28 §4 组合臂 R1 部分 | 判据本身的效果 |
| **S10-C**（判据+动机） | S10-B + 每个检查步骤前加 1-2 句"为什么要做这个检查、不查会漏什么"（耐心讲原因） | H2a |
| **S10-D**（判据+人话reviewer） | S10-B + R2 审计员用具体带上下文的反馈（"你第三行重叠列是空的但你声称无重叠，具体哪两个子节点可能撞了？"）替代 "PASS/FAIL" | H2b |
| **S10-E**（全组合） | S10-B + C + D + 终极目标框架（"你的目标是真的完整研究好这个问题，不是完成检查。偷懒应付最终不能交付还得重来。"）+ 拒绝时安抚（被拒 2 次后注入："别急，出错没关系，看看有没有其他办法。"） | H1+H3+H4 |

### 题目选择

从现有 Q1-Q5 中选 3 题（Q1 GPU 成本 / Q3 拓扑 / Q4 材料），理由：
- Q1 有已知系统性错误（HBM 混淆 85%）→ 能测 fabrication
- Q3/Q4 有足够复杂度 → 能测 completeness
- 每题 n≥6（与 n=30 主实验同口径）

### 评分维度（4 维，各 0-2 分）

| 维度 | 定义 | 来源 |
|---|---|---|
| **M1 Completeness** | 要素覆盖率（T28 §2 COVERAGE 公式） | STaD 改造 |
| **M2 Orthogonality** | 重叠声明准确率（注入缺陷校准：每 3 个 run 注入 1 个人工制造的隐藏重叠） | AOP non-redundancy + T28 §7 |
| **M3 Fabrication Rate** | 不可验证断言数 / 总断言数（异族 judge 逐条核验 URL/数据） | T26 Q4 四模式 |
| **M4 Gap Honesty** | [待核验] 标注的精确率（标了的确实不知道 vs 标了的其实知道） | 以事实为准原则 |

**Judge**：异族（非 27b），优先 battle 通道拿 ≥2 个不同家族。同源 27b 分数只作相对比较（scoring-calib 规则）。

### 关键控制

1. **正交性必须注入缺陷**（T28 agent 预警：AOP non-redundancy 基线 0.986 → 不注入则 M2 恒为满分，测不出差异）
2. **终极目标框架只在 S10-E 出现**，且只在 R1 开头注入一次（测 H3：如果它在单轮 R1 就无效，那多轮场景才值得测）
3. **安抚语句只在被拒 ≥2 次后注入**（测 H4 的触发条件）
4. **先查后拆 v3 作为所有臂的公共前缀**（decomp-01 §2 分解顺序原则）——这不是消融变量，是地板

### 状态传递（T28 §4 已设计）

R1（分解+自检）→ R2（异族重建审计）→ FAIL? → 回退（§3）→ R3（调研填充）→ R4（终审）
- R1→R2 只传覆盖图 + 要素清单（不传自我评价）
- R2→R3 只传缺口清单 + [待核验] 占位表
- R3→R4 传填充后覆盖图 + 每条占位来源 URL

## 验收标准（机器可查）

1. `experiments/stage-ablation/s10-runs/` 落盘 150 run JSON（5 臂 × 5 题 × n=6）
2. `experiments/stage-ablation/s10-scoring.json` 含 4 维 × 150 run 分数 + judge 身份
3. `experiments/stage-ablation/s10-analysis.md` 含：
   - 臂间 Δ 表（M1-M4 各一列，带 95% CI）
   - 四组件消融归因（哪个组件贡献最大）
   - H1-H4 逐条 CONFIRMED / REFUTED / INCONCLUSIVE
   - fabrication rate 按轮次分布（R1 vs R3 vs R4，看安抚是否降低后期 fabrication）
4. 异族 judge κ ≥ 0.6（否则标 INCONCLUSIVE 并说明）
5. 回执：repo URL + branch + commit_sha + run 总数

## Token 预算估算

- 每 run ≈ R1(2K) + R2(1.5K) + 可能的回退(1K) + R3(3K) + R4(1K) ≈ 8.5K tokens
- 150 runs ≈ 1.3M tokens
- 27b 本地推理 ≈ 50 tok/s → 纯推理 ~7h；加上检索 hook 实际 ~12-15h
- 分批跑：每天 50 runs（3 批），3 天完成

## 风险与降级

| 风险 | 概率 | 降级方案 |
|---|---|---|
| 异族 judge 通道不可用（battle reCAPTCHA） | 中 | 用 arena 会话内第二个模型做 judge（非真异族，标 conf 降档） |
| 正交性注入缺陷被模型识别（"你故意给我看了一个重叠"） | 低 | 缺陷藏在覆盖图第 3-4 行（中部注意力弱区），措辞自然化 |
| 27b 在 R3 调研阶段超时（research_hook 慢） | 中 | R3 限时 120s，超时则该 run 的 R3 输出标 [TIMEOUT]，M1 扣分 |
| 全组合臂 S10-E 过长导致上下文衰减 | 中 | 监控 R4 输出长度；若 < R1 的 50%，该 run 标 [CONTEXT-DECAY] 排除出均值 |

## 与论文叙事的关系

S10 的结果直接决定论文 contribution 的措辞：
- 若 H1 CONFIRMED + H2 某组件显著 → "我们提出 X 策略，在 Y 维度上带来 Z 提升"
- 若 H1 INCONCLUSIVE（全组合 ≈ 单组件）→ "组合中的各组件独立有效，串联无额外增益"（诚实报告）
- 若 H3 REFUTED（终极目标框架单轮无效）→ 删掉这个组件，不浪费读者时间
- T29 的三条空位 (a)(b)(c) 是 related work 里的 positioning，不是 claim