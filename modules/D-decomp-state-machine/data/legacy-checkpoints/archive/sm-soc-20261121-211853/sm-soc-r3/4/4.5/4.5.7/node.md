# N52: 替代解释的量化检验：‘降价后曝光不足’假设的检验指标为 ΔExposure = Exposure_post - Exposure_pre，若 ΔExposure

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18, N19, N20

## Claim

替代解释的量化检验：‘降价后曝光不足’假设的检验指标为 ΔExposure = Exposure_post - Exposure_pre，若 ΔExposure < -10% 且 ΔInquiry ≈ 0，则支持该假设；‘买家已流失’假设的检验指标为 ΔBuyerPool = BuyerPool_post - BuyerPool_pre，若 ΔBuyerPool < -5% 且 ΔInquiry ≈ 0，则支持该假设。需通过平台数据面板回归验证。

## Corrected Claim

替代解释的量化检验：‘降价后曝光不足’假设可通过监测 ΔExposure 显著为负且 ΔInquiry 无显著变化来初步支持；‘买家已流失’假设可通过监测 ΔBuyerPool 显著为负且 ΔInquiry 无显著变化来初步支持。具体阈值（如-10%、-5%）需根据历史数据波动率或业务基准动态确定，并通过平台数据面板回归验证。

## Evidence

父节点级核验未通过：不完备（子节点分别定义了三个核心变量（ΔExposure, ΔBuyerPool, ΔInquiry）的统计检验标准，彼此正交且无冗余。但父节点明确要求‘需通过平台数据面板回归验证’，而所有子节点均仅描述了基于配对/双样本 t 检验或 Wilcoxon 检验的单变量统计推断方法，完全遗漏了‘面板回归’这一关键验证手段及其对应的控制变量、固定效应等设定，导致完备性不足。）

## Search Query

panel data regression test alternative explanations post-price-drop inquiry drop

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Parapsychology', 'type': 'wikipedia', 'title': 'Parapsychology'}
- {'url': 'https://en.wikipedia.org/wiki/Intelligence_quotient', 'type': 'wikipedia', 'title': 'Intelligence quotient'}
- {'url': 'https://en.wikipedia.org/wiki/Evidence_and_efficacy_of_homeopathy', 'type': 'wikipedia', 'title': 'Evidence and efficacy of homeopathy'}
