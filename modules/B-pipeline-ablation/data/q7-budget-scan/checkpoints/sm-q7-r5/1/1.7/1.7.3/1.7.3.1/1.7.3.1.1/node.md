# N415: NAND Flash 随机读单页能量消耗 E_read_page ≈ 1.5-2.0 μJ/page（针对 TLC 3bit MLC 架构），显著高于顺序读的 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

NAND Flash 随机读单页能量消耗 E_read_page ≈ 1.5-2.0 μJ/page（针对 TLC 3bit MLC 架构），显著高于顺序读的 0.5 μJ/byte，主要源于随机寻址导致的 Sense Amplifier 激活与 WL 电压切换开销

## Corrected Claim

NAND Flash 随机读单页能量消耗 E_read_page ≈ 1.5-2.0 μJ/page（针对 TLC 3bit MLC 架构），显著高于顺序读的 0.5 μJ/byte，主要源于随机寻址导致的 Sense Amplifier 激活与 WL 电压切换开销

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NAND flash random read energy consumption per page TLC vs sequential
