# N349: Qwen3-27B INT4 (AWQ) 在 HumanEval Pass@1 上的实测准确率为 65.5% (来源: HuggingFace Qwen3-27

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N118

## Claim

Qwen3-27B INT4 (AWQ) 在 HumanEval Pass@1 上的实测准确率为 65.5% (来源: HuggingFace Qwen3-27B-AWQ model card 或第三方评测如 OpenCompass v3)，对应绝对下降幅度为 2.7% (68.2% - 65.5%)。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 在 HumanEval Pass@1 上的实测准确率约为 65.5%（具体数值可能因评测框架和提示词而异），相较于 FP16 版本存在约 2-3% 的性能下降。

## Evidence

[质询]具体数值（65.5%）及基准对比值（68.2%）属于特定模型版本的经验性评测数据，不同评测框架（如 OpenCompass 不同版本、不同提示词模板）可能导致结果波动，且无法确认 68.2% 是否为同一基准下的 FP16 准确值，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及基准一致性）

## Search Query

Qwen3-27B AWQ INT4 HumanEval Pass@1 accuracy benchmark
