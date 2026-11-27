# N67: A100 40GB 在 FP8 精度下运行 8K 上下文时的总显存占用为 40.82 GB（权重 27GB + KV Cache 13.82GB），超出 40G

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

A100 40GB 在 FP8 精度下运行 8K 上下文时的总显存占用为 40.82 GB（权重 27GB + KV Cache 13.82GB），超出 40GB 显存限制，需使用 KV Cache 量化（如 INT8）或限制上下文至 6K 以下。

## Corrected Claim

以Llama-2-13B为例，若权重以FP16存储（约27GB）且KV Cache在8K上下文下占用约13.82GB，总显存约40.82GB，超出A100 40GB限制，需量化或限制上下文。

## Evidence

[质询]数值量级与具体参数依赖性强：27GB权重通常对应约13B-14B参数的FP16模型（如Llama-2-13B），而13.82GB的KV Cache在8K上下文下隐含了特定的层数、头数和隐藏维度假设。若模型规模不同（如7B或70B），权重和KV Cache数值将发生显著变化，导致总显存占用结论失效。此外，FP8精度下权重通常减半（约13-14GB），此处27GB权重暗示可能仍使用FP16/BF16存储权重，仅KV Cache或计算使用FP8，存在精度口径混淆的可能。 | source=knowledge，逻辑上27+13.82=40.82>40，溢出结论自洽；但具体数值（27GB权重、13.82GB KV）为经验事实，缺乏通用性，且无外部来源支持特定模型配置，故降级。
