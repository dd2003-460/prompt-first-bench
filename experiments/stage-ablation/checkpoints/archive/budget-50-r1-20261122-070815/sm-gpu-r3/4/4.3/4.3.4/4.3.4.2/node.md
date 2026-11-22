# N324: 单卡数据中心 GPU (A100/H100) 的散热成本已包含在服务器整机价格中，其 C_cooling_delta 为 $0，但需确认服务器电源效率 (80 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

单卡数据中心 GPU (A100/H100) 的散热成本已包含在服务器整机价格中，其 C_cooling_delta 为 $0，但需确认服务器电源效率 (80 Plus Titanium) 是否因额外 GPU 负载而显著影响 PUE

## Corrected Claim

单卡数据中心 GPU (A100/H100) 的散热成本已包含在服务器整机价格中，其 C_cooling_delta 为 $0，但需确认服务器电源效率 (80 Plus Titanium) 是否因额外 GPU 负载而显著影响 PUE

## Evidence

先验知识/题面给定，逻辑校验通过：数据中心GPU散热成本通常包含在服务器整机价格中，C_cooling_delta为$0符合常规成本核算逻辑；电源效率对PUE的影响属于独立变量，陈述逻辑自洽。

## Search Query

data center server GPU cooling cost included PUE efficiency
