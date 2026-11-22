# N298: NVFP4 (4-bit floating point) 格式仅保留 1 位指数和 1 位尾数，动态范围极窄（约 4 倍），无法有效表示 Attention L

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

NVFP4 (4-bit floating point) 格式仅保留 1 位指数和 1 位尾数，动态范围极窄（约 4 倍），无法有效表示 Attention Logits 的长尾分布，导致 Softmax 后的概率向量出现大量零值或饱和值，即『精度崩溃』

## Corrected Claim

NVFP4 (4-bit floating point) 格式由于位宽限制，动态范围极窄，难以有效表示 Attention Logits 的长尾分布，可能导致 Softmax 后的概率向量出现零值或饱和值，即‘精度崩溃’。

## Evidence

[质询]NVFP4 的具体位宽分配（1位指数+1位尾数）及由此推导出的动态范围（约4倍）属于特定硬件/格式的经验规格，且不同厂商或标准下的 FP4 变体（如 E2M1 vs E1M2）可能存在差异，仅凭逻辑无法确认该特定格式在 Attention Logits 场景下必然导致‘大量’零值或饱和值，存在过度概括风险。 | 先验知识/题面给定，逻辑校验通过：4位浮点格式确实动态范围极窄，难以覆盖 Logits 长尾分布，但具体位宽分配及‘大量’零值的程度为经验事实，缺乏外部来源直接支持，故降级。

## Search Query

NVFP4 4-bit attention logits quantization precision collapse softmax
