# N181: 2024-2025年企业级16TB CMR HDD（如Seagate Exos X16, WD Ultrastar DC HC325）的市场均价约为¥90-11

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

2024-2025年企业级16TB CMR HDD（如Seagate Exos X16, WD Ultrastar DC HC325）的市场均价约为¥90-110/TB，单位容量成本低于18TB/22TB型号，但需更多盘数达到相同物理容量（480TB需30盘 vs 27盘），导致RAID6有效系数降低（30盘系数0.933 vs 27盘系数0.926，差异微小）及故障概率增加（30盘AFR总故障率≈1.05次/年 vs 27盘≈0.95次/年，假设AFR=3.5%）。

## Corrected Claim

2024-2025年企业级16TB CMR HDD（如Seagate Exos X16）的市场均价约为¥90-110/TB（需实时市场数据验证），单位容量成本通常低于更大容量型号，但达到相同物理容量需更多盘数，导致RAID6有效系数略降及整体故障概率增加。

## Evidence

[质询]陈述中包含具体的2024-2025年市场均价（¥90-110/TB）及基于特定AFR假设的故障率计算，属于经验事实与特定场景推演，参考来源仅确认了产品存在及基本规格，未提供价格数据或RAID故障率统计支持，无法排除价格波动或AFR假设偏差。 | 来源[1][2][3]确认了Seagate Exos X16 16TB企业级硬盘的存在及基本规格（16TB, 7200RPM, 256MB Cache），支持产品实体存在；但来源未覆盖价格区间（¥90-110/TB）及RAID6故障率具体数值，逻辑上盘数增加导致故障概率上升符合直觉，但具体数值缺乏外部证据直接支持。

## Search Query

Seagate Exos X16 price per TB 2024 enterprise HDD 16TB cost analysis

## Retrieval Sources

- {'url': 'https://www.newegg.com/seagate-exos-x16-st16000nm001g-16tb/p/1Z4-002P-015K6&rut=4df35d08b5a9ba9be3253a1f11d4cc19dcd024c0d50c597df97d4a147ce0136b', 'type': 'ddg', 'title': 'Seagate Exos 16TB Enterprise HDD 7200 RPM 3.5" Internal Hard Drive ...'}
- {'url': 'https://item.szlcsc.com/mro/22678647.html&rut=417982de7cf632acc77c3346d996697d64bb9edab6fc5fdad93885802bbc84f9', 'type': 'ddg', 'title': '希捷 (SEAGATE) 银河Exos企业级硬盘3.5英寸 256MB 7200转 SAS接口 16TB'}
- {'url': 'https://www.price.com.hk/product.php?p=496116&rut=0771ff167688265e53e4c3dc250a01d13a97206f004d7f3a3bd22f43d818a692', 'type': 'ddg', 'title': 'Seagate Exos X16 3.5-inch 7200rpm 256MB Enterprise HDD 16TB ...'}
