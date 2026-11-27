# N39: 长期热点复用忽略带来的误差量化：假设 $T_{recent} = 1$ 天，则被忽略的长期热点（$R_i < 1$ 次/天）贡献的字节占比为 $1 - W(1)

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

长期热点复用忽略带来的误差量化：假设 $T_{recent} = 1$ 天，则被忽略的长期热点（$R_i < 1$ 次/天）贡献的字节占比为 $1 - W(1)/TotalBytes$。需计算该值以评估下界偏差，预计偏差在 5-15% 之间，取决于 $\alpha$ 和 $\beta$ 的耦合。

## Corrected Claim

长期热点复用忽略带来的误差量化：假设 $T_{recent} = 1$ 天，则被忽略的长期热点（$R_i < 1$ 次/天）贡献的字节占比为 $1 - W(1)/TotalBytes$。需计算该值以评估下界偏差，预计偏差在 5-15% 之间，取决于 $\alpha$ 和 $\beta$ 的耦合。

## Search Query

LRU cache lower bound error due to ignoring long-term hot objects
