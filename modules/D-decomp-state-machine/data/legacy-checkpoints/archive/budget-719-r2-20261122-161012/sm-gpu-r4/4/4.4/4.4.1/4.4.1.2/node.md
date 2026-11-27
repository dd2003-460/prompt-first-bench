# N221: RTX 5090 单卡 BF16 不可行工作点：显存需求 55GB (权重 54GB + KV 1GB) 超出 32GB 物理显存，缺口 23GB，导致单卡 B

- **status**: pending
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

RTX 5090 单卡 BF16 不可行工作点：显存需求 55GB (权重 54GB + KV 1GB) 超出 32GB 物理显存，缺口 23GB，导致单卡 BF16 吞吐量为 0 tokens/s，必须触发量化或 Offload 机制。

## Corrected Claim

RTX 5090 单卡 BF16 不可行工作点：显存需求 55GB (权重 54GB + KV 1GB) 超出 32GB 物理显存，缺口 23GB，导致单卡 BF16 吞吐量为 0 tokens/s，必须触发量化或 Offload 机制。

## Evidence

父节点级核验未通过：不完备（子节点1详细拆解了显存需求构成，子节点2分析了Offload的代价，两者在逻辑上是‘原因分析’与‘替代方案评估’的正交关系，无重叠。但父节点明确提到‘必须触发量化或Offload机制’，子节点仅深入分析了Offload的代价，完全缺失了对‘量化方案’（如INT8/INT4）的具体分析或代价评估，导致对父节点中‘量化’这一关键分支的覆盖不完整。）
