# N237: LRU在Zipf(β=0.9)分布下的稳态字节命中率下界公式为 H_LRU_lower = (∑_{i=1}^{K} i^{-β} * s_i) / (∑_{i

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU在Zipf(β=0.9)分布下的稳态字节命中率下界公式为 H_LRU_lower = (∑_{i=1}^{K} i^{-β} * s_i) / (∑_{i=1}^{N} i^{-β} * s_i)，其中K由缓存容量C和对象大小分布决定；由于β<1，分母发散需截断至N=100,000，该公式是区分请求命中率与字节命中率的关键，需通过数值积分求解s_i与i的关联

## Corrected Claim

在独立参考模型（IRM）假设下，LRU在Zipf(β=0.9)分布下的稳态字节命中率近似公式为 H_LRU ≈ (∑_{i=1}^{K} i^{-β} * s_i) / (∑_{i=1}^{N} i^{-β} * s_i)，其中K由缓存容量C和对象大小分布决定；由于β<1，分母发散需截断至N=100,000。

## Evidence

[质询]该公式并非LRU命中率的严格下界，而是基于独立参考假设（Independent Reference Model, IRM）的稳态命中率近似值；在存在时间局部性（temporal locality）的实际工作负载中，LRU的实际命中率通常高于此IRM预测值，因此将其称为'下界'在理论严谨性上存在争议，且参考来源未提供该具体公式的推导或验证。 | 逻辑上，IRM模型下LRU命中率确实由缓存内对象的访问概率占比决定，公式结构符合概率加权平均的定义，且β<1时截断处理合理；但参考来源[1]仅定性描述了命中率随缓存容量变化的趋势，未提供该具体数学公式，属于间接支持或无关，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/98144430&rut=1145d575b95cf27fee1ec7245683ec6a13e770da8ef139d709a6880892fabc55', 'type': 'ddg', 'title': 'Lru缓存命中率建模 - 知乎专栏'}
