# N105: 大语言模型推理负载下的平均功耗占比系数 $\alpha_{avg}$：在持续生成（Decode）阶段，GPU 功耗通常稳定在 TDP 的 70%-85% 区间，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

大语言模型推理负载下的平均功耗占比系数 $\alpha_{avg}$：在持续生成（Decode）阶段，GPU 功耗通常稳定在 TDP 的 70%-85% 区间，而非 60%，因为矩阵乘法是计算密集型且保持高频率；需实测或引用第三方功耗曲线 [search]

## Corrected Claim

在持续生成（Decode）阶段，由于计算密集性和高频率维持，GPU功耗通常显著高于空闲或低负载状态，具体占比（如70%-85%）需根据特定GPU型号和负载实测确定，而非固定为60%。

## Evidence

[质询]该陈述包含具体的经验数值区间（70%-85%），属于硬件功耗的经验事实，无法从第一性原理严格推导；且不同GPU型号、驱动版本及具体负载（如Batch Size、序列长度）下，Decode阶段的功耗占比波动较大，固定区间可能缺乏普适性。 | 逻辑上Decode阶段因矩阵乘法密集且显存带宽受限，GPU通常维持较高频率，功耗高于Prefill阶段是合理的；但参考来源[1][2]主要讨论推理加速算法（LayerSkip）和架构优化，未提供具体的GPU功耗百分比数据，属于经验事实且缺直接来源支持。

## Search Query

LLM inference GPU power consumption average vs TDP ratio decode phase

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2001667036116455469&rut=575b0d9619e608b2a8b7f413efdb7455fcfba31cff5dfb5bff71194e2d59c7a1', 'type': 'ddg', 'title': '论文导读 | 大模型推理能耗优化 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1919407528363668517&rut=15695c81eefa4e6a857d9dcf5bd8af3248b3f014f9e9066cb792eca2f02e9024', 'type': 'ddg', 'title': '万字长文!大模型 (Llm)推理优化技术总结（非常详细） - 知乎'}
