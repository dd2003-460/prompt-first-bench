# N374: 年度机房+电力总成本中，租金部分需区分固定租金和可变部分（如超额电力费、空调费等），部分机房合同包含基本电力额度，超出部分按¥1.5-2.5/kWh计费，需量化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

年度机房+电力总成本中，租金部分需区分固定租金和可变部分（如超额电力费、空调费等），部分机房合同包含基本电力额度，超出部分按¥1.5-2.5/kWh计费，需量化超额比例

## Corrected Claim

年度机房+电力总成本中，租金部分需区分固定租金和可变部分（如超额电力费、空调费等），部分机房合同包含基本电力额度，超出部分按市场电价计费（具体单价需根据当地电网政策及合同约定确定，通常在¥1.0-3.0/kWh区间波动），需量化超额比例

## Evidence

[质询]具体数值区间（¥1.5-2.5/kWh）属于经验事实，不同地区、不同时期及不同合同条款下差异巨大，参考来源仅提供了成本结构框架，未提供该具体价格区间的支持，存在以偏概全或数据过时的风险。 | 来源[1][2][3]均支持IDC成本需区分固定与可变部分（如电费、租金）的逻辑框架，但均未直接提供¥1.5-2.5/kWh这一具体超额电力计费标准，属于经验事实缺来源直接支持。

## Search Query

China colocation data center overage electricity charge per kWh 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32050773/article/details/166540360&rut=b32b7f0b9661ab68b0a8f33848c56d3241a73b987c761f277a0729310661c3ff', 'type': 'ddg', 'title': 'Idc机房建设与运行成本分析：从单柜投资到tco的算账方法-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_29061509/article/details/167058621&rut=017427b91870f0c58a06f40eaf8448ee0c82c95f29f138254e81ebe660f980d3', 'type': 'ddg', 'title': 'Idc机房建设投资与运行成本分析报告：Capex/Opex模型与避坑指南-csdn博客'}
- {'url': 'https://javaguidepro.com/blog/idc-shu-ju-zhong-xin-de-fei-yong-jie-gou-ru-he/&rut=e2d11f0401a7633f5ab06f74f3723db0f9eda27a2bad7fd954e51a108ceb4c6b', 'type': 'ddg', 'title': 'IDC数据中心的费用结构解析：从基础设施到运营成本的全面梳理 — JavaGuidePro.com'}
