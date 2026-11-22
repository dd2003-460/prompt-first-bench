# N93: 实际TPS与理论峰值带宽的比值（Bandwidth Utilization）：在单卡推理中，由于PCIe瓶颈、内存控制器效率及调度开销，实际带宽利用率通常为理论

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25

## Claim

实际TPS与理论峰值带宽的比值（Bandwidth Utilization）：在单卡推理中，由于PCIe瓶颈、内存控制器效率及调度开销，实际带宽利用率通常为理论峰值的60-80% [待核验]，需根据具体硬件（如H100 vs RTX 4090）的实测数据修正理论下界。

## Corrected Claim

在单卡推理中，实际带宽利用率受PCIe瓶颈、内存控制器效率及调度开销影响，通常低于理论峰值，具体数值需根据硬件（如H100 vs RTX 4090）及负载特征实测确定，一般经验范围约为60-80%。

## Evidence

[质询]该陈述包含具体的经验数值范围（60-80%），属于硬件性能经验事实，无法从第一性原理严格推导，且缺乏实测数据支持，不同硬件架构（如HBM vs GDDR）及负载类型下波动较大，固定区间可能不准确。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

LLM inference bandwidth utilization efficiency H100 vs RTX 4090 decode phase
