# N420: [Verified-Hardware] 标记的适用范围应限定为：NVIDIA/AMD/Intel 官网规格表中的静态参数（如 TDP、显存容量、理论峰值带宽、F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N186

## Claim

[Verified-Hardware] 标记的适用范围应限定为：NVIDIA/AMD/Intel 官网规格表中的静态参数（如 TDP、显存容量、理论峰值带宽、FP8/FP16 算力）；任何基于这些参数推导出的动态性能指标（如实际吞吐量、延迟、能效比）必须标记为 [Derived]，并附带推导公式和假设条件（如 batch_size=1, context=32K），以避免混淆静态规格与动态性能。

## Corrected Claim

[Verified-Hardware] 标记的适用范围应限定为：NVIDIA/AMD/Intel 官网规格表中的静态参数（如 TDP、显存容量、理论峰值带宽、FP8/FP16 算力）；任何基于这些参数推导出的动态性能指标（如实际吞吐量、延迟、能效比）必须标记为 [Derived]，并附带推导公式和假设条件（如 batch_size=1, context=32K），以避免混淆静态规格与动态性能。

## Evidence

先验知识/题面给定，逻辑校验通过
