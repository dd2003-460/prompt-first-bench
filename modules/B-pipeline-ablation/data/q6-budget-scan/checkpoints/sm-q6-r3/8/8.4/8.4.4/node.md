# N317: BGP多线接入费年成本：C_bgp_annual = 10 * 12 * C_bgp_monthly，其中C_bgp_monthly取中位数¥3500（多运营商

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

BGP多线接入费年成本：C_bgp_annual = 10 * 12 * C_bgp_monthly，其中C_bgp_monthly取中位数¥3500（多运营商接入），年成本≈¥420k；若仅单线接入则此项为0，但多线接入可降低单运营商故障风险，需权衡成本与可用性

## Corrected Claim

BGP多线接入费年成本：C_bgp_annual = 10 * 12 * C_bgp_monthly，其中C_bgp_monthly取中位数¥3500（多运营商接入），年成本≈¥420k；若仅单线接入则此项为0，但多线接入可降低单运营商故障风险，需权衡成本与可用性

## Evidence

先验知识/题面给定，逻辑校验通过：10*12*3500=420,000，计算无误；BGP多线接入通常比单线贵，且具备高可用性，符合工程常识。
