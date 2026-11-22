# N131: CapEx 优势抵消点计算公式推导：定义 Break_even_T = (CapEx_Consumer - CapEx_Datacenter) / (OpEx_

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

CapEx 优势抵消点计算公式推导：定义 Break_even_T = (CapEx_Consumer - CapEx_Datacenter) / (OpEx_daily_Datacenter - OpEx_daily_Consumer)，其中 OpEx_daily = P_avg × 24h × E_price。需代入 N38/N39 的功耗数据和 N40 的电价，计算在典型电价下，多卡消费级方案相比单卡数据中心方案的 TCO 交叉时间点（月数）。

## Corrected Claim

CapEx 优势抵消点计算公式推导：定义 Break_even_T = (CapEx_Consumer - CapEx_Datacenter) / (OpEx_daily_Datacenter - OpEx_daily_Consumer)，其中 OpEx_daily = P_avg × 24h × E_price。需代入 N38/N39 的功耗数据和 N40 的电价，计算在典型电价下，多卡消费级方案相比单卡数据中心方案的 TCO 交叉时间点（月数）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于特定硬件组合（RTX 4090 vs A100）在给定数据下的正向计算与逻辑验证，子节点2聚焦于参数敏感性分析（临界阈值X/Y）及边界条件（负值/超期）。两者分别处理“点估计/逻辑校验”与“区间/边界分析”，内容正交且无重叠，共同覆盖了父节点要求的公式代入、典型情况计算及交叉点验证。）
