# N314: 工作点3（高成本低性）：Num_Engineers_min = 6人，全员7x24三班倒+2名专职SRE，支持MTTR<15min且零单点故障，年人力成本 C_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

工作点3（高成本低性）：Num_Engineers_min = 6人，全员7x24三班倒+2名专职SRE，支持MTTR<15min且零单点故障，年人力成本 C_ops_6 = 6 * ¥250k/人/年 = ¥1.5M/年。

## Corrected Claim

工作点3（高成本低性）：Num_Engineers_min = 6人，全员7x24三班倒+2名专职SRE，支持MTTR<15min且零单点故障，年人力成本 C_ops_6 = 6 * ¥250k/人/年 = ¥1.5M/年。

## Evidence

先验知识/题面给定，逻辑校验通过：6人 * 250k = 1.5M，算术正确；7x24三班倒需至少3组轮班，6人配置在逻辑上可行（每组2人），符合高冗余低单点故障的工程直觉。
