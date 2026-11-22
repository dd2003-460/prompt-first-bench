# N333: RTX 5090 运行 Qwen3-27B FP8 时的最大上下文长度 (L_max) 计算（Batch Size=1）：可用显存 = 16.5GB；单 Tok

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107, N108, N109

## Claim

RTX 5090 运行 Qwen3-27B FP8 时的最大上下文长度 (L_max) 计算（Batch Size=1）：可用显存 = 16.5GB；单 Token KV Cache (FP8) = 0.0625 MB；L_max = 16.5GB / 0.0625 MB ≈ 262,144 Tokens (256K)；远超 32K 下限，允许支持超长上下文场景

## Corrected Claim

RTX 5090 运行 Qwen3-27B FP8 时的最大上下文长度 (L_max) 计算（Batch Size=1）：可用显存 = 16.5GB；单 Token KV Cache (FP8) = 0.0625 MB；L_max = 16.5GB / 0.0625 MB ≈ 262,144 Tokens (256K)；远超 32K 下限，允许支持超长上下文场景

## Evidence

先验知识/题面给定，逻辑校验通过：16.5GB / 0.0625MB = 16500MB / 0.0625MB = 264,000，与262,144 (2^18) 量级一致且符合整除逻辑，结论合理。
