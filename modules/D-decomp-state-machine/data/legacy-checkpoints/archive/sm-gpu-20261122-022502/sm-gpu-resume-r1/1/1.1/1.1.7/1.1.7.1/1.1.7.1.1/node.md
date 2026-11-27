# N483: Qwen3-27B BF16 在 ARC-Challenge 上的基线准确率为 85.1%，该数值需通过检索 Qwen 官方技术报告或权威评测榜单（如 Open

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N149, N150, N151

## Claim

Qwen3-27B BF16 在 ARC-Challenge 上的基线准确率为 85.1%，该数值需通过检索 Qwen 官方技术报告或权威评测榜单（如 OpenCompass/LMSYS）确认，若官方未公布具体分数，则标记为 [待核验] 并采用社区复现均值

## Corrected Claim

Qwen3-27B BF16 在 ARC-Challenge 上的基线准确率需通过官方技术报告或权威榜单确认；现有来源[1]仅提供了 Qwen3.8-27B 在本地环境下的测试数据，不能直接作为 Qwen3-27B 的官方基线证据。

## Evidence

[质询]参考来源[1]明确标注为 'Qwen3.8-27B'，而待核验事实为 'Qwen3-27B'，模型版本号存在明显差异（3.8 vs 3），且来源为个人本地基准测试（Local Bench）而非官方技术报告或权威榜单，无法直接支持官方基线准确率这一经验事实。 | 经验事实，逻辑自洽但缺来源支持；来源[1]涉及不同版本号（Qwen3.8-27B）且为本地复现，非官方数据，无法直接验证 Qwen3-27B 的 85.1% 基线。

## Search Query

Qwen3-27B ARC-Challenge baseline accuracy BF16 official technical report

## Retrieval Sources

- {'url': 'https://github.com/Yunado/qwen3.8-27b-local-bench&rut=aa22bc0e31d12088fbd043e46d67852f2e43e00f5219190583a3a9462bc1dc4e', 'type': 'ddg', 'title': 'Qwen3.8-27B Local Bench — AIME 2026 & ARC-Challenge 500'}
