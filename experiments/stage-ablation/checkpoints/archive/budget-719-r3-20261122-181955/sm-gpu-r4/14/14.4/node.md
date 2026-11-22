# N391: AMD Radeon Pro W7900 48GB 的 TDP 为 300W (官方规格)，在 LLM 推理负载下平均功耗约为 0.7 * 300W ≈ 210

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

AMD Radeon Pro W7900 48GB 的 TDP 为 300W (官方规格)，在 LLM 推理负载下平均功耗约为 0.7 * 300W ≈ 210W，年电力成本 (7x24 运行, $0.15/kWh) 约为 210W * 8760h * $0.15/kWh ≈ $276 USD/年。

## Corrected Claim

AMD Radeon Pro W7900 48GB 的 TDP 为 300W (官方规格)，在 LLM 推理负载下平均功耗约为 210W (基于0.7负载系数估算)，年电力成本 (7x24 运行, $0.15/kWh) 约为 $276 USD/年。

## Evidence

[质询]LLM推理负载下的平均功耗系数0.7属于经验估计值，缺乏官方或权威基准测试支持，且不同模型和批次大小下功耗波动较大，该系数可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AMD Radeon Pro W7900 TDP power consumption watts
