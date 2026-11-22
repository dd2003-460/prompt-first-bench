# N52: AMD MI300X 的精确规格为：192GB HBM3, 内存带宽 5.3TB/s, TDP 750W, ROCm 6.x 对 PyTorch 2.3+ 的支

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

AMD MI300X 的精确规格为：192GB HBM3, 内存带宽 5.3TB/s, TDP 750W, ROCm 6.x 对 PyTorch 2.3+ 的支持已稳定，单卡价格区间 $15,000-$18,000 (2024 Q3 市场价)

## Corrected Claim

AMD MI300X 的规格为：192GB HBM3, 内存带宽约 5.3TB/s, TDP 750W；ROCm 6.x 对 PyTorch 2.3+ 的支持情况及单卡价格区间 $15,000-$18,000 (2024 Q3) 需进一步核实，当前来源未提供直接证据。

## Evidence

[质询]来源摘要中存在明显的单位错误（将内存带宽 5.3TB/s 误写为 5.325 TFLOPS），且参考来源完全未覆盖 ROCm 版本支持情况及 2024 Q3 的市场价格区间，导致部分关键事实缺乏直接证据支持。 | 来源 [1][2] 直接支持 192GB HBM3 和 750W TDP，但摘要中带宽单位有误（应为 TB/s 而非 TFLOPS，数值 5.325 对应 5.3TB/s 量级）；ROCm 支持状态与价格区间属于经验事实，逻辑自洽但缺乏来源直接支持。

## Search Query

AMD MI300X specifications price ROCm PyTorch support 2024

## Retrieval Sources

- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html&rut=6bd1d4a5b76525d5cf51f2f1fddd8511344271395216d7375ac569e93a84ee85', 'type': 'ddg', 'title': 'AMD Instinct™ MI300X Accelerators'}
- {'url': 'https://www.amd.com/zh-tw/products/accelerators/instinct/mi300/mi300x.html&rut=b4a4a47ee38c831468a387ce18f3b6afc423ac4ac4b30d21c202cf5fb886c9ff', 'type': 'ddg', 'title': 'AMD Instinct™ MI300X 加速器'}
