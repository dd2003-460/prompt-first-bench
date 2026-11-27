# N136: RTX 4080 Super 的显存带宽为 736 GB/s，若强行在短上下文（如 4K）下运行 INT4 模型，理论 Decode 吞吐上限约为 736 / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

RTX 4080 Super 的显存带宽为 736 GB/s，若强行在短上下文（如 4K）下运行 INT4 模型，理论 Decode 吞吐上限约为 736 / (13.5 + 1.1) ≈ 50 tokens/s（假设 KV Cache 1.1GB），但其性价比低于 RTX 4090（45.5 tokens/s @ 32K），因为 4080 Super 无法支持题目要求的 32K 上下文，故在本题约束下被排除。

## Corrected Claim

RTX 4080 Super 的显存带宽为 736 GB/s，若强行在短上下文（如 4K）下运行 INT4 模型，理论 Decode 吞吐上限约为 736 / (13.5 + 1.1) ≈ 50 tokens/s（假设 KV Cache 1.1GB），但其性价比低于 RTX 4090（45.5 tokens/s @ 32K），因为 4080 Super 无法支持题目要求的 32K 上下文，故在本题约束下被排除。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4080 Super 显存带宽 736 GB/s 符合规格，INT4 模型权重约 13.5GB 与 KV Cache 1.1GB 的假设下，736/(13.5+1.1)≈50 tokens/s 计算正确；4090 在 32K 上下文下因 KV Cache 增大导致吞吐下降至 45.5 tokens/s 符合内存带宽瓶颈逻辑；4080 Super 16GB 显存难以支持 32K 长上下文（KV Cache 占用大）故被排除，逻辑自洽。
