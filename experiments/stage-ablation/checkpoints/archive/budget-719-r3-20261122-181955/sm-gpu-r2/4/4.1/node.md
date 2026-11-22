# N22: 硬件一次性采购成本 (C_hw)：基于目标模型显存需求（Qwen3-27B 在 32K 上下文下 KV Cache 占用 + 权重占用），计算各候选卡（如 RT

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

硬件一次性采购成本 (C_hw)：基于目标模型显存需求（Qwen3-27B 在 32K 上下文下 KV Cache 占用 + 权重占用），计算各候选卡（如 RTX 4090, A100, H100, L40S）的最小满足显存数 N，C_hw = N * P_unit，其中 P_unit 为 2024 年 Q3 市场均价 [待核验]。

## Corrected Claim

硬件一次性采购成本 (C_hw) 的计算逻辑为 C_hw = N * P_unit，其中 N 为基于 Qwen3-27B 在 32K 上下文下显存需求（KV Cache + 权重）确定的最小满足显存卡数，P_unit 为对应时间点的市场均价。具体数值需依据实际采购时的市场价格及模型量化版本确定。

## Evidence

[质询]陈述中引用的具体时间点（2024年Q3）与参考来源[1]中提到的时间（2026年6月）存在显著偏差，且来源[1]针对的是Qwen3.6-27B而非Qwen3-27B，来源[2]针对的是Qwen3-235B-A22B，均无法直接支持该特定时间点下的具体硬件单价及最小满足显存数N的精确计算。 | 逻辑上C_hw = N * P_unit的公式自洽，但参考来源[1]和[2]分别涉及不同时间点和不同模型规模（235B vs 27B），无法直接验证2024年Q3针对Qwen3-27B的具体硬件采购成本数值，属于经验事实且缺乏直接来源支持。

## Search Query

RTX 4090 A100 H100 L40S current market price 2024 Q3

## Retrieval Sources

- {'url': 'https://omnitools.ai/article/qwen3-6-27b-2&rut=d9fe4d0a0cd8cff884c55e3c42777b4a257befce8d8cf1b1a28a26afff9f2b81', 'type': 'ddg', 'title': '本地部署 Qwen3.6-27B 需要多少钱？硬件采购、电费与运维成本核算指南 | 工具研究所'}
- {'url': 'https://blog.csdn.net/gitblog_01092/article/details/151598493&rut=b25852a00cf1898819830ecd957056479dc933f4f7b2185a92a0ddcc8f063f88', 'type': 'ddg', 'title': 'Qwen3-235B-A22B硬件需求清单：从消费级GPU到数据中心配置方案-CSDN博客'}
