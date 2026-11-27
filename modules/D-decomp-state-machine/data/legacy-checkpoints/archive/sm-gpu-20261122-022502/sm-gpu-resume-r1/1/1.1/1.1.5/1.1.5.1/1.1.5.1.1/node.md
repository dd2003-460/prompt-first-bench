# N459: vLLM v0.4.0 FP8 KV Cache 启用条件：必须同时满足 (1) GPU 支持 FP8 Tensor Core (Compute Capabil

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

vLLM v0.4.0 FP8 KV Cache 启用条件：必须同时满足 (1) GPU 支持 FP8 Tensor Core (Compute Capability 8.9+，即 Ada/Hopper)，(2) 显式设置 --kv-cache-dtype fp8，(3) 模型支持 FP8 推理；RTX 4090 (Compute Capability 8.9) 满足硬件条件，但默认回退 BF16

## Corrected Claim

vLLM v0.4.0 FP8 KV Cache 启用条件：必须同时满足 (1) GPU 支持 FP8 Tensor Core (Compute Capability 8.9+，即 Ada/Hopper)，(2) 显式设置 --kv-cache-dtype fp8，(3) 模型支持 FP8 推理；RTX 4090 (Compute Capability 8.9) 满足硬件条件，但默认回退 BF16

## Evidence

先验知识/题面给定，逻辑校验通过
