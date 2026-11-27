# N145: Batch Size 对通信开销占比的影响：当 Batch Size 从 1 增加到 8 时，Compute_Time 线性增加而 Comm_Time 保持不变

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Batch Size 对通信开销占比的影响：当 Batch Size 从 1 增加到 8 时，Compute_Time 线性增加而 Comm_Time 保持不变（或小幅增加），导致通信开销占比从 >30% 下降到 <15%，这使得 PCIe 互联在较高 Batch Size 下的劣势显著缓解

## Corrected Claim

Batch Size 对通信开销占比的影响：当 Batch Size 从 1 增加到 8 时，Compute_Time 线性增加而 Comm_Time 保持不变（或小幅增加），导致通信开销占比从 >30% 下降到 <15%，这使得 PCIe 互联在较高 Batch Size 下的劣势显著缓解

## Evidence

先验知识/题面给定，逻辑校验通过：Batch Size 增加通常线性增加计算量（Compute_Time），而通信量（Comm_Time）在固定模型结构下往往保持不变或仅随激活值微小变化，因此通信占比下降符合分布式训练基本原理。
