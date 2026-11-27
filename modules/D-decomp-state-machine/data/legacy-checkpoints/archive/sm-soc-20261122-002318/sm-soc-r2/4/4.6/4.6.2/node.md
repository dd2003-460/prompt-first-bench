# N72: 买家临界干预强度计算：展示中位价后，买家搜寻成本变化 ΔSearchCost_buyer 取决于信息获取是否替代了部分搜寻行为。若信息展示使平均搜寻次数从 N_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

买家临界干预强度计算：展示中位价后，买家搜寻成本变化 ΔSearchCost_buyer 取决于信息获取是否替代了部分搜寻行为。若信息展示使平均搜寻次数从 N_old 降至 N_new，则 ΔBS_buyer = -(N_new - N_old) * k_search + (P_old - P_new)。设定 Threshold_buyer = 10% 搜寻时间增加，需计算使 ΔBS_buyer / Initial_BS = -0.10 的信息展示精度阈值。

## Corrected Claim

买家临界干预强度计算：展示中位价后，买家搜寻成本变化 ΔSearchCost_buyer 取决于信息获取是否替代了部分搜寻行为。若信息展示使平均搜寻次数从 N_old 降至 N_new，则 ΔBS_buyer = -(N_new - N_old) * k_search + (P_old - P_new)。设定 Threshold_buyer = 10% 搜寻时间增加，需计算使 ΔBS_buyer / Initial_BS = -0.10 的信息展示精度阈值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

buyer search cost reduction information display threshold 10 percent
