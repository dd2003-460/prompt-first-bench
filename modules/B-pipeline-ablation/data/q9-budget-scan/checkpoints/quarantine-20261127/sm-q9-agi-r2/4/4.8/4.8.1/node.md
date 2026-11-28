# N86: 针对 Qwen3.8-27B 在科研任务上的 Logit 熵分布特征，P(token|context) < 0.7 的阈值导致假阳性率约为 15-20%，需通过

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

针对 Qwen3.8-27B 在科研任务上的 Logit 熵分布特征，P(token|context) < 0.7 的阈值导致假阳性率约为 15-20%，需通过校准集（Calibration Set）计算 ROC 曲线确定最优分割点，预计最优阈值应上调至 0.8-0.85 以平衡查全率与查准率。

## Corrected Claim

针对 Qwen3.8-27B 在科研任务上的 Logit 熵分布特征，建议通过校准集计算 ROC 曲线确定最优分割点以平衡查全率与查准率，具体阈值需根据实际数据分布进行实证测定。

## Evidence

[质询]该陈述包含具体的经验性数值（假阳性率15-20%、最优阈值0.8-0.85），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定数据集、评估指标和模型行为的经验统计结果。参考来源均未提供此类Logit熵分布的具体统计数据，因此无法验证其准确性，存在将特定实验结果泛化为通用规律的风险。 | 逻辑上，使用ROC曲线校准阈值以平衡查全率与查准率是标准的机器学习分类器调优方法，逻辑自洽；但参考来源[1][2][3]仅涉及Qwen3.8-27B的本地部署、显存优化及推理速度调优，完全未提及Logit熵分布、假阳性率或阈值校准的具体数值，属于经验事实且缺乏来源支持。

## Search Query

LLM logit probability threshold calibration hallucination detection ROC curve optimal cut-off

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29034963/article/details/165934934&rut=6c85451ef5a5fa23f922b22be8dc07d585dfa8b59865a556a42e2f4fc5571a41', 'type': 'ddg', 'title': '8G显存也能跑Qwen3.8 27B：本地部署踩坑与调参全记录-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29092579/article/details/166971367&rut=47c37a46a38eeb67e1dc64e59cfa88ab33040463d86dbbc3448e9e6b9abafd2d', 'type': 'ddg', 'title': 'Qwen3.8-27B本地部署实战：280+ tok/s生产力级推理指南-CSDN博客'}
- {'url': 'https://juejin.cn/post/7694474763449516074&rut=9a811b4fced0a14e53e327ba5c53504163e891a3750db09b32a3515dbb7f1865', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地推理实测：从 14 tok/s 到 159 tok/s 的投机解码调优解析 Qwen3.8- - 掘金'}
