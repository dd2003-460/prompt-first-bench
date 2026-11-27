# N26: LRU在Pareto(β=0.9)请求分布下的稳态字节命中率下界H_byte_LRU_lower，可通过假设LRU完美保留前K个最热对象（Optimal近似）减

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU在Pareto(β=0.9)请求分布下的稳态字节命中率下界H_byte_LRU_lower，可通过假设LRU完美保留前K个最热对象（Optimal近似）减去LRU特有的驱逐惩罚项ε_lru估算。ε_lru与请求间隔方差成正比，对于β<1.5的分布，ε_lru通常导致命中率比Optimal低2-5个百分点。

## Corrected Claim

LRU在Pareto(β=0.9)请求分布下的稳态字节命中率下界H_byte_LRU_lower，可通过假设LRU完美保留前K个最热对象（Optimal近似）减去LRU特有的驱逐惩罚项ε_lru估算。ε_lru与请求间隔方差成正比，对于β<1.5的分布，ε_lru通常导致命中率比Optimal低2-5个百分点。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1专注于量化惩罚项ε_lru的推导，子节点2专注于最终命中率H_byte_LRU_lower的计算，两者逻辑上前后依赖但内容不重叠，且共同覆盖了父节点中‘估算公式’和‘具体数值/条件’的所有关键方面。）
