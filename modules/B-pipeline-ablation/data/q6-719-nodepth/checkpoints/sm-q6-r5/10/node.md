# N32: TCO归一化公式：定义每千请求总拥有成本 C_tco_1k = (C_capex_annual / 12 + C_opex_monthly + C_penalt

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

TCO归一化公式：定义每千请求总拥有成本 C_tco_1k = (C_capex_annual / 12 + C_opex_monthly + C_penalty_monthly) / (R_daily / 1000)；其中 C_capex_annual 为自建硬件折旧（按5年直线折旧），C_opex_monthly 为带宽+人力月度支出；该公式用于在三种策略间进行同口径成本对比。

## Corrected Claim

TCO归一化公式（特定模型定义）：C_tco_1k = (C_capex_annual / 12 + C_opex_monthly + C_penalty_monthly) / (R_daily / 1000)；该公式用于在特定假设下（如月均30天）进行同口径成本对比，非通用TCO标准公式。

## Evidence

[质询]该公式为特定场景下的自定义归一化指标，并非通用的TCO标准定义；参考来源仅提供了TCO的通用概念，未包含此具体公式，且公式中分母使用日均请求量（R_daily）而非月均请求量，导致量纲上隐含了时间单位转换（月成本/日均流量），虽在特定对比逻辑下可能成立，但缺乏通用性支持，属于经验性/特定模型设定。 | 来源[1]仅定义TCO为全生命周期成本概念，未提供具体计算公式，无法直接支持该特定归一化公式；该公式逻辑自洽（将月度总成本除以日均请求量以得到每千请求成本，隐含了30天/月的假设或特定业务口径），但作为经验事实/特定模型参数，缺乏来源直接支持，故降级。

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%80%BB%E4%BD%93%E6%8B%A5%E6%9C%89%E6%88%90%E6%9C%AC/161034&rut=ce38dd68e4e418ee07e95f32e371a2bb568531840f1befc875e7397ae9af17b5', 'type': 'ddg', 'title': '总体拥有成本_百度百科'}
