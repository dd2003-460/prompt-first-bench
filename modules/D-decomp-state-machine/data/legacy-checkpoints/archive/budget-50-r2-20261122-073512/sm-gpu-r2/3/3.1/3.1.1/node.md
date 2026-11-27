# N113: Qwen3-27B 在 BF16 精度下的基准困惑度 (Perplexity) 在 WikiText-2 数据集上约为 3.5-4.2，在 C4 数据集上约为 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

Qwen3-27B 在 BF16 精度下的基准困惑度 (Perplexity) 在 WikiText-2 数据集上约为 3.5-4.2，在 C4 数据集上约为 4.8-5.5，需通过 HuggingFace evaluate 库实测获取具体值。

## Corrected Claim

Qwen3.8-27B 在 BF16 精度下的基准困惑度 (Perplexity) 在 WikiText-2 和 C4 数据集上的具体数值需通过 HuggingFace evaluate 库实测获取，参考来源未直接提供确切数值范围。

## Evidence

[质询]参考来源中提到的模型名称为 'Qwen3.8-27B' 或 'Qwen3.8 27B'，与陈述中的 'Qwen3-27B' 存在版本/命名不一致（可能是笔误或不同版本），且来源摘要中未直接提供 WikiText-2 和 C4 的具体困惑度数值，仅提及综合评测得分或定性描述，无法直接验证具体数值范围。 | 来源 [1][2][3] 均涉及 Qwen3.8-27B 的精度测试，但摘要中未直接给出 WikiText-2 和 C4 的困惑度具体数值，仅间接支持该模型存在 BF16 精度下的性能评估，且模型名称存在细微差异，故降级为定性表述。

## Search Query

Qwen3-27B BF16 perplexity WikiText-2 C4 benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32285357/article/details/167407252&rut=55d5703f7c362df424b0aed6772861c7ee7b32d63f5ece89533bbf5313a0ea39', 'type': 'ddg', 'title': 'Qwen3.8 27B本地办公实测：语义锚定、长上下文与FP16精度实战-CSDN博客'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=8d101b892bffb46b87003cdc8ef3a4d74fd9cad312ea5acd751e7c426bb2b5fe', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
- {'url': 'https://aishare.jizhiku.net/archives/52380&rut=3b97c9db4a92ffbac07c834f83d51a4650161cae52ace84d846e59bc5a5413a8', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：BF16/FP8/NVFP4 精度对比与部署优化指南 - AI技能智慧站'}
