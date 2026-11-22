# N132: RTX 4080 Super 16GB 在运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，总需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

RTX 4080 Super 16GB 在运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，总需求 15.5GB + 激活值开销，极易因激活值峰值导致 OOM，需强制使用 INT8 KV Cache 或降低上下文长度至 16K 方可稳定运行，性价比因稳定性风险而降低

## Corrected Claim

RTX 4080 Super 16GB 在运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，总需求 15.5GB + 激活值开销，极易因激活值峰值导致 OOM，需强制使用 INT8 KV Cache 或降低上下文长度至 16K 方可稳定运行，性价比因稳定性风险而降低

## Evidence

先验知识/题面给定，逻辑校验通过：13.5GB模型+2.0GB KV Cache=15.5GB，加上激活值开销后接近16GB显存上限，存在OOM风险，建议INT8 KV或降低上下文长度符合工程实践。
