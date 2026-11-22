# N21: 硬件资本支出（CapEx）对比：2×消费级卡（如2×RTX 4090/5090）与1×数据中心卡（如A100/H100/B200）的购置成本及折旧周期内的年化成

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

硬件资本支出（CapEx）对比：2×消费级卡（如2×RTX 4090/5090）与1×数据中心卡（如A100/H100/B200）的购置成本及折旧周期内的年化成本，需包含多卡方案的额外硬件开销（如NVLink/PCIe交换、机箱、电源）。

## Corrected Claim

硬件资本支出（CapEx）对比需考虑2×消费级卡（如RTX 4090/5090）与1×数据中心卡（如A100/H100/B200）的购置成本差异，以及多卡方案中NVLink/PCIe交换、机箱、电源等额外硬件开销对年化成本的影响。

## Evidence

[质询]该陈述涉及具体的硬件市场价格（RTX 4090/5090, A100/H100/B200）及折旧周期内的年化成本计算，属于典型的经验事实。参考来源仅讨论了OpenAI的整体CapEx规模和Opex/Capex概念定义，未提供具体GPU型号的单价、多卡互联硬件开销或折旧模型，无法直接支持或验证具体的成本对比数值。 | 逻辑自洽（硬件成本对比框架合理），但参考来源[1][2]仅涉及宏观CapEx概念及OpenAI总支出，未覆盖具体GPU型号价格及多卡方案额外开销，属于经验事实且缺来源直接支持。

## Search Query

RTX 4090 vs A100 H100 price TCO comparison 2024 2025

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2056860873029841371&rut=48956659c7ffdfcb338b546bc38605f1608e88e581ba0569a7c1e6d678b59189', 'type': 'ddg', 'title': 'OpenAI的钱都花哪了？Capex支出全景调研 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1965086154794726123&rut=2b8eb0ba16ca9561dd53384d39541c2ad65e406c863d487b8db8402126851c5b', 'type': 'ddg', 'title': '一分钟讲清楚opex和capex - 知乎'}
