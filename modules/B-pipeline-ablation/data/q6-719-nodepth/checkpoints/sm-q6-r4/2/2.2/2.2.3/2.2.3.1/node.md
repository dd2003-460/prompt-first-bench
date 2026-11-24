# N216: 硬件故障率分解：Hardware_Failure_Rate = Base_Failure_Rate + Age_Penalty，其中 Base_Failure_

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

硬件故障率分解：Hardware_Failure_Rate = Base_Failure_Rate + Age_Penalty，其中 Base_Failure_Rate 为服务器硬件平均年故障率（MTBF 倒数），典型值 3%-5%（即 MTBF ≈ 20-33 年）；Age_Penalty 为服役年限修正系数，通常每满 3 年故障率增加 50%-100%，若服务器平均服役 2 年，则 Age_Penalty ≈ 0，总故障率 ≈ 4%/年。

## Corrected Claim

硬件故障率分解：Hardware_Failure_Rate = Base_Failure_Rate + Age_Penalty，其中 Base_Failure_Rate 为服务器硬件平均年故障率（MTBF 倒数），典型值 3%-5%（即 MTBF ≈ 20-33 年）；Age_Penalty 为服役年限修正系数，通常每满 3 年故障率增加 50%-100%，若服务器平均服役 2 年，则 Age_Penalty ≈ 0，总故障率 ≈ 4%/年。

## Evidence

父节点级核验未通过：非正交（子节点2（Age_Penalty函数）与父节点定义存在严重矛盾。父节点定义 Age_Penalty 为加性项（Base + Penalty），且数值为百分比/系数；子节点2将其定义为乘性因子（Base × (1+Penalty)），且计算出的 Age_Penalty 值（2.24）远超父节点描述的“50%-100%”范围，导致逻辑不一致。此外，子节点3属于故障后果分析，超出了“故障率分解”这一纯量化定义的范畴，虽不直接重复，但破坏了主题聚焦。）

## Search Query

server hardware annual failure rate MTBF baseline
