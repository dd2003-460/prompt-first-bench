# N132: 修正 N62 中的解码延迟公式：vLLM 中 MTP (Multi-Token Prediction) 或投机解码的加速比并非简单的 1/(1+3α)，而是取决

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

修正 N62 中的解码延迟公式：vLLM 中 MTP (Multi-Token Prediction) 或投机解码的加速比并非简单的 1/(1+3α)，而是取决于 Draft 模型生成的 K 个 token 中有多少被 Target 模型接受。若平均接受率为 α，则每步实际生成的 token 数为 1 + α*K（K 为投机长度，此处 K=3 或 4），单 token 平均延迟 T_avg = T_target_step / (1 + α*K)。当 T_target_step=15ms, K=3, α=0.7 时，T_avg = 15 / (1 + 2.1) ≈ 4.84ms，而非 4.41ms。

## Corrected Claim

修正 N62 中的解码延迟公式：vLLM 中 MTP (Multi-Token Prediction) 或投机解码的加速比并非简单的 1/(1+3α)，而是取决于 Draft 模型生成的 K 个 token 中有多少被 Target 模型接受。若平均接受率为 α，则每步实际生成的 token 数为 1 + α*K（K 为投机长度，此处 K=3 或 4），单 token 平均延迟 T_avg = T_target_step / (1 + α*K)。当 T_target_step=15ms, K=3, α=0.7 时，T_avg = 15 / (1 + 2.1) ≈ 4.84ms，而非 4.41ms。

## Evidence

先验知识/题面给定，逻辑校验通过：投机解码加速比公式 T_avg = T_target / (1 + α*K) 符合标准定义，数值计算 15 / (1 + 0.7*3) = 15 / 3.1 ≈ 4.8387 正确，原公式 1/(1+3α) 确实忽略了 K 与 α 的乘积关系及基准延迟项。

## Search Query

speculative decoding average latency formula acceptance rate
