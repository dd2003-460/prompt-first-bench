# N680: NVMe SSD Active Read/Write功耗实测值修正：N282假设的15W为保守上限，主流7.68TB NVMe SSD（如Intel P5510

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N282

## Claim

NVMe SSD Active Read/Write功耗实测值修正：N282假设的15W为保守上限，主流7.68TB NVMe SSD（如Intel P5510）在持续顺序读写下的典型功耗约为10-12W，需采用该区间中值11W替代15W进行加权计算 [待核验]

## Corrected Claim

主流7.68TB NVMe SSD在持续顺序读写下的典型功耗通常在10-15W区间，建议根据具体型号数据表确认，若无确切数据可采用12W作为中间估计值进行加权计算。

## Evidence

[质询]具体型号（Intel P5510）及容量（7.68TB）的功耗数值属于经验事实，缺乏来源支持，且不同厂商/代际SSD功耗差异较大，10-12W仅为特定条件下的估计值，不能直接作为通用修正值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Intel P5510 7.68TB NVMe SSD power consumption active read write watts
