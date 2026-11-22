# N92: 修复成本 $C_{repair}$ 的边际递减函数：$C_{repair}$ 并非线性 $5\% P_{market}$，而是与缺陷程度 $q_{defect}

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N33

## Claim

修复成本 $C_{repair}$ 的边际递减函数：$C_{repair}$ 并非线性 $5\% P_{market}$，而是与缺陷程度 $q_{defect}$ 呈凸函数关系 $C_{repair} = C_0 + C_{marginal} \times (1 - q)^\gamma$，其中 $\gamma > 1$ 表示严重缺陷修复成本激增。量化示例：对于 $P_{market}=5000$ 元的商品，轻微划痕修复 $C_{repair} \approx 200$ 元（4%），而主板故障修复 $C_{repair} \approx 1500$ 元（30%）。在 $L_{lemon}$ 计算中，若忽略此非线性，会低估高缺陷商品的潜在损失，导致对买家风险厌恶系数 $\alpha$ 的高估。

## Corrected Claim

修复成本 $C_{repair}$ 通常与缺陷程度呈非线性递增关系（如凸函数），严重缺陷的修复成本占比显著高于轻微缺陷。在计算柠檬市场损失时，忽略此非线性可能导致对买家风险的高估或低估（具体取决于模型设定），需根据具体商品类别的经验数据确定具体函数形式。

## Evidence

[质询]该陈述包含具体的经验性数值（如轻微划痕修复200元、主板故障1500元）及特定的数学函数形式（凸函数关系），这些属于经验事实或特定模型假设，无法从第一性原理严格推导，且参考来源仅提供了“边际损害递增”的定性概念，未提供具体的成本函数或量化数据支持。 | 逻辑自洽（凸函数符合严重缺陷成本激增的直觉），但参考来源[1]仅定性支持“边际损害/成本递增”的概念，未直接支持具体的函数形式或量化数值，属于间接支持。

## Search Query

repair cost function convexity used electronics defect severity marginal cost

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/107509591&rut=a610b9927888f6dbb0e63d77d300db3e2a3c3fb72bc6ab431d07aaaa6a186726', 'type': 'ddg', 'title': '一个容易被忽视的重要概念：边际损害递增 - 知乎'}
