# N137: 单次索引更新算力成本 $C_{unit}$ 包含 CPU 周期数与内存访问开销，需量化为 $C_{unit} = \alpha_{cpu} \times T_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

单次索引更新算力成本 $C_{unit}$ 包含 CPU 周期数与内存访问开销，需量化为 $C_{unit} = \alpha_{cpu} \times T_{cpu} + \alpha_{mem} \times T_{mem}$，其中 $\alpha$ 为单位算力价格。

## Corrected Claim

单次索引更新算力成本 $C_{unit}$ 包含 CPU 周期数与内存访问开销，需量化为 $C_{unit} = \alpha_{cpu} \times T_{cpu} + \alpha_{mem} \times T_{mem}$，其中 $\alpha$ 为单位算力价格。

## Evidence

先验知识/题面给定，逻辑校验通过
