# N127: 多卡方案的 TCO 惩罚系数 (Multi-GPU Penalty Factor, MGP) 设定为 1.25。该系数涵盖：(1) 多卡互联导致的吞吐损失（约 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

多卡方案的 TCO 惩罚系数 (Multi-GPU Penalty Factor, MGP) 设定为 1.25。该系数涵盖：(1) 多卡互联导致的吞吐损失（约 15-20%，见 N52/N66）；(2) 多卡系统更高的故障率（MTBF 降低，维护成本增加约 10%）；(3) 多卡散热与电源冗余带来的额外 CapEx 和 OpEx。在计算 2x/4x 消费卡方案时，需将理论吞吐除以 1.25 以得到有效吞吐，并相应调整 TCO 模型。

## Corrected Claim

多卡方案的 TCO 惩罚系数 (Multi-GPU Penalty Factor, MGP) 设定为 1.25。该系数涵盖：(1) 多卡互联导致的吞吐损失（约 15-20%，见 N52/N66）；(2) 多卡系统更高的故障率（MTBF 降低，维护成本增加约 10%）；(3) 多卡散热与电源冗余带来的额外 CapEx 和 OpEx。在计算 2x/4x 消费卡方案时，需将理论吞吐除以 1.25 以得到有效吞吐，并相应调整 TCO 模型。

## Evidence

检索失败: no sources from any channel (all 5 failed)
