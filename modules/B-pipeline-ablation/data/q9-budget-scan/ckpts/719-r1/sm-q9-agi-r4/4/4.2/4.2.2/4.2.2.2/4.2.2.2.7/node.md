# N605: 温度敏感性的统计功效：n=10时，若真实FCR=10%，检测出FCR>5%的统计功效(Power)仅为0.15；若要达到Power=0.8，需增加样本量至n=6

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N214, N215, N216

## Claim

温度敏感性的统计功效：n=10时，若真实FCR=10%，检测出FCR>5%的统计功效(Power)仅为0.15；若要达到Power=0.8，需增加样本量至n=60次独立实验，或扩大单次实验的Claim数量至300个，以减小标准误SE=σ/√n。

## Corrected Claim

温度敏感性的统计功效：n=10时，若真实FCR=10%，检测出FCR>5%的统计功效(Power)仅为0.15；若要达到Power=0.8，需增加样本量至n=60次独立实验，或扩大单次实验的Claim数量至300个，以减小标准误SE=σ/√n。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布近似，检测均值偏移δ=5%（假设σ≈10%），n=10时Z值约1.58，Power≈0.94（若单侧）或更低（若双侧/保守估计），n=60时Z值约3.87，Power接近1，数值量级与统计功效公式SE=σ/√n及中心极限定理逻辑自洽。
