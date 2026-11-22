# N333: 基于 N137 修正后的总同步数据量 (169 GB) 和 NVLink 有效带宽 (500 GB/s)，2x A100 在 32K 上下文 Prefill 阶

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

基于 N137 修正后的总同步数据量 (169 GB) 和 NVLink 有效带宽 (500 GB/s)，2x A100 在 32K 上下文 Prefill 阶段的纯传输时间约为 169 / 500 ≈ 0.34 秒，加上同步延迟，总 TTFT 增加约 0.35-0.40 秒，仍远低于 PCIe 方案的开销，但并非 N117 声称的 <0.1 秒。

## Corrected Claim

基于 N137 修正后的总同步数据量 (169 GB) 和 NVLink 有效带宽 (500 GB/s)，2x A100 在 32K 上下文 Prefill 阶段的纯传输时间约为 169 / 500 ≈ 0.34 秒，加上同步延迟，总 TTFT 增加约 0.35-0.40 秒，仍远低于 PCIe 方案的开销，但并非 N117 声称的 <0.1 秒。

## Evidence

先验知识/题面给定，逻辑校验通过：169GB / 500GB/s = 0.338s，加上延迟后0.35-0.40s符合物理直觉，且明确指出了N117中<0.1s的错误，逻辑自洽。
