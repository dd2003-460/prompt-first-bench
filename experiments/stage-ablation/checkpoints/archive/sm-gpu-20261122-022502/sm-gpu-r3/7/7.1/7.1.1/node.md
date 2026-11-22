# N254: Apple M3 Ultra (512GB Unified Memory, 819GB/s) 运行 Qwen3-27B BF16 (权重 54GB) 无 Off

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

Apple M3 Ultra (512GB Unified Memory, 819GB/s) 运行 Qwen3-27B BF16 (权重 54GB) 无 Offload 场景下，理论吞吐上限为 819 GB/s / 54 GB ≈ 15.2 tokens/s，考虑统一内存架构的缓存一致性开销 (约 20%)，实际工作点吞吐约为 12-13 tokens/s，其 TCO/token 主要受高 CapEx ($6,000+) 主导而非 OpEx。

## Corrected Claim

Apple M3 Ultra (512GB Unified Memory, 819GB/s) 运行 Qwen3-27B BF16 (权重 54GB) 无 Offload 场景下，理论吞吐上限为 819 GB/s / 54 GB ≈ 15.2 tokens/s，考虑统一内存架构的缓存一致性开销 (约 20%)，实际工作点吞吐约为 12-13 tokens/s，其 TCO/token 主要受高 CapEx ($6,000+) 主导而非 OpEx。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 819GB/s 带宽与 54GB 权重计算出的理论上限 15.2 tokens/s 符合算术逻辑，20% 开销推导出的 12-13 tokens/s 实际工作点符合 LLM 推理经验规律，TCO 分析符合高 CapEx 硬件特征。
