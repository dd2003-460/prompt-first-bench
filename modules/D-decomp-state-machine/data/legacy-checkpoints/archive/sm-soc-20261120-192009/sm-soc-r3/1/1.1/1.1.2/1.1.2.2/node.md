# N125: 锚定偏差系数 β_anchor 的基准值：行为经济学实验表明，在缺乏明确市场参照时，卖家的初始定价锚定偏差 β_anchor 中位数约为 0.20；在二手交易平

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N34

## Claim

锚定偏差系数 β_anchor 的基准值：行为经济学实验表明，在缺乏明确市场参照时，卖家的初始定价锚定偏差 β_anchor 中位数约为 0.20；在二手交易平台中，由于存在历史成交数据作为参照，该系数应下调，预计基准值为 0.12，需通过 A/B 测试对比有无历史成交展示组的挂价差异来验证。

## Corrected Claim

行为经济学实验表明，在缺乏明确市场参照时，卖家的初始定价锚定偏差 β_anchor 存在显著影响；在二手交易平台中，由于存在历史成交数据作为参照，该系数预计会下调，具体数值需通过 A/B 测试对比有无历史成交展示组的挂价差异来验证。

## Evidence

[质询]具体数值（0.20和0.12）缺乏来源支持，属于经验事实，且来源仅定义概念未提供量化数据 | 来源[1][2]仅定义锚定效应概念，未提供具体系数数值，无法直接支持0.20/0.12的基准值，但逻辑上存在参照会降低偏差是合理的

## Search Query

anchoring bias magnitude second hand market price setting experiment

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E9%94%9A%E5%AE%9A%E5%81%8F%E8%A7%81/64842200&rut=519529248641f0f132e6ba6fc3f4b32b4c68072138966b0c6551932e9edd94ee', 'type': 'ddg', 'title': '锚定偏见 - 百度百科'}
- {'url': 'https://baike.baidu.com/item/%E9%94%9A%E5%AE%9A%E6%95%88%E5%BA%94/5726509&rut=7b422d64cf68742354780c07d9abb5e7b5e93a803ff7c11bfdb95602c7c53a73', 'type': 'ddg', 'title': '锚定效应_百度百科'}
