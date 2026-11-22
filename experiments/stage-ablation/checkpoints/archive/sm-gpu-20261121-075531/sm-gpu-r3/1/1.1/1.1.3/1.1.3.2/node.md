# N137: W4 量化后的实际权重显存占用 Bytes_W4_Actual = (Total_Params * 4 bits / 8) + Overhead_Scales 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

W4 量化后的实际权重显存占用 Bytes_W4_Actual = (Total_Params * 4 bits / 8) + Overhead_Scales = 13.55GB + 0.85GB ≈ 14.4GB，相比纯 4-bit 理论值 13.55GB 增加了约 6.3%，符合 5-10% 的预期范围。

## Corrected Claim

W4 量化后的实际权重显存占用 Bytes_W4_Actual = (Total_Params * 4 bits / 8) + Overhead_Scales = 13.55GB + 0.85GB ≈ 14.4GB，相比纯 4-bit 理论值 13.55GB 增加了约 6.3%，符合 5-10% 的预期范围。

## Evidence

先验知识/题面给定，逻辑校验通过：13.55GB + 0.85GB = 14.4GB，增量比例 0.85/13.55 ≈ 6.27%，符合 5-10% 范围，计算自洽。
