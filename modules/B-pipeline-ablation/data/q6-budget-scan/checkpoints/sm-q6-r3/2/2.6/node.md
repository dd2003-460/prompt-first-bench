# N20: 带宽成本-按带宽包计费：C_bandwidth_package = N_package * p_package，其中N_package为购买的带宽包数量，p_p

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

带宽成本-按带宽包计费：C_bandwidth_package = N_package * p_package，其中N_package为购买的带宽包数量，p_package为每个包的价格（通常¥1000-5000/包/月，每包10-100Mbps），需根据实际带宽需求选择最优组合

## Corrected Claim

带宽成本-按带宽包计费：C_bandwidth_package = N_package * p_package，其中N_package为购买的带宽包数量，p_package为每个包的价格（通常¥1000-5000/包/月，每包10-100Mbps），需根据实际带宽需求选择最优组合

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了核心变量N_package的计算逻辑，子节点2定义了总成本公式及与其他计费模式的决策对比，两者逻辑上层层递进且无重叠，共同完整覆盖了父节点中关于变量定义、成本计算及优化选择的描述。）

## Search Query

CDN bandwidth package pricing options
