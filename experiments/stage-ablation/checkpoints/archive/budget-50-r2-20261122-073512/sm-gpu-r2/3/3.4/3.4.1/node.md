# N126: Qwen3-27B 在 BF16 基准下于 MMLU 数据集上的具体准确率数值 (Baseline_Acc_BF16_MMLU)，作为计算 NVFP4/W4 下

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 BF16 基准下于 MMLU 数据集上的具体准确率数值 (Baseline_Acc_BF16_MMLU)，作为计算 NVFP4/W4 下降幅度的分母。

## Corrected Claim

Qwen3-27B 在 BF16 基准下于 MMLU 数据集上的具体准确率数值需查阅官方技术报告或权威基准测试平台，当前参考来源未提供该特定版本及精度下的确切数值。

## Evidence

[质询]参考来源中提到的模型版本（Qwen3.8-27B, Qwen3.6-27B）与事实节点中的 Qwen3-27B 存在版本不一致，且来源主要讨论 GGUF 量化或吞吐量，未直接提供 BF16 基准下 MMLU 的具体准确率数值，存在口径混淆和来源不匹配的风险。 | 来源 [3] 提及了 MMLU 评测但针对的是 Qwen3.8-27B-Uncensored-GGUF，来源 [2] 针对 Qwen3.6-27B 的吞吐量，均无 Qwen3-27B BF16 MMLU 具体数值支持，属于经验事实且缺直接来源支持。

## Search Query

Qwen3-27B MMLU benchmark accuracy BF16

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00070/article/details/165113753&rut=39a3466a07ed726e2dd3b984cc26cd4ca1dd23e953e79e35e01d3f654669e747', 'type': 'ddg', 'title': '655 万下载的 Qwen3.8-27B 登顶榜单背后，真正引擎是 24 个 GGUF 量化档位覆盖全部硬件-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=7aae2ac515b2d8496787d3262e190159eac55c7fb3ba5e9d4de1f8edb620e8de', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
- {'url': 'https://blog.csdn.net/gitblog_00688/article/details/152594884&rut=2ea9d2926423814f0c72df18929bb87fe87fd51d21ec45624adbbec869aadb02', 'type': 'ddg', 'title': '数据说话：Qwen3.8-27B-Uncensored-GGUF 基准评测全解读（MMLU、GSM8K 与安全测试）'}
