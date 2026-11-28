# N167: vLLM 在 Pipeline Parallelism (PP=2) 模式下，KV Cache 并非集中在单一 Stage，而是根据 Layer 切分均匀分布在

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

vLLM 在 Pipeline Parallelism (PP=2) 模式下，KV Cache 并非集中在单一 Stage，而是根据 Layer 切分均匀分布在所有参与 PP 的 GPU 上；每个 GPU 仅存储其负责 Layer 对应的 KV 块，因此单卡 KV 显存占用约为 Total_KV_Memory / PP_Size。

## Corrected Claim

vLLM 在 Pipeline Parallelism (PP=2) 模式下，KV Cache 并非集中在单一 Stage，而是根据 Layer 切分均匀分布在所有参与 PP 的 GPU 上；每个 GPU 仅存储其负责 Layer 对应的 KV 块，因此单卡 KV 显存占用约为 Total_KV_Memory / PP_Size。

## Evidence

先验知识/题面给定，逻辑校验通过：Pipeline Parallelism 的核心机制是将 Transformer 层按顺序切分到不同设备，KV Cache 与 Layer 绑定，因此显存占用随 PP_Size 线性分摊，符合分布式推理的基本原理。

## Search Query

vLLM pipeline parallelism KV cache distribution per gpu
