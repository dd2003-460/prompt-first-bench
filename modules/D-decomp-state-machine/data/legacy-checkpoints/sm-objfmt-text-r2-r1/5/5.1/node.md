# N27: Qwen3-27B 在 BF16 精度下，单卡（如 H100 80GB）的推理吞吐量基准值约为 150 tokens/s [待核验]

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

Qwen3-27B 在 BF16 精度下，单卡（如 H100 80GB）的推理吞吐量基准值约为 150 tokens/s [待核验]

## Corrected Claim

Qwen3-27B 在 BF16 精度下，单卡（如 H100 80GB）的推理吞吐量基准值约为 150 tokens/s（需进一步验证具体硬件与模型版本的匹配性）

## Evidence

[质询]来源[1]讨论的是 Qwen3.8-27B 在 L20 显卡上的表现，且文中提到对比对象速度超过 100 token/s，并未提供 Qwen3-27B 在 H100 80GB 上达到 150 tokens/s 的直接数据；不同硬件（L20 vs H100）和不同版本（Qwen3.8 vs Qwen3）导致数值不可直接迁移，存在口径混淆风险。 | 来源[1]主题相关但硬件和模型版本不完全匹配，未直接支持 H100 上 150 tokens/s 的具体数值，仅能作为间接参考；经验事实缺乏直接来源支持。

## Search Query

Qwen3-27B H100 inference throughput tokens per second

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072597504793880030&rut=304ab9b1949db5d068e5f24670c8b7c3dcf1028c44ee8d381a92e4513f6bc363', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 BF16、FP8、MTP、单卡表现，以及与 Qwen3.6 MoE 的差距'}
