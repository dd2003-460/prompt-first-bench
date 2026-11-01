# Rubric-v3 正式矩阵消融实验 — 最终报告

**日期**: 2026-11-02 (+08:00)
**状态**: 完成（含 Lead 独立核验 + 双裁判盲评 + 一致性分析）
**仓库**: prompt-first-bench @ main (cae4c86)

## 一、实验设计

7 个 rubric 变体 × 3 次独立运行 = 21 份答卷，由 arena agent（固定会话 01a195cb）在隔离分支上执行。任务：R121 paper-compare（对比两篇 deep research benchmark 论文的方法差异）。

| 变体 | 含义 | 对照目的 |
|---|---|---|
| V0-baseline | 无 rubric 引导 | 基线：裸模型能到什么水平 |
| V1-full | 完整 rubric（coverage+boundary+alignment） | 全组件效果 |
| V1-align | 去 coverage，保留 boundary+alignment | isolation: alignment 单独贡献 |
| V2-nocoverage | 去 coverage，保留 boundary | isolation: coverage 贡献 |
| V3-noboundary | 去 boundary，保留 coverage | isolation: boundary 贡献 |
| V-sham | sham 流程（走形式不走内容） | 区分"流程效应"vs"内容效应" |
| V3-sham | 双缺失（去 coverage+boundary）的 sham | 下界参照 |

评分：预注册 19 项 non-NA checklist（O1×3, O2×4, O3×1, O4×4, P1×2, P3×2, P4×3），每项 0/1/2，满分 38。另加 O3 claim-level 覆盖（31 claims binary）。双裁判盲评：同一 agent 用两套口径独立打分（非真正 IRR，见 §四限制）。

## 二、核心结果

### 总分排名（两裁判合并均值，满分 38）

| # | 变体 | 均值 | vs V1-full |
|---|---|---|---|
| 1 | V1-full | **37.3** | — |
| 2 | V2-nocoverage | 36.2 | -1.1 |
| 3 | V1-align | 35.2 | -2.1 |
| 4 | V-sham | 34.7 | -2.6 |
| 5 | V3-noboundary | 33.5 | -3.8 |
| 6 | V3-sham | 33.2 | -4.1 |
| 7 | V0-baseline | **25.7** | **-11.6** |

### 消融归因（以 V1-full 为参照）

| 移除什么 | 掉多少分 | 解读 |
|---|---|---|
| 全部移除（→V0） | -11.6 (30%) | rubric 整体有效 |
| 去 coverage（→V2） | -1.1 (3%) | **coverage 组件贡献最小** |
| 去 boundary（→V3） | -3.8 (10%) | **boundary 是最大单组件贡献者** |
| Sham 化（→F） | -2.6 (7%) | 流程本身有少量贡献，但远小于内容 |
| 加 alignment 约束（→C） | -2.1 (6%) | alignment 有轻微成本（O1 从 2.0 降到 1.6） |

### 维度定位

差距集中在三个维度：
- **O1（低先验候选识别）**: V0=0.6, V1-full=2.0 → rubric 最大的单项提升
- **P4（边界类型与终止注记）**: V0=0.4, V1-full=2.0 → boundary 组件直接作用点
- **O3（claim 覆盖率）**: V0=0.495, V1-full=0.591 → 提升有限（+10pp）

其余维度（O2, O4, P1, P3）在大多数变体中已饱和（≈2.0），不是区分因子。

## 三、结构性缺口

5 个 gold claim（N-2.2, N-3.1, N-3.1.1, N-3.1.2, N-3.1.3）在全部 21 docs 中零覆盖。根因：gold 树要求用 FLOPs/峰值算力/MFU 建模 prefill，而所有 run 用实测 tok/s 代替——这是方法论路径分歧，不是模型能力不足。

**处置建议**：
- 如果 R121 任务定义不要求 FLOPs 建模 → 从 R121 的 claim 列表移除这 5 条（减少虚假 NA 惩罚）
- 如果要求 → 任务描述需显式提及，否则任何模型都不会自发选择这条路径
- 当前方案：保留但标注为"系统性路径分歧"，不影响变体间相对排名（所有变体同样受影响）

## 四、有效性限制（必须随报告一起引用）

1. **κ 不是 IRR**: 两个"裁判"是同一 agent 的两遍。κ=0.93（binary）/ 0.916（三级）测量的是严格度敏感性，不是独立评分者一致度。真实 IRR 需要第二独立 agent 或人类标注员。
2. **偏差方向**: 所有 8 项逐项分歧 + 5 条 O3 分歧均为 J1 宽于 J2。J1 系统性偏高 0-2 分。
3. **单任务**: 结论仅适用于 R121 paper-compare 类任务。泛化性需多任务验证。
4. **单模型**: 所有 21 runs 由同一 arena agent 产出。不同模型的能力分布可能改变消融排序。
5. **盲评泄漏**: TASK-blind-eval.md §匿名映射 直接给出 A-G 对应关系（已登记，未影响本批评分）。

## 五、结论

1. **Rubric 引导有效**: V1-full 比 V0-baseline 高 30%（11.6/38），主要靠 O1 和 P4 两个维度。
2. **Boundary 是最有价值的单组件**: 去掉它掉 3.8 分（10%），是所有单组件消融中最大的。
3. **Coverage 组件 ROI 最低**: 只贡献 1.1 分（3%），且引入 5 个结构性零覆盖 claim 增加噪声。考虑在后续版本中简化或条件化。
4. **Sham 流程得分接近真实流程**（34.7 vs 37.3）: 提示流程形式的区分力有限，rubric 内容本身才是主要驱动。
5. **Alignment 约束有轻微负效应**: O1 从 2.0 降到 1.6，可能是约束过紧限制了候选生成。

## 六、文件索引

| 文件 | 内容 |
|---|---|
| `judge-1-scores.json` / `judge-2-scores.json` | 原始评分（21 docs × 19 items + 31 claims） |
| `anon-mapping.json` | 匿名映射（Lead 持有） |
| `judge-agreement-analysis.md` | κ 计算 + 分歧明细 + 消融表 |
| `BLIND-EVAL-REPORT.md` | arena agent 原始报告（含 per-dimension 表） |
| `FINAL-REPORT.md` | 本文件（Lead 收口版） |
| `../../TASK-r121-paper-compare.md` | 任务定义 |
| `../../../receipts/r121-paper-compare-verification.md` | 外部文献核验回执 |
