# N25: MTP 解码失败率分布：在数学证明与代码生成等高约束任务中，MTP 第 3-4 步的接受率可能低于 50%，导致回退惩罚显著，具体分布需 A/B 测试统计

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

MTP 解码失败率分布：在数学证明与代码生成等高约束任务中，MTP 第 3-4 步的接受率可能低于 50%，导致回退惩罚显著，具体分布需 A/B 测试统计

## Corrected Claim

在数学证明与代码生成等高约束任务中，MTP 后续步骤（如第 3-4 步）的接受率通常显著低于前序步骤，可能导致回退惩罚，具体分布需通过 A/B 测试统计确定。

## Evidence

[质询]陈述中关于“MTP 第 3-4 步接受率可能低于 50%”的具体数值阈值缺乏通用性，不同模型架构（如 EAGLE vs 原生 MTP）和任务难度下差异巨大，且参考来源中未提供该具体分布数据，属于未经证实的经验性断言。 | 来源 [2] 和 [3] 确认了 MTP 在代码/数学任务中的应用及接受率调参的重要性，但未提供具体的失败率分布数值；该陈述包含具体经验参数（<50%），属经验事实，逻辑自洽但缺直接来源支持，故降级。

## Search Query

speculative decoding rejection rate distribution high constraint tasks math code generation

## Retrieval Sources

- {'url': 'https://jwzheng96.github.io/sglang-learning/04-optimizations/02-speculative-decoding.html&rut=5f41f0be8825e6de7e3c00670d10a7f92edaae795827a026b4fa75d516181d24', 'type': 'ddg', 'title': '投机解码：EAGLE / MTP / n-gram 在 SGLang · SGLang 学习手册'}
- {'url': 'https://blog.csdn.net/gitblog_00371/article/details/155121043&rut=47ee879433d00b35bfbc66603debcd6449f860522b3326d3879ea5c311aef72d', 'type': 'ddg', 'title': 'Qwopus3.5-9B-Coder-MTP架构深度解析：多令牌预测技术如何改变AI推理-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00889/article/details/170355144&rut=862f6e48f0f4a2e94d73dbdc61d52f785a2013747fff78d122dc31441d357f61', 'type': 'ddg', 'title': '为什么 MTP 是 Kestrel-4B-Coder 的隐藏王牌？多 Token 预测投机解码原理与调参详解-CSDN博客'}
