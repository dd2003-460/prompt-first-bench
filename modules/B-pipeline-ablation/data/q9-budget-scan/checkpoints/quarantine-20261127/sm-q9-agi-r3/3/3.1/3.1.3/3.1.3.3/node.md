# N151: MTP×4 的净加速比 Speedup = (1 + α*k) / (1 + k*t_draft/t_target)，其中 k=4 为投机步数，t_draft/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

MTP×4 的净加速比 Speedup = (1 + α*k) / (1 + k*t_draft/t_target)，其中 k=4 为投机步数，t_draft/t_target 为 draft 与 target 单 token 生成时间比；在 V100 集群上，t_draft ≈ 0.3*t_target（因 draft 模型更小），当 α=0.65 时，Speedup = (1+2.6)/(1+1.2) = 1.63x，与题面 2.5x 存在偏差，需考虑 Batch Size 对 draft/target 吞吐的非线性影响。

## Corrected Claim

MTP×4 的净加速比 Speedup = (1 + α*k) / (1 + k*t_draft/t_target)，其中 k=4 为投机步数，t_draft/t_target 为 draft 与 target 单 token 生成时间比；在 V100 集群上，t_draft ≈ 0.3*t_target（因 draft 模型更小），当 α=0.65 时，Speedup = (1+2.6)/(1+1.2) = 1.63x，与题面 2.5x 存在偏差，需考虑 Batch Size 对 draft/target 吞吐的非线性影响。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算无误（(1+0.65*4)/(1+4*0.3)=3.6/2.2≈1.636），且正确指出了理论值与题面观测值的偏差及潜在原因（Batch Size非线性影响）。

## Search Query

speculative decoding speedup formula batch size effect draft target latency ratio
