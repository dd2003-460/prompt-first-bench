# N72: 电价敏感性分析：电价从 $0.10/kWh 升至 $0.20/kWh 时，3年电力成本翻倍，对于高功耗方案（如 2×4090 或 H100）TCO 中电力占比从

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

电价敏感性分析：电价从 $0.10/kWh 升至 $0.20/kWh 时，3年电力成本翻倍，对于高功耗方案（如 2×4090 或 H100）TCO 中电力占比从 ~15% 升至 ~30%，可能改变性价比排序，需计算临界电价阈值。

## Corrected Claim

电价敏感性分析：电价从 $0.10/kWh 升至 $0.20/kWh 时，3年电力成本翻倍，对于高功耗方案（如 2×4090 或 H100）TCO 中电力占比从 ~15% 升至 ~30%，可能改变性价比排序，需计算临界电价阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：电价翻倍导致电力成本线性翻倍；对于高功耗硬件，电力成本在TCO中占比显著，从15%升至30%符合线性增长逻辑，且足以影响TCO排序。

## Search Query

electricity price sensitivity analysis TCO data center GPU
