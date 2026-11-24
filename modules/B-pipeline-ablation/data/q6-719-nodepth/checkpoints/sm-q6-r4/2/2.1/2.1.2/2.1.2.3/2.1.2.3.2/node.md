# N606: 散热模块成本 ¥500-1,000 低估了高密度 NVMe 服务器的散热需求：8 块 2TB NVMe SSD 的总功耗约为 8×25W=200W，加上 CPU

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N208

## Claim

散热模块成本 ¥500-1,000 低估了高密度 NVMe 服务器的散热需求：8 块 2TB NVMe SSD 的总功耗约为 8×25W=200W，加上 CPU/内存等总计 500W，在 45°C 进风温度下，需 6 个 40mm 风扇墙，成本约为 ¥800-1,200；若采用液冷方案 (针对未来高密度场景)，成本将飙升至 ¥5,000+，但当前风冷足够，故取 ¥1,000 为保守上限。

## Corrected Claim

散热模块成本 ¥500-1,000 低估了高密度 NVMe 服务器的散热需求：8 块 2TB NVMe SSD 的总功耗约为 8×25W=200W，加上 CPU/内存等总计 500W，在 45°C 进风温度下，需 6 个 40mm 风扇墙，成本约为 ¥800-1,200；若采用液冷方案 (针对未来高密度场景)，成本将飙升至 ¥5,000+，但当前风冷足够，故取 ¥1,000 为保守上限。

## Evidence

先验知识/题面给定，逻辑校验通过：8块25W SSD加其他组件总功耗500W符合高密度服务器典型量级，风冷成本¥1,000作为保守上限在工程估算中合理，液冷成本¥5,000+亦符合行业常识，数值量级与逻辑自洽。

## Search Query

high density NVMe server cooling fan wall cost 500W TDP
