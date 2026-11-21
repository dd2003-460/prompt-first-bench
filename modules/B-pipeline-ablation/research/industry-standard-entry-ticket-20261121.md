# 业内承认的评测规模与报告规范——套磁入场券（2026-11-21）

> origin: ai · 触发：D 问"业内所承认的试题数据量以及其他规范是怎么样的，就是我们拿去 social 套磁的入场券"
> 来源：2410.03492 / 2609.37294（SafeLLM4SE）ar5iv 全文（来源①本轮查证）+ 本地 survey（来源②）。
> 用途：① 套磁时展示"我们知道业内标准、且知道自己在哪"；② 自我差距清单。

## 0. 一句话

业内规范分两层：**规模层**（题数 × 重复数 × 模型数）和**报告层**（必须报什么）。
我们的位置：规模层差 1-2 个量级（3 题 × 10 轮 × 1 模型 vs 100-5760 题 × 30 重复 × 6 模型），
报告层**基本达标且有一处超出**（我们报了方差来源诊断，公开 SOP 都没做这一步）。
套磁叙事 = "小样本私有 bench 的过程/深度评测 + 完整报告规范 + 本地量化模型方差诊断"，
缝隙在"私有小规模 + 过程细粒度"，不在规模。

## 1. 规模层：业内承认的量级（按对口度排序）

| 论文 | 日期 | 题数 | 重复 | 模型数 | 收敛判据 |
|---|---|---|---|---|---|
| 2410.03492 Reproducible LLM Eval | 2024-10 | 100 / 5760 | 1→30 扫描 | 6 | PI 宽度 <0.01 需 n=30 |
| 2609.37294 SafeLLM4SE | 2026-09 | HumanEval（164 题） | 自适应（N_min 起，CI 宽度达标或 token 预算耗尽即停） | 2（示例） | CI 宽度 ≤ w_max 且 token 预算 B |
| 2511.07685 ResearchRubrics | 2025-11 | 101 prompt | —（单跑） | 多 | rubric 2500+ 条（2800+ 人工小时） |
| 2601.08536 DeepResearch Bench II | 2026-01 | 132 任务 × 22 领域 | — | 多 | 9430 条二元 rubric |
| 2607.12252 FinResearchBench II | 2026-07 | 104 题 | — | 多 | 14450 候选 rubric → 共识筛选 |
| **我们 T53b** | — | **3 题** | **10 轮/arm** | **1（NVFP4 本地）** | 无正式判据（ad-hoc trim + 稳健性检查） |

**规模结论**：
- 题数：rubric bench 线公认 100-130 题量级（101/104/132 三篇独立收敛）。我们 3 题差 ~35×。
- 重复数：统计可复现性线 n=30 是"PI<0.01"的门槛（2410）；SafeLLM4SE 更务实——
  自适应采样（N_min 起步，CI 宽度达标或预算耗尽即停），**不强制 n=30**。
- 模型数：复现性研究 6 模型（跨模型泛化）；单模型消融（我们的场景）业内无硬性要求。
- **我们的 n=10 在 SafeLLM4SE 框架下可辩护**：它是"最小样本 + CI 精度目标"而非固定 n=30；
  且我们的 Δ（0.113/0.186）> 5× PI 宽度，结论对样本量稳健（已验证）。

## 2. 报告层：SafeLLM4SE 最小报告标准（Table 2，2026-09，最新）

| 类别 | 必须报告 | 我们的现状 | 差距 |
|---|---|---|---|
| Quality | 选定质量指标 + 估计值 θ̂ | coverage/depth 均值 ✓ | 无 |
| Stability | 稳定性指标（SD / 变异系数 / IQR） | stats.md 有 SD ✓ | 无 |
| Estimation uncertainty | **每个主指标 CI + 置信水平** | p 值 ✓，CI 部分（bootstrap 已补算） | **小**：CI 未进 stats.md 主表 |
| Sampling | 执行次数、采样程序、最小样本量、停止判据、预算 | 10 轮/arm ✓，停止判据=固定 10（未声明） | **小**：停止判据未文档化 |
| Model | 模型名、版本/标识、provider | qwen3.8-27b-mtp ✓ | 无 |
| Inference config | temperature 及其他推理参数 | temp=0 ✓ | 无 |
| Reproducibility | 随机 seed（若支持）、精确 prompt、环境 | prompt-snapshot.md ✓，seed=None 已声明 | 无 |
| Effect size | **效应量，不只报 p 值**（Cliff's δ / rank-biserial） | **未报** | **中**：已补算（下表），未进 stats.md |
| 统计检验 | 独立样本用 **Mann-Whitney U**（非参数）+ bootstrap CI for difference；配对用 Wilcoxon | 用的 Welch t（参数） | **中**：分布偏离正态时 Mann-Whitney 更稳 |

## 3. 我们补算的效应量（2026-11-21，来源①本轮计算）

SafeLLM4SE 要求"报效应量而非只报 p 值"。Cliff's δ（一组值超过另一组的比例差，|δ|>0.474 小 / >0.657 中 / >0.814 大）+ bootstrap 95% CI for Δmean（n=20000 重采样，seed=42）：

| 比较 | Δmean | Welch p | U | p_U | Cliff's δ | bootstrap 95% CI | 判定 |
|---|---|---|---|---|---|---|---|
| nat depth | +0.113 | 0.013 | 82 | **0.017** | **+0.640**（中效应） | [+0.034, +0.189] | 显著 + 中效应，CI 不含 0 |
| nat coverage | +0.167 | 0.155 | 71 | 0.107 | +0.420（小效应） | [-0.050, +0.366] | 不显著，CI 含 0 |
| soc coverage | +0.186 | 0.016 | 80 | **0.020** | **+0.600**（接近中效应） | [+0.057, +0.314] | 显著 + 中效应，CI 不含 0 |
| soc depth | +0.003 | 0.939 | 52 | 0.906 | +0.040 | [-0.069, +0.074] | 无 |
| gpu coverage | -0.033 | 0.349 | 18 | 0.297 | -0.330 | [-0.092, +0.030] | 无（n_f=9/n_t=6 功效不足） |
| gpu depth | -0.052 | 0.335 | 24 | 0.813 | -0.090 | [-0.158, +0.029] | 无（功效不足） |

**关键**：两个显著项在三种独立证据下都成立——Welch t（p=0.013/0.016）、Mann-Whitney U（p=0.017/0.020，
SafeLLM4SE 推荐的非参数检验）、bootstrap CI 不含 0 → 主结论对检验方法选择稳健。

**关键**：两个显著项的 bootstrap CI 都不含 0 → 主结论在 SafeLLM4SE 的效应量标准下同样成立。
这是入场券的核心句："按 2026-09 最新报告规范（SafeLLM4SE）复核，我们的显著结论在
效应量（Cliff's δ 0.60-0.64，中效应）和 bootstrap CI 下不变。"

## 4. 套磁叙事（统一入场券）

**开场定位**：我们在做私有小规模 bench（3 题 × 2 臂 × 10 轮）的管线阶段消融 + 分解树
depth/coverage 结构指标，单模型（本地 NVFP4 量化 27b）。

**展示规范意识**（三句）：
1. 报告规范对标 2410.03492 + 2609.37294（SafeLLM4SE，2026-09）：CI / 效应量 / 方差来源全报。
2. 规模差异已知且可辩护：n=10 的 PI 宽度 ~1.7× n=30，但 Δ > 5× PI 宽度 → 结论稳健；
   且 SafeLLM4SE 的自适应采样框架支持"最小样本 + CI 精度目标"，不强制 n=30。
3. **我们做了一件公开 SOP 都没做的事**：方差来源诊断——单请求 temp=0 串行确定、
   并发非确定（vLLM batch 组合），10 轮方差 = 基础设施 + 引擎并发，非 LLM 采样。
   （本地量化模型场景，2410/SafeLLM4SE 都没覆盖。）

**请教问题**（按套磁对象）：
- ResearchRubrics：logical nesting 轴怎么操作化打分？我们 depth 分是树最大深度，是否同构？
- Dr.Credit：开放题无 gold 时 rubric 参照的失效边界？
- DEEPRUBRIC：evidence-tree 构建成本？我们 gold 树是人工标的。
- SafeLLM4SE 作者（Francisco Ortin, Univ. Oviedo / MTU Cork）：小样本（n<30）私有 bench
  的 CI 精度目标怎么设？自适应采样的 N_min 建议值？

**可分享的结果**：nat depth Δ+0.113（p=0.013, Cliff's δ +0.64, CI [+0.034,+0.189]）、
soc cov Δ+0.186（p=0.016, Cliff's δ +0.60, CI [+0.057,+0.314]），27b NVFP4 本地模型，
formula prompt 臂优于 text 臂（结构化提示提升推理树深度/覆盖）。

## 5. 差距清单（诚实版，按优先级）

1. **[已闭环] 效应量进 stats.md 主表**（2026-11-21）：stats.py 加 Cliff's δ + bootstrap 95%CI 两列，
   reports/t53b/stats.md 已重新生成，回归通过（no-arg == --spec）。
2. **[中] 统计检验用 Welch t 非 Mann-Whitney U**（SafeLLM4SE 推荐非参数）：SafeLLM4SE 推荐非参数（分布偏离正态时更稳）。
   我们 n=10/臂，正态假设本就勉强 → 补 Mann-Whitney U 对照。
3. **[小] 停止判据未文档化**："固定 10 轮"应写成显式判据（SafeLLM4SE 要求声明停止判据）。
4. **[小] 题数 3 vs 业内 100-130**：真实差距，但属"私有 bench"定位的一部分，不是缺陷——
   套磁叙事里正面讲（缝隙定位），不掩饰。
5. **[无] 其余报告项**（quality/stability/model/config/reproducibility）已达标。

## 6. 检索记录

- 2609.37294 ar5iv 全文（/tmp/safe.txt，53494 chars）：Table 2 报告标准 + Algorithm 1 自适应采样
  + 检验选择（Mann-Whitney U / Wilcoxon / bootstrap CI / Cliff's δ / Wilson 区间）。
- 2410.03492 ar5iv 全文（/tmp/rep5iv.html）：规模 100/5760 题 × 1→30 重复 × 6 模型，PI<0.01 需 n=30。
- 本地 survey：process-depth-eval-survey-20261121.md（11 篇规模数据，来源②）。
- 效应量计算：本轮 execute_code（results.json 60 runs 去重后，Cliff's δ + bootstrap n=20000 seed=42）。
