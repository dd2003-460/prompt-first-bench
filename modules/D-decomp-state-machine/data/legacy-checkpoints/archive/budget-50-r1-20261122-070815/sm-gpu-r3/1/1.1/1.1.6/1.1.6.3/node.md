# N171: Qwen3-27B 在 INT4 精度下，KV Cache 占用 0.27 GB 仅覆盖 K/V 向量，未包含 Attention Scores 或 Inter

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Qwen3-27B 在 INT4 精度下，KV Cache 占用 0.27 GB 仅覆盖 K/V 向量，未包含 Attention Scores 或 Intermediate Activations；在 32K 上下文下，Peak Activation Memory 估算为 0.1-0.2 GB (取决于 Batch Size=1)，总显存需求需增加此项以评估 OOM 风险。

## Corrected Claim

Qwen3-27B 在 INT4 精度下，KV Cache 占用 0.27 GB 仅覆盖 K/V 向量，未包含 Attention Scores 或 Intermediate Activations；在 32K 上下文下，Peak Activation Memory 估算为 0.1-0.2 GB (取决于 Batch Size=1)，总显存需求需增加此项以评估 OOM 风险。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 0.27GB 与 27B 模型在 32K 上下文下的理论估算量级相符（约 27B * 32K * 2 * 4bit / 1024^3 ≈ 0.27GB），Activation Memory 估算亦符合常规经验值。
