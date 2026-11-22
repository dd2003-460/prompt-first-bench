# N77: Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU 基准测试准确率及相对于 BF16 基线的绝对下降值（ΔMMLU）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU 基准测试准确率及相对于 BF16 基线的绝对下降值（ΔMMLU）

## Corrected Claim

Qwen3-27B（或Qwen3.8-27B）在FP8精度下的MMLU基准测试准确率及相对于BF16基线的绝对下降值需查阅完整测试报告以获取具体数值，当前摘要仅证实进行了相关调优测试。

## Evidence

[质询]参考来源[1]的标题和摘要中提到的模型名称为 'Qwen3.8-27B'，而待核验事实节点指定的是 'Qwen3-27B'。虽然两者可能指代同一系列或存在笔误，但名称不一致导致无法直接确认来源数据完全对应目标模型；此外，摘要仅提及速度提升，未直接展示 MMLU 准确率及 ΔMMLU 的具体数值，需依赖全文隐含信息或假设摘要未截断关键数据。 | 来源[1]主题相关（Qwen3系列27B模型FP8量化测试），但摘要未直接提供MMLU具体数值，且模型版本号存在细微差异（Qwen3.8 vs Qwen3），属于间接支持且存在不确定性，故降级。

## Search Query

Qwen3-27B FP8 MMLU accuracy benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073193935342679989&rut=12d9da5b2794c8e1125ad6c5f8ccd773e2e4ff77db623ff76f925ec6f08c10dd', 'type': 'ddg', 'title': '双 NVIDIA L20 上 Qwen3.8-27B-FP8 + MTP 调优测试报告'}
