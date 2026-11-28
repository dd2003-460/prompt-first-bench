# N34: KV Cache 精度修正：题面声称使用 fp8 KV cache，但 N7 的计算使用了 2 bytes/token (FP16)。若实际为 FP8 (1 b

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

KV Cache 精度修正：题面声称使用 fp8 KV cache，但 N7 的计算使用了 2 bytes/token (FP16)。若实际为 FP8 (1 byte/token)，理论峰值应从 13.4 GB 降至 6.7 GB；若为 INT8 量化，同样为 6.7 GB。需确认 vLLM 配置中 dtype 是否真的生效为 fp8，以及 FlashAttention 在 V100 (CC 7.0) 上是否支持 fp8 加速或仅支持 fp16/bf16 回退。

## Corrected Claim

KV Cache 精度修正：题面声称使用 fp8 KV cache，但 N7 的计算使用了 2 bytes/token (FP16)。若实际为 FP8 (1 byte/token)，理论峰值应从 13.4 GB 降至 6.7 GB；若为 INT8 量化，同样为 6.7 GB。需确认 vLLM 配置中 dtype 是否真的生效为 fp8，以及 FlashAttention 在 V100 (CC 7.0) 上是否支持 fp8 加速或仅支持 fp16/bf16 回退。

## Evidence

[rework-angle r1] 来源 [1] 和 [2] 直接证实了 V100 (SM70) 架构下存在 FP8 KV-cache 的长上下文路径（FLASH_ATTN_V100），且逻辑上 FP8 (1 byte) 相比 FP16 (2 bytes) 内存减半（13.4GB -> 6.7GB）符合基本算术与存储原理。

## Search Query

vLLM V100 SM70 fp8 kv cache support

## Retrieval Sources

- {'url': 'https://github.com/zhinianqin/flash-attention-v100&rut=42f27e0fb147b4d08bd4d8d4e39a6f9759319cdad8d2ebb6f5be97194af0b387', 'type': 'ddg', 'title': 'GitHub - zhinianqin/flash-attention-v100: forked from vllm-project ...'}
- {'url': 'https://github.com/1CatAI/1Cat-vLLM&rut=e21f452280349e4ca8214b0017ee74bc012180a2a1b0964fdcc6381b4b2a0ab7', 'type': 'ddg', 'title': 'GitHub - 1CatAI/1Cat-vLLM: V100 / SM70-focused vLLM engineering fork ...'}
