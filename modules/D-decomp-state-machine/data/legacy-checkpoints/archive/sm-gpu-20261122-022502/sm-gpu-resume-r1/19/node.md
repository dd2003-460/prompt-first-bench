# N364: 构建条件分支推荐逻辑：若用户电价 > $0.15/kWh 且预期持有期 < 2 年，RTX 4090 单卡 (INT4) 为最优；若电价 < $0.10/kWh

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

构建条件分支推荐逻辑：若用户电价 > $0.15/kWh 且预期持有期 < 2 年，RTX 4090 单卡 (INT4) 为最优；若电价 < $0.10/kWh 且追求极致吞吐 (>100 tokens/s)，RTX 5090 单卡 (FP8/INT4) 为最优；若需支持高并发 (Batch > 4) 且预算充足，H100 单卡为唯一可行消费级替代方案。

## Corrected Claim

构建条件分支推荐逻辑：若用户电价 > $0.15/kWh 且预期持有期 < 2 年，RTX 4090 单卡 (INT4) 为最优；若电价 < $0.10/kWh 且追求极致吞吐 (>100 tokens/s)，RTX 5090 单卡 (FP8/INT4) 为最优；若需支持高并发 (Batch > 4) 且预算充足，H100 单卡为唯一可行消费级替代方案。

## Evidence

检索失败: no sources from any channel (all 5 failed)
