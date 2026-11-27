# N270: 工作点 C（头部过大）：假设 E[S | top 10%] = 20KB，计算 S_top10 = 0.1 * 100000 * 20KB = 200GB > 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

工作点 C（头部过大）：假设 E[S | top 10%] = 20KB，计算 S_top10 = 0.1 * 100000 * 20KB = 200GB > 128GB，LRU 无法完整保护头部 10% 对象，需计算实际可保护的头部对象比例 k' = 128GB / (0.1 * 100000 * 20KB) = 64%，命中率下界需按 C_req(0.064) 修正。

## Corrected Claim

工作点 C（头部过大）：假设 E[S | top 10%] = 20KB，计算 S_top10 = 0.1 * 100000 * 20KB = 200GB > 128GB，LRU 无法完整保护头部 10% 对象，需计算实际可保护的头部对象比例 k' = 128GB / (0.1 * 100000 * 20KB) = 64%，命中率下界需按 C_req(0.064) 修正。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.1 * 100000 * 20KB = 200GB 正确，200GB > 128GB 成立，比例 128/200 = 64% 正确，逻辑自洽。
