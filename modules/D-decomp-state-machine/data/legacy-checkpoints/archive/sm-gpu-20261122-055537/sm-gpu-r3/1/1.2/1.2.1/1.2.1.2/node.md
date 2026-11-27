# N139: NVIDIA A100 80GB SXM 的典型功耗为 400W (TDP)，在 7x24 运行场景下，年度电力成本为 400W * 8760h * $0.15

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

NVIDIA A100 80GB SXM 的典型功耗为 400W (TDP)，在 7x24 运行场景下，年度电力成本为 400W * 8760h * $0.15/kWh = $525.6 USD/year；若租赁，则无需承担电力成本（包含在租赁费中），但租赁费 $2/hour * 8760h = $17,520 USD/year，远高于购买方案的电力成本。

## Corrected Claim

NVIDIA A100 80GB SXM 的典型功耗为 400W (TDP)，在 7x24 运行场景下，年度电力成本为 400W * 8760h * $0.15/kWh = $525.6 USD/year；若租赁，则无需承担电力成本（包含在租赁费中），但租赁费 $2/hour * 8760h = $17,520 USD/year，远高于购买方案的电力成本。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM TDP 400W 符合官方规格；电力成本计算 400W * 8760h * $0.15/kWh = $525.6 数学正确；租赁成本计算 $2/h * 8760h = $17,520 数学正确；结论逻辑自洽。
