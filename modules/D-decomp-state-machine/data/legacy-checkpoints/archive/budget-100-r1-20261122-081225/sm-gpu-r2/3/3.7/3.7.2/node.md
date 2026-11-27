# N120: 数据中心级 GPU (如 A100) 通常部署在机架服务器中，服务器整体功耗（含 CPU、内存、网络、散热）约为 GPU TDP 的 1.5-2 倍，即 A10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

数据中心级 GPU (如 A100) 通常部署在机架服务器中，服务器整体功耗（含 CPU、内存、网络、散热）约为 GPU TDP 的 1.5-2 倍，即 A100 服务器的总功耗约为 600W-800W，远高于单卡 400W 的估算。

## Corrected Claim

数据中心级 GPU (如 A100) 通常部署在机架服务器中，服务器整体功耗（含 CPU、内存、网络、散热）约为 GPU TDP 的 1.5-2 倍，即 A100 服务器的总功耗约为 600W-800W，远高于单卡 400W 的估算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data center server total power consumption per GPU A100
