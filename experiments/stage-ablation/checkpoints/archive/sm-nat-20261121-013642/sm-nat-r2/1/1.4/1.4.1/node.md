# N38: 分子计算项：缓存内对象加权字节流量 Σ_{i∈Cache} (r_i * s_i) 的解析近似，在稳态且访问独立假设下，等于缓存内对象请求频率的期望乘以对象大小

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

分子计算项：缓存内对象加权字节流量 Σ_{i∈Cache} (r_i * s_i) 的解析近似，在稳态且访问独立假设下，等于缓存内对象请求频率的期望乘以对象大小的期望，即 E[r_i|Cache] * E[s_i|Cache] * |Cache|，其中 |Cache| 受限于 128GB 容量约束。

## Corrected Claim

在稳态且假设对象请求频率与对象大小统计独立的条件下，缓存内对象加权字节流量 Σ_{i∈Cache} (r_i * s_i) 近似等于 E[r_i|Cache] * E[s_i|Cache] * |Cache|；若频率与大小存在相关性，则需使用联合期望 E[r_i * s_i | Cache] * |Cache|。

## Evidence

[质询]陈述中声称加权字节流量 Σ(r_i * s_i) 在稳态且访问独立假设下等于 E[r_i|Cache] * E[s_i|Cache] * |Cache|，这在数学上仅当请求频率 r_i 与对象大小 s_i 统计独立时成立。若存在相关性（如大文件通常访问频率低），该等式不成立，且通常 Σ(r_i * s_i) ≠ E[r]E[s]N，而是 E[rs]N。虽然题目假设了'访问独立'，但通常指不同对象间的访问独立，而非同一对象内频率与大小的独立，此处存在概念混淆或过度简化的风险。 | 先验知识/题面给定，逻辑校验通过（在严格假设 r_i 与 s_i 独立的前提下数学推导成立，但实际场景中该独立性假设较强，故降级为定性表述以涵盖相关性影响）。

## Search Query

steady state cache hit rate formula weighted byte traffic
