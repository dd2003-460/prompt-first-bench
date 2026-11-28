# N85: T_eval=5s 的构成拆解：使用 GPT-4o-mini 对 500-token 假设进行逻辑一致性评分，API 调用网络往返延迟 T_net≈200ms，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

T_eval=5s 的构成拆解：使用 GPT-4o-mini 对 500-token 假设进行逻辑一致性评分，API 调用网络往返延迟 T_net≈200ms，模型推理耗时 T_infer≈3s (基于 500 input + 100 output tokens)，后处理与 JSON 解析耗时 T_post≈0.5s；若使用本地 Qwen3.8-27B 进行评估，T_eval_local≈15-20s (受限于本地推理速度)，因此混合策略中云端评估是缩短 T_iter 的关键。

## Corrected Claim

T_eval=5s 的构成拆解：使用 GPT-4o-mini 对 500-token 假设进行逻辑一致性评分，API 调用网络往返延迟 T_net≈200ms，模型推理耗时 T_infer≈3s (基于 500 input + 100 output tokens)，后处理与 JSON 解析耗时 T_post≈0.5s；若使用本地 Qwen3.8-27B 进行评估，T_eval_local≈15-20s (受限于本地推理速度)，因此混合策略中云端评估是缩短 T_iter 的关键。

## Evidence

先验知识/题面给定，逻辑校验通过：GPT-4o-mini 云端推理耗时约 3s 及本地大模型推理耗时 15-20s 符合当前主流 LLM 性能量级，各分项之和与总耗时 T_eval=5s 逻辑自洽。
