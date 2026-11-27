# N34: 在 TP=4 且 max_model_len=262144 的配置下，单个序列的 KV Cache 占用为 262144 * 16KB = 4.19 GB，4 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 TP=4 且 max_model_len=262144 的配置下，单个序列的 KV Cache 占用为 262144 * 16KB = 4.19 GB，4 卡总 KV 池为 13.76GB * 4 = 55GB，理论最大并发序列数为 55GB / 4.19GB ≈ 13 个长上下文序列。然而，考虑到 MTP 草稿头占用和激活内存，实际安全并发上限为 8 个序列（题目设定 max-num-seqs=8），此时显存余量仅 15%，任何突发长文本生成将触发 vLLM 的 Preemption 机制，导致 P99 延迟增加 200ms+。

## Corrected Claim

在 TP=4 且 max_model_len=262144 的配置下，单个序列的 KV Cache 占用为 262144 * 16KB = 4.19 GB，4 卡总 KV 池为 13.76GB * 4 = 55GB，理论最大并发序列数为 55GB / 4.19GB ≈ 13 个长上下文序列。然而，考虑到 MTP 草稿头占用和激活内存，实际安全并发上限为 8 个序列（题目设定 max-num-seqs=8），此时显存余量仅 15%，任何突发长文本生成将触发 vLLM 的 Preemption 机制，导致 P99 延迟增加 200ms+。

## Evidence

父节点级核验未通过：非正交（子节点1修正了KV Cache的单序列占用计算，子节点2基于该修正值重新计算并发上限并推翻父节点结论，两者存在强烈的逻辑依赖关系而非正交；此外，子节点3引入的Prefill激活内存分析属于新的技术维度，虽然独立，但整体结构上子节点1和2是同一核心论点（KV计算错误导致并发结论错误）的两个阶段，不够正交。）
