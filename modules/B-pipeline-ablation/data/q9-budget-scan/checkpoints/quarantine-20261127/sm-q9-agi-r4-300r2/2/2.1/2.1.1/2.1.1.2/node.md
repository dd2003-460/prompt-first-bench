# N118: Action 字段解析鲁棒性：LLM 生成 JSON 格式 Action 的语法错误率 P_syntax_err 随模型规模减小而指数上升；对于 27B 模型，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

Action 字段解析鲁棒性：LLM 生成 JSON 格式 Action 的语法错误率 P_syntax_err 随模型规模减小而指数上升；对于 27B 模型，在无 Few-shot 示例情况下 P_syntax_err ≈ 5%-8%；引入 3-shot 示例后降至 <1%；解析失败需触发正则修复或重试机制，平均增加 0.5s 延迟

## Corrected Claim

Action 字段解析鲁棒性：LLM 生成 JSON 格式 Action 的语法错误率通常随模型规模减小而上升；引入 Few-shot 示例可显著降低错误率；解析失败需触发修复或重试机制，会增加额外延迟。

## Evidence

[质询]具体数值（27B模型5%-8%错误率、3-shot降至<1%、0.5s延迟）缺乏通用基准支持，不同模型架构、提示词工程及解码策略下差异巨大，属于特定实验条件下的经验数据而非普适规律。 | 来源[1]仅定性描述了LLM输出JSON易出错的现象及后果，未提供具体的错误率数值、模型规模对比或延迟数据，无法直接支持具体量化指标；该陈述包含具体经验参数，属经验事实，逻辑自洽但缺来源直接支持。

## Search Query

LLM JSON action generation syntax error rate 27B model few-shot

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2027807594228589148&rut=4594ccb27b645a6a6ab9a3f671c2c7493f5936b9f8ce60f665e6a8273000d780', 'type': 'ddg', 'title': '如何让llm稳定输出 Json 格式结果？ - 知乎'}
