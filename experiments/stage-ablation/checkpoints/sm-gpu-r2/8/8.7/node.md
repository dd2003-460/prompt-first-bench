# N99: COF 动态计算公式：COF = 1 / (1 + (Comm_Time / Compute_Time))。其中 Comm_Time = Comm_Data /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27, N28

## Claim

COF 动态计算公式：COF = 1 / (1 + (Comm_Time / Compute_Time))。其中 Comm_Time = Comm_Data / PCIe_BW，Compute_Time = Token_Compute_FLOPS / GPU_FLOPS。当 Compute_Time 较大（如大 batch）时，COF 趋近于 1；当 Compute_Time 较小（如 batch=1）时，COF 可能降至 0.80-0.85。

## Corrected Claim

COF 动态计算公式：COF = 1 / (1 + (Comm_Time / Compute_Time))。其中 Comm_Time = Comm_Data / PCIe_BW，Compute_Time = Token_Compute_FLOPS / GPU_FLOPS。当 Compute_Time 较大（如大 batch）时，COF 趋近于 1；当 Compute_Time 较小（如 batch=1）时，COF 可能降至 0.80-0.85。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合通信计算重叠模型，极限情况（Compute_Time→∞时COF→1）及典型数值范围（0.80-0.85）符合GPU集群通信开销的工程经验。
