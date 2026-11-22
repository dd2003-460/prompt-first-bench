# N142: 2×RTX 5090 在 TP=2 下推理 Qwen3-27B 的 Decode 吞吐量损失率，由于 Blackwell 架构可能引入新的互联机制或更高带宽的 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

2×RTX 5090 在 TP=2 下推理 Qwen3-27B 的 Decode 吞吐量损失率，由于 Blackwell 架构可能引入新的互联机制或更高带宽的 PCIe Gen5，其损失率预计低于 RTX 4090，需实测验证具体百分比（预计 15%-25%）

## Corrected Claim

2×RTX 5090 在 TP=2 下推理 Qwen3-27B 的 Decode 吞吐量损失率预计低于 RTX 4090，具体百分比需实测验证。

## Evidence

[质询]该陈述包含具体的经验性数值预测（15%-25%）和架构性能对比结论，属于经验事实，无法从第一性原理严格推导，且缺乏实测数据支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

RTX 5090 tensor parallelism Qwen 27B throughput loss PCIe Gen5
