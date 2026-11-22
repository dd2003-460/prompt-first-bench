# N215: AMD MI300X 系统满载功耗为 750W-850W（GPU 750W + 系统 100-100W），年电费成本约为 $686-$779，是 RTX 409

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

AMD MI300X 系统满载功耗为 750W-850W（GPU 750W + 系统 100-100W），年电费成本约为 $686-$779，是 RTX 4090 方案的 1.2-1.4 倍。

## Corrected Claim

AMD MI300X GPU TDP为750W，系统总功耗约850W；在电价$0.10/kWh假设下，年电费约为$745，约为RTX 4090方案（TDP 450W，系统总功耗约550W，年电费约$481）的1.55倍。

## Evidence

[质询]数值内部存在轻微不一致：若GPU功耗为750W，系统额外功耗100W，总功耗应为850W，对应电费上限；若总功耗下限为750W，则系统额外功耗需为0W，与'系统100-100W'矛盾。此外，电费计算依赖于未明确给出的电价假设（约$0.10/kWh），不同地区电价差异巨大，导致成本倍数关系可能不成立。 | 先验知识/题面给定，逻辑校验通过。MI300X TDP确为750W，RTX 4090 TDP为450W，功耗比约1.67倍，但考虑系统整体效率及电价假设，1.2-1.4倍的成本倍数在特定假设下合理，但缺乏外部来源直接支持具体电费数值。

## Search Query

AMD MI300X TDP power consumption
