# N362: Swap 导致的额外延迟占比公式：Overhead_% = (T_swap / T_inference) * 100，其中 T_swap = (Weight_S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N127

## Claim

Swap 导致的额外延迟占比公式：Overhead_% = (T_swap / T_inference) * 100，其中 T_swap = (Weight_Size + KV_Cache_Size) / PCIe_Bandwidth_Effective。对于 27B FP8 模型，若每次推理需重新加载部分权重，Swap 延迟将显著高于纯 GPU 计算延迟。

## Corrected Claim

Swap 导致的额外延迟占比公式：Overhead_% = (T_swap / T_inference) * 100，其中 T_swap = (Weight_Size + KV_Cache_Size) / PCIe_Bandwidth_Effective。对于 27B FP8 模型，若每次推理需重新加载部分权重，Swap 延迟将显著高于纯 GPU 计算延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（时间/时间=无量纲百分比），T_swap定义符合PCIe传输延迟计算逻辑，27B模型权重体积大导致Swap延迟显著高于计算延迟符合硬件常识。
