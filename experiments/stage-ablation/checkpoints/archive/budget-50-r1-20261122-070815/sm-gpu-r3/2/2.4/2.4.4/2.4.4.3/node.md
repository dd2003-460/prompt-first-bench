# N235: NVFP4 量化相对于 BF16 的 Perplexity 相对增加率 (Delta PPL / PPL_BF16)，需计算该百分比是否超过 5% 阈值；若 D

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

NVFP4 量化相对于 BF16 的 Perplexity 相对增加率 (Delta PPL / PPL_BF16)，需计算该百分比是否超过 5% 阈值；若 Delta PPL 为 0.3 且 PPL_BF16 为 5.2，则相对增加率为 5.77%，超过阈值，需结合具体数值判断。

## Corrected Claim

NVFP4 量化相对于 BF16 的 Perplexity 相对增加率 (Delta PPL / PPL_BF16)，需计算该百分比是否超过 5% 阈值；若 Delta PPL 为 0.3 且 PPL_BF16 为 5.2，则相对增加率为 5.77%，超过阈值，需结合具体数值判断。

## Evidence

先验知识/题面给定，逻辑校验通过：0.3/5.2 ≈ 0.0577 (5.77%) > 5%，计算无误且逻辑自洽。
