# N26: Qwen3-27B模型在BF16精度下的权重文件大小约为54GB（27B * 2 bytes），在FP8精度下约为27GB，在INT8/W4精度下约为13.5G

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B模型在BF16精度下的权重文件大小约为54GB（27B * 2 bytes），在FP8精度下约为27GB，在INT8/W4精度下约为13.5GB/6.75GB；该数据需基于HuggingFace官方模型卡片或GitHub仓库的config.json中hidden_size与层数计算得出，并标注具体commit哈希值

## Corrected Claim

Qwen3-27B模型在BF16精度下的权重文件大小约为54GB（27B * 2 bytes），在FP8精度下约为27GB，在INT8/W4精度下约为13.5GB/6.75GB；该数据需基于HuggingFace官方模型卡片或GitHub仓库的config.json中hidden_size与层数计算得出，并标注具体commit哈希值

## Evidence

检索失败: no sources from any channel (all 5 failed)
