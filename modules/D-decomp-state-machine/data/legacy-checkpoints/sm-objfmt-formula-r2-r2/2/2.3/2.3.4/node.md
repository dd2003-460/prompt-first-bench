# N76: INT8 KV Cache 在主流 GPU (RTX 4090/A100/H100) 上的支持状态：所有候选 GPU 均原生支持 INT8 整数运算及内存操作，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

INT8 KV Cache 在主流 GPU (RTX 4090/A100/H100) 上的支持状态：所有候选 GPU 均原生支持 INT8 整数运算及内存操作，INT8 KV Cache 可将显存占用缩减至 BF16 的 50%，且无需 FP8 特有的硬件单元。

## Corrected Claim

INT8 KV Cache 在主流 GPU (RTX 4090/A100/H100) 上的支持状态：所有候选 GPU 均原生支持 INT8 整数运算及内存操作，INT8 KV Cache 可将显存占用缩减至 BF16 的 50%，且无需 FP8 特有的硬件单元。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8位宽为BF16的一半，显存占用缩减50%符合数学逻辑；主流GPU（Ampere/Hopper架构）均原生支持INT8运算，无需FP8专用硬件单元，陈述准确。

## Search Query

INT8 KV cache support RTX 4090 A100 H100 vLLM implementation
