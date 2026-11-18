# N62: 全局有效命中率 H_eff 的加权平均：H_eff = Σ (H_LRU_i * (1 - R_inv_i) * ByteShare_i)，其中 ByteSha

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

全局有效命中率 H_eff 的加权平均：H_eff = Σ (H_LRU_i * (1 - R_inv_i) * ByteShare_i)，其中 ByteShare_i 为对象 i 的字节流量占比；由于热门对象 ByteShare 高且 R_inv 极低，全局 H_eff 接近 H_LRU，折损主要来自冷门对象，但冷门对象 ByteShare 低，因此总折损 < 1%。

## Corrected Claim

全局有效命中率 H_eff 的加权平均：H_eff = Σ (H_LRU_i * (1 - R_inv_i) * ByteShare_i)，其中 ByteShare_i 为对象 i 的字节流量占比；由于热门对象 ByteShare 高且 R_inv 极低，全局 H_eff 接近 H_LRU，折损主要来自冷门对象，但冷门对象 ByteShare 低，因此总折损 < 1%。

## Evidence

父节点级核验未通过：不完备（子节点分别计算了公式中的两个关键变量 ByteShare 和 R_inv，彼此正交且不冗余。但父节点结论强调 H_eff 接近 H_LRU 且折损 < 1%，这依赖于 H_LRU_i 的值以及加权求和后的最终对比。当前子节点缺失了对 H_LRU_i（各层基础命中率）的计算或定义，也未包含最终加权求和与阈值验证的步骤，因此无法完整推导父节点关于'折损 < 1%'的结论。）
