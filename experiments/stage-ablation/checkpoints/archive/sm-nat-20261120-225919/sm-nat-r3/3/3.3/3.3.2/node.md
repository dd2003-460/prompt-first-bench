# N60: 频率突变后 LFU 的负增益幅度 ΔH_neg 取决于旧热点与新热点的请求频率重叠度，量化为 ΔH_neg ≈ -f_stale * (Σ_{i∈Old} R_

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

频率突变后 LFU 的负增益幅度 ΔH_neg 取决于旧热点与新热点的请求频率重叠度，量化为 ΔH_neg ≈ -f_stale * (Σ_{i∈Old} R_i - Σ_{i∈New} R_i) / Total_R，其中 Old 和 New 分别为突变前后的热点集合。

## Corrected Claim

频率突变后 LFU 的负增益幅度 ΔH_neg 与旧热点和新热点的请求频率差异相关，其量级大致正比于频率重叠度的缺失，具体量化需结合缓存容量和替换策略细节，简化模型下可近似为 ΔH_neg ∝ -f_stale * |Σ_{i∈Old} R_i - Σ_{i∈New} R_i| / Total_R。

## Evidence

[质询]该公式将命中率损失（ΔH_neg）直接等同于频率差值的线性加权，忽略了缓存容量限制、替换策略的具体实现细节（如是否考虑访问频率衰减）以及新旧热点集合大小可能不同导致的分母/分子口径不一致问题；此外，'负增益'通常指性能下降，但公式中若 Σ_Old > Σ_New，结果为正，符号定义可能存在混淆或需要额外上下文解释。 | 先验知识/题面给定，逻辑校验通过（量纲合理，线性近似在特定条件下成立），但缺乏外部来源直接支持该具体量化公式，且存在符号定义和线性假设的潜在争议，故降级。

## Search Query

cache hit ratio degradation after workload shift LFU vs LRU
