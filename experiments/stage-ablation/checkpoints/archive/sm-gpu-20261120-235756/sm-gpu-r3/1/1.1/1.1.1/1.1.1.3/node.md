# N143: MoE 模型的显存带宽瓶颈修正：由于非激活专家参数（47.68 GB）不参与计算，实际推理时的有效带宽需求仅由激活参数（6.6 GB）和 KV Cache 读取

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

MoE 模型的显存带宽瓶颈修正：由于非激活专家参数（47.68 GB）不参与计算，实际推理时的有效带宽需求仅由激活参数（6.6 GB）和 KV Cache 读取决定，因此理论 TPOT 计算应基于激活参数而非总参数，修正后的理论 TPOT 上限为 (3.3e9 * 2) / 带宽。

## Corrected Claim

MoE 模型的显存带宽瓶颈修正：由于非激活专家参数（47.68 GB）不参与计算，实际推理时的有效带宽需求仅由激活参数（6.6 GB）和 KV Cache 读取决定，因此理论 TPOT 计算应基于激活参数而非总参数，修正后的理论 TPOT 上限为 (3.3e9 * 2) / 带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：MoE推理带宽瓶颈确实由激活参数决定，公式推导符合物理直觉
