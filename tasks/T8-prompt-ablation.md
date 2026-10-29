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
- 注：decomp L1 已用 qwen3.8-27b 本地 ninfer（@100.112.53.47:8000），可复用环境做行为层对照

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

## Part C: 可解释性加速（r34 新增 r37 升级，核心加速器）

**原理**：全 paired runs 贵且慢。先用内部状态归因把 7 段 prompt 缩到 top-k 嫌疑段，再只对 top-k 跑 paired runs 确认。
**r37 升级（成璐指令）**：单实例跑一次拿向量不可信（单次前向噪声+任务混杂）→ 必须**双实例对照**：同变体 vs 基线，各 ≥3 seed，比较内部状态分布差异而非绝对值。用户将提供 API key 支持双实例精确实验。

### C1 内部状态归因（双实例对照协议）

工具栈（按因果强度排序）：
| 工具 | 测什么 | 因果性 | conf |
|------|--------|--------|------|
| **activation patching** | A 实例某层某位置激活 patch 到 B 实例→输出变化量 = 该位置承载的功能量 | 强（干预性） | 0.7 |
| **probing classifier** | 线性探针分类"是否发现真矛盾"(对接 M8)，看哪些层/位置可分 | 中 | 0.6 |
| **representation engineering** | 找"核验真实性""候选集冻结"概念方向向量，测 prompt 段是否激活该方向 | 中（依赖标定） | 0.6 |
| **logits lens** | 每层隐状态解码的 token 概率轨迹——prompt 段在哪层被理解 | 弱（观测性） | 0.4 |
| **attention rollout** | token 级注意力归因 | 弱 | 0.4 |
| **integrated gradients** | 输入 token 积分梯度贡献 | 中 | 0.5 |

双实例执行方案（r38 三机分工定稿）：
| 机器 | 配置 | 角色 | 能拿什么 |
|------|------|------|---------|
| **远程 ninfer** | qwen3.8-27b-w8a16 @ 100.112.53.47:8000（已验证在线） | 主算力：C1 内部状态实验 + C3 paired runs 生成 | hidden states / logits / 完整 transcript |
| **Mac (M1 Max, 64GB)** | MLX 已装 + mlx-abliteration 框架（~/D1-automation/mlx-abliteration，已有 abliteration 管线+数据集生成器） | ①消融/abliteration 交叉验证（独立于 ninfer 的第二实现）②3B 小模型快速探针 ③数据中转 | 本地激活、abliteration 效应量 |
| **Win 5060 (8GB)** | 待部署 | 行为层双实例之一（7-14B 量化跑 pipeline 行为对照）；8GB 上限 ~14B-Q4 | 完整 transcript + 最终 logits（行为层够用） |

- 实例 A = V-full，实例 B = 待测变体（V-noralph 等），同域同题，seed 集 ≥3（同温度不同 seed）
- 比较 Δ(层 l, 位置 p)：激活差 / 注意力差 / 探针得分差 / patch 效应量
- 数据流：Win/Mac 产出统一 push 到 decomp 仓 `experiments/T8-matrix/runs/`（git 中转，不搭额外同步服务）
- 产出：per-segment × per-layer 效应量矩阵；效应量≈0 的段 = 内部状态无痕迹 = 强删除候选
- 降级：Win 未部署 → Mac MLX 3B 顶行为层（conf 降档标注）；ninfer 不可用 → 全部降级 C2 行为代理

**r41 实测结论（2026-10-29，对 100.112.53.47:8000 端点逐项验证）**：
| 能力 | 状态 | 证据 |
|------|------|------|
| chat completions 推理 | ✅ 200 | 正常出 token（注意：该模型是 reasoning 模型，短 max_tokens 会全烧在 reasoning_content 上） |
| logprobs / top_logprobs | ❌ 静默忽略 | 请求带 logprobs:true 返回 200 但响应无 logprobs 字段——服务端没开 `--served-model-name`/logprobs 支持或版本裁剪 |
| return_hidden_states | ❌ 静默忽略 | 同上，响应无 hidden states |
| /v1/completions (legacy) | ❌ 404 | 端点未暴露 |
| /v1/embeddings | ❌ 404 | 端点未暴露 |

**含义**：通过 HTTP API 只能拿最终文本 + usage，**拿不到任何内部状态**（logits/hidden states/attention 全无）。C1 的 activation patching / probing / rep-engine / logits lens 走 ninfer 网关做不了。

### r46 实测突破（2026-10-29）：第三条路——llama.cpp+GGUF 与 ninfer 共存
- **已跑通**：在 ninfer 服务器上编译 llama.cpp（CUDA sm_70），用 `Qwen3.8-27B-GGUF-Q8_0.gguf`（28G）起 `llama-server --pooling last --embeddings`，`/embedding` 端点返回 **dim=5120 归一化向量**（= Qwen3.8-27B 隐藏维度）= 模型最后一层 hidden state。**不必停 ninfer 主实例、不必用 Mac MLX**。
- **语义区分度验证成功**（核心假设成立）：cos(好天气,差天气)=**0.78**（同域）≫ cos(好天气,量子纠缠)=**0.24**（跨域）→ 最后一层表征编码了 prompt 语义，可用作探针缩窄"哪个组件导致效果差异"的可疑范围。
- **限制**：①公开 API 只暴露**最后一层**，中间层需改 llama.cpp 源码加 forward hook（后续）；②与 ninfer 共存时 4×V100 各只剩 ~4GB 空闲（共 ~16GB），塞不下 28G 全模型，最多 offload ~30/65 层，其余走 CPU（被 ninfer MTP 占着）→ 单条 embedding ~60-80s，吞吐低。
- **提速选项**：临时停 ninfer 独占 64GB 全 offload（秒级，能跑完整矩阵）——需停机窗口，暂不启用。
- **现状**：probe server 保留 @127.0.0.1:8099（`-ngl 30 --device CUDA0,CUDA1,CUDA2,CUDA3` 避开 GT1010）。

- **修订分工（r46）**：**ninfer 服务器 = 双角色**（HTTP :8000 = 行为层 paired runs 生成器；llama.cpp :8099 = 最后一层 hidden-state 探针，慢速少量样本）；**Mac MLX = 中间层/全套 activation hook 主阵地**（要任意层时上）；Win 5060 = 第二行为实例（deprioritized）。

### C2 行为代理指标（零成本）
每段 prompt 签名行为出现率（对已有工件直接算）：候选集冻结声明出现率+漂移次数 / 主张带 URL 比例 / owner 标注比例 / reviewer 逐条打勾率 / ralph web-llm 调用记录（预期≈0）。

### C3 定向 paired runs（只对 top-k≤3 嫌疑段）
- 顺序门禁：C1+C2 定完 top-k 才开 C3；C3 方案先过对抗核验（r29）
- 配置：A 全量 / B 删 top-k（一次一个）/ 阳性对照（删候选集冻结，预期 M8 降）
- 样本：≥2 域 × 2 run/配置；度量 M8 + M9

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
