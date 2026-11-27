# N26: 对象更新率 1%/天 对 LRU 有效命中率的衰减系数估算：假设对象平均驻留时间 T_res 由访问频率决定。对于热度为 h 的对象，T_res ≈ 1/h (

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 1%/天 对 LRU 有效命中率的衰减系数估算：假设对象平均驻留时间 T_res 由访问频率决定。对于热度为 h 的对象，T_res ≈ 1/h (天)。更新导致失效的概率 P_stale ≈ λ_upd * T_res = 0.01 * (1/h)。对于热门对象 (h 大)，P_stale 小；对于冷门对象 (h 小)，P_stale 大。整体有效命中率 Hit_eff = ∫ P_hit(s,h) * (1 - P_stale(h)) * f_S(s,h) dsdh / E[S]。由于热门对象贡献大部分字节流量，且其 P_stale 较小，整体衰减系数 D ≈ 1 - E[P_stale | Byte Weighted]。若平均字节加权的热度 h_avg 使得 1/h_avg ≈ 10 天，则 D ≈ 1 - 0.01*10 = 0.9，即打 9 折。

## Corrected Claim

在假设对象平均驻留时间 T_res ≈ 1/h 且字节加权平均驻留时间为 10 天的特定模型下，1%/天的对象更新率预计导致 LRU 有效命中率衰减至约 90%（即打 9 折）。该估算依赖于具体的访问热度分布和更新模式，实际衰减系数需根据具体业务数据校准。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于衰减因子D的数学定义与公式推导，子节点2聚焦于关键参数h_avg的具体计算逻辑与数值来源，两者在内容上互不重叠且互补，共同覆盖了父节点中关于公式和参数估算的所有关键方面，无冗余。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/98144430&rut=bffd219857e911b72762d8291a2aad02641f7a98966313f25dd4420d25c7fdfa', 'type': 'ddg', 'title': 'Lru缓存命中率建模 - 知乎专栏'}
