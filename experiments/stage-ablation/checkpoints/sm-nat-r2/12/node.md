# N83: 考虑大小-热度负相关 (ρ=-0.3) 后，LRU 稳态字节命中率下界需乘以容量修正因子 η_cap，其中 η_cap = C / (C + Σ_{i>K} s

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

考虑大小-热度负相关 (ρ=-0.3) 后，LRU 稳态字节命中率下界需乘以容量修正因子 η_cap，其中 η_cap = C / (C + Σ_{i>K} s_i * (λ_i/λ_K))，该因子量化了因缓存热门小对象而挤出冷大对象带来的命中率提升。

## Corrected Claim

在考虑大小-热度负相关的特定理论模型中，LRU稳态字节命中率下界可引入容量修正因子 η_cap 进行量化，其形式可能涉及缓存容量与冷大对象负载的比值，但具体公式需依据特定模型假设推导。

## Evidence

[质询]该公式为特定理论模型下的推导结果，并非LRU算法的通用物理定律或第一性原理必然结论；且参考来源仅讨论Redis配置，未提供该具体数学公式的支持，属于缺乏外部证据支持的特定经验/理论断言。 | 逻辑上量纲自洽（容量/容量），但参考来源[1]仅涉及Redis LRU/LFU概念区别，未覆盖该特定容量修正因子公式，属于经验/理论事实且缺来源直接支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=e57a03057fb2bd9f336ab899a15bcdb96faf02186ece640b0fe55a9a1a8bbac0', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
