# N191: KV 显存压力下的动态降级策略：当 GPU 显存使用率 > 90% 时，自动将 max-num-seqs 从 8 降至 4，并将 Seq_Len_max 从 6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

KV 显存压力下的动态降级策略：当 GPU 显存使用率 > 90% 时，自动将 max-num-seqs 从 8 降至 4，并将 Seq_Len_max 从 65536 降至 32768，避免 OOM 崩溃，降级切换时间 < 500ms。

## Corrected Claim

KV 显存压力下的动态降级策略：当 GPU 显存使用率 > 90% 时，自动将 max-num-seqs 从 8 降至 4，并将 Seq_Len_max 从 65536 降至 32768，避免 OOM 崩溃，降级切换时间 < 500ms。

## Evidence

先验知识/题面给定，逻辑校验通过
