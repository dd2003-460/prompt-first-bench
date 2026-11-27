# N189: 2×RTX 4090 (48GB) 运行 BF16 Qwen3-27B 的显存缺口量化：需求 54GB(权重) + 6.4GB(KV Cache@32K) + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

2×RTX 4090 (48GB) 运行 BF16 Qwen3-27B 的显存缺口量化：需求 54GB(权重) + 6.4GB(KV Cache@32K) + 2GB(Overhead) = 62.4GB，缺口 = 62.4GB - 48GB = 14.4GB。

## Corrected Claim

2×RTX 4090 (48GB) 运行 BF16 Qwen3-27B 的显存缺口量化：需求 54GB(权重) + 6.4GB(KV Cache@32K) + 2GB(Overhead) = 62.4GB，缺口 = 62.4GB - 48GB = 14.4GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，32K上下文KV Cache约6.4GB，总需求62.4GB，减去48GB显存得14.4GB缺口，计算自洽。
