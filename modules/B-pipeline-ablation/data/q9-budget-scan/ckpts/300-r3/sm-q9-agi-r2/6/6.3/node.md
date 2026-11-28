# N30: 特定领域知识缺失率的估算方法：构建一个包含 100 个冷门科研问题的基准集，让 27b 模型在无检索（RAG off）条件下作答，由专家标注正确率。该正确率的补

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

特定领域知识缺失率的估算方法：构建一个包含 100 个冷门科研问题的基准集，让 27b 模型在无检索（RAG off）条件下作答，由专家标注正确率。该正确率的补集即为“知识缺失率”，用于确定 RAG 检索增强的必要性和检索库的覆盖广度下限

## Corrected Claim

特定领域知识缺失率可通过构建基准问题集并让模型在无检索条件下作答，由专家标注正确率后取其补集来估算，该方法可用于评估RAG检索增强的必要性。

## Evidence

父节点级核验通过：正交+完备+无冗余（四个子节点分别对应了基准集构建（领域分布）、数据质量控制（冷门度筛选）、实验执行协议（无检索约束）和评估指标定义（标注标准与计算公式）。它们分别解决了‘测什么’、‘怎么保证难度/有效性’、‘怎么控制变量’和‘怎么算结果’的问题，逻辑链条完整且互不重叠，无冗余。）

## Search Query

Open source LLM domain-specific knowledge gap benchmark evaluation methodology

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/872626365_120233365&rut=5e1fb6c024a9b28c50ffc911a661675e341fca87cd1a58b0e1b1ed2357620cd6', 'type': 'ddg', 'title': '预测模型缺失数据比例大于10%怎么办？来看Lancet子刊文章_研究_团队_方法'}
