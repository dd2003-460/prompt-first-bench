# N655: 低命中率工作点（H=0.70）：Traffic_out_self_low = 2,000,000 MB * (1 - 0.70) = 600,000 MB/da

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N220

## Claim

低命中率工作点（H=0.70）：Traffic_out_self_low = 2,000,000 MB * (1 - 0.70) = 600,000 MB/day = 600 GB/day；此工作点代表缓存策略失效或长尾内容占比极高的极端情况，回源带宽需求为基准值的1.5倍，直接导致P_bw_self线性增加33%。

## Corrected Claim

低命中率工作点（H=0.70）：Traffic_out_self_low = 2,000,000 MB * (1 - 0.70) = 600,000 MB/day = 600 GB/day；此工作点代表缓存策略失效或长尾内容占比极高的极端情况，回源带宽需求为基准值的1.5倍，直接导致P_bw_self线性增加33%。
