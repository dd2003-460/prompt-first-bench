# N130: 阈值 t_threshold 的解析解：t_threshold = (V_gain - C_0) / k_t，其中 V_gain 为买家感知商品降价后的价值增益

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

阈值 t_threshold 的解析解：t_threshold = (V_gain - C_0) / k_t，其中 V_gain 为买家感知商品降价后的价值增益（V_gain = P_initial - P_current - V_search_alt），V_search_alt 为搜索替代商品的预期收益，需代入 V_gain 和 k_t 的具体数值计算 t_threshold 是否落在 48 小时窗口内。

## Corrected Claim

阈值 t_threshold 的解析解：t_threshold = (V_gain - C_0) / k_t，其中 V_gain 为买家感知商品降价后的价值增益（V_gain = P_initial - P_current - V_search_alt），V_search_alt 为搜索替代商品的预期收益，需代入 V_gain 和 k_t 的具体数值计算 t_threshold 是否落在 48 小时窗口内。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

threshold time value gain search cost alternative expected utility
