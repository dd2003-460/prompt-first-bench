# N169: LFU 字节命中率增益的量化上限：ΔH_lfu ≈ H_lru * (1 - 1/Factor) * P_access_hot，其中 Factor=0.738 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69, N70, N72

## Claim

LFU 字节命中率增益的量化上限：ΔH_lfu ≈ H_lru * (1 - 1/Factor) * P_access_hot，其中 Factor=0.738 (N76)，P_access_hot≈0.85，得 ΔH_lfu ≈ 0.53 * 0.26 * 0.85 ≈ 11.7%，与 N40 的 9-12% 区间一致，验证了负相关对 LFU 优势的放大效应。

## Corrected Claim

LFU 字节命中率增益的量化估算：基于经验模型 ΔH_lfu ≈ H_lru * (1 - 1/Factor) * P_access_hot，代入 Factor=0.738 和 P_access_hot≈0.85，估算增益约为 11.7%，落在 N40 的 9-12% 区间内，表明负相关对 LFU 优势有放大效应。

## Evidence

[质询]公式中的系数 0.53 来源不明，且将复杂的缓存替换策略性能差异简化为单一乘法公式缺乏理论依据，属于经验性估算而非严格推导。 | 先验知识/题面给定，逻辑校验通过（数值计算 0.53*0.26*0.85≈0.117 无误，且与 N40 区间一致），但公式本身为经验拟合，非第一性原理严格推导，故降级。
