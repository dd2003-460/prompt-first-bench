# N71: B2区间(10k-50k CNY)内的硬件组合可行性：包含 2×RTX 5090 (64GB 总显存) 支持 BF16 或 FP8，以及 1×L40S (48G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

B2区间(10k-50k CNY)内的硬件组合可行性：包含 2×RTX 5090 (64GB 总显存) 支持 BF16 或 FP8，以及 1×L40S (48GB) 或 1×A6000 (48GB) 支持 FP8/INT8；需对比单卡数据中心卡与双卡消费级卡的 TCO 差异。

## Corrected Claim

B2区间(10k-50k CNY)内的硬件组合可行性：包含 2×RTX 5090 (64GB 总显存) 支持 BF16 或 FP8，以及 1×L40S (48GB) 或 1×A6000 (48GB) 支持 FP8/INT8；需对比单卡数据中心卡与双卡消费级卡的 TCO 差异。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存为 32GB，双卡共 64GB 符合事实；L40S 和 A6000 显存均为 48GB 符合事实；价格区间 10k-50k CNY 覆盖了单张高端数据中心卡（如 L40S 约 3-4 万）或双张消费级旗舰卡（如 2x RTX 5090 约 4-5 万）的市场行情，TCO 对比逻辑自洽。
