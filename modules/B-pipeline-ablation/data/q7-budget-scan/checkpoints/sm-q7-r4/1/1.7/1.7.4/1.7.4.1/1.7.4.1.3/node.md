# N423: 控制器逻辑在写路径下的额外功耗 ΔP_ctrl_write = 0.8-1.2W，主要用于 FTL 映射表更新 (Mapping Table Update) 和

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N185

## Claim

控制器逻辑在写路径下的额外功耗 ΔP_ctrl_write = 0.8-1.2W，主要用于 FTL 映射表更新 (Mapping Table Update) 和日志写入 (Log Journaling)；相比读路径，写路径的控制逻辑能耗高出约 25-30%，主要源于随机写导致的元数据扇区重写频率增加

## Corrected Claim

控制器逻辑在写路径下的额外功耗主要用于FTL映射表更新和日志写入；相比读路径，写路径的控制逻辑能耗通常更高，主要源于随机写导致的元数据扇区重写频率增加

## Evidence

[质询]具体数值（0.8-1.2W, 25-30%）缺乏来源支持，且不同容量/接口/代际的SSD控制器功耗差异巨大，固定数值范围可能不准确 | 来源[1]仅提及FTL映射表概念，未提供具体功耗数值或读写能耗对比数据；该陈述包含具体经验参数，逻辑自洽但缺来源直接支持

## Search Query

SSD controller FTL mapping table update power overhead random write vs read

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Solid-state_drive', 'type': 'wikipedia', 'title': 'Solid-state drive'}
