# N136: 索引更新频率增量 $\Delta F_{update}$ 与阈值降低幅度 $\Delta \theta$ 的关系为 $\Delta F_{update} = F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

索引更新频率增量 $\Delta F_{update}$ 与阈值降低幅度 $\Delta \theta$ 的关系为 $\Delta F_{update} = F_{base} \times (\theta_{old}/\theta_{new} - 1)$。当 $\theta$ 从 5% 降至 2% 时，$\Delta F_{update} = F_{base} \times 1.5$，即更新频率增加 150%。

## Corrected Claim

索引更新频率增量 $\Delta F_{update}$ 与阈值降低幅度 $\Delta \theta$ 的关系为 $\Delta F_{update} = F_{base} \times (\theta_{old}/\theta_{new} - 1)$。当 $\theta$ 从 5% 降至 2% 时，$\Delta F_{update} = F_{base} \times 1.5$，即更新频率增加 150%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算无误（5%/2% - 1 = 1.5）
