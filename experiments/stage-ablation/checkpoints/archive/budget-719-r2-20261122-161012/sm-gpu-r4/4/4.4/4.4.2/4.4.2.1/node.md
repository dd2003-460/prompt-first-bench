# N223: RTX 4090 单卡性价比工作点：基于 Street Price $2000 (2024 均价，修正 N106 中 $1600 的假设偏差) 和理论吞吐 18

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

RTX 4090 单卡性价比工作点：基于 Street Price $2000 (2024 均价，修正 N106 中 $1600 的假设偏差) 和理论吞吐 18.3 tokens/s (BF16 不可行，此处指 INT4/FP8 量化后单卡可行场景或作为基准对比)，单位成本吞吐 = 18.3 / 2000 ≈ 0.00915 tok/s/$。

## Corrected Claim

RTX 4090 单卡性价比工作点：基于假设 Street Price $2000 (2024 均价) 和特定量化场景下理论吞吐 18.3 tokens/s，单位成本吞吐 ≈ 0.00915 tok/s/$。

## Evidence

[质询]来源提供的价格数据为2026年的时租价格（1.48-2.8元/小时），与陈述中2024年的单卡购买均价（$2000）在时间、货币单位及交易性质（租赁vs购买）上均不匹配，无法直接支持该具体数值；且18.3 tokens/s的吞吐量为特定模型下的经验值，缺乏通用性。 | 逻辑计算正确（18.3/2000≈0.00915），但参考来源[1][2]均为2026年时租或行情分析，未提供2024年$2000均价的直接证据，属于经验事实且缺乏直接来源支持。

## Search Query

RTX 4090 street price 2024 average cost tokens per dollar inference

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7638881556525761064/&rut=22fa959c45ce2cc2a9529df703c8922a06621d530d3f883e9074e5b7f324c572', 'type': 'ddg', 'title': '2026年rtx 4090单卡时租价格排行榜最低价盘点 - 今日头条'}
- {'url': 'https://www.sohu.com/a/1083749929_122471764&rut=99dc725f970896fcfaefdc11aba7b24bc7fcc0085b8d348c59d860f3395dfdf6', 'type': 'ddg', 'title': '2026年rtx 4090显卡全解析：从工包到涡轮版，哪款才是你的性价比之选？'}
