# N113: 单卡GPU硬件年均故障率λ_single的量化估算：基于MTBF=50,000小时，λ_single = 1/50000 = 2e-5 failures/hou

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N34, N35

## Claim

单卡GPU硬件年均故障率λ_single的量化估算：基于MTBF=50,000小时，λ_single = 1/50000 = 2e-5 failures/hour，对应年均故障次数 = λ_single * 8760 = 0.1752次/年

## Corrected Claim

单卡GPU硬件年均故障率λ_single的量化估算：基于MTBF=50,000小时，λ_single = 1/50000 = 2e-5 failures/hour，对应年均故障次数 = λ_single * 8760 = 0.1752次/年

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一数学模型（λ=1/MTBF, Cost=λ*RepairCost）在不同硬件层级参数下的具体实例，存在严重的结构性冗余；且父节点仅定义了基准值，子节点却引入了父节点未提及的维护成本模型参数（如维修时长、单次故障损失），导致分解超出了父节点的语义范围，且未覆盖非硬件层面的故障因素（如驱动/软件故障）。）
