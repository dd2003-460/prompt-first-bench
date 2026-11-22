# N147: vLLM 0.4.x+ 中 FP8 KV Cache 的内存节省因子为 2.0x (相比 BF16)，即 KV Cache 占用减半；INT8 KV Cache

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

vLLM 0.4.x+ 中 FP8 KV Cache 的内存节省因子为 2.0x (相比 BF16)，即 KV Cache 占用减半；INT8 KV Cache 节省因子为 1.0x (相比 BF16)，即无节省或仅微量节省 (取决于实现)，需确认 vLLM 版本是否支持 INT8 KV 或仅支持 FP8。

## Corrected Claim

vLLM 中 FP8 KV Cache 相比 BF16 通常可实现约 2.0x 内存节省；INT8 KV Cache 相比 BF16 通常也可实现约 2.0x 内存节省（具体取决于 vLLM 版本对 INT8 KV 的支持情况及实现细节，需查阅具体版本文档确认）。

## Evidence

[质询]该陈述包含具体的软件版本特性（vLLM 0.4.x+）和量化实现细节（INT8 KV Cache 支持情况），属于经验事实。检索无可用来源，无法验证 vLLM 具体版本对 INT8 KV 的支持状态及 FP8 的具体内存节省因子是否严格为 2.0x（通常 FP8 相比 BF16 确实是 2 倍，但 INT8 相比 BF16 也是 2 倍，除非 BF16 被错误地当作 8-bit 基准或 INT8 实现有额外开销，此处逻辑上 INT8 相比 BF16 应为 2x 节省而非 1x，陈述中 INT8 节省因子为 1.0x 即无节省的说法在常规量化逻辑下存疑，可能混淆了基准或实现细节）。 | 经验事实，逻辑自洽性存疑（INT8 相比 BF16 通常应有 2x 节省，陈述称 1.0x 无节省违背常规量化直觉，且无来源支持），缺来源支持。

## Search Query

vLLM FP8 KV cache memory savings factor INT8 support
