# N263: 商品非标化程度 S_nonstandard 的精确计算公式：S_nonstandard = 1 - exp(-H_description / H_max)，其中

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

商品非标化程度 S_nonstandard 的精确计算公式：S_nonstandard = 1 - exp(-H_description / H_max)，其中 H_description 为商品描述文本的信息熵（比特/字符），H_max 为同类商品描述的最大信息熵。基于闲鱼数据，H_description 平均为 4.2 bits/char，H_max 为 5.0 bits/char，计算得 S_nonstandard ≈ 0.58，属于中等非标化，置信度下调至 0.55。

## Corrected Claim

商品非标化程度 S_nonstandard 可通过公式 S_nonstandard = 1 - exp(-H_description / H_max) 估算，其中 H_description 为描述文本信息熵，H_max 为同类最大信息熵。具体数值需依据实际数据集统计确定。

## Evidence

[质询]该陈述包含具体的经验数据（闲鱼数据中 H_description 平均 4.2 bits/char, H_max 5.0 bits/char）及特定的置信度调整规则（下调至 0.55），这些属于经验事实或特定模型参数，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及置信度规则）

## Search Query

information entropy calculation for product description non-standardization metric e-commerce
