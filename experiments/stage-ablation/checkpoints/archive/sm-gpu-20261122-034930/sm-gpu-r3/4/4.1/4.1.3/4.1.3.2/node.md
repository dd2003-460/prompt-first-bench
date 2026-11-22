# N312: Mac Studio M2 Ultra 在50% GPU利用率下的平均功耗修正为150W（而非200W），依据是M2 Ultra在低负载下功耗可降至100W以下

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110

## Claim

Mac Studio M2 Ultra 在50% GPU利用率下的平均功耗修正为150W（而非200W），依据是M2 Ultra在低负载下功耗可降至100W以下，50%负载时约180W，加权平均 = 0.5*200W + 0.5*100W = 150W。年耗电量 = 150W * 8760h / 1000 = 1314 kWh，年电力成本 = $197.1，3年TCO中电力占比修正为12.5%。

## Corrected Claim

Mac Studio M2 Ultra 在50% GPU利用率下的平均功耗估计为150W（基于简化线性模型：0.5*200W + 0.5*100W），年耗电量约1314 kWh，年电力成本约$197.1，3年TCO中电力占比约12.5%。注意：功耗参数为经验估计，实际值可能因工作负载和散热条件而异。

## Evidence

[质询]功耗模型假设过于简化且缺乏实证支持：M2 Ultra在50% GPU利用率下的实际功耗并非简单的线性加权平均（0.5*200W + 0.5*100W），实际芯片功耗曲线是非线性的，且'低负载下功耗可降至100W以下'和'50%负载时约180W'这两个关键参数缺乏可靠来源支持，属于经验事实但无外部证据。 | 经验事实，逻辑自洽但缺来源支持。数学计算正确（150W * 8760h / 1000 = 1314 kWh，1314 * $0.15 = $197.1），但功耗参数（100W/180W/200W）为经验估计，无来源直接支持，且线性加权平均模型可能不准确。

## Search Query

Mac Studio M2 Ultra power consumption watts load
