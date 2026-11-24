# N120: P99 延迟合成模型修正：由于各分量独立，总延迟分布近似为各分量分布的卷积。$P99(T_{total}) \approx \sum P99(T_{comp,i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

P99 延迟合成模型修正：由于各分量独立，总延迟分布近似为各分量分布的卷积。$P99(T_{total}) \approx \sum P99(T_{comp,i})$ 仅在分量完全相关时成立；实际需考虑尾部相关性，通常 $P99(T_{total}) < \sum P99(T_{comp,i})$，但需通过蒙特卡洛模拟或历史数据拟合确定修正系数 $\alpha \in [0.8, 1.0]$。

## Corrected Claim

P99 延迟合成模型修正：由于各分量独立，总延迟分布近似为各分量分布的卷积。$P99(T_{total}) \approx \sum P99(T_{comp,i})$ 仅在分量完全相关时成立；实际需考虑尾部相关性，通常 $P99(T_{total}) < \sum P99(T_{comp,i})$，但需通过蒙特卡洛模拟或历史数据拟合确定修正系数 $\alpha \in [0.8, 1.0]$。

## Evidence

先验知识/题面给定，逻辑校验通过：独立随机变量之和的尾部延迟确实小于各分量尾部延迟之和（除非完全正相关），且蒙特卡洛模拟是确定修正系数的标准工程方法，量级与逻辑自洽。

## Search Query

P99 latency aggregation convolution independent components tail correlation
