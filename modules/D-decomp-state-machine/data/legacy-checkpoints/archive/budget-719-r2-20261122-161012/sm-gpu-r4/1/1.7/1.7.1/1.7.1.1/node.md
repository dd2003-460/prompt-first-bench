# N181: Qwen3-27B FP8 (E4M3) 权重文件大小精确计算：27,000,000,000 参数 * 1 byte/param = 27 GB；若包含 Emb

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

Qwen3-27B FP8 (E4M3) 权重文件大小精确计算：27,000,000,000 参数 * 1 byte/param = 27 GB；若包含 Embedding 层和 LM Head 层（通常未量化或保持 BF16），额外增加约 0.5-1 GB，总权重占用约为 27.5-28 GB。

## Corrected Claim

Qwen3-27B FP8 (E4M3) 权重文件大小精确计算：27,000,000,000 参数 * 1 byte/param = 27 GB；若包含 Embedding 层和 LM Head 层（通常未量化或保持 BF16），额外增加约 0.5-1 GB，总权重占用约为 27.5-28 GB。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点2存在严重的逻辑矛盾和冗余。子节点1声称 tie_word_embeddings=true，这意味着 Embedding 层和 LM Head 层共享权重，不存在额外的 2.5 GB 独立权重；而子节点2却计算了 2.5 GB 的额外 BF16 权重，这与子节点1的架构参数直接冲突。此外，子节点2重复了父节点中关于 FP8 主体大小（27 GB）的计算，且对 GiB/GB 的换算表述混乱，导致信息冗余。）
