# N183: Depth_CoT 的量化估算公式为 Depth_CoT = Σ(Step_Complexity_i)，其中 Step_Complexity_i 为第 i 步的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N65

## Claim

Depth_CoT 的量化估算公式为 Depth_CoT = Σ(Step_Complexity_i)，其中 Step_Complexity_i 为第 i 步的归一化复杂度评分（0-1），具体评分标准基于任务类型模板（如数学推导=0.8, 代码调试=0.6, 文献检索=0.3）；初始基准值需通过 10 个标准科研任务的 CoT 日志标注确定。

## Corrected Claim

Depth_CoT 是一种用于量化思维链深度的估算指标，通常定义为各步骤复杂度的加权和或总和，具体评分标准和基准值取决于特定的评估框架或研究设定。

## Evidence

[质询]该陈述包含具体的经验性参数（如数学推导=0.8, 代码调试=0.6, 文献检索=0.3）及特定的基准确定方法（10个标准科研任务），这些属于特定研究或框架的定义细节，无法从第一性原理推导，且参考来源中未包含这些具体数值和定义。 | 参考来源[1][2][3]主要讨论CoT机制、Latent Reasoning及推理范式对比，均未提及'Depth_CoT'这一特定量化指标的具体计算公式、归一化评分标准或基准值确定方法，属于经验事实且缺乏来源直接支持。

## Search Query

complexity scoring criteria for chain of thought steps in scientific reasoning tasks

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2507.02199&rut=cdb04cd7176a8034274c6298633a99c6045664d2197bd3498d91b05d3038817a', 'type': 'ddg', 'title': 'Latent Chain-of-Thought? Decoding the Depth-Recurrent Transformer'}
- {'url': 'https://zhuanlan.zhihu.com/p/2081046398942954725&rut=f2e22b83eebf518f9151971dbe515b2738497de4301ac8897c1aaad090860548', 'type': 'ddg', 'title': 'Test-Time Scaling 不止长 CoT：从 Loop Transformer 到 Latent Reasoning，计算到底搬去了 ...'}
- {'url': 'https://zhuanlan.zhihu.com/p/2014389672588097470&rut=a6b793ac69518a3030f03a1cf5fcd306dd57396ffc6c0cacd3b3db664600157e', 'type': 'ddg', 'title': 'CoT/ToT/ReAct 等 Reasoning 方法对比&实践 - 知乎'}
