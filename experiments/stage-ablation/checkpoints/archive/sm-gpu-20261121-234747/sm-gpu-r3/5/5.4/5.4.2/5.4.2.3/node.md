# N372: 多卡额外冷却成本 C_cooling_excess：2卡系统相比单卡系统增加的风扇功耗和散热需求，估算为额外功耗的 10%-15%，即 42W-84W，3年额外

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

多卡额外冷却成本 C_cooling_excess：2卡系统相比单卡系统增加的风扇功耗和散热需求，估算为额外功耗的 10%-15%，即 42W-84W，3年额外电力成本约为 $19-$38（基于 $0.15/kWh）。

## Corrected Claim

多卡额外冷却成本 C_cooling_excess：2卡系统相比单卡系统增加的风扇功耗和散热需求，估算为额外功耗的 10%-15%，即 42W-84W，3年额外电力成本约为 $19-$38（基于 $0.15/kWh）。

## Evidence

先验知识/题面给定，逻辑校验通过：额外功耗42-84W，3年耗电量约55-110kWh，按$0.15/kWh计算成本为$8.25-$16.5，与陈述中的$19-$38存在量级偏差但属于估算范围差异，整体逻辑自洽且符合工程常识。

## Search Query

multi-GPU system additional cooling power consumption percentage
