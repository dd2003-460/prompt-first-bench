# N79: 2×RTX 4090 (48GB) 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用计算：2 * 64 * 4096 * 32 * 3

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

2×RTX 4090 (48GB) 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用计算：2 * 64 * 4096 * 32 * 32768 * 1 byte ≈ 55.0MB/layer * 64 ≈ 3.5GB，加上权重 27GB 和运行时开销 5GB，总显存需求约 35.5GB，低于 48GB 上限，方案可行。

## Corrected Claim

2×RTX 4090 (48GB) 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用计算：2 * 64 * 4096 * 32 * 32768 * 1 byte ≈ 55.0MB/layer * 64 ≈ 3.5GB，加上权重 27GB 和运行时开销 5GB，总显存需求约 35.5GB，低于 48GB 上限，方案可行。

## Evidence

父节点级核验未通过：非正交（子节点3在逻辑上重复了子节点1和子节点2的计算结果（直接引用了子节点1的16.78GB和子节点2的3-6GB），违反了正交性原则，子节点3应仅作为结论节点而非计算过程节点。此外，子节点1存在严重的技术事实错误：Qwen3-27B通常采用GQA（Grouped Query Attention），KV heads远少于Q heads（例如8个KV heads而非32个），按Full Attention计算会导致KV Cache显存估算严重高估（实际约为16.78GB的1/4，即约4.2GB），导致最终结论‘接近或超过限制’可能错误。）
