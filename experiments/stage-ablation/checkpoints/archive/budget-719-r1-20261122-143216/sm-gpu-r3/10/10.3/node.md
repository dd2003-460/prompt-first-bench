# N141: 2×RTX 4090 在 TP=2 下推理 Qwen3-27B 的 Decode 吞吐量损失率，基准为单卡理论峰值带宽利用率，实测显示 PCIe 互联导致吞吐量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

2×RTX 4090 在 TP=2 下推理 Qwen3-27B 的 Decode 吞吐量损失率，基准为单卡理论峰值带宽利用率，实测显示 PCIe 互联导致吞吐量下降 20%-35%，具体数值取决于 Batch Size 和框架优化（如 vLLM 的 custom all-reduce 实现）

## Corrected Claim

2×RTX 4090 在 TP=2 下推理 Qwen3-27B 时，由于 PCIe 互联的带宽限制和通信开销，Decode 吞吐量通常低于单卡理论峰值，具体损失率取决于 Batch Size、PCIe 版本及框架优化（如 vLLM 的 custom all-reduce），实测中常出现显著性能下降。

## Evidence

[质询]该陈述包含具体的经验性数值范围（20%-35%），属于经验事实而非第一性原理可推导结论。在缺乏外部来源支持的情况下，无法验证该具体数值范围的准确性，且不同硬件配置（如PCIe版本、NVLink vs PCIe）和软件栈优化程度可能导致差异远超此范围，存在以偏概全或数值不严谨的风险。 | 经验事实，逻辑自洽但缺来源支持。TP=2下通过PCIe通信确实会引入额外延迟和带宽瓶颈，导致吞吐量低于单卡理论峰值，定性逻辑成立，但具体20%-35%的损失率缺乏来源佐证。

## Search Query

RTX 4090 tensor parallelism Qwen 27B throughput loss PCIe vs NVLink
