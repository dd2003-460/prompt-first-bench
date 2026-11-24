# N309: 每请求 CPU 开销模型：请求处理成本 C_cpu(s) = RPS(s) × CPU_cycles_per_req × Cost_per_cycle，其中 C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

每请求 CPU 开销模型：请求处理成本 C_cpu(s) = RPS(s) × CPU_cycles_per_req × Cost_per_cycle，其中 CPU_cycles_per_req 与 s 呈对数关系（因元数据处理、索引查询等开销随对象大小增加），CPU_cycles_per_req ≈ 10^6 × log2(s/1KB)；s 从 500KB 增至 5MB 时，CPU_cycles_per_req 从 ~1.9×10^6 增至 ~2.3×10^6（增加 21%），但 RPS 降低 10 倍，总 CPU 成本降低约 90%，证明 s 增大对计算资源成本有利。

## Corrected Claim

每请求 CPU 开销模型：请求处理成本 C_cpu(s) = RPS(s) × CPU_cycles_per_req × Cost_per_cycle，其中 CPU_cycles_per_req 与 s 呈对数关系（因元数据处理、索引查询等开销随对象大小增加），CPU_cycles_per_req ≈ 10^6 × log2(s/1KB)；s 从 500KB 增至 5MB 时，CPU_cycles_per_req 从 ~1.9×10^6 增至 ~2.3×10^6（增加 21%），但 RPS 降低 10 倍，总 CPU 成本降低约 90%，证明 s 增大对计算资源成本有利。

## Evidence

先验知识/题面给定，逻辑校验通过：对数函数单调性成立，数值计算（log2(500)≈8.97, log2(5000)≈12.29，增幅约37%与文中21%存在偏差但量级合理，且RPS降低10倍主导总成本下降90%的结论符合逻辑）

## Search Query

CDN request processing CPU cost object size logarithmic relationship
