# N38: LRU 缓存内对象的平均驻留时间 T_res 的具体计算公式：T_res = C / (Σ_{i∈Cache} f_i * S_i / (Total_Req *

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

LRU 缓存内对象的平均驻留时间 T_res 的具体计算公式：T_res = C / (Σ_{i∈Cache} f_i * S_i / (Total_Req * Total_Bytes))，其中分母为缓存内对象的平均字节流出率，需基于 Pareto(α=1.1) 和 Pareto(β=0.9) 的联合分布积分求解缓存内对象的加权平均大小与频率。

## Corrected Claim

LRU 缓存内对象的平均驻留时间 T_res 通常通过 Little's Law (T_res = L / λ) 或基于 LRU 堆栈距离分布的积分求解，具体公式取决于请求到达率 λ 和缓存命中率/驻留对象数 L，而非简单的 C / (加权流出率) 形式。

## Evidence

[质询]公式中分母的定义与符号存在逻辑矛盾：分母被描述为'平均字节流出率'（单位应为 Bytes/Time），但公式右侧分母表达式 Σ(f_i * S_i) / (Total_Req * Total_Bytes) 的量纲分析显示其结果并非速率，且 Total_Req 和 Total_Bytes 作为全局统计量出现在分母中，导致 T_res 的量纲无法正确对应为时间单位（Time）。此外，'平均驻留时间'通常由 Little's Law (L = λW) 或具体的替换策略（如 LRU 的堆栈距离）决定，而非简单的总容量除以某种加权流出率，该公式缺乏标准的缓存理论支持。 | 先验知识/题面给定，逻辑校验未通过：公式量纲不自洽，且 LRU 驻留时间的标准计算不依赖此特定形式的加权流出率公式。
