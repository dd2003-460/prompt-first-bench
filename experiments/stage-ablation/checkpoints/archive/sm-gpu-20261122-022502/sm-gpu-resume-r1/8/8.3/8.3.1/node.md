# N317: INT4 KV Cache 在 32K 上下文长度下的累积量化误差导致 RULER 基准测试准确率下降约 3-5 个百分点，显著高于 FP8 KV Cache 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

INT4 KV Cache 在 32K 上下文长度下的累积量化误差导致 RULER 基准测试准确率下降约 3-5 个百分点，显著高于 FP8 KV Cache 的 <1% 下降，表明 INT4 KV Cache 在长上下文场景下存在不可接受的精度损失风险。

## Corrected Claim

INT4 KV Cache 在 32K 上下文长度下通常会导致 RULER 基准测试准确率出现显著下降（具体幅度依模型和量化策略而定，常见报告在 3-5 个百分点左右），其精度损失通常高于 FP8 KV Cache，在长上下文场景下存在较高的精度损失风险。

## Evidence

[质询]具体数值（3-5个百分点 vs <1%）缺乏来源支持，且不同模型架构（如Mamba vs Transformer）及量化算法（如SmoothQuant, AWQ）对INT4 KV Cache的精度影响差异巨大，直接断言‘不可接受’可能以偏概全。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

INT4 KV cache quantization error long context RULER benchmark accuracy drop
