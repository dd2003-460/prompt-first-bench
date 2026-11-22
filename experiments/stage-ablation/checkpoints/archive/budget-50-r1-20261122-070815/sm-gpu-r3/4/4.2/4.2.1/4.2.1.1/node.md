# N302: RTX 4090 的 TDP 标称值为 450W，但在 LLM 推理（Decode 阶段，低算力高带宽）负载下，实际功耗通常降至 250W-350W 区间，需基

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

RTX 4090 的 TDP 标称值为 450W，但在 LLM 推理（Decode 阶段，低算力高带宽）负载下，实际功耗通常降至 250W-350W 区间，需基于 HWiNFO 实测数据修正 P_avg 而非使用 TDP 上限

## Corrected Claim

RTX 4090 的 TDP 标称值为 450W，但在 LLM 推理（Decode 阶段，低算力高带宽）负载下，实际功耗通常降至 250W-350W 区间，需基于 HWiNFO 实测数据修正 P_avg 而非使用 TDP 上限

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 450W 为官方规格；LLM Decode 阶段主要受显存带宽限制，GPU 核心利用率低，功耗显著低于峰值符合物理直觉及工程实测规律。

## Search Query

RTX 4090 power consumption LLM inference decode phase watts HWiNFO
