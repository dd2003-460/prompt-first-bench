# N23: BF16 精度下 Qwen3-27B 的困惑度（Perplexity）基准为 8.2 [待核验]，这是评估量化质量损失的基准值。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

BF16 精度下 Qwen3-27B 的困惑度（Perplexity）基准为 8.2 [待核验]，这是评估量化质量损失的基准值。

## Corrected Claim

BF16 精度下 Qwen3.8-27B（或 Qwen3-27B，视具体版本定义而定）的困惑度基准约为 8.2，这是评估量化质量损失的基准值。

## Evidence

[质询]来源标题及摘要中明确提及的模型版本为 'Qwen3.8-27B'，而待核验事实节点声称的是 'Qwen3-27B'。虽然两者可能指代同一系列或存在版本混淆，但具体版本号不一致，且来源摘要未直接给出 8.2 这一具体困惑度数值，仅描述了测试背景。 | 来源 [1] 主题相关（Qwen3 系列 27B 模型在 BF16 下的性能测试），但标题版本号为 Qwen3.8-27B 而非 Qwen3-27B，且摘要未直接提供 8.2 的困惑度数值，属于间接支持且存在版本标识差异，无法完全排除版本混淆或数值误差，故降级。

## Search Query

Qwen3-27B perplexity BF16 benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072597504793880030&rut=2ee4b10bd19be2fffacef0cfaa6b2bb680098ec8c3a715ff670656c64b2e6f68', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 BF16、FP8、MTP、单卡表现，以及与 Qwen3.6 MoE 的差距'}
