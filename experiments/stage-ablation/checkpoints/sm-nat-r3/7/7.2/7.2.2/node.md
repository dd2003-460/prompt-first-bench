# N269: 工作点 B（边界临界）：假设 E[S | top 10%] = 12.8KB，计算 S_top10 = 0.1 * 100000 * 12.8KB = 128G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

工作点 B（边界临界）：假设 E[S | top 10%] = 12.8KB，计算 S_top10 = 0.1 * 100000 * 12.8KB = 128GB = 128GB，LRU 恰好能保护头部 10% 对象，命中率下界为 C_req(0.1)，但无任何余量，任何大小波动都会导致部分头部对象被驱逐。

## Corrected Claim

工作点 B（边界临界）：假设 E[S | top 10%] = 12.8KB，计算 S_top10 = 0.1 * 100000 * 12.8KB = 128GB = 128GB，LRU 恰好能保护头部 10% 对象，命中率下界为 C_req(0.1)，但无任何余量，任何大小波动都会导致部分头部对象被驱逐。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 0.1 * 100000 * 12.8KB = 128GB 正确，LRU 边界临界逻辑自洽
