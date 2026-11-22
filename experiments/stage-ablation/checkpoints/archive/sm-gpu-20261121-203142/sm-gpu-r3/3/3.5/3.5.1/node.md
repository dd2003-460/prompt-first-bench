# N74: 电力成本修正因子：实际功耗 = TDP * 负载系数(推理通常0.8-0.9)；对于2×RTX 4090，实际功耗 ≈ 900W * 0.85 = 765W，而

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

电力成本修正因子：实际功耗 = TDP * 负载系数(推理通常0.8-0.9)；对于2×RTX 4090，实际功耗 ≈ 900W * 0.85 = 765W，而非名义900W

## Corrected Claim

电力成本修正因子：实际功耗 = TDP * 负载系数(推理通常0.8-0.9)；对于2×RTX 4090，实际功耗 ≈ 900W * 0.85 = 765W，而非名义900W

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别从工作负载特征（Batch/Context）、计算阶段（Prefill/Decode）和物理环境（散热/降频）三个正交维度解释了负载系数的变化因素，逻辑清晰且无重叠，覆盖了影响实际功耗的主要变量。）
