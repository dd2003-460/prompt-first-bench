# N12: Qwen3-27B 在 BF16 下 Prefill 阶段（计算密集）的算力需求约为 270 TOPS（2 × 27B 参数），在 Decode 阶段（访存密集

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 BF16 下 Prefill 阶段（计算密集）的算力需求约为 270 TOPS（2 × 27B 参数），在 Decode 阶段（访存密集）的带宽需求约为 54GB/s（27B 参数 × 2 bytes）

## Corrected Claim

Qwen3-27B 在 BF16 下 Prefill 阶段（计算密集）的算力需求约为 270 TOPS（2 × 27B 参数），在 Decode 阶段（访存密集）的带宽需求约为 54GB/s（27B 参数 × 2 bytes）

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别针对 Prefill（计算密集）和 Decode（访存密集）两个不同阶段进行修正和扩展，主题互不重叠且无矛盾。它们共同覆盖了父节点提到的两个关键方面（算力和带宽），并补充了具体的硬件性能推算，结构清晰。）
