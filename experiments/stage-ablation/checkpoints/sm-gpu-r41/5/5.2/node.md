# N80: Qwen3-27B W4 量化在 HumanEval 代码生成任务上的 Pass@1 准确率下降幅度，以及长上下文（32K）下的困惑度（Perplexity）增

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

Qwen3-27B W4 量化在 HumanEval 代码生成任务上的 Pass@1 准确率下降幅度，以及长上下文（32K）下的困惑度（Perplexity）增加比例，需对比 INT8 基线

## Corrected Claim

Qwen3-27B W4 量化在 HumanEval 代码生成任务上的 Pass@1 准确率及长上下文（32K）下的困惑度（Perplexity）相较于 INT8 基线存在性能下降，具体下降幅度需查阅官方技术报告或基准测试数据。

## Evidence

[质询]参考来源中未包含任何关于 Qwen3-27B W4 量化在 HumanEval 上的具体 Pass@1 下降幅度或 32K 长上下文困惑度增加比例的数值数据，属于缺乏直接证据支持的经验事实断言。 | 经验事实，逻辑自洽但缺来源支持（来源[2][3]仅涉及评测脚本，无具体量化性能数据；来源[1][4]无关）

## Search Query

Qwen3-27B W4 quantization HumanEval Pass@1 perplexity long context

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://github.com/evanzhangxin/qwen-human-eval&rut=e678d7a5374213caa768177104ee6445d5ffa8c7e74e557686dcb52f0a41ef04', 'type': 'ddg', 'title': 'GitHub - evanzhangxin/qwen-human-eval'}
- {'url': 'https://github.com/QwenLM/Qwen/blob/main/eval/evaluate_humaneval.py&rut=173591fd82fdedf17521e98c3867b07a10b4e5818a3ff60248f32e116bc527ef', 'type': 'ddg', 'title': 'Qwen/eval/evaluate_humaneval.py at main · QwenLM/Qwen'}
- {'url': 'https://ja.wikipedia.org/wiki/%E6%86%B2%E6%B3%95%E8%A8%98%E5%BF%B5%E6%97%A5_(%E6%97%A5%E6%9C%AC)', 'type': 'bing', 'title': '憲法記念日 (日本) - Wikipedia'}
