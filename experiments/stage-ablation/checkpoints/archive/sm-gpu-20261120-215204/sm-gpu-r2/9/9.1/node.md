# N146: AMD MI300X 在 BF16 精度下运行 Qwen3-27B 的理论峰值速度为 98 Tokens/s (5300 GB/s 带宽 / 54 GB 权重)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

AMD MI300X 在 BF16 精度下运行 Qwen3-27B 的理论峰值速度为 98 Tokens/s (5300 GB/s 带宽 / 54 GB 权重)，但受限于 ROCm 软件栈优化程度，实际有效带宽利用率通常为 60-70%，预计实际速度为 59-68 Tokens/s

## Corrected Claim

AMD MI300X 在 BF16 精度下运行 Qwen3-27B 的理论峰值速度为 98 Tokens/s (5300 GB/s 带宽 / 54 GB 权重)，但受限于 ROCm 软件栈优化程度，实际有效带宽利用率通常为 60-70%，预计实际速度为 59-68 Tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X HBM3带宽约5300GB/s，Qwen3-27B BF16权重约54GB，理论峰值98 Tokens/s计算正确；60-70%带宽利用率符合当前ROCm栈实际表现，推导自洽。

## Search Query

AMD MI300X BF16 inference efficiency bandwidth utilization LLM benchmark
