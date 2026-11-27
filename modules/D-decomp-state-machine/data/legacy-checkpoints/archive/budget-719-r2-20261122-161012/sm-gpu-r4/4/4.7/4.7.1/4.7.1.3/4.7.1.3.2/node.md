# N600: RTX 4090 双卡 TP=2 在 PCIe 4.0 x16 互联下的 All-Reduce 同步开销量化：每生成一个 token，需在两卡间交换 KV Ca

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N250, N251, N252

## Claim

RTX 4090 双卡 TP=2 在 PCIe 4.0 x16 互联下的 All-Reduce 同步开销量化：每生成一个 token，需在两卡间交换 KV Cache 增量及 Attention 中间结果。PCIe 4.0 x16 双向带宽约 32 GB/s (理论)，有效带宽约 25 GB/s。假设每 token 需同步数据量为 S_sync (取决于 Head 数量和量化精度)，则 T_sync = S_sync / 25 GB/s。若 S_sync 为 1 MB，则 T_sync ≈ 40 μs，占理论 T_decode (13.9 GB / 1008 GB/s ≈ 13.8 ms) 的 0.3%，此时 80-90% 效率系数主要受软件调度延迟而非带宽限制，需引入 vLLM 双卡实测数据修正该系数。

## Corrected Claim

RTX 4090 双卡 TP=2 在 PCIe 4.0 x16 互联下的 All-Reduce 同步开销量化：每生成一个 token，需在两卡间交换 KV Cache 增量及 Attention 中间结果。PCIe 4.0 x16 双向带宽约 32 GB/s (理论)，有效带宽约 25 GB/s。假设每 token 需同步数据量为 S_sync (取决于 Head 数量和量化精度)，则 T_sync = S_sync / 25 GB/s。若 S_sync 为 1 MB，则 T_sync ≈ 40 μs，占理论 T_decode (13.9 GB / 1008 GB/s ≈ 13.8 ms) 的 0.3%，此时 80-90% 效率系数主要受软件调度延迟而非带宽限制，需引入 vLLM 双卡实测数据修正该系数。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 带宽数值（理论~32GB/s，有效~25GB/s）及由此推导的同步延迟占比（~0.3%）符合物理规律与工程常识，且结论（软件调度为主要瓶颈）逻辑自洽。

## Search Query

vLLM tensor parallel 2x RTX 4090 PCIe latency overhead benchmark
