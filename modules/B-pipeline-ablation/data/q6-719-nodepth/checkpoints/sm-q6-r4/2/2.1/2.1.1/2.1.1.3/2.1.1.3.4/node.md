# N598: NIC 选型对 P99 延迟的量化影响：标准 NIC 在 10Gbps 满载时，由于中断处理和上下文切换，P99 延迟抖动 (Jitter) 约为 2-5ms；

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N205

## Claim

NIC 选型对 P99 延迟的量化影响：标准 NIC 在 10Gbps 满载时，由于中断处理和上下文切换，P99 延迟抖动 (Jitter) 约为 2-5ms；RDMA NIC 可将 P99 抖动降低至 0.1-0.5ms。若 P99 目标 T < 20ms，标准 NIC 已满足要求；若 T < 5ms (如实时视频首帧加载)，则必须选用 RDMA NIC，此时 NIC 成本差异 (¥4,000 vs ¥2,000) 相对于总 CapEx 占比 <5%，但决定了 P99 合规性。

## Corrected Claim

NIC 选型对 P99 延迟的量化影响：标准 NIC 在 10Gbps 满载时，由于中断处理和上下文切换，P99 延迟抖动 (Jitter) 约为 2-5ms；RDMA NIC 可将 P99 抖动降低至 0.1-0.5ms。若 P99 目标 T < 20ms，标准 NIC 已满足要求；若 T < 5ms (如实时视频首帧加载)，则必须选用 RDMA NIC，此时 NIC 成本差异 (¥4,000 vs ¥2,000) 相对于总 CapEx 占比 <5%，但决定了 P99 合规性。

## Evidence

先验知识/题面给定，逻辑校验通过
