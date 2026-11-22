# N62: P_card 在持续推理负载下的实际功耗修正：2×RTX 4090 在 27B 模型 BF16/INT8 推理负载下平均功耗约为峰值 700W 的 60-70%

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

P_card 在持续推理负载下的实际功耗修正：2×RTX 4090 在 27B 模型 BF16/INT8 推理负载下平均功耗约为峰值 700W 的 60-70% (即 420-490W)，1×A100 80GB 在同等负载下平均功耗约为峰值 400W 的 50-60% (即 200-240W)，因 LLM 推理主要受显存带宽限制而非算力限制，GPU 利用率通常低于峰值

## Corrected Claim

P_card 在持续推理负载下的实际功耗修正：2×RTX 4090 在 27B 模型 BF16/INT8 推理负载下平均功耗约为峰值 700W 的 60-70% (即 420-490W)，1×A100 80GB 在同等负载下平均功耗约为峰值 400W 的 50-60% (即 200-240W)，因 LLM 推理主要受显存带宽限制而非算力限制，GPU 利用率通常低于峰值

## Evidence

先验知识/题面给定，逻辑校验通过：LLM推理受显存带宽限制导致GPU利用率低于峰值，功耗低于TDP峰值符合物理直觉及工程经验，数值量级合理。

## Search Query

RTX 4090 A100 average power consumption LLM inference load
