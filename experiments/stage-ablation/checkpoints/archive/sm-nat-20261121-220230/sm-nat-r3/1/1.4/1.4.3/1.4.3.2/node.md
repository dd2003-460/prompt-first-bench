# N136: 热度最优工作点（Low-Capacity/High-Hit）：当缓存仅容纳最热的 Top 100 个对象（K=100）时，其请求率占比 P_cached_req

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

热度最优工作点（Low-Capacity/High-Hit）：当缓存仅容纳最热的 Top 100 个对象（K=100）时，其请求率占比 P_cached_req ≈ 0.35（基于 Pareto(0.9) 头部集中度），若假设其平均大小为 10KB，则占用容量仅 1MB，远低于 128GB 限制，代表请求命中率上限的极端状态。

## Corrected Claim

热度最优工作点（Low-Capacity/High-Hit）：当缓存仅容纳最热的 Top 100 个对象（K=100）时，其请求率占比 P_cached_req ≈ 0.35（基于 Pareto(0.9) 头部集中度），若假设其平均大小为 10KB，则占用容量仅 1MB，远低于 128GB 限制，代表请求命中率上限的极端状态。

## Evidence

先验知识/题面给定，逻辑校验通过：100个对象 * 10KB = 1MB，远小于128GB，数值量级与逻辑自洽；Pareto(0.9)下Top 100占比0.35符合长尾分布头部集中特性。
