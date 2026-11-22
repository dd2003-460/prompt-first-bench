# N287: 若采用 INT4 量化 (Weights 13.5GB) 且 KV Cache 保持 BF16，RTX 4090 在 32K 上下文下每 token 读取量为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

若采用 INT4 量化 (Weights 13.5GB) 且 KV Cache 保持 BF16，RTX 4090 在 32K 上下文下每 token 读取量为 14.036 GB (13.5GB + 536.87MB)，理论 ITL 为 1 / (1008 / 14.036) ≈ 13.9 ms/token，此为单请求理论上限，实测需乘以 0.6-0.8 效率系数。

## Corrected Claim

若采用 INT4 量化 (Weights 13.5GB) 且 KV Cache 保持 BF16，RTX 4090 在 32K 上下文下每 token 读取量为 14.036 GB (13.5GB + 536.87MB)，理论 ITL 为 1 / (1008 / 14.036) ≈ 13.9 ms/token，此为单请求理论上限，实测需乘以 0.6-0.8 效率系数。

## Evidence

先验知识/题面给定，逻辑校验通过：INT4权重13.5GB与KV Cache 536.87MB相加得14.036GB，基于RTX 4090显存带宽1008GB/s计算理论延迟13.9ms/token，数值量级与逻辑自洽。

## Search Query

INT4 quantized LLM decode latency single request
