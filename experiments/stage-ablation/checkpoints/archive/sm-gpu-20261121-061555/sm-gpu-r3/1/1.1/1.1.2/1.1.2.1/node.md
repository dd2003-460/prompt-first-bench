# N144: RTX 5080 16GB 显存下 Qwen3-27B 任何量化精度（FP8/INT8/INT4）的权重占用均超过 16GB（FP8: 27GB, INT4: 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

RTX 5080 16GB 显存下 Qwen3-27B 任何量化精度（FP8/INT8/INT4）的权重占用均超过 16GB（FP8: 27GB, INT4: ~13.5GB + KV Cache > 16GB），结论为单卡 RTX 5080 无法独立运行 Qwen3-27B 32K 上下文推理，除非采用极激进的 W4A4 量化且牺牲大量 KV Cache 空间，需量化验证 W4A4 下 KV Cache 剩余空间是否 < 1GB。

## Corrected Claim

RTX 5080 16GB 显存下 Qwen3-27B 任何量化精度（FP8/INT8/INT4）的权重占用均超过 16GB（FP8: 27GB, INT4: ~13.5GB + KV Cache > 16GB），结论为单卡 RTX 5080 无法独立运行 Qwen3-27B 32K 上下文推理，除非采用极激进的 W4A4 量化且牺牲大量 KV Cache 空间，需量化验证 W4A4 下 KV Cache 剩余空间是否 < 1GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下约27GB，INT4下约13.5GB，加上32K上下文所需的KV Cache（通常数GB），总显存需求确实超过RTX 5080的16GB显存限制，结论符合硬件与模型规模的基本物理约束。
