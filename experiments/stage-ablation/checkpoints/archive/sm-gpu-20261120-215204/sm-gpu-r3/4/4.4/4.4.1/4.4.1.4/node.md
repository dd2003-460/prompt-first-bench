# N298: KV Cache 精度对输出质量的影响量化：INT8 KV Cache 相比 BF16 在 MMLU 基准上通常导致 <1% 的准确率下降，而 FP8 KV C

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

KV Cache 精度对输出质量的影响量化：INT8 KV Cache 相比 BF16 在 MMLU 基准上通常导致 <1% 的准确率下降，而 FP8 KV Cache 几乎无感知损失 (<0.5%)，因此 N104 中'固定 BF16'并非绝对约束，而是保守策略

## Corrected Claim

INT8 KV Cache 相比 BF16 在 MMLU 基准上通常导致较小的准确率下降，而 FP8 KV Cache 损失更小，因此 N104 中'固定 BF16'并非绝对约束，而是保守策略

## Evidence

[质询]该陈述包含具体的经验性数值（INT8 <1%, FP8 <0.5%），属于硬件/模型性能经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

KV cache quantization FP8 INT8 accuracy loss MMLU benchmark
