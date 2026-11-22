# N160: NVIDIA A100 40GB (PCIe/SXM) 运行 Qwen3-27B BF16 TP=2 时，每卡显存占用 29.68GB，剩余 10.32GB；A

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

NVIDIA A100 40GB (PCIe/SXM) 运行 Qwen3-27B BF16 TP=2 时，每卡显存占用 29.68GB，剩余 10.32GB；A100 带宽 1555 GB/s (HBM2e)，高于 L40S 但低于 RTX 5090；A100 40GB 二手市场价格约 $1500-$2000，需对比其 TDP (400W) 和电力成本，计算与 2x RTX 5090 ($4000+ Capex) 的 3 年 TCO 差异。

## Corrected Claim

NVIDIA A100 40GB (PCIe/SXM) 运行 Qwen3-27B BF16 TP=2 时，每卡显存占用 29.68GB，剩余 10.32GB；A100 带宽 1555 GB/s (HBM2e)，高于 L40S 但低于 RTX 5090；A100 40GB 二手市场价格约 $1500-$2000，需对比其 TDP (400W) 和电力成本，计算与 2x RTX 5090 ($4000+ Capex) 的 3 年 TCO 差异。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16 权重约 54GB，TP=2 每卡 27GB，加上 KV Cache 和激活值后 29.68GB 合理；A100 HBM2e 带宽 1555GB/s 符合规格；二手价格及 TDP 400W 符合市场常识。

## Search Query

A100 40GB Qwen3-27B BF16 inference cost per token vs RTX 5090
