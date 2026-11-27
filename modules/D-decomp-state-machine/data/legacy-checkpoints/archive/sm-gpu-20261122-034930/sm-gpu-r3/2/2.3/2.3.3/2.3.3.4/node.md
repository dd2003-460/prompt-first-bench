# N233: W4权重+INT8 KV Cache组合下，Qwen3-27B在MMLU基准测试中的准确率损失预计为3-5% [待核验]，该数值需与BF16基准（<0.5%损失

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

W4权重+INT8 KV Cache组合下，Qwen3-27B在MMLU基准测试中的准确率损失预计为3-5% [待核验]，该数值需与BF16基准（<0.5%损失）对比，以量化精度下降幅度，并作为是否选择该组合的决策依据。

## Corrected Claim

W4权重+INT8 KV Cache组合下，Qwen3-27B在MMLU基准测试中的准确率预计会有显著损失（通常高于BF16基准的<0.5%损失），具体数值需通过实际量化实验验证，通常预期在3-5%左右，该幅度可作为评估该组合可行性的参考依据。

## Evidence

[质询]该陈述包含具体的经验性数值预测（3-5%准确率损失），属于硬件/模型量化后的性能表现，无法从第一性原理推导，且缺乏具体实验数据支持，存在数值量级不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B W4 INT8 KV cache MMLU accuracy loss
