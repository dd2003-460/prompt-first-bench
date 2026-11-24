# N13: HDD+SSD分层硬件折旧：HDD部分（400TB冷数据）单价约¥500-800/TB，SSD部分（100TB温数据）单价约¥3000-5000/TB，年折旧 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

HDD+SSD分层硬件折旧：HDD部分（400TB冷数据）单价约¥500-800/TB，SSD部分（100TB温数据）单价约¥3000-5000/TB，年折旧 = (HDD成本 + SSD成本) / 折旧年限

## Corrected Claim

HDD+SSD分层硬件折旧：HDD部分（400TB冷数据）单价约¥500-800/TB，SSD部分（100TB温数据）单价约¥3000-5000/TB，年折旧 = (HDD成本 + SSD成本) / 折旧年限

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了HDD物理容量、SSD物理容量以及最终的折旧成本计算，逻辑上呈递进关系（输入->处理->输出），互不重叠且无矛盾。父节点中的单价和折旧年限参数已在子节点3中具体化应用，覆盖了父节点定义的所有关键计算要素。）

## Search Query

HDD price per TB 2024
