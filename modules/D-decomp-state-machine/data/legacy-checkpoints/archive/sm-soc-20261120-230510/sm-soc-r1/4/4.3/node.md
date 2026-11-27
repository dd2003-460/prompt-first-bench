# N18: 干预措施B（搜索排序惩罚）：修改搜索排序算法，将挂价高于 P_median * 1.15 的商品排序权重 w 从 1.0 降至 0.5，量化影响：假设搜索流量 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

干预措施B（搜索排序惩罚）：修改搜索排序算法，将挂价高于 P_median * 1.15 的商品排序权重 w 从 1.0 降至 0.5，量化影响：假设搜索流量 Q 与排序权重 w 成线性关系，高挂价商品曝光量减少 50%，成交周期 T 从 T0 延长至 T0 * (1 + λ * 0.5)，其中 λ 为流量敏感度系数，典型值 λ ∈ [0.3, 0.8] [待核验]。

## Corrected Claim

干预措施B（搜索排序惩罚）：修改搜索排序算法，将挂价高于 P_median * 1.15 的商品排序权重 w 从 1.0 降至 0.5。假设搜索流量 Q 与排序权重 w 成线性关系，高挂价商品曝光量减少 50%，成交周期 T 预计延长，具体延长幅度取决于流量敏感度系数 λ（需通过 A/B 测试或历史数据校准，典型经验值可能在 0.3-0.8 之间，但需实证验证）。

## Evidence

[质询]该陈述包含具体的经验参数（如 λ 的典型值范围 [0.3, 0.8]）和特定的业务假设（流量与权重线性关系），这些属于经验事实，无法从第一性原理推导，且参考来源中未提供相关数据支持。 | 逻辑自洽（权重减半导致曝光减半，进而影响成交周期符合直觉），但参考来源 [1][2] 仅讨论搜索排序算法原理，未涉及具体业务量化参数或 λ 系数，属于经验事实缺来源支持。

## Search Query

search ranking penalty high priced items exposure reduction conversion rate

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2501_91930600/article/details/148050976&rut=b03b4fbcf07b300c6d6c0c67bca8d8021277808dd959ce27ef47a7c96a19f3f6', 'type': 'ddg', 'title': '搜索领域重排序的策略调整与优化 - Csdn博客'}
- {'url': 'https://blog.csdn.net/lov1993/article/details/140925175&rut=8ba723bf1c674d08bef106c073f6b0d54c12261433f2772b1a1aae3ab9751e3e', 'type': 'ddg', 'title': '【搜索策略-驯化】一文彻底讲明白搜索系统中的策略算法：query解析、召回、排序_搜索召回排序-CSDN博客'}
- {'url': 'https://cloud.tencent.com/developer/article/2205782&rut=0f452b8041f600f00272d54b51e94e2e5df5e4a2535d1226f2c3c2f56f465f56', 'type': 'ddg', 'title': '论文拾萃 | PISTS算法求解obnoxious p-median problem (附Python代码）'}
