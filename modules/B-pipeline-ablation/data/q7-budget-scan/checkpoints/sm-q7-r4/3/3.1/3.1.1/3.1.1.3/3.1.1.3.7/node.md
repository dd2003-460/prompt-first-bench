# N677: 托管机房 PUE 1.25 的 SLA 约束：主流 IDC 合同通常承诺 PUE ≤1.3 或 ≤1.25，若实际 PUE 超标，客户可获得电费折扣（如 5%-

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N249, N250, N251

## Claim

托管机房 PUE 1.25 的 SLA 约束：主流 IDC 合同通常承诺 PUE ≤1.3 或 ≤1.25，若实际 PUE 超标，客户可获得电费折扣（如 5%-10%）；若选择 PUE 1.2 的液冷托管，IT 功耗 1400W 下年电费 = 1.2 * 1.4 * 8760 * 0.8 ≈ ¥11,730，比自建 PUE 1.4 节省 ¥1,962/年，但托管费通常包含电力，需对比综合单价。

## Corrected Claim

托管机房 PUE 1.25 的 SLA 约束：主流 IDC 合同通常关注 PUE 指标，部分合同可能包含基于 PUE 的电费调整机制；若选择 PUE 1.2 的液冷托管，IT 功耗 1400W 下年电费约为 ¥11,730（假设电价 0.8 元/kWh），相比 PUE 1.4 方案在纯电力成本上有所节省，但需综合对比托管费与自建总成本。

## Evidence

[质询]陈述中关于“PUE超标获得5%-10%电费折扣”的具体合同条款及“¥1,962/年”的具体节省金额属于高度依赖特定市场、电价和合同细节的经验事实，缺乏通用性，且参考来源未提供这些具体数值的支持。 | 逻辑计算自洽（1.2*1.4*8760*0.8≈11730，差值约1962），但来源[1][2]仅讨论PUE/SLA概念，来源[3]讨论PUE定价理论，均未直接支持具体的折扣比例或特定电费节省金额，属经验事实缺来源支持。

## Search Query

IDC hosting PUE SLA penalty electricity cost per kW

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33423874/article/details/167596704&rut=6dd3547313f89639b9ecf0624693076bd73aaa2e111ab89d2c9be75119f7c60f', 'type': 'ddg', 'title': 'Idc入门到精通：带宽、Pue与sla避坑实用指南 - Csdn博客'}
- {'url': 'https://www.idcjifang.com/news/detail/hosting-sla-penalty-2026&rut=600e203f8906cf53ab5a2d07a8e1b4b4da8c33b61e08ba3ca52e83b7e7ce0701', 'type': 'ddg', 'title': '托管 Sla 与赔付条款怎么读：先读排除项，再读那个百分比，七步看清合同陷阱 · Idc机房网'}
- {'url': 'https://www.sciencedirect.com/science/article/pii/S0306261926009761&rut=89f19c6c13af977a6c1e23877a10d77afb447ac39f36f8d38ca34e60d8ba9192', 'type': 'ddg', 'title': 'Beyond arbitrage: How PUE-linked electricity pricing reshapes the ...'}
