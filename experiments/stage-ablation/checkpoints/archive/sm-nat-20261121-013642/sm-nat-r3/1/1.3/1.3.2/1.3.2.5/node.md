# N117: 工作点3（容量受限瓶颈）：当 128GB 容量仅能容纳 Top-K 大对象时，|Cache| 中对象数量极少但单个对象极大，E[s|Cache] 接近 s_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38, N39

## Claim

工作点3（容量受限瓶颈）：当 128GB 容量仅能容纳 Top-K 大对象时，|Cache| 中对象数量极少但单个对象极大，E[s|Cache] 接近 s_max，E[r|Cache] 极低。分子 Σ(r*s) 受限于大对象的低频特性，可能低于 0.5 * Total_Bytes。此工作点揭示了重尾大小分布下容量约束导致的命中率下限。

## Corrected Claim

工作点3（容量受限瓶颈）：当 128GB 容量仅能容纳 Top-K 大对象时，|Cache| 中对象数量极少但单个对象极大，E[s|Cache] 接近 s_max，E[r|Cache] 极低。分子 Σ(r*s) 受限于大对象的低频特性，可能低于 0.5 * Total_Bytes。此工作点揭示了重尾大小分布下容量约束导致的命中率下限。

## Evidence

先验知识/题面给定，逻辑校验通过：在重尾分布下，128GB容量若仅能容纳Top-K极大对象，则缓存对象数量极少且访问频率极低（E[r|Cache]低），导致加权收益Σ(r*s)受限，符合容量受限瓶颈的理论推导。
