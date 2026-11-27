# N49: N26 中 2.15 GB 的 KV Cache 显存开销计算存在数量级错误：262144 tokens * 4096 hidden_dim * 2 bytes

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

N26 中 2.15 GB 的 KV Cache 显存开销计算存在数量级错误：262144 tokens * 4096 hidden_dim * 2 bytes (FP8) = 2.147 TB，远超单卡 15.2 GB 显存，表明 max_model_len=262144 在当前硬件下完全不可行，实际最大上下文长度受限于 N18/N21 计算的 4000-5000 tokens 或 141 tokens（取决于矛盾解决）。

## Corrected Claim

N26 中 2.15 GB 的 KV Cache 显存开销计算存在数量级错误：262144 tokens * 4096 hidden_dim * 2 bytes (FP8) = 2.147 TB，远超单卡 15.2 GB 显存，表明 max_model_len=262144 在当前硬件下完全不可行，实际最大上下文长度受限于 N18/N21 计算的 4000-5000 tokens 或 141 tokens（取决于矛盾解决）。

## Evidence

父节点级核验未通过：不完备（子节点1和子节点2在逻辑上是递进关系（先纠正公式，再应用公式），因此是正交的。但是，父节点的核心主张之一是“max_model_len=262144 在当前硬件下完全不可行”，以及“实际最大上下文长度受限于...141 tokens（取决于矛盾解决）”。子节点2计算出最大长度约为28,160 tokens，这虽然证明了262k不可行，但并未解释为何父节点提到“141 tokens”这一极端限制（通常141 tokens这种极小值可能源于其他瓶颈如激活值、权重加载或特定的批处理配置，或者是对‘矛盾解决’指代不明情况的引用）。此外，父节点明确指出了与N18/N21的矛盾，子节点仅给出了一个基于新假设的计算值，未涵盖对原有矛盾来源的全面分析或确认。）
