# N187: 量化尾部对象对字节未命中率的贡献占比：Ratio_byte_miss_tail = (P_tail * E[S|Tail]) / (Σ_{i=1}^{N} p_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

量化尾部对象对字节未命中率的贡献占比：Ratio_byte_miss_tail = (P_tail * E[S|Tail]) / (Σ_{i=1}^{N} p_i * s_i)，该比率表明尽管尾部对象数量少，但因尺寸大且热度低，占据了未命中字节流量的绝大部分。

## Corrected Claim

量化尾部对象对字节未命中率的贡献占比：Ratio_byte_miss_tail = (P_tail * E[S|Tail]) / (Σ_{i=1}^{N} p_i * s_i)，该比率表明尽管尾部对象数量少，但因尺寸大且热度低，占据了未命中字节流量的绝大部分。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合加权平均逻辑，且符合Zipf分布下长尾对象因尺寸大、访问频率低导致缓存未命中字节占比高的经典缓存理论结论。
