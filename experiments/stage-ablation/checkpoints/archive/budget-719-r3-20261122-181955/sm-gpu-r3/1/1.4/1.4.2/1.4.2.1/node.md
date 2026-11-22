# N191: Intel Max 1550 的 FP8 算力真实性核验：官方规格表中 '2.5 PFLOPS (sparse)' 通常指理论峰值，实际 LLM 推理中由于稀疏

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

Intel Max 1550 的 FP8 算力真实性核验：官方规格表中 '2.5 PFLOPS (sparse)' 通常指理论峰值，实际 LLM 推理中由于稀疏度限制和内存带宽瓶颈，有效算力通常仅为峰值的 30-50%，即实际可用算力约为 0.75-1.25 PFLOPS，需据此修正 Prefill 阶段吞吐量估算 [待核验]

## Corrected Claim

Intel Max 1550 的官方规格 '2.5 PFLOPS (sparse)' 为理论峰值。实际 LLM 推理中，受稀疏度实现难度和内存带宽瓶颈影响，有效算力通常低于峰值，具体效率需参考实际基准测试数据，一般经验估计可能在峰值的 30-50% 左右，但具体数值需实证验证。

## Evidence

[质询]该陈述包含具体的经验性数值范围（30-50% 效率、0.75-1.25 PFLOPS），属于经验事实而非第一性原理可推导的数学/物理定律。在缺乏官方基准测试或权威第三方评测来源支持的情况下，无法确认该特定效率区间是否准确适用于 Intel Max 1550 在 LLM 推理中的实际表现。 | 逻辑自洽（峰值算力乘以效率系数得到有效算力符合基本计算逻辑），但作为经验事实，缺乏来源直接支持具体数值范围，且检索无可用来源，依据经验事实排除条款降级。

## Search Query

Intel Max 1550 FP8 sparse FLOPS real-world inference performance
