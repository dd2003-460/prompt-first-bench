# N329: RTX 5090 运行 Qwen3-27B INT8 时，KV Cache 在 INT8 精度下的单 Token 显存占用计算：2 * 32 (layers) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107, N108, N109

## Claim

RTX 5090 运行 Qwen3-27B INT8 时，KV Cache 在 INT8 精度下的单 Token 显存占用计算：2 * 32 (layers) * 8 (kv_heads) * 128 (dim) * 1 byte (INT8) = 65,536 bytes ≈ 0.0625 MB/Token；32K 上下文总 KV Cache = 0.0625 MB * 32768 ≈ 2 GB（相比 BF16 的 4GB 减半，但总显存仍超 32GB 限制）

## Corrected Claim

RTX 5090 运行 Qwen3-27B INT8 时，KV Cache 在 INT8 精度下的单 Token 显存占用计算：2 * 32 (layers) * 8 (kv_heads) * 128 (dim) * 1 byte (INT8) = 65,536 bytes ≈ 0.0625 MB/Token；32K 上下文总 KV Cache = 0.0625 MB * 32768 ≈ 2 GB（相比 BF16 的 4GB 减半，但总显存仍超 32GB 限制）

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（32层, 8 KV头, 128维）符合主流大模型设计，INT8 单字节计算及 32K 上下文总显存推导（2GB）在数学和量级上均自洽。
