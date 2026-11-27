# N94: Qwen3-27B 在 INT4 (AWQ) 量化下，HumanEval 代码生成任务 (Pass@1) 的准确率下降幅度：相比 BF16 基线 (约 70-7

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，HumanEval 代码生成任务 (Pass@1) 的准确率下降幅度：相比 BF16 基线 (约 70-75%)，INT4 版本 Pass@1 通常下降 5-10 个百分点 (即降至 60-70%)，对应 Q_score 约为 0.85-0.93。代码生成任务对量化噪声更敏感，因为代码逻辑依赖精确的 token 概率分布，小误差易导致语法错误。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，HumanEval 代码生成任务 (Pass@1) 的准确率相比 BF16 基线通常会出现一定程度的下降（具体幅度取决于量化实现和评测细节，一般认为在几个百分点范围内），对应 Q_score 会有所降低。代码生成任务对量化噪声较敏感，因为代码逻辑依赖精确的 token 概率分布，小误差易导致语法错误。

## Evidence

[质询]具体数值（BF16基线70-75%、下降5-10个百分点、Q_score 0.85-0.93）属于特定模型版本和量化配置下的经验测量数据，缺乏通用性，且不同评测集（如HumanEval vs MBPP）和量化实现细节会导致结果波动，直接断言固定区间存在过度精确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3 27B AWQ INT4 HumanEval Pass@1 accuracy drop
