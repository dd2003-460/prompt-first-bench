# N362: AMD RX 7900 XTX 运行 Qwen3-27B INT4 时，ROCm 栈的 Kernel Launch Overhead 在 Batch Size=

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD RX 7900 XTX 运行 Qwen3-27B INT4 时，ROCm 栈的 Kernel Launch Overhead 在 Batch Size=1 场景下占比高达 30-40% [待核验]，若该比例属实，其实际吞吐将从理论 71.1 tokens/s 降至 ~45 tokens/s，单位成本将反超 RTX 4090，从而改变‘AMD 消费卡性价比高’的结论。

## Corrected Claim

AMD RX 7900 XTX 运行 Qwen3-27B INT4 时，ROCm 栈的 Kernel Launch Overhead 在 Batch Size=1 场景下占比高达 30-40% [待核验]，若该比例属实，其实际吞吐将从理论 71.1 tokens/s 降至 ~45 tokens/s，单位成本将反超 RTX 4090，从而改变‘AMD 消费卡性价比高’的结论。

## Evidence

检索失败: no sources from any channel (all 5 failed)
