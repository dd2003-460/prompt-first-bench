# N47: 负相关对 LFU 增益抑制的物理机制量化：由于 ρ=-0.3，热门对象倾向于较小。LFU 的优势在于保留高频对象，而 LRU 的优势在于保留最近访问。当热门对象

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

负相关对 LFU 增益抑制的物理机制量化：由于 ρ=-0.3，热门对象倾向于较小。LFU 的优势在于保留高频对象，而 LRU 的优势在于保留最近访问。当热门对象较小时，LRU 更容易在有限容量下保留它们（因为占用空间小，驱逐频率低），从而缩小 LFU 相对于 LRU 的差距。量化指标：LRU 在 ρ=-0.3 下的有效容量利用率提升系数 C_eff_factor = 1 / (1 - ρ * σ_size/σ_rank)。

## Corrected Claim

负相关（ρ=-0.3）使得热门对象倾向于较小，从而在有限容量下 LRU 能更有效地保留高频对象，缩小 LFU 相对于 LRU 的性能差距。具体量化系数需依赖特定缓存模型假设，通用公式 C_eff_factor = 1 / (1 - ρ * σ_size/σ_rank) 缺乏广泛认可的物理推导。

## Evidence

[质询]公式 C_eff_factor = 1 / (1 - ρ * σ_size/σ_rank) 缺乏明确的物理或数学推导依据，且量纲/定义模糊（σ_size/σ_rank 的比值含义不明，通常相关系数 ρ 无量纲，但此处乘积项的物理意义未定义），属于经验事实或特定模型假设，无法从第一性原理严格推出。 | 先验知识/题面给定，逻辑校验通过（定性机制合理，但定量公式缺乏通用理论支持，视为特定模型假设）

## Search Query

cache efficiency size popularity negative correlation LRU advantage
