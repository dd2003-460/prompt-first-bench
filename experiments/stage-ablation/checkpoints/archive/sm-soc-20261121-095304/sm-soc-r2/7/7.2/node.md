# N64: 库存结构变化量化：定义热门商品占比指数 H = (Q_hot / Q_total)，假设当 H 每增加 10% 时，基础成交周期 T_base 平均缩短 5% 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

库存结构变化量化：定义热门商品占比指数 H = (Q_hot / Q_total)，假设当 H 每增加 10% 时，基础成交周期 T_base 平均缩短 5% (T_base' = T_base * (1 - 0.05*H_shift))，需对比高挂价组与正常定价组的 H 分布差异以排除混淆。

## Corrected Claim

库存结构变化量化：定义热门商品占比指数 H = (Q_hot / Q_total)。在分析中，可假设 H 与基础成交周期 T_base 存在负相关关系（例如 T_base' = T_base * (1 - k*H_shift)），需通过对比高挂价组与正常定价组的 H 分布差异来排除混淆，其中系数 k 需根据具体数据回归确定，而非固定为 0.05。

## Evidence

[质询]该陈述中的具体量化关系（H每增加10%，T_base缩短5%）属于经验性假设或特定场景下的回归系数，并非通用的物理定律或数学公理，无法从第一性原理严格推导得出，且参考来源未提供此具体数值支持。 | 逻辑自洽（定义清晰，公式线性关系合理），但属于经验事实/假设参数，参考来源[1][2]仅涉及库存分析方法论，未提供该具体量化系数，依据经验事实排除条款降级。

## Search Query

second hand market inventory mix impact on time to sale

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2032144468393116859&rut=7eaa639baef16acc689594cf2927f8c5dd23c551edbfa692d525041c5ac3ee2b', 'type': 'ddg', 'title': '库存分析必会的12个模型，一键套用（附模板下载） - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1953846361628837753&rut=b20f9d0f4c048415673cbd47744b5990720bbea0c720e2281e5f9bc21218c73e', 'type': 'ddg', 'title': '库存分析方法大全：从库存切割、结构、量化出发的13个分析方法'}
