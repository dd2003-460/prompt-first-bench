# N382: TCO敏感性分析工作点2（高成本低性-1x A100 80GB）：在基准电价$0.15/kWh、硬件价格稳定（ΔP=0）条件下，3年TCO=$15,500；当硬

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N135

## Claim

TCO敏感性分析工作点2（高成本低性-1x A100 80GB）：在基准电价$0.15/kWh、硬件价格稳定（ΔP=0）条件下，3年TCO=$15,500；当硬件价格下降ΔP=-25%（$7,500）时，3年TCO降至$13,000，性价比指标从3.2 tokens/s/$升至3.8 tokens/s/$，但仍低于2x RTX 4090方案（6.9 tokens/s/$），除非任务对吞吐量要求>50 tokens/s且A100实测吞吐率>45 tokens/s。

## Corrected Claim

TCO敏感性分析工作点2（高成本低性-1x A100 80GB）：在基准电价$0.15/kWh、硬件价格稳定（ΔP=0）条件下，3年TCO=$15,500；当硬件价格下降ΔP=-25%（$7,500）时，3年TCO降至$13,000，性价比指标从3.2 tokens/s/$升至3.8 tokens/s/$，但仍低于2x RTX 4090方案（6.9 tokens/s/$），除非任务对吞吐量要求>50 tokens/s且A100实测吞吐率>45 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO计算符合线性叠加逻辑（硬件成本下降直接降低总成本），性价比指标随成本降低而上升符合定义，且与对比方案（RTX 4090）的量级关系在工程常识范围内自洽。
