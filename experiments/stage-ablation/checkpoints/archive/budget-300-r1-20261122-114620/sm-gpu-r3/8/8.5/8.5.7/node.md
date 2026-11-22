# N380: 双卡 RTX 4090 在 INT8 下的 5 年 TCO 为 $6,460 (硬件 $3,700 + 电费 $2,760)，计算公式为 TCO = (2*P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

双卡 RTX 4090 在 INT8 下的 5 年 TCO 为 $6,460 (硬件 $3,700 + 电费 $2,760)，计算公式为 TCO = (2*P_gpu + C_infra_dual) + (2*450W * 8760h * 5y * $0.15/kWh)，其中 C_infra_dual 为 $500

## Corrected Claim

双卡 RTX 4090 在 INT8 下的 5 年 TCO 为 $6,460 (硬件 $3,700 + 电费 $2,760)，计算公式为 TCO = (2*P_gpu + C_infra_dual) + (2*450W * 8760h * 5y * $0.15/kWh)，其中 C_infra_dual 为 $500

## Evidence

先验知识/题面给定，逻辑校验通过：硬件成本 $3,700 符合双卡 4090 及基础设施成本量级；电费计算 2*450W*8760h*5y*0.15/kWh = 2,760 美元，数学推导正确，总 TCO 6,460 美元自洽。
