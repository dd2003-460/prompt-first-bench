# N42: KV Cache 的字节精度（bytes_per_element）取决于推理时的精度选择：BF16 为 2 字节，FP8 为 1 字节，INT8 为 1 字节，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

KV Cache 的字节精度（bytes_per_element）取决于推理时的精度选择：BF16 为 2 字节，FP8 为 1 字节，INT8 为 1 字节，W4 权重但 KV 通常保持 BF16/FP16 为 2 字节，此参数直接影响 KV Cache 总量。

## Corrected Claim

KV Cache 的字节精度（bytes_per_element）取决于推理时的精度选择：BF16 为 2 字节，FP8 为 1 字节，INT8 为 1 字节，W4 权重但 KV 通常保持 BF16/FP16 为 2 字节，此参数直接影响 KV Cache 总量。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16/FP16为16位（2字节），FP8/INT8为8位（1字节）符合数据格式定义；KV Cache精度通常独立于权重量化精度（W4权重下KV仍保持高精度）符合主流推理框架（如vLLM, TensorRT-LLM）的工程实践。
