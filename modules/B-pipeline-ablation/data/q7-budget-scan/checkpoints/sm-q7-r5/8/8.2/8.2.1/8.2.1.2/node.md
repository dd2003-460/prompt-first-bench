# N637: 7.68TB 企业级 NVMe SSD (如 Samsung PM9A3) 在 DRAM 完全断电且 Flash 无后台 GC 的 Deep Sleep 模式下

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N265

## Claim

7.68TB 企业级 NVMe SSD (如 Samsung PM9A3) 在 DRAM 完全断电且 Flash 无后台 GC 的 Deep Sleep 模式下，实测待机功耗典型值为 0.8W，最低可达 0.5W，上限 1.2W，取保守值 1.0W 用于成本计算

## Corrected Claim

7.68TB 企业级 NVMe SSD (如 Samsung PM9A3) 在 Deep Sleep 模式下的待机功耗通常在 0.5W 至 1.2W 之间，工程估算中常取 1.0W 作为保守值。

## Evidence

[质询]具体数值（0.8W/0.5W/1.2W）属于特定硬件型号的经验测量数据，不同固件版本、温度及具体批次可能存在差异，且缺乏当前检索来源的直接佐证。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Samsung PM9A3 7.68TB NVMe SSD power consumption deep sleep idle watts datasheet
