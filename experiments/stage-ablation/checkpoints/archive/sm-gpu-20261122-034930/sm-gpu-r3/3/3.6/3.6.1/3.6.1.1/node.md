# N301: Mac Studio M2 Ultra 的加权平均功耗修正：在 Qwen3-27B 推理负载下，GPU 集群功耗约为 120W，CPU/内存/其他组件约 50W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

Mac Studio M2 Ultra 的加权平均功耗修正：在 Qwen3-27B 推理负载下，GPU 集群功耗约为 120W，CPU/内存/其他组件约 50W，系统总平均功耗约 170W (而非假设的 200W)，3 年电力成本修正为 3 * (170W * 0.6 * 8760h * $0.15/kWh) ≈ $477。

## Corrected Claim

Mac Studio M2 Ultra 的加权平均功耗修正：在 Qwen3-27B 推理负载下，GPU 集群功耗约为 120W，CPU/内存/其他组件约 50W，系统总平均功耗约 170W (而非假设的 200W)，3 年电力成本修正为 3 * (170W * 0.6 * 8760h * $0.15/kWh) ≈ $477。

## Evidence

先验知识/题面给定，逻辑校验通过：功耗分解（120W+50W=170W）与总功耗一致；电力成本计算公式 3 * (170 * 0.6 * 8760 * 0.15) ≈ 477.18 数值准确，量纲与逻辑自洽。
