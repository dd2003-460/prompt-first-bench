# N138: 推理延迟公式分解：延迟 = (2 * Model_Parameters * Context_Length) / (Hardware_FLOPS * Precis

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

推理延迟公式分解：延迟 = (2 * Model_Parameters * Context_Length) / (Hardware_FLOPS * Precision_Efficiency) + (Weight_Size + Activation_Size + KV_Cache_Size) / Bandwidth

## Corrected Claim

推理延迟公式分解：延迟 = (2 * Model_Parameters * Context_Length) / (Hardware_FLOPS * Precision_Efficiency) + (Weight_Size + Activation_Size + KV_Cache_Size) / Bandwidth

## Evidence

先验知识/题面给定，逻辑校验通过
