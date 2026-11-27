# N55: 信息不对称强度的调节作用：ε_buyer 的非线性程度受信息不对称指标 I_asym 调节，I_asym = 1 - (P_median / P_ask)；当 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

信息不对称强度的调节作用：ε_buyer 的非线性程度受信息不对称指标 I_asym 调节，I_asym = 1 - (P_median / P_ask)；当 I_asym > 0.2（即挂价高于中位数 20% 以上）时，ε_buyer 的负向峰值 ε_1 增大至 1.5，意味着买家怀疑更强烈；当 I_asym < 0.1 时，ε_1 减小至 0.6，市场更接近完全信息状态。

## Corrected Claim

信息不对称强度可能调节 ε_buyer 的非线性程度，通常信息不对称程度越高（如挂价显著高于中位数），买家怀疑越强，导致弹性峰值增大；但具体的阈值（0.1/0.2）及参数值（0.6/1.5）需依据特定模型设定或实证数据确定，并非通用常数。

## Evidence

[质询]该陈述中的具体数值阈值（I_asym > 0.2 对应 ε_1=1.5，I_asym < 0.1 对应 ε_1=0.6）及公式定义（I_asym = 1 - P_median/P_ask）属于特定模型或经验设定，缺乏通用理论支持，且参考来源仅讨论上市公司信息不对称的通用度量方法，未涉及此特定非线性调节机制及具体参数值，存在将特定模型参数误述为普遍规律的风险。 | 逻辑上自洽（信息不对称程度越高，买家怀疑越强，弹性峰值越大符合直觉），但参考来源[1]仅介绍信息不对称的通用衡量指标（如KV指数、盈余管理等），与该节点中特定的价格比率公式及弹性参数数值无直接关联，属于经验事实且缺乏来源直接支持。

## Search Query

information asymmetry price elasticity moderation effect marketplace

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/715321375&rut=66e4d823512e436ac5a87efa47e0f4b9582bfac72ef9dd0a28feb5fc5ba87f5d', 'type': 'ddg', 'title': '上市公司信息不对称指标测算 - 知乎'}
