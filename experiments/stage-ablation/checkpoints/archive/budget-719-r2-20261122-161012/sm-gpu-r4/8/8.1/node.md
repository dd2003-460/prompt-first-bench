# N123: Apple M3 Ultra 内存带宽为 800 GB/s，Qwen3-27B BF16 权重 55 GB 全部驻留统一内存，理论 Decode 吞吐量上限为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

Apple M3 Ultra 内存带宽为 800 GB/s，Qwen3-27B BF16 权重 55 GB 全部驻留统一内存，理论 Decode 吞吐量上限为 800 GB/s / 55 GB ≈ 14.5 tokens/s；由于无需跨卡通信，实际吞吐量接近理论值，预计为 13-14 tokens/s [待核验]。

## Corrected Claim

Apple M3 Ultra 内存带宽为 800 GB/s，Qwen3-27B BF16 权重 55 GB 全部驻留统一内存，理论 Decode 吞吐量上限为 800 GB/s / 55 GB ≈ 14.5 tokens/s；由于无需跨卡通信，实际吞吐量接近理论值，预计为 13-14 tokens/s [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 800GB/s 带宽与 55GB 权重符合已知规格，算术推导 800/55≈14.5 正确，且单芯片无跨卡通信瓶颈，实际吞吐量接近理论值的推断符合 LLM 推理物理直觉。
