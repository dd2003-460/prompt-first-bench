# N125: BF16 精度下 Qwen3-27B 的纯权重文件大小 (Weight File Size) 精确计算为 27.8B * 2 bytes = 55.6 GB，此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

BF16 精度下 Qwen3-27B 的纯权重文件大小 (Weight File Size) 精确计算为 27.8B * 2 bytes = 55.6 GB，此数值未包含 KV Cache 或激活值 (Activations)。

## Corrected Claim

BF16 精度下 Qwen3-27B 的纯权重文件大小 (Weight File Size) 精确计算为 27.8B * 2 bytes = 55.6 GB，此数值未包含 KV Cache 或激活值 (Activations)。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16 为 16 位浮点格式（2 字节/参数），27.8B 参数 * 2 字节 = 55.6GB，计算准确且符合定义（仅权重，不含 KV Cache/激活值）。
