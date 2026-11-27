# N13: 各候选硬件的当前市场均价（USD）及二手/促销价格区间：需建立价格-性能比（$/TFLOPS, $/GB）的量化基准，用于TCO计算。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

各候选硬件的当前市场均价（USD）及二手/促销价格区间：需建立价格-性能比（$/TFLOPS, $/GB）的量化基准，用于TCO计算。

## Corrected Claim

需利用硬件价格追踪器（如HardwareRK、Kensoul等）获取各候选硬件的当前市场均价及二手/促销价格区间，并计算价格-性能比（$/TFLOPS, $/GB）以用于TCO计算。

## Evidence

[质询]该陈述是一个任务目标或方法论描述，而非具体的经验事实数据。它声称需要建立价格-性能比基准，但未提供具体的数值或已验证的基准结果。作为事实节点，它缺乏具体的可验证内容（如具体价格、具体比率），且参考来源仅提供了数据获取渠道，并未直接提供该陈述所指的“已建立的量化基准”或具体市场均价数据。 | 逻辑自洽，但属于经验事实/任务描述，参考来源[1][2][3]仅提供了获取硬件价格和性能数据的工具/网站，未直接提供具体的市场均价数值或已计算好的$/TFLOPS基准，无法直接支持该陈述中的具体量化结果，故降级。

## Search Query

GPU price list 2024 RTX 4090 A100 H100 RX 7900 XTX used market price USD

## Retrieval Sources

- {'url': 'https://hardwarerk.com/zh-CN/price-tracker&rut=38ef9607b952c28c598e42608d50bae00d3adaef46d5b9b67528bb6f4840cd29', 'type': 'ddg', 'title': '硬件价格追踪器 - Cpu 与 Gpu 历史价格走势'}
- {'url': 'https://hardwarerk.com/zh-CN&rut=bb4549c8dc211420b9f379e2575a214b919e2a69b877f51382ddcd4223a6a45b', 'type': 'ddg', 'title': 'HardwareRK — CPU 与 GPU 性能天梯图、性价比排名、历史价格走势追踪'}
- {'url': 'https://kensoul.fun/hardware-price/&rut=5dda35bf2da28dd5b5f982a207e2d74421e34adfc5026178a6b053a8ca69f920', 'type': 'ddg', 'title': '硬件价格风向标：显卡 / Cpu / 内存 / Ssd 国行与海外价格采样 | Kensoul'}
