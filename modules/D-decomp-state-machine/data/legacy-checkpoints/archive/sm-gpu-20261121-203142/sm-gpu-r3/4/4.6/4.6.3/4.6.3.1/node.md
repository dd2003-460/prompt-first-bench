# N308: 延迟约束下 Prefill 吞吐量的线性关系：Prefill_TPS_batch = Prefill_TPS_single / Batch_Size (近似)。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

延迟约束下 Prefill 吞吐量的线性关系：Prefill_TPS_batch = Prefill_TPS_single / Batch_Size (近似)。若单请求 TTFT 目标为 2s，且单请求 Prefill 耗时 T_prefill_single，则最大 Prefill Batch Size B_prefill_max = T_target / T_prefill_single。

## Corrected Claim

延迟约束下 Prefill 吞吐量的线性关系：Prefill_TPS_batch = Prefill_TPS_single / Batch_Size (近似)。若单请求 TTFT 目标为 2s，且单请求 Prefill 耗时 T_prefill_single，则最大 Prefill Batch Size B_prefill_max = T_target / T_prefill_single。

## Evidence

先验知识/题面给定，逻辑校验通过
