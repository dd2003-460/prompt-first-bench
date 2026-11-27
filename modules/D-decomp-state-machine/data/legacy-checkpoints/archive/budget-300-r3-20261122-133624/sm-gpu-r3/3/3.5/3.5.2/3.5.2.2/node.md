# N287: 在 RTX 4090 上通过软件模拟 FP8 推理时，数值转换误差（FP8->BF16->FP8 往返转换中的舍入误差累积）导致的 WikiText-103 P

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

在 RTX 4090 上通过软件模拟 FP8 推理时，数值转换误差（FP8->BF16->FP8 往返转换中的舍入误差累积）导致的 WikiText-103 PPL 额外损失并非固定的 0.02-0.05，而是与序列长度正相关：在 32K 上下文下，由于误差在 Transformer 层间累积，PPL 额外损失预计达到 0.08-0.12，使总 PPL 损失从 Hopper 原生的 0.05-0.15 升至 0.13-0.27。

## Corrected Claim

在 RTX 4090 上通过软件模拟 FP8 推理时，数值转换误差导致的 WikiText-103 PPL 额外损失预计与序列长度正相关，在 32K 上下文下可能高于短序列场景，但具体数值范围（如 0.08-0.12）缺乏实证数据支持。

## Evidence

[质询]该陈述包含具体的经验数值（PPL损失范围0.08-0.12及总损失0.13-0.27），属于经验事实而非第一性原理可推导的数学/物理定律。在缺乏任何外部来源支持的情况下，无法验证这些具体数值量级的准确性，且‘正相关’的具体量化关系缺乏实证数据支撑。 | 经验事实，逻辑自洽（误差累积导致长序列PPL损失增加符合直觉）但缺来源支持，且检索无可用来源，无法验证具体数值。

## Search Query

RTX 4090 FP8 emulation accuracy loss WikiText perplexity degradation long context
