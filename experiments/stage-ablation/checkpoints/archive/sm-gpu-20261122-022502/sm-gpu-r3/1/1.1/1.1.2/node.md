# N34: Qwen3-27B BF16权重文件大小为 54GB (27,000,000,000 params * 2 bytes/param)，加上KV Cache (~

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

Qwen3-27B BF16权重文件大小为 54GB (27,000,000,000 params * 2 bytes/param)，加上KV Cache (~0.2GB) 和激活值/临时缓冲区 (~1-2GB)，总显存需求下限为 55.2GB，因此32GB显存GPU在BF16下缺口为 23.2GB

## Corrected Claim

Qwen3-27B BF16权重文件大小为 54GB (27,000,000,000 params * 2 bytes/param)，加上KV Cache (~0.2GB) 和激活值/临时缓冲区 (~1-2GB)，总显存需求下限为 55.2GB，因此32GB显存GPU在BF16下缺口为 23.2GB

## Evidence

父节点级核验未通过：非正交, 不完备（1. 矛盾性：父节点声称总显存下限为55.2GB（基于KV Cache ~0.2GB），而子节点2声称总显存下限为58.65GB（基于KV Cache 2.15GB）。这两个数值在相同上下文（32K）下存在显著矛盾，子节点直接否定了父节点的结论，违反了分解中子节点应细化而非直接反驳父节点核心事实的原则（除非父节点明确标记为错误估算且子节点为修正，但通常分解应保持逻辑一致性或明确标注修正关系，此处表现为事实冲突）。2. 不完备：父节点的核心结论是“缺口为23.2GB”，子节点1仅详细展开了激活值部分，子节点2给出了新的总显存和缺口，但没有明确解释为何KV Cache从0.2GB变为2.15GB（例如是否因为32K上下文导致KV Cache大幅增加，而父节点可能使用了错误的KV Cache估算值）。子节点未能完整覆盖父节点中所有参数（权重、KV Cache、激活）的修正逻辑，导致逻辑链条断裂。）
