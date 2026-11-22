# N598: Apple Silicon 上 Qwen3-27B Q4_K_M 的实际 Decode 吞吐修正因子：理论上限 48.5 tokens/s (M2 Ultra,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N249

## Claim

Apple Silicon 上 Qwen3-27B Q4_K_M 的实际 Decode 吞吐修正因子：理论上限 48.5 tokens/s (M2 Ultra, 800 GB/s) 需乘以实际带宽利用率 (通常 0.6-0.8) 和量化反量化开销 (GGUF 反量化引入额外 CPU/GPU 计算)，实际吞吐约为 29-39 tokens/s；若 M3 Ultra 带宽为 1.2 TB/s，理论上限 72.7 tokens/s，实际约为 44-58 tokens/s；此修正因子是判断 Apple 方案是否满足 >20 tokens/s 阈值的关键。

## Corrected Claim

Apple Silicon 上 Qwen3-27B Q4_K_M 的实际 Decode 吞吐修正因子：理论上限 48.5 tokens/s (M2 Ultra, 800 GB/s) 需乘以实际带宽利用率 (通常 0.6-0.8) 和量化反量化开销 (GGUF 反量化引入额外 CPU/GPU 计算)，实际吞吐约为 29-39 tokens/s；若 M3 Ultra 带宽为 1.2 TB/s，理论上限 72.7 tokens/s，实际约为 44-58 tokens/s；此修正因子是判断 Apple 方案是否满足 >20 tokens/s 阈值的关键。

## Evidence

先验知识/题面给定，逻辑校验通过：基于内存带宽瓶颈的LLM解码吞吐估算公式（Throughput ≈ Bandwidth / ModelSize）及常见的硬件带宽利用率（0.6-0.8）和量化开销修正，数值量级与工程经验一致，逻辑自洽。
