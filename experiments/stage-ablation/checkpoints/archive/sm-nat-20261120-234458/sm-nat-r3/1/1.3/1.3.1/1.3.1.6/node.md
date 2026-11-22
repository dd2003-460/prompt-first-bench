# N90: 容量受限（K<N）时，热度-大小负相关对 LRU 命中率的量化影响：ΔH_LFU-LRU = (S_cold - S_hot) * (P_LRU_evict_c

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26, N27, N28

## Claim

容量受限（K<N）时，热度-大小负相关对 LRU 命中率的量化影响：ΔH_LFU-LRU = (S_cold - S_hot) * (P_LRU_evict_cold - P_LFU_evict_cold) * (1/μ_S)，其中 P_LRU_evict_cold > P_LFU_evict_cold，故 LFU 优于 LRU，具体增益取决于 K/N 比值和 ρ 的强度

## Corrected Claim

在容量受限且存在热度-大小负相关（即冷对象通常更大）的场景下，LFU 通常优于 LRU，因为 LFU 倾向于保留高频访问的小对象，而 LRU 可能因大冷对象占据空间导致高频小对象被驱逐。具体增益取决于 K/N 比值、访问频率分布（ρ）以及对象大小分布，但无法用单一简单公式 ΔH = (S_cold - S_hot) * ΔP * (1/μ_S) 精确量化。

## Evidence

[质询]公式中的量纲和物理意义存在严重问题：(S_cold - S_hot) 是大小差，P 是概率，1/μ_S 是平均大小的倒数，三者相乘得到的量纲是 [Size] * [Prob] * [1/Size] = [Prob]，虽然量纲上看似匹配命中率差值（无量纲或概率），但逻辑上 LFU 和 LRU 的命中率差异并非由简单的“大小差”线性驱动，而是由访问频率分布和缓存替换策略的交互决定。此外，P_LRU_evict_cold > P_LFU_evict_cold 这一前提在一般热度-大小负相关场景下并不总是成立，取决于具体的访问模式（如 Zipf 分布参数）和缓存大小 K。该公式更像是一个启发式近似或特定假设下的推导，而非普适的量化公式。 | 先验知识/题面给定，逻辑校验未通过：公式缺乏普适性，量纲虽勉强匹配但物理机制描述过于简化且前提条件（P_LRU_evict_cold > P_LFU_evict_cold）非必然成立，属于经验性/启发式结论而非严格推导。
