# N290: RTX 5090 相对 RTX 4090 的 Decode 理论吞吐量提升 77.8% 的前提条件：模型权重完全驻留显存且 Batch Size=1；若启用 C

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

RTX 5090 相对 RTX 4090 的 Decode 理论吞吐量提升 77.8% 的前提条件：模型权重完全驻留显存且 Batch Size=1；若启用 CPU Offload 或 Batch Size>1，实际提升幅度因 KV Cache 带宽竞争而降至 50-65%

## Corrected Claim

RTX 5090 相对 RTX 4090 的 Decode 理论吞吐量在模型权重完全驻留显存且 Batch Size=1 时有显著提升；若启用 CPU Offload 或 Batch Size>1，实际提升幅度可能因显存带宽竞争等因素而降低。

## Evidence

[质询]具体数值（77.8% 和 50-65%）缺乏公开基准测试支持，且 'KV Cache 带宽竞争' 作为 Batch Size>1 时性能提升幅度下降的主要解释在逻辑上不够严谨（通常 Batch Size 增加会提高计算密度从而提升吞吐量，除非显存带宽成为绝对瓶颈且模型极大，但此处表述过于绝对且数值精确度可疑）。 | 先验知识/题面给定，逻辑校验通过，但具体数值缺乏来源支持，降级为定性表述
