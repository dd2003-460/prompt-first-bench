# N64: 库存结构变化量化：定义热门商品占比指数 H = (Q_hot / Q_total)，假设当 H 每增加 10% 时，基础成交周期 T_base 平均缩短 5% 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

库存结构变化量化：定义热门商品占比指数 H = (Q_hot / Q_total)，假设当 H 每增加 10% 时，基础成交周期 T_base 平均缩短 5% (T_base' = T_base * (1 - 0.05*H_shift))，需对比高挂价组与正常定价组的 H 分布差异以排除混淆。

## Corrected Claim

库存结构变化量化：定义热门商品占比指数 H = (Q_hot / Q_total)。在分析中，可假设 H 与基础成交周期 T_base 存在负相关关系（例如 T_base' = T_base * (1 - k*H_shift)），需通过对比高挂价组与正常定价组的 H 分布差异来排除混淆，其中系数 k 需根据具体数据回归确定，而非固定为 0.05。

## Evidence

父节点级核验未通过：不完备（子节点分别处理了变量定义（Q_hot）和模型形式（非线性关系），两者正交且不冗余。但父节点明确提出了“需对比高挂价组与正常定价组的 H 分布差异以排除混淆”这一关键的实证分析步骤，而现有两个子节点均未涵盖此对比验证或混淆变量控制的内容，导致分解不完备。）

## Search Query

second hand market inventory mix impact on time to sale

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2032144468393116859&rut=7eaa639baef16acc689594cf2927f8c5dd23c551edbfa692d525041c5ac3ee2b', 'type': 'ddg', 'title': '库存分析必会的12个模型，一键套用（附模板下载） - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1953846361628837753&rut=b20f9d0f4c048415673cbd47744b5990720bbea0c720e2281e5f9bc21218c73e', 'type': 'ddg', 'title': '库存分析方法大全：从库存切割、结构、量化出发的13个分析方法'}
