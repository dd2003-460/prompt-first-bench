# N298: Qwen3-27B 在 W4/INT4 量化、4K 上下文长度下 WikiText2 数据集的困惑度 (PPL_W4_4K) 具体数值，用于计算短上下文下的量化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N98

## Claim

Qwen3-27B 在 W4/INT4 量化、4K 上下文长度下 WikiText2 数据集的困惑度 (PPL_W4_4K) 具体数值，用于计算短上下文下的量化误差基线 ΔPPL_4K = PPL_W4_4K - PPL_BF16_4K。

## Corrected Claim

Qwen3-27B 在 W4/INT4 量化、4K 上下文长度下 WikiText2 数据集的困惑度 (PPL_W4_4K) 的具体数值需查阅特定量化方案（如GPTQ/AWQ）的官方基准测试报告，无法从当前来源直接获取确切数值。

## Evidence

[质询]该陈述要求提供具体的数值（PPL_W4_4K），但参考来源为空，无法验证具体数值是否准确，且不同量化实现（如GPTQ, AWQ, SmoothQuant）可能导致数值差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT4 W4 quantized WikiText2 perplexity 4K benchmark
