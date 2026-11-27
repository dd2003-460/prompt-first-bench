# N331: 若 2×RTX 4090 方案必须使用 PCIe 扩展/转接硬件（如 x16 转 x8+x8 或 PCIe 5.0 延长线），具体型号（如 StarTech 或

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95, N96, N97

## Claim

若 2×RTX 4090 方案必须使用 PCIe 扩展/转接硬件（如 x16 转 x8+x8 或 PCIe 5.0 延长线），具体型号（如 StarTech 或 Cable Matters）的市场均价约为 $80-$120 USD，且需注意 PCIe 4.0 x16 带宽在转接后可能降至 x8 模式（16GB/s），进而影响 All-Reduce 通信效率

## Corrected Claim

若 2×RTX 4090 方案必须使用 PCIe 扩展/转接硬件，需注意 PCIe 4.0 x16 带宽在转接后可能降至 x8 模式（16GB/s），进而影响 All-Reduce 通信效率；具体硬件（如 x16 转 x8+x8 或延长线）的市场价格因品牌和规格而异，通常需在 $50-$200 USD 范围内根据具体型号查询。

## Evidence

[质询]具体品牌（StarTech/Cable Matters）的市场均价属于实时变动的经验事实，且不同规格（如是否有主动散热、是否支持PCIe 5.0）价格差异巨大，$80-$120的区间可能因型号选择不同而失效，缺乏具体型号限定导致数值范围可能不准确。 | 经验事实，逻辑自洽但缺来源支持。PCIe 4.0 x16带宽为32GB/s，x8为16GB/s，物理逻辑正确；但具体市场价格无来源覆盖，且属于易变动的商业数据，无法通过第一性原理推导。

## Search Query

PCIe x16 riser card price 2024 for dual GPU LLM inference
