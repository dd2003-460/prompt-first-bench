# N267: GSM8K基准测试的评分标准需明确：是否采用Pass@1、Pass@k或平均准确率；不同评分方式下INT8与BF16的相对损失幅度可能不同，需确认N115中-1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N115

## Claim

GSM8K基准测试的评分标准需明确：是否采用Pass@1、Pass@k或平均准确率；不同评分方式下INT8与BF16的相对损失幅度可能不同，需确认N115中-1.9%对应的具体评分协议

## Corrected Claim

GSM8K基准测试的评分标准（如Pass@1、Pass@k或平均准确率）会影响最终得分，在评估INT8与BF16的量化损失时，需明确并统一具体的评分协议以确保对比的有效性。

## Evidence

[质询]该陈述是一个关于实验方法论的假设性建议（即“需确认”评分协议），而非一个已证实的事实结论。参考来源仅介绍了GSM8K基准的基本构成和评测流程，并未提供INT8与BF16在Pass@1与Pass@k下具体损失幅度差异的实证数据，因此无法直接验证“不同评分方式下相对损失幅度可能不同”这一具体论断的数值真实性，仅能确认评分协议确实影响结果。 | 来源[1]和[3]确认了GSM8K评测涉及具体的评分规则和流程，逻辑上评分协议（如Pass@k vs Pass@1）确实会影响量化模型的最终得分表现，但来源未直接提供INT8/BF16在不同协议下的具体损失对比数据，属于间接支持。

## Search Query

GSM8K evaluation metric Pass@1 vs average accuracy LLM benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42609225/article/details/171092824&rut=e2ad67526cecb3c5aeff32b6bb553a2b79ebec90fb20616b82abe7b5dcf63f17', 'type': 'ddg', 'title': 'GSM8K 评测基准实战：用 TaoToken 统一 API 跑通大模型数学推理对比-CSDN博客'}
- {'url': 'https://blog.csdn.net/InitPulse/article/details/161077170&rut=aa66c2116f6acb9ebd490396256208df9edcbe0079582c3f374919a0f09e0785', 'type': 'ddg', 'title': 'Gsm8k基准测试全维度复现报告（仅限内部研究员使用的12项评估指标首次流出）-csdn博客'}
- {'url': 'https://akiyangdev.github.io/llm-inference-notes/articles/sglang/gsm8k-accuracy-debugging-from-200-to-full-evaluation/&rut=7e7af7008c66d6be1f9023c99f32a6177d7280aa6a4b36621dd321dae2eed14f', 'type': 'ddg', 'title': 'GSM8K 精度不达标怎么排查？从 200 题到全量评测 · AkiYang'}
