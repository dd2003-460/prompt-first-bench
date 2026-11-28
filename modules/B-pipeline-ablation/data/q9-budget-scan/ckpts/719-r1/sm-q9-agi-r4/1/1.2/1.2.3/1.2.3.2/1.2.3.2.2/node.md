# N395: Attention Score 分布扰动量 δ_S 在 L=128k 时的 L2 范数实测值：δ_S(128k) = ||S_fp8 - S_fp16||_2，

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N130

## Claim

Attention Score 分布扰动量 δ_S 在 L=128k 时的 L2 范数实测值：δ_S(128k) = ||S_fp8 - S_fp16||_2，用于验证线性增长假设，预期值约为 δ_S(32k) 的 4 倍 [待核验]。

## Corrected Claim

Attention Score 分布扰动量 δ_S 在 L=128k 时的 L2 范数实测值 δ_S(128k) = ||S_fp8 - S_fp16||_2，用于验证线性增长假设，预期值可能约为 δ_S(32k) 的 4 倍，但需实际测量确认。

## Evidence

[质询]该陈述包含具体的实测数值关系（4倍），属于经验事实。虽然线性增长假设在理论上可能成立（取决于注意力机制的具体实现和输入分布），但缺乏实际测量数据支持，且不同模型架构或实现细节可能导致非线性偏差。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

vLLM profiling attention weights L2 norm FP8 vs FP16 128k
