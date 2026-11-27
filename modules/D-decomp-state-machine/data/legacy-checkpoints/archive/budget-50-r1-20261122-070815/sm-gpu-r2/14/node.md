# N152: 性价比最优解的条件性边界：当用户主要负载为短上下文 (<4K) 且对延迟不敏感时，RTX 4090 INT4 方案 TCO 最低；但当负载转为长上下文 (32K

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比最优解的条件性边界：当用户主要负载为短上下文 (<4K) 且对延迟不敏感时，RTX 4090 INT4 方案 TCO 最低；但当负载转为长上下文 (32K) 或需要高并发 (Batch>4) 时，由于 KV Cache 占用激增导致 4090 显存溢出或需量化 KV Cache (质量损失)，此时 L40S 或 A100 的性价比反超，需明确该切换点的具体 Batch Size 或 Context Length 阈值。

## Corrected Claim

性价比最优解的条件性边界：当用户主要负载为短上下文 (<4K) 且对延迟不敏感时，RTX 4090 INT4 方案 TCO 最低；但当负载转为长上下文 (32K) 或需要高并发 (Batch>4) 时，由于 KV Cache 占用激增导致 4090 显存溢出或需量化 KV Cache (质量损失)，此时 L40S 或 A100 的性价比反超，需明确该切换点的具体 Batch Size 或 Context Length 阈值。

## Evidence

检索失败: no sources from any channel (all 5 failed)
