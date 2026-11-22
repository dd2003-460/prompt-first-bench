# N451: 最终推荐方案的条件性约束 2：若用户计划在未来 12 个月内升级至 70B 参数模型，则当前购买 2x RTX 4090 (48GB total) 或 1x R

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

最终推荐方案的条件性约束 2：若用户计划在未来 12 个月内升级至 70B 参数模型，则当前购买 2x RTX 4090 (48GB total) 或 1x RTX 6000 Ada (48GB) 的沉没成本更低，因为 2x 4090 可通过 NVLink-less 并行勉强运行 70B INT4，而单卡 A100 80GB 虽能运行 70B BF16 但价格高出 3-4 倍，故在‘模型规模可扩展性’维度下，消费级双卡方案优于数据中心单卡方案

## Corrected Claim

最终推荐方案的条件性约束 2：若用户计划在未来 12 个月内升级至 70B 参数模型，则当前购买 2x RTX 4090 (48GB total) 或 1x RTX 6000 Ada (48GB) 的沉没成本更低，因为 2x 4090 可通过 NVLink-less 并行勉强运行 70B INT4，而单卡 A100 80GB 虽能运行 70B BF16 但价格高出 3-4 倍，故在‘模型规模可扩展性’维度下，消费级双卡方案优于数据中心单卡方案

## Evidence

检索失败: no sources from any channel (all 5 failed)
