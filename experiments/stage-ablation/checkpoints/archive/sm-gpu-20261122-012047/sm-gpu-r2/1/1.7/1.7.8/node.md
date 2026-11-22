# N75: H100 SXM5 (80GB) 在 2024-2025 年的实际采购价格约为 $25,000-$35,000 [待核验]，波动较大；A100 80GB PCI

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12, N13, N14

## Claim

H100 SXM5 (80GB) 在 2024-2025 年的实际采购价格约为 $25,000-$35,000 [待核验]，波动较大；A100 80GB PCIe 价格约为 $12,000-$18,000 [待核验]。价格区间的不确定性意味着 TCO 计算需采用保守估计（取上限）进行敏感性分析。

## Corrected Claim

H100 SXM5 (80GB) 在 2024-2025 年的实际采购价格约为 $35,000-$40,000 [来源 [2]]，波动较大；A100 80GB PCIe 价格约为 $12,000-$18,000 [待核验]。价格区间的不确定性意味着 TCO 计算需采用保守估计（取上限）进行敏感性分析。

## Evidence

[质询]H100 SXM5 的价格区间被低估：来源 [2] 明确指出 2025 年中 H100 80GB SXM 的价格范围为 $35,000-$40,000，而陈述中给出的 $25,000-$35,000 上限仅触及来源区间的下限，且下限 $25,000 更接近 PCIe 版本的价格（来源 [1] 和 [2] 均指出 PCIe 约为 $25,000-$30,000）。陈述混淆了 PCIe 和 SXM 的价格层级，导致 SXM 价格区间整体偏低。 | 来源 [2] 直接指出 H100 80GB SXM 价格为 $35,000-$40,000，与陈述中的 $25,000-$35,000 存在显著偏差（上限偏低 $5,000-$10,000）；来源 [3] 给出的 $25,000-$35,000 是 PCIe 和 SXM 的混合区间，未单独区分 SXM。A100 价格无直接来源支持，但逻辑上合理。

## Search Query

H100 SXM5 actual market price 2025 A100 80GB PCIe current cost data center GPU pricing volatility

## Retrieval Sources

- {'url': 'https://cyfuture.cloud/kb/gpu/how-much-does-an-h100-gpu-cost-in-2025&rut=d118fb217bc5146ed6c0d6ad9447c804933f71f72b916f01e26093f823c44298', 'type': 'ddg', 'title': 'How Much Does an H100 GPU Cost in 2025? - cyfuture.cloud'}
- {'url': 'https://northflank.com/blog/how-much-does-an-nvidia-h100-gpu-cost&rut=7bce3ef301e029f2ebe80ec8c53444d67c4e0365d306e03878893ae7a99a8552', 'type': 'ddg', 'title': 'How much does an NVIDIA H100 GPU cost? - Blog — Northflank'}
- {'url': 'https://cyfuture.cloud/kb/gpu/nvidia-h100-80gb-price-2025-specs-cost-and-market-trends&rut=2808b61c3dbd57b12fbc3cce2ffe3f45173510e1c6dd419b312adf7cead54c90', 'type': 'ddg', 'title': 'NVIDIA H100 80GB Price 2025-Specs, Cost, and Market Trends'}
