# N297: FP8 精度下 KV Cache 占用量：2 * 64 * 10 * 128 * 32768 * 1 byte = 5.37 GB，相比 BF16 节省 50%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104, N105, N106

## Claim

FP8 精度下 KV Cache 占用量：2 * 64 * 10 * 128 * 32768 * 1 byte = 5.37 GB，相比 BF16 节省 50% 显存，但需推理框架支持 FP8 KV Cache (如 vLLM 0.6+)

## Corrected Claim

FP8 精度下 KV Cache 占用量：2 * 64 * 10 * 128 * 32768 * 1 byte = 5.37 GB，相比 BF16 节省 50% 显存，但需推理框架支持 FP8 KV Cache (如 vLLM 0.6+)

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 2*64*10*128*32768*1 = 5,368,709,120 bytes ≈ 5.37 GB (GiB)，量级正确；FP8 (1字节) 相比 BF16 (2字节) 节省 50% 显存符合定义；vLLM 0.6+ 支持 FP8 KV Cache 为已知工程事实。

## Search Query

vLLM FP8 KV cache support Qwen3
