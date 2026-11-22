# N352: M2 Ultra 在 INT4 量化精度下的工作点：理论 TPS 59.2 tokens/s (800GB/s / 13.5GB)，硬件成本不变，5年TCO 不

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

M2 Ultra 在 INT4 量化精度下的工作点：理论 TPS 59.2 tokens/s (800GB/s / 13.5GB)，硬件成本不变，5年TCO 不变；吞吐量达 BF16 的 4 倍，但 INT4 量化通常导致显著的质量损失（MMLU 下降 3-5% [待核验]），仅在非关键任务或允许高幻觉率的场景下可行。

## Corrected Claim

M2 Ultra 在 INT4 量化精度下的工作点：理论 TPS 59.2 tokens/s (800GB/s / 13.5GB)，硬件成本不变，5年TCO 不变；吞吐量达 BF16 的 4 倍，但 INT4 量化通常导致一定程度的质量损失（具体幅度依模型和量化方法而定），仅在非关键任务或允许高幻觉率的场景下可行。

## Evidence

[质询]MMLU下降3-5%的具体数值缺乏通用基准支持，不同模型和量化方法（如GPTQ vs AWQ）差异巨大，且'显著质量损失'的定性描述与'3-5%'的定量数据可能存在口径不一致或过度简化。 | source=knowledge，逻辑自洽（TPS计算符合带宽瓶颈模型，4倍吞吐量符合INT4 vs BF16位宽比），但MMLU下降幅度为经验事实且无来源支持，依据经验事实排除条款降级。
