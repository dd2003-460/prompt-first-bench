# N42: 由于理论需求 256GB 远大于可用内存 48.5GB，vLLM 将触发抢占机制 (Preemption) 或拒绝新请求，实际并发数受限于 48.5GB / (

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

由于理论需求 256GB 远大于可用内存 48.5GB，vLLM 将触发抢占机制 (Preemption) 或拒绝新请求，实际并发数受限于 48.5GB / (262144 * 128KB) ≈ 1.4 个序列，即实际最大并发约为 1

## Corrected Claim

由于理论需求 256GB 远大于可用内存 48.5GB，vLLM 将触发抢占机制 (Preemption) 或拒绝新请求，实际并发数受限于 48.5GB / (262144 * 128KB) ≈ 1.4 个序列，即实际最大并发约为 1

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一资源约束（内存容量）下不同参数组合（max_model_len, max_num_seqs）的实例化，存在高度冗余；且未覆盖父节点核心论点中的'拒绝新请求'或'抢占机制触发后的具体行为/代价'这一关键方面，仅展示了无风险的可行解，未解释理论需求超出时的后果。）
