# N587: 贝叶斯 A/B 测试在资源受限场景下的决策阈值设定：后验概率 P(B>A|data) > 0.95 时停止实验；相比频率派固定样本量设计，其平均试验轮次 ASN

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N209

## Claim

贝叶斯 A/B 测试在资源受限场景下的决策阈值设定：后验概率 P(B>A|data) > 0.95 时停止实验；相比频率派固定样本量设计，其平均试验轮次 ASN_bayes 通常比频率派少 15%-30%，具体数值取决于先验分布的集中度（如 Beta(1,1) vs Beta(5,5)）及效应量 δ 的大小。

## Corrected Claim

贝叶斯 A/B 测试在资源受限场景下常采用后验概率阈值（如 P(B>A|data) > 0.95）进行动态停止；相比频率派固定样本量设计，其平均试验轮次通常更少，具体节省比例取决于先验分布、效应量及停止规则，文献中常见报告范围为 15%-30% 或更高，但非恒定值。

## Evidence

[质询]具体数值范围（15%-30%）及特定先验分布（Beta(1,1) vs Beta(5,5)）的影响属于经验性统计结论，缺乏通用理论保证，且不同效应量和样本量下差异波动极大，该具体区间可能过于绝对或仅适用于特定模拟场景。 | 逻辑自洽（贝叶斯序贯测试通常比固定样本量频率派测试更高效），但参考来源[1][2][3]仅涵盖频率派推断和基础A/B测试定义，未提供贝叶斯ASN对比的具体数值支持，属于经验事实且缺来源直接支持。

## Search Query

Bayesian A/B testing average sample number reduction compared to frequentist

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Frequentist_inference', 'type': 'wikipedia', 'title': 'Frequentist inference'}
- {'url': 'https://en.wikipedia.org/wiki/A%2FB_testing', 'type': 'wikipedia', 'title': 'A/B testing'}
- {'url': 'https://en.wikipedia.org/wiki/Student%27s_t-test', 'type': 'wikipedia', 'title': "Student's t-test"}
