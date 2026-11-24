# N43: NVMe SSD阵列的单盘TBW规格验证：主流4TB企业级NVMe SSD（如Samsung PM9A3, Intel D7-P5520）TBW通常为1000-

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

NVMe SSD阵列的单盘TBW规格验证：主流4TB企业级NVMe SSD（如Samsung PM9A3, Intel D7-P5520）TBW通常为1000-3000TB；若TBW=1000TB，则单盘寿命 = 1000TB / 5.08TB/5年 ≈ 197年，远超5年需求；若TBW=100TB（低端），则寿命 = 100/5.08/5 ≈ 3.9年，需更换；需选择TBW>=100TB的SSD以确保5年寿命。

## Corrected Claim

主流4TB企业级NVMe SSD的TBW规格因型号而异，通常在数百TB至数千TB之间。若年写入量为5.08TB，则TBW=100TB的SSD寿命约为3.9年，不满足5年需求；而TBW=1000TB的SSD寿命远超5年。因此，需根据实际写入负载选择TBW足以覆盖5年总写入量的SSD。

## Evidence

[质询]具体TBW数值（1000-3000TB）属于经验事实，且不同厂商/型号差异巨大，缺乏来源支持无法确认具体量级；此外，'需选择TBW>=100TB'的结论基于特定写入量假设，若实际写入量低于5.08TB/5年，则100TB TBW也足够，该阈值并非绝对物理限制。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

4TB enterprise NVMe SSD TBW specs Samsung PM9A3 Intel D7-P5520
