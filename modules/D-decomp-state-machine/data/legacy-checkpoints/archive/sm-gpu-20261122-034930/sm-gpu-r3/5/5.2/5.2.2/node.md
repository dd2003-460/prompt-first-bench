# N124: 量化损失工作点2（平衡/中显存）：INT8精度（GPTQ/AWQ）下Qwen3-27B的MMLU准确率损失约1-2% [待核验]，Perplexity增加约0.

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

量化损失工作点2（平衡/中显存）：INT8精度（GPTQ/AWQ）下Qwen3-27B的MMLU准确率损失约1-2% [待核验]，Perplexity增加约0.3-0.5%，显存需求27GB（权重），单卡RTX 4090 (24GB) 不足，需双卡或A100 40GB，质量损失在可接受范围内，适合通用对话任务。

## Corrected Claim

量化损失工作点2（平衡/中显存）：INT8精度（GPTQ/AWQ）下Qwen3-27B的MMLU准确率损失约1-2% [待核验]，Perplexity增加约0.3-0.5% [待核验]，权重显存需求约27GB，加上KV Cache和激活值后总显存需求超过24GB，单卡RTX 4090 (24GB) 不足，需双卡或A100 40GB，质量损失在可接受范围内，适合通用对话任务。

## Evidence

父节点级核验未通过：不完备（子节点完全偏离了父节点的核心主题。父节点明确讨论的是'INT8精度（GPTQ/AWQ）'下的量化损失、显存需求及硬件适配性；而两个子节点均讨论的是'BF16精度'下的性能与显存。虽然两者在逻辑上互不冲突（正交），但子节点未能覆盖父节点关于INT8量化效果、INT8显存占用（约27GB）以及针对INT8方案的硬件建议（如双卡4090或A100 40GB的可行性分析），导致分解内容缺失，无法支撑父节点结论。）

## Search Query

Qwen3-27B INT8 GPTQ AWQ MMLU accuracy loss perplexity degradation
