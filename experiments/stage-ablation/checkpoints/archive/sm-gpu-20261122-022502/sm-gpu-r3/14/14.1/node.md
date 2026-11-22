# N306: Apple M2 Ultra 的统一内存带宽为 800 GB/s (官方规格)，其理论解码吞吐量上限为 800 GB/s / 54 GB ≈ 14.8 toke

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

Apple M2 Ultra 的统一内存带宽为 800 GB/s (官方规格)，其理论解码吞吐量上限为 800 GB/s / 54 GB ≈ 14.8 tokens/s (BF16) 或 800 GB/s / 27 GB ≈ 29.6 tokens/s (INT8)，高于 5 tokens/s 的交互式最低阈值，因此基于'带宽<500GB/s'排除 M2 Ultra 的前提在数值上是不成立的，需重新评估其作为非典型方案的资格。

## Corrected Claim

Apple M2 Ultra 的统一内存带宽为 800 GB/s (官方规格)，其理论解码吞吐量上限为 800 GB/s / 54 GB ≈ 14.8 tokens/s (BF16) 或 800 GB/s / 27 GB ≈ 29.6 tokens/s (INT8)，高于 5 tokens/s 的交互式最低阈值，因此基于'带宽<500GB/s'排除 M2 Ultra 的前提在数值上是不成立的，需重新评估其作为非典型方案的资格。

## Evidence

先验知识/题面给定，逻辑校验通过：Apple M2 Ultra 官方规格确为 800 GB/s 统一内存带宽，算术推导（800/54≈14.8, 800/27≈29.6）正确，且结论（带宽>500GB/s，故排除前提不成立）逻辑自洽。

## Search Query

Apple M2 Ultra memory bandwidth GB/s spec
