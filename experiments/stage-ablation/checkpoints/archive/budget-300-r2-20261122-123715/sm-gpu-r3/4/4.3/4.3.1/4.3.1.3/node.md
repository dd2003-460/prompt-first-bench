# N310: 2x RTX 4090 TP=2 并行效率 k_parallel_efficiency 的精确计算公式：k = (T_single * 2) / T_dual，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91, N92, N93

## Claim

2x RTX 4090 TP=2 并行效率 k_parallel_efficiency 的精确计算公式：k = (T_single * 2) / T_dual，其中 T_single 为单卡吞吐，T_dual 为双卡吞吐；由于 T_dual ≈ T_single / (1 + Latency_comm / T_compute_per_token)，需实测 T_compute_per_token (纯计算时间) 与 Latency_comm 的比值来确定 k 的具体数值，而非仅凭经验值 0.7-0.8。

## Corrected Claim

2x RTX 4090 TP=2 并行效率 k_parallel_efficiency 的精确计算公式：k = (T_single * 2) / T_dual，其中 T_single 为单卡吞吐，T_dual 为双卡吞吐；由于 T_dual ≈ T_single / (1 + Latency_comm / T_compute_per_token)，需实测 T_compute_per_token (纯计算时间) 与 Latency_comm 的比值来确定 k 的具体数值，而非仅凭经验值 0.7-0.8。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 k = (T_single * 2) / T_dual 是并行效率的标准定义（理想加速比2与实际加速比之比），且基于 Amdahl 定律或通信开销模型的推导逻辑自洽，数值量级合理。

## Search Query

tensor parallel efficiency calculation communication overhead ratio
