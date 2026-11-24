# N58: NVMe SSD 阵列的稳态工作负载混合比（Read/Write/Idle 比例），用于加权计算平均功耗，温数据每日扫描 1-2 次且 80% 冷数据极少访问，

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

NVMe SSD 阵列的稳态工作负载混合比（Read/Write/Idle 比例），用于加权计算平均功耗，温数据每日扫描 1-2 次且 80% 冷数据极少访问，假设工作负载为 10% Read, 10% Write, 80% Idle。

## Corrected Claim

NVMe SSD 阵列的稳态工作负载混合比（Read/Write/Idle 比例），用于加权计算平均功耗，温数据每日扫描 1-2 次且 80% 冷数据极少访问，假设工作负载为 10% Read, 10% Write, 80% Idle。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在逻辑包含关系而非正交；父节点明确给出的假设参数（10% Read, 10% Write, 80% Idle）在子节点中被完全忽略，导致计算结果与父节点设定矛盾；两个子节点本质上是在推导同一个“最终有效工作负载分布”的不同步骤，具有高度冗余。）
