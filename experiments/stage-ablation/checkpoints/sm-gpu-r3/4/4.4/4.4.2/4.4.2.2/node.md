# N224: H100 SXM 单卡性价比工作点：基于二手/租赁均价 $15000 (修正 N106 中 $25000 的新卡 MSRP 偏差，参考 N130 二手折扣 40

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

H100 SXM 单卡性价比工作点：基于二手/租赁均价 $15000 (修正 N106 中 $25000 的新卡 MSRP 偏差，参考 N130 二手折扣 40%) 和理论吞吐 60.9 tokens/s，单位成本吞吐 = 60.9 / 15000 ≈ 0.00406 tok/s/$，此时 4090 性价比约为 H100 的 2.25 倍 (0.00915/0.00406)。

## Corrected Claim

H100 SXM 单卡二手均价约为 $15,000（来源支持），但基于 60.9 tokens/s 吞吐量的性价比计算（约为 4090 的 2.25 倍）缺乏来源支持，需补充具体推理场景下的吞吐基准测试数据。

## Evidence

[质询]陈述中引用的理论吞吐 60.9 tokens/s 和 4090 的对比数据（0.00915 tok/s/$）在提供的参考来源中完全缺失，且 60.9 tokens/s 对于 H100 而言是一个极度依赖具体模型、序列长度和批处理大小的经验值，并非固定物理常数，无法仅凭逻辑推导验证其准确性。 | 来源 [1] 和 [2] 支持 H100 二手价格约为 $15,000（或处于 $12,000-$15,000 区间上限），但所有来源均未提供 H100 或 4090 的推理吞吐量数据，因此性价比倍数（2.25倍）缺乏外部证据支持，属于经验事实且缺来源支持。

## Search Query

H100 SXM used price 2024 cost per token inference benchmark

## Retrieval Sources

- {'url': 'https://serverbuyback.com/resources/gpu-resale-value-index/&rut=22de341dfc4dd3b677f59586444576ff4441995cb37322d2dc553d8e946ad040', 'type': 'ddg', 'title': 'GPU Resale Value Index (H100, A100, L40S) | ServerBuyback'}
- {'url': 'https://clusterbid.com/blog/h100-h200-gpu-depreciation-2026-buying-used-hardware-vs-renting&rut=bf6ee037dec84f6ae6525c2d9b43fce34ef2d7d22145fdfcc96ddbb3ca1bc2c2', 'type': 'ddg', 'title': 'H100 and H200 GPU Depreciation in 2026 - clusterbid.com'}
- {'url': 'https://clusterbid.com/blog/how-to-buy-used-h100-h200-gpus-2026-secondary-market-guide&rut=2a3b49f897745601fa39bbdc80bf1155336ef0b287e7c248a7eb85ffeb152531', 'type': 'ddg', 'title': 'How to Buy Used H100 and H200 GPUs in 2026'}
