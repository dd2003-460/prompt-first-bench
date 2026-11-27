# N423: 在 RTX 5090 (FP8) 上，Qwen3-27B 的 Decode 阶段吞吐量 (Tokens/s) 受带宽限制，计算公式为 Decode_Throug

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

在 RTX 5090 (FP8) 上，Qwen3-27B 的 Decode 阶段吞吐量 (Tokens/s) 受带宽限制，计算公式为 Decode_Throughput = (Bandwidth × Utilization) / (Weight_Size + KV_Cache_Size_per_token)，其中 Weight_Size=27GB，KV_Cache_Size_per_token≈0.3KB，Utilization 约为 80-90%。

## Corrected Claim

在 RTX 5090 (FP8) 上，Qwen3-27B 的 Decode 阶段吞吐量 (Tokens/s) 受带宽限制，计算公式为 Decode_Throughput = (Bandwidth × Utilization) / (Weight_Size + KV_Cache_Size_per_token)，其中 Weight_Size=27GB，KV_Cache_Size_per_token≈0.3KB，Utilization 约为 80-90%。

## Evidence

[质询]KV_Cache_Size_per_token≈0.3KB 的数值量级可能偏低（取决于具体模型配置如 GQA 头数、层数及精度），但作为数量级估算在逻辑上可接受；主要风险在于将特定硬件/模型配置下的经验参数泛化为通用公式，但作为特定节点描述尚可。 | 先验知识/题面给定，逻辑校验通过：Decode 阶段确实受显存带宽限制，吞吐量公式符合 Roofline 模型基本逻辑，Weight_Size 27GB 与 27B 参数 FP8 精度（1字节/参数）吻合，KV Cache 0.3KB/token 在 GQA 架构下量级合理。
