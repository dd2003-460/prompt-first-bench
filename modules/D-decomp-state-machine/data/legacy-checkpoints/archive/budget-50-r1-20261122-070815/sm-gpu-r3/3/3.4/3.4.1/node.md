# N86: 2x RTX 4090 双卡方案的初始硬件采购总成本 C_hw_2x4090 = 2 * P_4090 + P_chassis_dual + P_psu_120

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21, N22, N23

## Claim

2x RTX 4090 双卡方案的初始硬件采购总成本 C_hw_2x4090 = 2 * P_4090 + P_chassis_dual + P_psu_1200W + P_cooling_mod，其中 P_4090 约为 $1600-$2000 [时效待核]，机箱与电源附加成本约为 $300-$500，总计约 $3500-$4500

## Corrected Claim

2x RTX 4090 双卡方案的初始硬件采购总成本 C_hw_2x4090 由两张 GPU 及机箱、电源、散热等配件组成。以 RTX 4090 单价约 $1600-$2000 估算，加上约 $300-$500 的配套成本，总成本大致在 $3500-$4500 区间（具体价格随市场波动）。

## Evidence

[质询]RTX 4090 的市场价格波动极大且随时间变化显著（从首发 $1599 到后续溢价或降价），$1600-$2000 的范围虽在合理区间内，但缺乏具体时间点限定，且参考来源摘要中未提供具体的硬件采购成本数值，无法直接验证该具体金额区间。 | 逻辑自洽（2张卡+机箱电源冷却成本构成合理），但参考来源[1][2]仅讨论搭建思路和集群效率，未提供具体硬件采购成本数据，属于经验事实且缺乏直接来源支持。

## Search Query

RTX 4090 current price 2024 dual card system cost

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/16864316403&rut=35bf424984418c94012228904908f69344c7f1b2f80d961e6dda0e6b4d6d6adb', 'type': 'ddg', 'title': '基于双卡 Rtx 4090 搭建家用深度学习主机 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2020458980598633680&rut=9d4124efa2f26ccd217432c035c10783059c0394a31b8b5f839fb3d61e0f9e73', 'type': 'ddg', 'title': '8卡4090集群实测：多卡并行效率能到多少？ - 知乎'}
