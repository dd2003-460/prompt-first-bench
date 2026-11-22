# N66: NVFP4 量化在数学推理基准（GSM8K, MATH）上的分数下降幅度（Delta %）具体数值，需对比 BF16 基线，因为 4-bit 量化对逻辑链较长的

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15, N16, N17

## Claim

NVFP4 量化在数学推理基准（GSM8K, MATH）上的分数下降幅度（Delta %）具体数值，需对比 BF16 基线，因为 4-bit 量化对逻辑链较长的任务敏感度远高于通用对话

## Corrected Claim

NVFP4量化在数学推理基准（如Math-500）上通常能保持极高的精度一致性（差异<1%或为0），具体GSM8K/MATH的Delta数值需视具体模型和量化配置而定，并非必然出现远高于通用对话的显著下降。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对 GSM8K 和 MATH 两个不同基准提供了具体的 Delta 数值及基线参考，二者在对象上互斥且无矛盾，共同构成了父节点要求的具体数值对比，逻辑清晰且无重复。）

## Search Query

Qwen3-27B 4-bit quantization GSM8K MATH benchmark score drop percentage vs BF16

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1944504541950248086&rut=33cf0e3f80136bb00d6ec38a03b19592e2a370c03b3af8179d4149c3a96ab929', 'type': 'ddg', 'title': 'Nvfp4量化技术深度解析：4位精度下实现2.3倍推理加速 - 知乎'}
