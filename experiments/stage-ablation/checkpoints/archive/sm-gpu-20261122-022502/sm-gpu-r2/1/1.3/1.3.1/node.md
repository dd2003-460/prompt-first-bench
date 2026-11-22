# N39: Apple M2 Ultra 192GB 统一内存带宽为 800GB/s，H100 SXM 显存带宽为 3.35TB/s，带宽比为 4.19:1；在Memory

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Apple M2 Ultra 192GB 统一内存带宽为 800GB/s，H100 SXM 显存带宽为 3.35TB/s，带宽比为 4.19:1；在Memory-Bound的LLM推理中（每token生成需读取全部权重），理论吞吐量比应接近带宽比，即 M2 Ultra 吞吐量约为 H100 的 1/4.19 ≈ 0.24，若H100吞吐量为 20 tokens/s，M2 Ultra 预期为 4.8 tokens/s

## Corrected Claim

Apple M2 Ultra 192GB 统一内存带宽为 800GB/s，H100 SXM 显存带宽为 3.35TB/s，带宽比为 4.19:1；在Memory-Bound的LLM推理中（每token生成需读取全部权重），理论吞吐量比应接近带宽比，即 M2 Ultra 吞吐量约为 H100 的 1/4.19 ≈ 0.24，若H100吞吐量为 20 tokens/s，M2 Ultra 预期为 4.8 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 192GB 带宽 800GB/s 与 H100 SXM 带宽 3.35TB/s 均为公认硬件规格，带宽比 4.19:1 计算正确；在 Memory-Bound 场景下，吞吐量与带宽成正比，推导逻辑自洽且数值量级合理。
