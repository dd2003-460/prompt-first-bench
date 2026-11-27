# N224: H100 SXM 单卡性价比工作点：基于二手/租赁均价 $15000 (修正 N106 中 $25000 的新卡 MSRP 偏差，参考 N130 二手折扣 40

- **status**: pending
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

父节点级核验未通过：不完备（子节点按精度（BF16 vs FP8）划分，逻辑正交且无冗余。但父节点明确包含“与4090的性价比对比（2.25倍）”这一关键结论，而子节点仅罗列了H100自身的单位成本吞吐数据，完全缺失了4090的对比数据及最终比值推导，导致信息不完备。）

## Search Query

H100 SXM used price 2024 cost per token inference benchmark

## Retrieval Sources

- {'url': 'https://serverbuyback.com/resources/gpu-resale-value-index/&rut=22de341dfc4dd3b677f59586444576ff4441995cb37322d2dc553d8e946ad040', 'type': 'ddg', 'title': 'GPU Resale Value Index (H100, A100, L40S) | ServerBuyback'}
- {'url': 'https://clusterbid.com/blog/h100-h200-gpu-depreciation-2026-buying-used-hardware-vs-renting&rut=bf6ee037dec84f6ae6525c2d9b43fce34ef2d7d22145fdfcc96ddbb3ca1bc2c2', 'type': 'ddg', 'title': 'H100 and H200 GPU Depreciation in 2026 - clusterbid.com'}
- {'url': 'https://clusterbid.com/blog/how-to-buy-used-h100-h200-gpus-2026-secondary-market-guide&rut=2a3b49f897745601fa39bbdc80bf1155336ef0b287e7c248a7eb85ffeb152531', 'type': 'ddg', 'title': 'How to Buy Used H100 and H200 GPUs in 2026'}
