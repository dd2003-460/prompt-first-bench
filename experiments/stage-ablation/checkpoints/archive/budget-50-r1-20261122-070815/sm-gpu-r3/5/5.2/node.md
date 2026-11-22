# N28: 价格波动区间分析：针对候选 GPU 型号，列出过去 6 个月的价格波动范围（min-max）及当前市场供需状态（缺货/平衡/过剩），以量化采购时机风险。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

价格波动区间分析：针对候选 GPU 型号，列出过去 6 个月的价格波动范围（min-max）及当前市场供需状态（缺货/平衡/过剩），以量化采购时机风险。

## Corrected Claim

可通过公开数据集（如HardwareDealsCo/gpu-deals）和价格仪表盘（如nvidia-gpu-price-dashboard）获取候选GPU型号过去6个月的价格波动范围及市场供需状态，以量化采购时机风险。

## Evidence

[质询]该陈述是一个任务指令或分析框架，而非具体的事实陈述。参考来源仅提供了数据获取渠道（GitHub数据集/仪表盘），并未包含具体的“过去6个月价格波动范围”数值或“当前市场供需状态”的具体结论，因此无法从来源中直接提取出该事实节点所要求的具体量化数据。 | 来源[1]和[2]提供了GPU价格追踪的数据集和可视化仪表盘，间接支持了获取此类数据的可能性，但未直接提供具体的min-max数值或供需状态结论，属于间接支持。

## Search Query

GPU price history last 6 months RTX 4090 A100 H100

## Retrieval Sources

- {'url': 'https://github.com/HardwareDealsCo/gpu-deals&rut=17715d13ee1ab2ca48aed1528482d6874412496580e973d376210c47f3321a84', 'type': 'ddg', 'title': 'HardwareDealsCo/gpu-deals: Open dataset of GPU deals - GitHub'}
- {'url': 'https://github.com/kikulmj/nvidia-gpu-price-dashboard/blob/master/%E5%9F%BA%E4%BA%8ENAVIDA%E6%98%BE%E5%8D%A1%E4%BB%B7%E6%A0%BC%E7%9A%84%E6%80%BB%E7%BB%93.md&rut=95d8059e0571a0df7f2e9396d1fe9057bcd26554df215b1e36c5bc2f569161f3', 'type': 'ddg', 'title': 'nvidia-gpu-price-dashboard/基于NAVIDA显卡价格的总结.md at master · kikulmj ...'}
