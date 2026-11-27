# N590: Apple M2 Ultra 在 32K 上下文、INT4 量化 + INT8 KV Cache（单请求 KV Cache 4GB）下，剩余 178.5GB 显

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N204, N205, N206

## Claim

Apple M2 Ultra 在 32K 上下文、INT4 量化 + INT8 KV Cache（单请求 KV Cache 4GB）下，剩余 178.5GB 显存可支持 44 个并发请求（178.5GB / 4GB per req），此工作点以最小化 KV Cache 占用为目标，但需验证 INT8 KV Cache 对 Qwen3-27B 的精度损失是否可接受（通常 <0.5% MMLU 损失）。

## Corrected Claim

Apple M2 Ultra 在 32K 上下文、INT4 量化 + INT8 KV Cache（单请求 KV Cache 4GB）下，剩余 178.5GB 显存可支持 44 个并发请求（178.5GB / 4GB per req），此工作点以最小化 KV Cache 占用为目标，但需验证 INT8 KV Cache 对 Qwen3-27B 的精度损失是否可接受（通常 <0.5% MMLU 损失）。

## Evidence

先验知识/题面给定，逻辑校验通过：178.5GB / 4GB = 44.375，取整为44个并发请求，算术正确；INT8 KV Cache精度损失通常较低，符合工程常识。
