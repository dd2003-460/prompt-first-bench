# T8: prompt-first 消融研究——prompt 变体 × 任务类型 交叉矩阵

**状态**: ready（T7.1 跑完后开跑）
**执行通道**: arena agent mode @ prompt-first-bench（任务书走仓库，prompt 只指路）
**动机**（成璐 r31/r33/r34/r36 指令）：①中间轮次区分真矛盾 vs 表演 ②七阶段 prompt 逐条研究清楚 ③每类 prompt 用途/论文结论/复现完整调研 ④实验结构完整清晰 ⑤可解释性加速 ⑥按"prompt 变体 × 模型/任务类型"交叉矩阵做消融，测对不同情况的有效性 ⑦decomp 只是第一步（目标分解，最简单任务类型），pfb 全 pipeline 还很远 ⑧问 arena 内部流程 vs 我们发的 pfb 流程对比。

## 定位修正（r36）

decomp bench（ablation-L1）测的是**单 prompt 组件级**消融，对象是最简单的任务类型（目标分解）。pfb 是六阶段 pipeline，复杂度高一档，需要独立的矩阵实验体系。两者关系：L1 = 第一格（最简任务 × 组件变体），T8 = 扩展为 (任务类型 × prompt 变体) 完整矩阵。

## 实验设计：交叉矩阵

### 轴 1: 任务类型（从简到繁，逐步扩展）
| 代号 | 任务类型 | 示例域 | 复杂度 |
|------|---------|--------|--------|
| T-decomp | 目标分解（单 prompt） | GPU 选型、统计范式 | ★ |
| T-select | 选购决策（01+02+03） | 机械键盘、会议室系统 | ★★ |
| T-research | 调研+核验（01+02+02.5+03） | 竞品分析、技术选型 | ★★★ |
| T-full | 全流程（01→04.5 含回退修复） | 真实项目立项 | ★★★★ |

### 轴 2: prompt 变体（pfb pipeline 的变体）
| 代号 | 变体 | 说明 |
|------|------|------|
| V-full | 全量 pfb | 当前 loop/prompt-first/ 全部 7 段 |
| V-noralph | 删 ralph web-llm 命令段 | 疑似无效负载（arena 无 ralph） |
| V-noqc | 删各阶段 Reviewer 质检标准 | 疑似冗余 |
| V-noprinciples | 删 04.5 通用原则 12 条 | 与操作流程重叠 |
| V-nofreeze | 删候选集冻结声明 | 阳性对照（预期 M8 降） |
| V-arena-native | **arena 内部默认流程**（r36 新增） | 不发我们的 prompt，让 arena 用自己的 agent mode 默认行为 |
| V-minimal | 最小骨架（只留阶段名+输入输出格式） | 下界参照 |

### 轴 3: 模型（后续扩展，当前先固定）
- 当前：arena 默认模型（不指定）
- 后续：若 arena 支持选模型 → qwen/gpt/claude 各跑一遍
- 注：decomp L1 已用 qwen3.8-27b 本地 vLLM，可复用环境做对照

### 矩阵规模控制
- 起步：T-select × {V-full, V-noralph, V-arena-native} × 2 域 = 6 runs
- 扩展：加 T-research + V-noqc/V-noprinciples → 最多 4×7×2=56 runs（分批跑）
- 每 run ≥2 域（防 n=1 出结论）
- 判定指标：M1-M7（self-opt-tester）+ M8 核验真实性率 + M9 token 效率

## Part A: 中间轮次真实性审计（零额外 run，先做）

对象：pfb 仓全部历史核验/复核工件 + decomp ablation-L1 review 记录。
审计协议（每条"矛盾/漏洞/质疑"过三测）：
1. **具体性**：必须指向具体来源+具体字段
2. **可证伪**：该矛盾后来被跟进消解或显式保留？只写不跟 = 表演
3. **反事实**：删掉这条质疑结论会变吗？不变 = 装饰
输出：`experiments/T8-audit/intermediate-rounds-audit.md`

## Part B: 文献调研补齐（arena 代干，≥2 源 + conf）

1. multi-stage agent pipeline 各阶段 prompt 贡献度的系统性研究
2. critic/reviewer prompt 设计：什么条件真提升、什么是表演（Self-Refine/CRITIC/LLM-as-judge 偏差）
3. staged revision vs one-shot 效果对比
4. L1 组件级结论映射到 pipeline 阶段级的合理性
产出：`experiments/T8-lit/lit-survey-pipeline-prompts.md`

## Part C: 可解释性加速（C1 归因 + C2 行为代理 → 缩 top-k）

- C1: attention rollout / integrated gradients（vLLM 环境，conf≤0.5 只排序）
- C2: 每段 prompt 签名行为出现率（零成本，对已有工件直接算）
- 顺序门禁：C1+C2 定完 top-k 嫌疑段后才开定向 paired runs

## Part D: arena 内部流程对比（r36 新增，核心新维度）

**方法**：V-arena-native 变体——同一任务书发给 arena，但**不附带任何 pfb prompt 指令**，让它用自己 agent mode 的默认行为跑。收集其完整 transcript + 产出工件。

**对比维度**（逐项打分，独立 AI 裁决防自估偏差）：
| 维度 | 我们 pfb 流程 | arena 默认流程 | 差值含义 |
|------|-------------|--------------|---------|
| 候选集完整性 | 01 是否冻结+逐一核验 | 是否自行枚举+排除 | pfb 的 01 阶段价值 |
| 证据来源完备 | 02 主张带 URL/时间戳比例 | 默认引用习惯 | pfb 的 02 阶段价值 |
| 核验真实性 | M8（Part A 协议） | 同协议打分 | pfb 的 02.5 对抗核验价值 |
| 分解粒度 | 03 owner 标注+步骤可执行性 | 默认分解深度 | pfb 的 03 阶段价值 |
| 回退修复 | 04.5 反方复核后是否真改 | 默认 self-critique 行为 | pfb 的 04.5 价值 |
| token 效率 | M9 | 同口径 | 流程开销 |
| 总质量 | M1-M7 综合 | 同口径 | 端到端 |

**关键问题**（arena 自己回答，交叉核验）：
- "你的 agent mode 内部有没有类似分阶段流程？如果有，和我们发的 pfb prompt 相比，你觉得哪个方面你做得更好、哪个方面我们的更好？"
- "如果你要优化自己的默认流程，你会加什么、删什么？"
- 注意：arena 的回答本身也是数据点，需经 r29 对抗核验（找它回答里的未验证前提/样本偏差）

## Part E: 结构整改（pfb 仓 experiments/ 目录）

```
experiments/
  README.md          # 实验索引
  T8-audit/          # Part A
  T8-lit/            # Part B
  T8-matrix/         # 矩阵实验: design.md + runs/<task-type>-<variant>-<domain>/ + report.md
  T8-arena-compare/  # Part D: arena-native transcript + 对比表
```
旧资产 git mv 归位，README 登记。

## 验收标准

1. Part A 审计表覆盖全部历史核验工件
2. Part B ≥4 问全答，≥2 源 + conf，经对抗核验
3. 矩阵起步 6 runs 完成，per-(任务类型×变体) verdict 落地
4. Part D arena 对比表完整（7 维度 × 2 流程），arena 自评经对抗核验
5. 无用段落实际从 workspace loop/prompt-first/ 移除并 sync pfb
6. experiments/ 结构落地，README 索引齐全

## 失败降级

- arena 不支持选模型 → 轴 3 标 pending，先跑 2D 矩阵
- 单 run 超时 → 重跑 1 次，仍死标 VOID 换域
- arena 拒绝回答内部流程问题 → 只收 transcript 行为对比，跳过自评
- 文献某问穷尽渠道无答案 → 标"信息搜集瓶颈"，不编
