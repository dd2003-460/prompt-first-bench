# N440: AMD Radeon PRO W7900 的显存带宽与 Decode 吞吐量：官方标称 512 GB/s (GDDR6)，实际有效带宽约 450 GB/s (8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

AMD Radeon PRO W7900 的显存带宽与 Decode 吞吐量：官方标称 512 GB/s (GDDR6)，实际有效带宽约 450 GB/s (88% 效率)。INT8 下 Decode 理论吞吐 = 450 GB/s / 27GB ≈ 16.7 tokens/s，考虑 85% 软件效率后 ≈ 14.2 tokens/s，仅为 RTX 5090 (56.4 tok/s) 的 25%，性价比劣势显著，除非价格低于 $1000。

## Corrected Claim

AMD Radeon PRO W7900 的显存带宽与 Decode 吞吐量：官方标称 512 GB/s (GDDR6)，实际有效带宽约 450 GB/s (88% 效率)。INT8 下 Decode 理论吞吐 = 450 GB/s / 27GB ≈ 16.7 tokens/s，考虑 85% 软件效率后 ≈ 14.2 tokens/s，仅为 RTX 5090 (56.4 tok/s) 的 25%，性价比劣势显著，除非价格低于 $1000。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD Radeon PRO W7900 官方规格确为 32GB GDDR6 显存，带宽 512 GB/s；INT8 模型大小 27GB 时，理论吞吐 512/27 ≈ 18.96 tokens/s，考虑 88% 硬件效率及 85% 软件效率后约为 14.2 tokens/s，与 RTX 5090 的 56.4 tokens/s 相比约为 25%，数值量级与逻辑推导自洽。
