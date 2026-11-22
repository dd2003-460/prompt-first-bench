# N91: 低质量商品真实价值 $V_{low}$ 的分布特征：在二手市场（如手机/数码）中，低质量（$q < q^*$，如电池老化>30%或屏幕划痕）商品的残值 $V_{

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N33

## Claim

低质量商品真实价值 $V_{low}$ 的分布特征：在二手市场（如手机/数码）中，低质量（$q < q^*$，如电池老化>30%或屏幕划痕）商品的残值 $V_{low}$ 并非固定为 $0.6 P_{market}$，而是服从右偏分布，其条件期望 $E[V_{low} | q]$ 随缺陷类型非线性变化。需量化：若 $P_{market}=5000$ 元，严重缺陷（$q < 0.3 q^*$）的 $V_{low}$ 均值约为 $2500-3000$ 元（即 $0.5-0.6 P_{market}$），而轻微缺陷（$q \in [0.5, 1.0] q^*$）的 $V_{low}$ 均值约为 $4000-4500$ 元（即 $0.8-0.9 P_{market}$）。此差异导致 $L_{lemon}$ 在严重缺陷场景下高达 $2000-2500$ 元，而在轻微缺陷场景下仅 $500-1000$ 元，直接决定买家风险溢价的下限。

## Corrected Claim

在二手市场中，低质量商品的残值并非固定值，而是随缺陷程度非线性下降。严重缺陷商品的残值显著低于轻微缺陷商品，导致买家面临的风险溢价在严重缺陷场景下远高于轻微缺陷场景。

## Evidence

[质询]该陈述包含具体的二手市场残值量化数据（如严重缺陷均值2500-3000元，轻微缺陷4000-4500元），属于经验事实。参考来源仅涵盖柠檬市场的理论定义和机制，未提供具体的二手商品残值分布数据或实证统计，无法验证这些具体数值是否准确。 | 逻辑上，缺陷程度与残值负相关符合经济直觉，且来源[1][2][3]确认了柠檬市场理论背景，但均无具体数值支持，属于经验事实缺来源支持。

## Search Query

used electronics market residual value distribution by defect severity empirical data

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%9F%A0%E6%AA%AC%E5%B8%82%E5%9C%BA/2174659&rut=711d314abef20ea6ee88bdcfa9b70e8ba98b63daafc7df1b58e5dbecb3c2e258', 'type': 'ddg', 'title': '柠檬市场_百度百科'}
- {'url': 'https://baike.baidu.com/item/%E9%98%BF%E5%85%8B%E7%BD%97%E5%A4%AB%E6%A8%A1%E5%9E%8B/5599017&rut=59bfb546c61b1e55e45d8942720aa0d7426e999400c86bd805867ade14bfb5e8', 'type': 'ddg', 'title': '阿克罗夫模型_百度百科'}
- {'url': 'https://zh.wikipedia.org/zh-hans/%E6%9F%A0%E6%AA%AC%E5%B8%82%E5%9C%BA&rut=ee8b216643072ab17242a9983584ff3f778c076d1387fd9994e5d47ef4fa1af5', 'type': 'ddg', 'title': '柠檬市场 - 维基百科，自由的百科全书 - zh.wikipedia.org'}
