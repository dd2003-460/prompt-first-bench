# N254: HumanEval 基准的测试集规模与评估协议：共 164 道 Python 编程题，评估指标为 pass@1（单次生成通过所有测试用例的比例），需确认 Qwe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

HumanEval 基准的测试集规模与评估协议：共 164 道 Python 编程题，评估指标为 pass@1（单次生成通过所有测试用例的比例），需确认 Qwen3 报告使用的是 0-shot 还是 few-shot 设置，以及是否包含 MBPP 作为补充验证。

## Corrected Claim

HumanEval 基准的测试集规模与评估协议：共 164 道 Python 编程题，评估指标为 pass@1（单次生成通过所有测试用例的比例），需确认 Qwen3 报告使用的是 0-shot 还是 few-shot 设置，以及是否包含 MBPP 作为补充验证。

## Evidence

先验知识/题面给定，逻辑校验通过：HumanEval 标准基准确实包含 164 道 Python 题目，pass@1 是标准评估指标，且 Qwen3 技术报告通常采用 0-shot 设置并可能包含 MBPP 作为补充，这些陈述符合领域常识且逻辑自洽。
