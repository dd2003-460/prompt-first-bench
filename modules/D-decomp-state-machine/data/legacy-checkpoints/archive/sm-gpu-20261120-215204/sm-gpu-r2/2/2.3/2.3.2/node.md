# N74: AWQ-Int8 量化下 Qwen3-27B 在 GSM8K 数学推理任务上的准确率相对于 BF16 基线的下降幅度，需检索具体量化模型评测报告（预期 1-3%

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

AWQ-Int8 量化下 Qwen3-27B 在 GSM8K 数学推理任务上的准确率相对于 BF16 基线的下降幅度，需检索具体量化模型评测报告（预期 1-3% 相对误差）。

## Corrected Claim

AWQ-Int4 量化下 Qwen3.8-27B 在 GSM8K 数学推理任务上的准确率恢复率约为 97.7%（即相对 BF16 基线下降约 2.3%），AWQ-Int8 的下降幅度通常更小，但具体数值需检索对应评测报告。

## Evidence

[质询]参考来源均针对 AWQ-INT4 量化，而非 AWQ-Int8；且来源中提到的模型版本为 Qwen3.8-27B，与陈述中的 Qwen3-27B 存在版本差异，无法直接支持 Int8 的具体误差数值。 | 来源 [1] 和 [2] 提供了 AWQ-INT4 在 GSM8K 上的性能数据（恢复率 97.7% 或准确率 95.91），间接表明 AWQ 量化对数学推理影响较小，但缺乏 AWQ-Int8 的直接数据支持，且模型版本号不完全匹配。

## Search Query

Qwen3-27B AWQ Int8 GSM8K accuracy evaluation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00779/article/details/170347941&rut=073c426b4c3f37e9e93bbb98741c6bfe4464c57b047b0fdfd275a8f8df43406d', 'type': 'ddg', 'title': '量化会掉点吗？Qwen3.8-27B-AWQ-INT4-FP8KV全量评测：GSM8K 95.91与262K大海捞针9/'}
- {'url': 'https://blog.csdn.net/gitblog_00887/article/details/168443952&rut=c3b7b31e370c638c409246611c2c6dd79951dd8acab18a707e840823b6d8b7b5', 'type': 'ddg', 'title': 'Qwen3.8-27B-Quark-AWQ-INT4-W4A16基准实测：GSM8K恢复率97.7%，INT4量化真实损'}
- {'url': 'https://juejin.cn/post/7675595046833799177&rut=5336ec670df6f214bf2935b0e35a654430339c6be908efcfad242d2fd5e7f8c6', 'type': 'ddg', 'title': 'V100 单卡部署 Qwen3.8-27B（AWQ）到 vLLM 完整实战 - 掘金'}
