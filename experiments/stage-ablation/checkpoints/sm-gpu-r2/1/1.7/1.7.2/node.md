# N93: Qwen3-27B 在 W4 (INT4/AWQ/GPTQ) 精度下的权重文件大小为 13.5 GB (27B * 0.5 bytes)，相比 BF16 节省 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B 在 W4 (INT4/AWQ/GPTQ) 精度下的权重文件大小为 13.5 GB (27B * 0.5 bytes)，相比 BF16 节省 75% 权重显存；若 KV Cache 同步量化为 FP8，则总显存占用约为 13.5 GB + (32K * KV_FP8_size)，需计算具体 KV 节省值。

## Corrected Claim

Qwen3-27B 在 W4 (INT4/AWQ/GPTQ) 精度下的权重文件大小为 13.5 GB (27B * 0.5 bytes)，相比 BF16 节省 75% 权重显存；若 KV Cache 同步量化为 FP8，则总显存占用约为 13.5 GB + (32K * KV_FP8_size)，需计算具体 KV 节省值。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT4下每参数0.5字节，27e9 * 0.5 = 13.5e9 bytes = 13.5 GB，计算正确；BF16为2字节/参数，INT4为0.5字节/参数，节省(2-0.5)/2 = 75%，逻辑自洽。
