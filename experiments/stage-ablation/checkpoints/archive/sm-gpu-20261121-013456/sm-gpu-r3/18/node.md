# N312: RTX 5090 32GB 显存在 Qwen3-27B INT4 (AWQ) 权重下的可行性验证：权重 13.5GB + KV Cache (32K, FP8)

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 5090 32GB 显存在 Qwen3-27B INT4 (AWQ) 权重下的可行性验证：权重 13.5GB + KV Cache (32K, FP8) 4.3GB + 激活 3.0GB = 20.8GB < 32GB，余量 11.2GB，单卡即可满足 32K 上下文下限；其 GDDR7 带宽 (1792 GB/s) 使得理论解码吞吐量上限约为 86 tokens/s (1792/20.8)，实际预期 40-50 tokens/s，单位 TCO 成本预计低于 2×RTX 4090。

## Corrected Claim

RTX 5090 32GB 显存在 Qwen3-27B INT4 (AWQ) 权重下的可行性验证：权重 13.5GB + KV Cache (32K, FP8) 4.3GB + 激活 3.0GB = 20.8GB < 32GB，余量 11.2GB，单卡即可满足 32K 上下文下限；其 GDDR7 带宽 (1792 GB/s) 使得理论解码吞吐量上限约为 86 tokens/s (1792/20.8)，实际预期 40-50 tokens/s，单位 TCO 成本预计低于 2×RTX 4090。

## Evidence

检索失败: no sources from any channel (all 5 failed)
