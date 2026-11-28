# N28: Qwen3-27B 在 BF16 精度下，单张消费级 GPU（如 RTX 4090 24GB）由于显存不足需量化至 FP8 或更低，其吞吐量约为 40 toke

- **status**: degraded
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

[质询]来源[1]讨论的是Qwen3.8-27B在L20显卡上的表现，而非Qwen3-27B在RTX 4090上的表现，且未提供40 tokens/s的具体数据，存在模型版本、硬件型号及具体数值的口径不匹配问题。 | 来源[1]主题相关但硬件和模型版本不完全匹配，未直接支持40 tokens/s的数值，属于间接支持或无关，故降级。

## Search Query

Qwen3-27B RTX 4090 inference speed quantized

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072597504793880030&rut=304ab9b1949db5d068e5f24670c8b7c3dcf1028c44ee8d381a92e4513f6bc363', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 BF16、FP8、MTP、单卡表现，以及与 Qwen3.6 MoE 的差距'}
