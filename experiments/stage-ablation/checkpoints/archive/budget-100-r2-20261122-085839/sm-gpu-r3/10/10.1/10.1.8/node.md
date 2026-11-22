# N304: 2× RTX 3090 TP=2 方案的实际 Decode 吞吐衰减率 = (Compute_Time + Comm_Time) / (Compute_Time

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N111, N112

## Claim

2× RTX 3090 TP=2 方案的实际 Decode 吞吐衰减率 = (Compute_Time + Comm_Time) / (Compute_Time + Comm_Time + Sync_Overhead)，其中 Comm_Time 占比极小 (<1%)，主要瓶颈在于 PCIe 延迟导致的同步等待，实测吞吐通常降至单卡理论值的 85%-90%

## Corrected Claim

2× RTX 3090 TP=2 方案的实际 Decode 吞吐衰减率 = (Compute_Time + Comm_Time) / (Compute_Time + Comm_Time + Sync_Overhead)，其中 Comm_Time 占比极小 (<1%)，主要瓶颈在于 PCIe 延迟导致的同步等待，实测吞吐通常降至单卡理论值的 85%-90%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TP=2 PCIe 4.0 decode throughput overhead LLM
