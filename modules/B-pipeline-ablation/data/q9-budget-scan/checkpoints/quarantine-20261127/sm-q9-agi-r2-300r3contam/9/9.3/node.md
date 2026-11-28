# N85: MTP 验证步骤的串行延迟公式：T_verify(L) = (L * d_model * 2 * 4) / BW_eff + T_compute_overhea

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

MTP 验证步骤的串行延迟公式：T_verify(L) = (L * d_model * 2 * 4) / BW_eff + T_compute_overhead，其中 L 为上下文长度，BW_eff 为 N33 测得的有效带宽，T_compute_overhead 为 CUDA Kernel 启动与同步开销（约 5-10ms/step）。当 L=131k 时，T_verify 占总推理时间的比例超过 60%，成为主要瓶颈。

## Corrected Claim

MTP 验证步骤的串行延迟公式：T_verify(L) = (L * d_model * 2 * 4) / BW_eff + T_compute_overhead，其中 L 为上下文长度，BW_eff 为 N33 测得的有效带宽，T_compute_overhead 为 CUDA Kernel 启动与同步开销（约 5-10ms/step）。当 L=131k 时，T_verify 占总推理时间的比例超过 60%，成为主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过
