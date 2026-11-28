# N15: 在NVFP4量化与TP=4配置下，Qwen3.8-27B的单token生成延迟 T_gen 可通过公式 T_gen = T_prefill / n_tokens

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

在NVFP4量化与TP=4配置下，Qwen3.8-27B的单token生成延迟 T_gen 可通过公式 T_gen = T_prefill / n_tokens + T_decode 计算，其中 T_prefill 为预填充阶段耗时，T_decode 为解码阶段每token耗时

## Corrected Claim

在NVFP4量化与TP=4配置下，Qwen3.8-27B的总推理延迟 T_total 可通过公式 T_total = T_prefill + n_tokens * T_decode 计算，其中 T_prefill 为预填充阶段耗时，T_decode 为解码阶段每token耗时。

## Evidence

[质询]公式逻辑不自洽：T_gen 通常指单 token 生成延迟（即 T_decode），而公式右侧包含 T_prefill/n_tokens，这混淆了总推理时间（Total Latency）与单 token 生成延迟（Per-token Latency）的概念。若 T_gen 定义为单 token 延迟，则不应包含 prefill 部分；若定义为总延迟，则不应称为 'single token generation latency'。 | 逻辑校验发现概念混淆：单 token 生成延迟通常等同于解码阶段耗时，不包含预填充阶段的摊销成本。该公式描述的是平均总延迟或特定上下文下的总耗时，而非标准的单 token 生成延迟定义。
