# N574: 工作点2（中性价比/跨运营商BGP互联）：AS_Hops=3，单跳延迟 L_hop ≈ 5ms，增加2个AS跳导致延迟+10ms，总延迟 L_total ≈ 2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187

## Claim

工作点2（中性价比/跨运营商BGP互联）：AS_Hops=3，单跳延迟 L_hop ≈ 5ms，增加2个AS跳导致延迟+10ms，总延迟 L_total ≈ 25ms。

## Corrected Claim

工作点2（中性价比/跨运营商BGP互联）：AS_Hops=3，单跳延迟 L_hop ≈ 5ms，增加2个AS跳导致延迟+10ms，总延迟 L_total ≈ 25ms。

## Evidence

先验知识/题面给定，逻辑校验通过：AS_Hops=3意味着相比直连（1跳）增加了2个AS跳，2 * 5ms = 10ms，基础延迟15ms + 10ms = 25ms，数值量级与逻辑自洽。
