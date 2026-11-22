# N23: 大小-热度负相关（ρ=-0.3）的联合分布建模需使用Copula函数，具体为Gaussian Copula或Clayton Copula，以构建联合累积分布函数

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

大小-热度负相关（ρ=-0.3）的联合分布建模需使用Copula函数，具体为Gaussian Copula或Clayton Copula，以构建联合累积分布函数 F(S, H) = C(F_S(s), F_H(h); ρ)，而非简单的线性修正。

## Corrected Claim

大小-热度负相关（ρ=-0.3）的联合分布建模需使用Copula函数，具体为Gaussian Copula或Clayton Copula，以构建联合累积分布函数 F(S, H) = C(F_S(s), F_H(h); ρ)，而非简单的线性修正。

## Evidence

父节点级核验未通过：不完备（子节点在数学形式上正交且无冗余，但存在严重的数学事实错误（Clayton Copula 无法表示负相关），且遗漏了父节点中关于'联合累积分布函数构建'和'数值求解边缘概率'的方法论描述。）

## Search Query

Gaussian vs Clayton Copula negative correlation size heat modeling

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/682109200&rut=727673baaf45426045876ddda1a27ee916e78887698b2c870f3209847a96b457', 'type': 'ddg', 'title': '这可能是多变量联合分布函数Copula的最全的计算公式分享了'}
- {'url': 'https://zhuanlan.zhihu.com/p/138800469&rut=00eca177cc2c121a12d6b8a207c8791f6153fedfd64f708d9f005791ad1316cf', 'type': 'ddg', 'title': 'Copula系列（一）-什么是Copula函数 - 知乎'}
