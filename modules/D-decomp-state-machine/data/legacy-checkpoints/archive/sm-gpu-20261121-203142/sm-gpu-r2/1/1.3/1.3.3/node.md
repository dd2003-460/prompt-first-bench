# N44: W4量化下的KV Cache显存：通常KV Cache保持BF16精度，占用4.29GB（同N36），除非使用KV Cache量化（如INT8 KV Cache

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

W4量化下的KV Cache显存：通常KV Cache保持BF16精度，占用4.29GB（同N36），除非使用KV Cache量化（如INT8 KV Cache），此时可降至2.15GB但可能增加延迟

## Corrected Claim

W4量化下的KV Cache显存：通常KV Cache保持BF16精度，占用4.29GB（同N36），除非使用KV Cache量化（如INT8 KV Cache），此时可降至2.15GB但可能增加延迟

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache通常保持BF16精度，4.29GB与2.15GB的数值关系符合INT8量化减半的规律，且W4量化主要影响权重而非KV Cache，逻辑自洽。
