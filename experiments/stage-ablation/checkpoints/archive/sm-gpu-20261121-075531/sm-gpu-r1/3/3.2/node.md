# N16: TCO电力成本 = (GPU TDP + 平台功耗) * 使用小时 * 电价; 例如RTX 4090 (450W) + 平台 (150W) = 600W, 10

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

TCO电力成本 = (GPU TDP + 平台功耗) * 使用小时 * 电价; 例如RTX 4090 (450W) + 平台 (150W) = 600W, 10小时/天, $0.15/kWh = $0.9/天; A100 (400W) + 服务器平台 (300W) = 700W, 24小时/天, $0.15/kWh = $2.52/天

## Corrected Claim

TCO电力成本 = (GPU TDP + 平台功耗) * 使用小时 * 电价; 例如RTX 4090 (450W) + 平台 (150W) = 600W, 10小时/天, $0.15/kWh = $0.9/天; A100 (400W) + 服务器平台 (300W) = 700W, 24小时/天, $0.15/kWh = $2.52/天

## Evidence

先验知识/题面给定，逻辑校验通过：公式 TCO=功率*时间*电价 符合物理定义；数值计算 0.6kW*10h*0.15=0.9 和 0.7kW*24h*0.15=2.52 均准确无误；硬件功耗参数（RTX 4090 TDP 450W, A100 TDP 400W）符合公开规格常识。
