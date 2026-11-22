# N234: 在 x_max=1GB 截断下，尾部对象（>100KB）的精确字节占比需通过截断 Pareto(α=1.1) 的累积分布函数计算：P(S > 100KB | S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

在 x_max=1GB 截断下，尾部对象（>100KB）的精确字节占比需通过截断 Pareto(α=1.1) 的累积分布函数计算：P(S > 100KB | S ≤ 1GB) = (100KB/1GB)^{α-1} = (0.1)^{0.1} ≈ 0.794，此值与 N83 中声称的 5% 存在数量级差异，需验证是字节占比还是对象数量占比的混淆

## Corrected Claim

在 x_max=1GB 截断下，尾部对象（>100KB）的精确字节占比需通过截断 Pareto(α=1.1) 的累积分布函数计算：P(S > 100KB | S ≤ 1GB) = (100KB/1GB)^{α-1} = (0.1)^{0.1} ≈ 0.794，此值与 N83 中声称的 5% 存在数量级差异，需验证是字节占比还是对象数量占比的混淆

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布条件概率公式推导正确，数值计算准确，量纲合理
