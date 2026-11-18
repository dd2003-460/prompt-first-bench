# N62: 全局有效命中率 H_eff 的加权平均：H_eff = Σ (H_LRU_i * (1 - R_inv_i) * ByteShare_i)，其中 ByteSha

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

全局有效命中率 H_eff 的加权平均：H_eff = Σ (H_LRU_i * (1 - R_inv_i) * ByteShare_i)，其中 ByteShare_i 为对象 i 的字节流量占比；由于热门对象 ByteShare 高且 R_inv 极低，全局 H_eff 接近 H_LRU，折损主要来自冷门对象，但冷门对象 ByteShare 低，因此总折损 < 1%。

## Corrected Claim

全局有效命中率 H_eff 的加权平均：H_eff = Σ (H_LRU_i * (1 - R_inv_i) * ByteShare_i)，其中 ByteShare_i 为对象 i 的字节流量占比；由于热门对象 ByteShare 高且 R_inv 极低，全局 H_eff 接近 H_LRU，折损主要来自冷门对象，但冷门对象 ByteShare 低，因此总折损 < 1%。

## Evidence

先验知识/题面给定，逻辑校验通过
