# N38: 推荐方案的条件性约束2 - 并发量与延迟：若并发数 > 4 且要求 P99 延迟 < 2s，单卡消费级 GPU 因显存带宽和 KV Cache 容量限制可能成为

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推荐方案的条件性约束2 - 并发量与延迟：若并发数 > 4 且要求 P99 延迟 < 2s，单卡消费级 GPU 因显存带宽和 KV Cache 容量限制可能成为瓶颈，需升级为数据中心级 H100 或 L40S；若并发数 <= 1 且无硬性延迟指标，消费级双卡方案在 TCO 上通常优于单张数据中心卡。

## Corrected Claim

推荐方案的条件性约束2 - 并发量与延迟：若并发数 > 4 且要求 P99 延迟 < 2s，单卡消费级 GPU 因显存带宽和 KV Cache 容量限制可能成为瓶颈，需升级为数据中心级 H100 或 L40S；若并发数 <= 1 且无硬性延迟指标，消费级双卡方案在 TCO 上通常优于单张数据中心卡。

## Evidence

检索失败: no sources from any channel (all 5 failed)
