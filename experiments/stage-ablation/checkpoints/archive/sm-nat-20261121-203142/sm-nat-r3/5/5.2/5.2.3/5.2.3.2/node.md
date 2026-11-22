# N179: 在高开销实现（10% 元数据）下，LFU 计数器占用 12.8GB，有效缓存容量 C_eff = 115.2GB，容量损失项 ΔH_capacity 显著增大，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

在高开销实现（10% 元数据）下，LFU 计数器占用 12.8GB，有效缓存容量 C_eff = 115.2GB，容量损失项 ΔH_capacity 显著增大，计算公式同上，需量化该额外 6.4GB 损失对最终命中率的具体百分点影响。

## Corrected Claim

在高开销实现（10% 元数据）下，LFU 计数器占用 12.8GB，有效缓存容量 C_eff = 115.2GB，容量损失项 ΔH_capacity 显著增大，计算公式同上，需量化该额外 6.4GB 损失对最终命中率的具体百分点影响。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB总容量下10%元数据开销对应12.8GB，剩余有效容量115.2GB，数值计算自洽。
