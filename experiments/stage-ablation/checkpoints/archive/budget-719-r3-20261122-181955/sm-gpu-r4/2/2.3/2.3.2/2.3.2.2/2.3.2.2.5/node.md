# N698: ExLlama2 KV Cache 量化 (INT8) 的显存节省量：BF16 KV Cache 为 256KB/token (基于 N369 参数)，INT8

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N248, N249, N250

## Claim

ExLlama2 KV Cache 量化 (INT8) 的显存节省量：BF16 KV Cache 为 256KB/token (基于 N369 参数)，INT8 量化后为 128KB/token，节省 50%；在 32K 上下文中，单请求 KV Cache 从 8GB 降至 4GB，节省 4GB 显存，直接增加可用并发数或上下文长度上限。

## Corrected Claim

ExLlama2 KV Cache 量化 (INT8) 的显存节省量：BF16 KV Cache 为 256KB/token (基于 N369 参数)，INT8 量化后为 128KB/token，节省 50%；在 32K 上下文中，单请求 KV Cache 从 8GB 降至 4GB，节省 4GB 显存，直接增加可用并发数或上下文长度上限。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化将位宽从16位减半至8位，显存占用减半（256KB->128KB, 8GB->4GB）符合基本算术与硬件常识。

## Search Query

ExLlama2 KV cache quantization INT8 memory savings ratio
