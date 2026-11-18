# 消融矩阵 + 前人标记任务书（cc 执行 · 2026-11-18 夜）

> origin: ai · D 指令「我要的消融矩阵和前人标记也做成任务书给cc，另外这些都可以作为研究过程记录在pfb，同时避免重复做」
> 一句话：消融矩阵（A0-A13）和前人标记（复现vs创新）的调研/分析已做完落盘，cc 只执行「待做」节，「已完成」节直接读结果不要重做。

## 0. 研究过程记录（已落盘 pfb，cc 直接读，不要重做）

这些文件是研究过程记录，已 git commit（4bf8b7d0 / 77379175），在 `pfb/experiments/stage-ablation/` 下：

| 文件 | 内容 | 状态 |
|------|------|------|
| `ablation-matrix-full.md` | A0-A13 完整矩阵定义（14臂×3题×3rep=126runs，4因子，二阶交互角点） | 已完成 |
| `ablation-prior-work-mapping.md` | C1-C10 组件 × 前人工作映射（复现vs创新 + 套磁优先级 + 来源核验状态） | 已完成 |
| `competitor-survey.md` | 前人调研原始数据（485行，2026-11-03/11-17 观察） | 已完成 |
| `s5-pipeline-spec.md` | S5 管线完整 prompt + 核验方法 + 节点通过/返工条件 | 已完成 |

## 1. 已完成（cc 不要重做，直接读结果）

- [x] 前人调研（competitor-survey.md，485行，覆盖 GPT Researcher / Arbor / FALCA / Crucible / navinsreyas / LangGraph 等）
- [x] 组件×前人映射（ablation-prior-work-mapping.md §2，C1-C10 逐个映射）
- [x] 复现vs创新清单（mapping §4：7 个复现组件 + 7 个 pfb 独有创新）
- [x] 套磁优先级（mapping §3：FALCA > Arbor > Crucible > navinsreyas > LangChain）
- [x] A0-A13 矩阵定义（ablation-matrix-full.md，含统计可估计性分析）
- [x] no_challenge bug 修复（s5_pipeline.py 加 P3_VERIFY_NC + verify_node_nc，qc_ablation_sweep.py no_challenge 分支真走它）
- [x] max_nodes 12→150（ralph-night.sh + cc-tasks/ralph-loop-night.md 重启命令更新）

## 2. 待做（cc 执行）

### T1: arXiv 编号核验（套磁前必做，30min）
- **为什么**：mapping §5 的 9 个 arXiv 编号来自 competitor-survey.md（②类来源），本轮未独立去 arXiv 核验。套磁前必须确认论文真实存在 + 内容匹配，避免套错人。
- **动作**：用 ego-browser 去 arXiv 搜编号 + 读摘要，核验 mapping §5 的 9 个编号：
  - arXiv:2606.11926（Arbor）
  - arXiv:2610.28361（FALCA）
  - arXiv:2608.06714（ReASearch）
  - arXiv:2602.22480（VeRO）
  - arXiv:2603.28052（Meta-Harness）
  - arXiv:2609.40330（Turbo Harness）
  - arXiv:2605.27276（SIA-W）
  - arXiv:2605.19156（ResearchArena）
  - arXiv:2605.20025（AutoResearchClaw）
- **核验标准**：论文标题/作者/摘要与 mapping 描述匹配 → 标「已核验」；不匹配或不存在 → 标「[不存在]」+ 记录实际找到的论文
- **落盘**：更新 mapping §5 的核验状态列（每个编号后加「已核验 YYYY-MM-DD」或「[不存在]」）
- **注意**：cc 无网络（subagent 规则），如果 cc 不能联网，由 Lead（Hermes）代查并写入文件。cc 只负责把 Lead 给的核验结果更新到 mapping §5。

### T2: 套磁信（按 mapping §3 优先级，1-2h）
- **为什么**：D 要「方便交流套磁」，重合度最高的团队最可能理解 pfb 工作、最可能合作/引用/接收。
- **动作**：按 mapping §3 优先级写套磁信：
  1. FALCA 团队（BAAI+THU+CASIA）——切入点「开放 web vs 本地 HNSW」+「prompt 版 falsification vs SFT+RL 版」
  2. Arbor 团队（RUC-NLPIR）——切入点「edge 分类（cartesian/quotient）+ insight 传播机制对比」
  3. Crucible（eren23）——切入点「judge-dependence 实证 + judge separation 方案对比」
- **套磁信模板**：
  ```
  Subject: pfb (prompt-first research) — 与 [团队名] 工作的对比与合作可能

  我们是 [D 的机构/身份]，在做 prompt-first 研究系统（pfb），核心是分解树 + falsification 核验 + rework 闭环 + 质检门。

  注意到 [团队名] 的 [论文名]（arXiv:XXXX）在 [重合组件] 上与 pfb 高度同构。我们的差异在 [创新点]。

  想讨论：
  1. [具体对比切入点]
  2. [可能的合作方向]

  附件：pfb 消融矩阵 + 前人重合映射（ablation-prior-work-mapping.md）
  ```
- **落盘**：`cc-tasks/outreach/outreach-<团队名>.md`
- **前置**：T1 核验完成（确认论文真实存在再套磁）

### T3: 论文 related work 组织（2-3h）
- **为什么**：写论文 related work 时，复现组件要引用对应论文（站在他们肩上），创新组件要强调差异化（说明贡献）。
- **动作**：按 mapping §4 组织 related work：
  - 复现组件（7 个）：引用对应论文，说明「我们复现了 X 的 Y 机制」
  - 创新组件（7 个）：强调差异化，说明「前人没有 Z，我们做了 Z」
  - 组织方式：按组件（C1-C10）分节，每节先复现（引用）再创新（差异化）
- **落盘**：`experiments/stage-ablation/related-work-draft.md`
- **格式**：markdown，每节含「复现前人（引用）+ pfb 创新（差异化）+ 来源核验状态」

### T4: 消融矩阵每个臂标注复现/创新（1h）
- **为什么**：D 要「方便标记复现和创新」，每个消融臂要标清它测的是复现前人的组件还是 pfb 独有创新。
- **动作**：在 ablation-matrix-full.md 的每个臂（A0-A13）加「复现/创新」标注列：
  - A0（基线）：复现 Arbor 树结构 + FALCA falsification
  - A1（去质询）：测 FALCA falsification 的增益（复现组件的消融）
  - A4/A5/A6（质检门）：测 pfb 独有创新（前人没有）
  - A7/A8（矛盾扫描）：测 FALCA contradiction-first（复现）+ 全局扫描（创新）
  - 等等（参考 mapping §2 的组件映射）
- **落盘**：更新 ablation-matrix-full.md 的矩阵表（加一列「复现/创新」）

### T5: A0-A13 消融 sweep 执行（10-17h，见 ralph-loop-night.md T6）
- **前置**：gptr + langgraph nat + gpu 全完成（避免抢 8787 推理）
- **命令**：
  ```bash
  cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
  /Library/Developer/CommandLineTools/usr/bin/python3 -u qc_ablation_sweep.py --arms all --qs nat,soc,gpu --reps 3 > /tmp/qc-ablation-14arms.log 2>&1 &
  ```
- **验收**：runs-qc-ablation/summary.md 存在，126 行
- **断点续跑**：step-log/{arm}-{qid}.jsonl 每步落盘 + 每 run 完成写 {arm}-{qid}-r{rep}.json，重启跳过已完成

## 3. 避免重复做（硬约束）

- **不要重新搜前人工作**（competitor-survey.md 已做完，485行）
- **不要重新做组件映射**（ablation-prior-work-mapping.md 已做完，C1-C10）
- **不要重新定义消融矩阵**（ablation-matrix-full.md 已做完，A0-A13）
- **不要重新修 no_challenge bug**（s5_pipeline.py 已修，verify_node_nc 已加）
- **不要重新改 max_nodes**（ralph-night.sh 已改回 150）
- cc 只执行「待做」节（T1-T5），「已完成」节直接读结果
- 如果发现已完成的文件有错误，记录到 mapping 的勘误节（§7 勘误），不要删改原文

## 4. 执行顺序

1. T1（arXiv 核验，30min）→ 前置 T2
2. T4（臂标注，1h）→ 独立，可并行
3. T3（related work，2-3h）→ 依赖 T1（核验后引用才准确）
4. T2（套磁信，1-2h）→ 依赖 T1（核验后套磁）
5. T5（消融 sweep，10-17h）→ 依赖 gptr+langgraph 全完成

T1 和 T4 可并行（T1 要联网/Lead 代查，T4 是纯标注）。T3/T2 等 T1 完成后做。T5 等夜间任务全完成后做。

## 5. 验收标准

- T1：mapping §5 的 9 个编号都有核验状态（已核验 / [不存在]）
- T2：cc-tasks/outreach/ 下有 ≥2 封套磁信（FALCA + Arbor）
- T3：related-work-draft.md 存在，7 个复现组件 + 7 个创新组件都有
- T4：ablation-matrix-full.md 的矩阵表有「复现/创新」列，14 臂都标了
- T5：runs-qc-ablation/summary.md 存在，126 行
