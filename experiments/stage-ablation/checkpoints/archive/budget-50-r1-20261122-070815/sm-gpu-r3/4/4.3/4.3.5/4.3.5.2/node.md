# N326: 1x A100/H100 单卡方案的多卡额外开销 C_overhead 为 $0，因为其通常部署于标准 1U/2U 服务器中，电源、机箱、互联均包含在服务器 B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

1x A100/H100 单卡方案的多卡额外开销 C_overhead 为 $0，因为其通常部署于标准 1U/2U 服务器中，电源、机箱、互联均包含在服务器 BOM 中，无额外硬件采购需求

## Corrected Claim

1x A100/H100 单卡方案的多卡额外开销 C_overhead 为 $0，因为其通常部署于标准 1U/2U 服务器中，电源、机箱、互联均包含在服务器 BOM 中，无额外硬件采购需求

## Evidence

先验知识/题面给定，逻辑校验通过：单卡方案通常集成于标准服务器BOM中，无额外独立硬件采购成本，符合工程常识。

## Search Query

A100 H100 server BOM cost overhead single GPU
