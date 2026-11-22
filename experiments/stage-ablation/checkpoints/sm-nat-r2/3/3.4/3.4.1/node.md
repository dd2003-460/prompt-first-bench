# N66: LFU 频率统计滞后导致的命中率损失下界 ΔH_lag 可量化为 LFU 计数器收敛时间 T_conv 与负载变化率 λ_change 的乘积对应的字节占比，公

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

LFU 频率统计滞后导致的命中率损失下界 ΔH_lag 可量化为 LFU 计数器收敛时间 T_conv 与负载变化率 λ_change 的乘积对应的字节占比，公式为 ΔH_lag_min ≈ (T_conv / T_load_cycle) * (H_byte_LFU_ideal - H_byte_LRU)，其中 T_conv 为 LFU 计数器达到稳态所需时间（通常与请求数成正比），T_load_cycle 为负载特征变化周期。

## Corrected Claim

LFU 频率统计滞后导致的命中率损失与 LFU 计数器收敛时间 T_conv 及负载变化率正相关，具体量化需结合特定缓存实现与负载模型，通用下界公式 ΔH_lag_min ≈ (T_conv / T_load_cycle) * (H_byte_LFU_ideal - H_byte_LRU) 仅在特定理想化假设下近似成立。

## Evidence

[质询]该公式将命中率损失下界简化为时间比与理想/实际命中率差的乘积，缺乏严格的理论推导支持。LFU 的滞后效应通常与计数器重置策略、访问分布的平稳性假设以及具体缓存替换算法的实现细节（如是否使用近似 LFU）强相关，简单的线性乘积关系在一般负载下可能不成立，且 T_conv 的定义在不同实现中差异巨大，导致该公式可能仅适用于特定理想化场景而非通用下界。 | 先验知识/题面给定，逻辑校验通过（量纲与变量定义自洽），但作为经验性量化公式，缺乏通用理论证明，且无外部来源支持，故降级为定性表述。
