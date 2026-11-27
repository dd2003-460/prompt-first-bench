# N217: 重新计算性价比指标：基于修正后的吞吐量（30 tokens/s中值）和修正后的TCO（$5,074），2x RTX 4090的性价比为 30/5074 ≈ 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

重新计算性价比指标：基于修正后的吞吐量（30 tokens/s中值）和修正后的TCO（$5,074），2x RTX 4090的性价比为 30/5074 ≈ 0.0059 tokens/s/$；对比1x A100 80GB（吞吐量50 tokens/s, TCO $15,519, 性价比 50/15519 ≈ 0.0032 tokens/s/$），2x RTX 4090在INT8精度下的性价比仍高于A100，N70的反转结论不成立。

## Corrected Claim

重新计算性价比指标：基于修正后的吞吐量（30 tokens/s中值）和修正后的TCO（$5,074），2x RTX 4090的性价比为 30/5074 ≈ 0.0059 tokens/s/$；对比1x A100 80GB（吞吐量50 tokens/s, TCO $15,519, 性价比 50/15519 ≈ 0.0032 tokens/s/$），2x RTX 4090在INT8精度下的性价比仍高于A100，N70的反转结论不成立。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（30/5074≈0.0059, 50/15519≈0.0032），且0.0059 > 0.0032，结论自洽。
