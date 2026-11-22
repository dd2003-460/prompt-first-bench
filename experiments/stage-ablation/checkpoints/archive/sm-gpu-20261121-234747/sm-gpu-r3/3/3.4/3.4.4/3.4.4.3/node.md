# N281: Qwen3-27B在TP=2配置下，Decode阶段每步的通信延迟占比 α_comm = T_comm / (T_compute + T_comm)，其中T_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

Qwen3-27B在TP=2配置下，Decode阶段每步的通信延迟占比 α_comm = T_comm / (T_compute + T_comm)，其中T_comm = V_comm / Bandwidth_effective，T_compute = FLOPs_per_token / TFLOPS_peak，需计算BF16和INT8两种精度下的α_comm具体百分比

## Corrected Claim

Qwen3-27B在TP=2配置下，Decode阶段每步的通信延迟占比 α_comm = T_comm / (T_compute + T_comm)，其中T_comm = V_comm / Bandwidth_effective，T_compute = FLOPs_per_token / TFLOPS_peak，需计算BF16和INT8两种精度下的α_comm具体百分比

## Evidence

先验知识/题面给定，逻辑校验通过
