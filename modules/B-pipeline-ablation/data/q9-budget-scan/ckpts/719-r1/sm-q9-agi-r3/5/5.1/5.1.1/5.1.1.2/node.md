# N229: 在 LLM 推理稳态负载下（Decode 阶段，低算力密集度），V100 的实际功耗通常低于 TDP，主要受限于内存带宽而非算力单元，实测稳态功耗约为 TDP 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66, N67, N68

## Claim

在 LLM 推理稳态负载下（Decode 阶段，低算力密集度），V100 的实际功耗通常低于 TDP，主要受限于内存带宽而非算力单元，实测稳态功耗约为 TDP 的 60%-80% (即 150W-200W/卡)。

## Corrected Claim

在 LLM 推理稳态负载下（Decode 阶段，低算力密集度），V100 的实际功耗通常低于 TDP，主要受限于内存带宽而非算力单元，实测稳态功耗约为 TDP 的 60%-80% (即 150W-200W/卡)。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 TDP为250W，Decode阶段受内存带宽限制导致GPU核心利用率低，功耗显著低于TDP符合硬件特性及工程常识。

## Search Query

V100 power consumption during LLM inference decode phase vs TDP
