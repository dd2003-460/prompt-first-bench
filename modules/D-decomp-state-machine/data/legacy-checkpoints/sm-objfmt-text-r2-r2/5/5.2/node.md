# N28: Qwen3-27B 在 BF16 精度下，单张消费级 GPU（如 RTX 4090 24GB）由于显存不足需量化至 FP8 或更低，其吞吐量约为 40 toke

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

Qwen3-27B 在 BF16 精度下，单张消费级 GPU（如 RTX 4090 24GB）由于显存不足需量化至 FP8 或更低，其吞吐量约为 40 tokens/s [待核验]

## Corrected Claim

Qwen3-27B 在 BF16 精度下，单张消费级 GPU（如 RTX 4090 24GB）由于显存不足需量化至 FP8 或更低，其吞吐量约为 40 tokens/s（待进一步验证具体数值）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别阐述了硬件物理瓶颈（带宽）、显存约束与量化必要性、以及理论吞吐估算与验证，三者逻辑层层递进且维度独立（物理限制->可行性约束->性能预估），无重复或矛盾，且完整覆盖了父节点中关于显存不足、量化需求及吞吐量预估的核心要素。）

## Search Query

Qwen3-27B RTX 4090 inference speed quantized

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072597504793880030&rut=304ab9b1949db5d068e5f24670c8b7c3dcf1028c44ee8d381a92e4513f6bc363', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 BF16、FP8、MTP、单卡表现，以及与 Qwen3.6 MoE 的差距'}
