# N210: RTX 4090 在 BF16 下 Decode 理论最大吞吐为 1008 GB/s / 55.07 GB ≈ 18.3 tokens/s；考虑内存控制器效率 

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

RTX 4090 在 BF16 下 Decode 理论最大吞吐为 1008 GB/s / 55.07 GB ≈ 18.3 tokens/s；考虑内存控制器效率 (60%-80%)，实际吞吐约为 11-14.6 tokens/s；H100 SXM 理论最大吞吐为 3350 GB/s / 55.07 GB ≈ 60.8 tokens/s，实际吞吐约为 36-48.6 tokens/s

## Corrected Claim

RTX 4090 在 BF16 下 Decode 理论最大吞吐为 1008 GB/s / 55.07 GB ≈ 18.3 tokens/s；考虑内存控制器效率 (60%-80%)，实际吞吐约为 11-14.6 tokens/s；H100 SXM 理论最大吞吐为 3350 GB/s / 55.07 GB ≈ 60.8 tokens/s，实际吞吐约为 36-48.6 tokens/s

## Evidence

父节点级核验未通过：不完备（子节点之间存在配置上的正交性（不同硬件/精度组合），但存在逻辑矛盾和覆盖缺失。1. 矛盾：父节点明确限定为 BF16 权重（55.07GB），但子节点1和2分别引入了 FP8 和 INT4 权重，改变了模型大小和计算条件，导致子节点不再是对父节点（BF16场景）的分解，而是引入了新的独立场景，破坏了上下文的逻辑一致性。2. 缺失：父节点中关于 H100 的 BF16 具体数值范围（11-14.6 tokens/s for 4090, 36-48.6 for H100）在子节点中未得到完整对应。子节点3仅给出了 H100 的单一效率点（70%），而子节点1和2针对 RTX 4090 给出了不同精度下的新计算，完全偏离了父节点设定的 'BF16' 约束。）

## Search Query

RTX 4090 H100 decode throughput actual vs theoretical LLM
