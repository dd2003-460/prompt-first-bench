# N81: 1x A100 80GB 方案的 3 年 TCO 量化计算：TCO_1xA100 = P_A100_market + P_server_chassis + P_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

1x A100 80GB 方案的 3 年 TCO 量化计算：TCO_1xA100 = P_A100_market + P_server_chassis + P_psu_2000W + E_power_A100 * 3年 + C_failure_A100，其中 P_A100_market 需区分 SXM4 (需专用基板) 与 PCIe 版本价格差异 [实时查询]，SXM4 需额外计入服务器级散热与供电基础设施成本。

## Corrected Claim

1x A100 80GB 方案的 3 年 TCO 量化计算框架为：TCO_1xA100 = P_A100_market + P_server_chassis + P_psu_2000W + E_power_A100 * 3年 + C_failure_A100。其中 P_A100_market 需区分 SXM4 与 PCIe 版本，SXM4 版本通常需额外计入服务器级散热与供电基础设施成本，具体数值需实时查询市场报价。

## Evidence

[质询]该陈述包含具体的实时市场价格（P_A100_market）和具体的硬件配置成本（SXM4专用基板、2000W PSU等），属于经验事实。参考来源仅提供了云租赁价格（$0.52/hour）和二手市场存在性，未提供具体的硬件采购单价、服务器机箱/电源成本或SXM4与PCIe版本的具体价差数据，无法直接支持TCO公式中各项的具体数值或定性结论的精确性。 | 逻辑自洽：TCO公式结构合理，SXM4确实需要专用基板且通常伴随更高的基础设施成本，这与硬件常识一致。但作为source=search节点，缺乏来源直接支持具体价格差异或完整TCO数值，依据经验事实排除条款，降级为degraded。

## Search Query

NVIDIA A100 80GB SXM4 PCIe price 2024 2025 market quote

## Retrieval Sources

- {'url': 'https://www.ebay.com/itm/197636199567&rut=6920a3d9913101987af052ba9d30bc9e656319fbe4b16ed879dfa071127fe982', 'type': 'ddg', 'title': 'Nvidia A100 80GB SXM4 AI GPU 699-2G506-0210 - eBay'}
- {'url': 'https://www.ebay.com/sch/i.html?_nkw=nvidia+a100+80gb&_sop=12&rut=40f3dfe28996a2a68dbab957ab4cad4c7cf2967fd6eecb4aaa8b82386f945b8f', 'type': 'ddg', 'title': 'Nvidia A100 80GB for sale - eBay'}
- {'url': 'https://flopper.io/pricing/nvidia-a100-sxm4-80gb&rut=52fab3193b05da3ca0a778693d36c89efbf3ab058ccb5505cb6ce7b80d8f59c9', 'type': 'ddg', 'title': 'NVIDIA A100 SXM4 Price: from $0.52/hour across 25 providers'}
