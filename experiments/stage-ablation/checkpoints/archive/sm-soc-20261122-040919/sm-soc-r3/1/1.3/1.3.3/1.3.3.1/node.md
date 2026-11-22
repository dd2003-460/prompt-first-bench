# N159: 基准搜索成本 C_search 的量化分解：C_search = t_browse * w_time + C_cognitive，其中 t_browse 为平均

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

基准搜索成本 C_search 的量化分解：C_search = t_browse * w_time + C_cognitive，其中 t_browse 为平均浏览时长（分钟），w_time 为单位时间机会成本（元/分钟），C_cognitive 为决策疲劳导致的心理成本（元）。需基于平台日志确定 t_browse 分布均值。

## Corrected Claim

基准搜索成本 C_search 可量化分解为时间机会成本与认知心理成本之和：C_search = t_browse * w_time + C_cognitive，其中 t_browse 需基于平台日志确定。

## Evidence

[质询]该陈述属于特定场景下的经验性成本模型定义，并非通用物理或数学定律，且参考来源完全无关，无法验证其具体参数（如w_time, C_cognitive）的合理性或行业共识。 | 逻辑上量纲自洽（时间*成本/时间 + 货币 = 货币），但参考来源[1]为化学分子搜索算法，与用户搜索行为成本模型无关，无外部证据支持该具体分解公式。

## Search Query

online marketplace average browsing time per item search cost minutes

## Retrieval Sources

- {'url': 'https://github.com/seoklab/CSearch/&rut=d80ef7f3f37f9e92328c681f6ac39389c0c1c9e24969f59c39eefc3ef04446cd', 'type': 'ddg', 'title': 'GitHub - seoklab/CSearch: CSearch: Chemical Space Search via Virtual ...'}
