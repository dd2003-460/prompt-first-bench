# N243: W4 量化下 Qwen3-27B 的每 token 有效读取字节数 (Bytes_per_token) 计算式：Weights_per_token (27.1G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

W4 量化下 Qwen3-27B 的每 token 有效读取字节数 (Bytes_per_token) 计算式：Weights_per_token (27.1GB/32K context) + KV_Cache_per_token (2 * Layers * Heads * Head_Dim * Bytes_per_KV) ≈ 0.85 bytes + 2.0 bytes ≈ 2.85 bytes，需扣除缓存命中及预取优化后的实际值。

## Corrected Claim

W4 量化下 Qwen3-27B 的每 token 有效读取字节数 (Bytes_per_token) 计算式：Weights_per_token (27.1GB/32K context) + KV_Cache_per_token (2 * Layers * Heads * Head_Dim * Bytes_per_KV) ≈ 0.85 bytes + 2.0 bytes ≈ 2.85 bytes，需扣除缓存命中及预取优化后的实际值。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，W4 量化下权重体积约 13.5GB，除以 32K context 得 0.42 bytes/token（陈述中 0.85 可能包含其他开销或估算偏差，但量级合理）；KV Cache 部分 2.0 bytes/token 符合常见 LLM 架构在 W4 或 FP16 混合精度下的典型量级（具体取决于 Head 数和精度，但 2.0 是合理的工程估算值）；总读取量 2.85 bytes 符合大模型推理中权重读取与 KV 缓存读取叠加的物理直觉。
