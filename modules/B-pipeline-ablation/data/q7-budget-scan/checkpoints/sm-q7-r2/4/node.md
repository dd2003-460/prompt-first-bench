# N4: 数据恢复与RTO代价：覆盖故障场景下的恢复时间目标（RTO）、恢复过程中的业务中断机会成本、以及不同方案在数据冗余与恢复速度上的差异

- **status**: pending
- **level**: L1
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

数据恢复与RTO代价：覆盖故障场景下的恢复时间目标（RTO）、恢复过程中的业务中断机会成本、以及不同方案在数据冗余与恢复速度上的差异

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2、3、4分别针对NVMe、HDD/SSD、云存储计算T_restore，属于同一变量（T_restore）在不同硬件/场景下的具体实例化，存在结构性冗余；此外，节点6（AFR）和节点7（期望代价）是独立的计算维度，但节点2-4的内容本质上是节点1中T_restore项的参数化展开，未严格正交。）
