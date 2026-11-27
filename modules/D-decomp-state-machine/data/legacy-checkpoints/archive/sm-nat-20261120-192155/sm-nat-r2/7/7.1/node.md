# N45: 量化负相关ρ对LRU命中率的下界修正：在独立假设下，LRU保留的对象集合C_LRU由热度前k'个对象组成（k'由大小约束决定）；负相关使得大对象更冷，LRU驱逐

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

量化负相关ρ对LRU命中率的下界修正：在独立假设下，LRU保留的对象集合C_LRU由热度前k'个对象组成（k'由大小约束决定）；负相关使得大对象更冷，LRU驱逐大对象时损失的热度字节流更少，因此H_LRU_ρ > H_LRU_independent；具体提升量ΔH ≈ |ρ| * (H_LFU - H_LRU_independent) * 0.5，需通过蒙特卡洛模拟验证。

## Corrected Claim

在独立假设下，LRU保留的对象集合由热度前k'个对象组成；负相关使得大对象更冷，理论上可能减少LRU驱逐大对象时的热度损失，从而提升命中率，但具体提升量需通过蒙特卡洛模拟验证，无通用解析公式。

## Evidence

[质询]该陈述包含具体的经验性公式（ΔH ≈ |ρ| * ... * 0.5）和特定的因果机制推导，属于经验事实/模型结论，无法仅从第一性原理严格推出，且参考来源未提供相关数据支持。 | 逻辑上负相关确实可能通过改变驱逐顺序影响命中率，但具体量化公式缺乏来源支持，且来源[1]仅介绍LRU历史，与该具体修正公式无关。

## Search Query

LRU cache hit rate correlation between size and popularity simulation

## Retrieval Sources

- {'url': 'https://github.com/AdaMartin18010/BufferCache/blob/main/docs/01-%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80/01.01-%E5%9F%BA%E7%A1%80%E6%9B%BF%E6%8D%A2%E7%AE%97%E6%B3%95/01.01.01-LRU%E7%AE%97%E6%B3%95%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E7%8E%B0.md&rut=f4772cbf8eb9a4f4395edeebcef330ac786b1908279f3eec505b26fb5a97d27d', 'type': 'ddg', 'title': '01.01.01-LRU算法原理与实现.md - GitHub'}
