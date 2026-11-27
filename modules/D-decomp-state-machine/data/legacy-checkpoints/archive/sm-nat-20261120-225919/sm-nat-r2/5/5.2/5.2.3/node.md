# N76: N21 公式 H_LRU ≥ 1 - (C/S_total)^β 假设缓存填充了最热的对象集合，但在 LRU 动态更新下，缓存实际包含的对象集合 C' 受限于最

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21

## Claim

N21 公式 H_LRU ≥ 1 - (C/S_total)^β 假设缓存填充了最热的对象集合，但在 LRU 动态更新下，缓存实际包含的对象集合 C' 受限于最近访问频率，导致稳态命中率下界需修正为 H_LRU_eff = H_static * (1 - P_eviction)，其中 P_eviction 为对象在驻留期内被淘汰的概率。

## Corrected Claim

在 LRU 动态更新下，缓存实际包含的对象集合受限于最近访问频率，稳态命中率通常低于静态最优下界，需考虑对象驻留期内的淘汰概率影响，但具体修正公式依赖于访问模式假设。

## Evidence

[质询]公式 H_LRU_eff = H_static * (1 - P_eviction) 缺乏严格的理论推导支持，属于经验性修正而非标准缓存理论结论；标准 LRU 分析通常基于访问序列的独立性或特定分布假设，而非简单的乘法修正因子。 | 先验知识/题面给定，逻辑校验通过（量纲合理，概念自洽），但具体修正公式缺乏通用理论支持，降级为定性表述。

## Search Query

LRU steady state hit ratio eviction probability
