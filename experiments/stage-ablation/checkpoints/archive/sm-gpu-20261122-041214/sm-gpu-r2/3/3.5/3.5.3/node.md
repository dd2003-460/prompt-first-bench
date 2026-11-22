# N113: 2x RTX 4090 方案需要支持双 PCIe x16 插槽且物理间距足够的主板（如 ASUS ProArt X670E-Creator WiFi），额外主板

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

2x RTX 4090 方案需要支持双 PCIe x16 插槽且物理间距足够的主板（如 ASUS ProArt X670E-Creator WiFi），额外主板成本约 $300-$500，加上 1000W-1200W 电源（$150-$200）和双卡支架/散热增强（$50-$100），基础设施总成本约 $500-$800，而非 N31 中的 $500。

## Corrected Claim

2x RTX 4090 方案需要支持双 PCIe x16（或 x8+x8）插槽且物理间距足够的主板（如 ASUS ProArt X670E-Creator WiFi），并需配备 1000W-1200W 电源及双卡支架/散热增强，基础设施总成本显著高于单卡方案（具体金额需实时市场报价确认，通常远高于 $500）。

## Evidence

[质询]参考来源仅提供了主板的技术选型建议（需支持双PCIe x8/x8或x16/x16及空间布局），但完全未提及任何具体的硬件价格（主板、电源、支架）或总成本数值，无法验证$500-$800这一具体金额范围。 | 来源[1]间接支持了双卡对主板PCIe通道和物理空间的要求，但缺乏价格数据支持；作为经验事实（市场价格），逻辑自洽但缺来源直接支持，故降级。

## Search Query

dual RTX 4090 motherboard power supply cost 2024

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/16864316403&rut=35bf424984418c94012228904908f69344c7f1b2f80d961e6dda0e6b4d6d6adb', 'type': 'ddg', 'title': '基于双卡 Rtx 4090 搭建家用深度学习主机 - 知乎'}
