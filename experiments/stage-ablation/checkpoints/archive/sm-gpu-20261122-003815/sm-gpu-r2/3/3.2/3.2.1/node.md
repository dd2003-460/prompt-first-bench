# N110: Qwen3-27B 在 BF16 精度下的基准测试分数：MMLU, GSM8K, HumanEval 的具体数值，作为精度对比的基线 (Baseline)

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 BF16 精度下的基准测试分数：MMLU, GSM8K, HumanEval 的具体数值，作为精度对比的基线 (Baseline)

## Corrected Claim

Qwen3系列中不存在27B参数规模的模型（常见为32B或14B等）。若指Qwen3-32B，需查阅官方技术报告获取BF16精度下的MMLU、GSM8K、HumanEval具体分数作为基线。

## Evidence

[质询]参考来源[1]讨论的是'Qwen3.8-27B'（疑似笔误或非标准版本号，通常应为Qwen3-27B或Qwen2.5-32B等，且'3.8'版本不存在于主流发布序列中，更可能是Qwen3-235B-A22B或Qwen3-32B的误写，或者指代Qwen3系列某特定量化版本），且摘要仅提及'550题基准平均分差'，未提供MMLU、GSM8K、HumanEval在BF16精度下的具体数值。此外，'Qwen3-27B'这一具体型号在官方发布中并不存在（Qwen3系列有0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B, 235B-A22B等，没有27B），因此该事实节点的前提（存在Qwen3-27B）本身存疑，且来源未提供所需的具体基准分数。 | 来源[1]主题相关但内容不匹配：未提供BF16基线分数，且模型名称'Qwen3.8-27B'与'Qwen3-27B'存在版本/型号疑点（Qwen3无27B规格），无法支持具体数值。

## Search Query

Qwen3-27B official benchmark scores MMLU GSM8K HumanEval BF16

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073832437491287186&rut=cfb80a25d52d5727626a2baec0302714755cfb148f0352ba41e97b60a48378dd', 'type': 'ddg', 'title': 'qwen3.8-27b量化模型实测对比情况 - 知乎'}
