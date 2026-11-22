# N521: 数据中心方案 (H100 SXM) 的 TCO 公式：TCO_dc(T) = CapEx_h100 + (Power_h100 * T / 8760)，其中 P

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N160

## Claim

数据中心方案 (H100 SXM) 的 TCO 公式：TCO_dc(T) = CapEx_h100 + (Power_h100 * T / 8760)，其中 Power_h100 约为 700W (峰值) 或 350W (平均推理负载)，CapEx_h100 约为 $30,000-$40,000 [待核验：当前现货价格及电价假设 0.1 $/kWh]，该方案在 T > 2 年时因高 CapEx 摊销而成本上升，但在高利用率下单位 Token 成本更低

## Corrected Claim

数据中心方案 (H100 SXM) 的简化 TCO 模型：TCO_dc(T) ≈ CapEx_h100 + (Power_h100 * T / 8760 * 电价)，其中 Power_h100 峰值约 700W，平均推理负载约 350W，CapEx_h100 市场参考价约为 $25,000-$40,000（需根据具体采购渠道调整），该模型未包含机房及运维成本，在高利用率下相比云租赁具有长期成本优势。

## Evidence

[质询]CapEx 数值（$30k-$40k）与当前 H100 SXM 市场现货价格（通常 $25k-$35k 或更高，视渠道和时期而定）存在偏差，且 TCO 公式中未包含冷却、机房租金（Colo）及运维成本，仅计算电力和硬件折旧，导致 TCO 被低估；此外，'T > 2 年时因高 CapEx 摊销而成本上升'的表述在逻辑上略有歧义，通常 TCO 随时间线性增加，但单位时间成本随 T 增加而降低（摊销效应），除非指与云租赁相比的相对优势窗口。 | 来源 [1][2][3] 提供了 H100 TCO 分析框架及云租赁价格（£2.19/hr），间接支持 TCO 包含硬件和电力成本的逻辑，但未直接验证 $30k-$40k 的 CapEx 具体数值或 700W/350W 的功耗假设，属于经验事实且缺乏直接来源支持。

## Search Query

H100 SXM TCO total cost of ownership electricity cost inference workload average power draw

## Retrieval Sources

- {'url': 'https://aggressive.ai/gpu-cloud-h100-tco-with-free-trial&rut=b19a5b037c1243a0442249dec70bbf258ef3f402df5c9ad00cbfa8fc2c6e8fea', 'type': 'ddg', 'title': 'H100 GPU cloud total cost of ownership with a free trial (2026)'}
- {'url': 'https://aggressive.ai/gpu-cloud-h100-tco-with-monthly-billing&rut=ffe56dafe05c3360971cd21797b1ec29d6c369498ef0407b89e709c9259203d3', 'type': 'ddg', 'title': 'H100 GPU cloud total cost of ownership with monthly billing (2026)'}
- {'url': 'https://gpuleaseindex.com/tools/gpu-tco-analysis&rut=74b0468633893b03578ea15f8d021d0412844f524b99f6fc5647222a8d486f1b', 'type': 'ddg', 'title': 'GPU TCO Analysis: Cloud vs. Buy vs. Lease (2026)'}
