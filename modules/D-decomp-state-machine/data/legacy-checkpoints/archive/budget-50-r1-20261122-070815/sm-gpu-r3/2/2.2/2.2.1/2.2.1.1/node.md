# N215: Qwen3-27B 在 FP8 精度（E4M3 格式，用于权重和激活）下，MMLU 基准测试的具体得分，需区分是 FP8 权重+BF16 激活还是全 FP8 推

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N58

## Claim

Qwen3-27B 在 FP8 精度（E4M3 格式，用于权重和激活）下，MMLU 基准测试的具体得分，需区分是 FP8 权重+BF16 激活还是全 FP8 推理，不同配置下精度损失不同

## Corrected Claim

Qwen3-27B 在 FP8 精度（E4M3 格式）下的 MMLU 基准测试得分需根据具体推理配置（如 FP8 权重+BF16 激活或全 FP8 推理）进行区分，不同配置下精度损失存在差异，具体数值需查阅官方技术报告或权威评测数据。

## Evidence

[质询]该陈述包含具体的经验事实（特定模型在特定精度下的基准测试得分），且未提供具体数值，仅描述了需区分的配置情况。由于缺乏具体数值，无法验证其准确性，且属于经验事实，不能仅凭逻辑自洽判定为 verified。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B FP8 MMLU score E4M3
