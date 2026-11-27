# N149: Qwen3-27B在INT8量化（AWQ）下HumanEval Pass@1得分约为69%，BF16基准得分约为72%，绝对损失3个百分点。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Qwen3-27B在INT8量化（AWQ）下HumanEval Pass@1得分约为69%，BF16基准得分约为72%，绝对损失3个百分点。

## Corrected Claim

Qwen3-27B在INT8量化（AWQ）下HumanEval Pass@1得分相比BF16基准有轻微下降，具体数值需参考官方技术报告或详细评测数据。

## Evidence

[质询]具体数值（69%、72%、3个百分点）属于经验事实，参考来源仅定性描述8位量化“基本保持无损性能”，未提供具体基准测试数据，无法验证具体数值量级及绝对损失幅度。 | 来源[1]定性支持8位量化性能损失小，但未提供具体数值支持；该事实为经验数据，逻辑自洽但缺直接来源支持，依据经验事实排除条款降级。

## Search Query

Qwen3-27B INT8 AWQ HumanEval Pass@1 benchmark score

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1904196249697101553&rut=d839ffe9950b2a267e46796011c6380a31f26a29f2576f2456d77d6a8e647b8b', 'type': 'ddg', 'title': 'Qwen3量化技术深度解析：性能极限与挑战 - 知乎'}
