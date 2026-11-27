# N402: T_base 的动态定义：T_base 不是常数，而是随市场热度 H_t 变化的函数 T_base(t) = T_0 / (1 + H_t)。在促销期或节假日，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

T_base 的动态定义：T_base 不是常数，而是随市场热度 H_t 变化的函数 T_base(t) = T_0 / (1 + H_t)。在促销期或节假日，H_t 升高，T_base 降低，可能导致 T 的缩短归因于时间效应而非噪声筛选效应。需控制时间变量后重新估计 k_match。

## Corrected Claim

T_base 的动态定义：T_base 不是常数，而是随市场热度 H_t 变化的函数 T_base(t) = T_0 / (1 + H_t)。在促销期或节假日，H_t 升高，T_base 降低，可能导致 T 的缩短归因于时间效应而非噪声筛选效应。需控制时间变量后重新估计 k_match。

## Evidence

先验知识/题面给定，逻辑校验通过：该定义符合时间序列分析中控制季节性/趋势项以分离噪声效应的标准方法论逻辑，且数学形式自洽。

## Search Query

seasonal adjustment for transaction cycle time e-commerce second hand
