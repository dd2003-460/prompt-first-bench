# N445: 若自建 POP 采用按量计费（Pay-per-Use）而非固定月租（如部分 IDC 提供的弹性带宽），超量流量费单价 k_overage 典型区间为 ¥1.5-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N139

## Claim

若自建 POP 采用按量计费（Pay-per-Use）而非固定月租（如部分 IDC 提供的弹性带宽），超量流量费单价 k_overage 典型区间为 ¥1.5-3.0/GB（95th percentile 计费或实际流量计费），远高于固定月租的边际成本，因此仅在流量波动极大（K_peak > 10）时才考虑混合计费模式。

## Corrected Claim

若自建 POP 采用按量计费（Pay-per-Use），其超量流量费单价通常显著高于固定月租的边际成本。具体单价因运营商、地区及计费模式（如95th percentile或实际流量）而异，需根据实际合同确定。因此，仅在流量波动极大时，混合计费模式才可能更具成本优势。

## Evidence

[质询]该陈述包含具体的经验性价格区间（¥1.5-3.0/GB）和特定的业务阈值（K_peak > 10），属于经验事实而非第一性原理可推导内容。由于检索失败无外部来源支持，且不同地区、不同运营商及不同计费模式（95th percentile vs 实际流量）下的单价差异巨大，该具体数值区间缺乏普适性证据，存在口径混淆或特定场景泛化的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

IDC elastic bandwidth pay per use price per GB China 2023
