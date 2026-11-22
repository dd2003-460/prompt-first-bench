# N222: 修正 N65 的功耗估算：NVIDIA H100 SXM5 的整机满载功耗 P_draw_1xH100 约为 900-1000W（700W GPU TDP + 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

修正 N65 的功耗估算：NVIDIA H100 SXM5 的整机满载功耗 P_draw_1xH100 约为 900-1000W（700W GPU TDP + 200-300W 服务器基础负载），其中服务器基础负载包含 CPU (2x Xeon) ~150W、RAM ~50W、风扇/散热 ~50W，来源为 NVIDIA DGX H100 系统功耗规格及第三方服务器功耗测试。

## Corrected Claim

NVIDIA H100 SXM5 的整机满载功耗估算约为 900-1000W（基于700W GPU TDP及典型服务器基础负载），具体数值随服务器配置（CPU、内存、散热方案）有所波动。

## Evidence

[质询]参考来源未提供具体的功耗数值，无法直接验证900-1000W的估算值；且服务器基础负载的具体构成（CPU/RAM/风扇）属于经验性估算，不同配置下波动较大，缺乏单一权威来源直接支持该特定分解。 | 逻辑自洽（H100 TDP 700W + 服务器基础负载符合工程常识），但参考来源[1][2]仅提及H100存在及TOP500排名，未提供具体功耗数据，属于经验事实且缺直接来源支持。

## Search Query

NVIDIA H100 SXM5 server total power consumption watts

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units', 'type': 'wikipedia', 'title': 'List of Nvidia graphics processing units'}
- {'url': 'https://en.wikipedia.org/wiki/TOP500', 'type': 'wikipedia', 'title': 'TOP500'}
