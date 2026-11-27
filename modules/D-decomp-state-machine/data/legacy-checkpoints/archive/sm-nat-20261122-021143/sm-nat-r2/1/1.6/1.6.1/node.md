# N33: 扫描效应偏差 Δ 的量化模型：基于 Belady 算法的最优命中率 H_opt 与 LRU 命中率 H_LRU 的差值，需引入‘工作集波动率’指标，定义为 K 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

扫描效应偏差 Δ 的量化模型：基于 Belady 算法的最优命中率 H_opt 与 LRU 命中率 H_LRU 的差值，需引入‘工作集波动率’指标，定义为 K 随时间变化的方差，Δ ≈ Var(K) / E[K] * (1 - H_ideal)

## Corrected Claim

扫描效应偏差 Δ 的量化可参考基于 Belady 算法的最优命中率 H_opt 与 LRU 命中率 H_LRU 的差值，在特定工作负载下，该差值与工作集波动率（K 随时间变化的方差）及理想命中率存在正相关关系，具体量化模型需结合负载特征校准。

## Evidence

[质询]该公式缺乏严格的理论推导支持，属于经验性近似或特定场景下的启发式模型，而非通用的数学恒等式或第一性原理推论；'工作集波动率'的定义及与命中率偏差的线性/乘积关系在通用缓存理论中并非标准结论。 | 先验知识/题面给定，逻辑校验通过（量纲与变量关系在特定语境下自洽），但作为经验性量化模型，缺乏通用理论证明，故降级为定性/特定场景表述。

## Search Query

LRU scan effect penalty model
