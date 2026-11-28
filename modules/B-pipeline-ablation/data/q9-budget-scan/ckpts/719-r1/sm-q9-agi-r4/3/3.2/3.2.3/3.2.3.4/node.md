# N191: KV 显存压力下的动态降级策略：当 GPU 显存使用率 > 90% 时，自动将 max-num-seqs 从 8 降至 4，并将 Seq_Len_max 从 6

- **status**: pending
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

父节点级核验未通过：不完备（子节点分别聚焦于‘检测机制’和‘执行机制’，两者维度不同，无重复或矛盾，正交性良好。但父节点明确包含两个核心动作：降低 max-num-seqs 和降低 Seq_Len_max。当前子节点仅覆盖了 max-num-seqs 的执行问题，完全缺失了对 Seq_Len_max 动态调整机制及其执行成本的分析，导致覆盖不全。）
