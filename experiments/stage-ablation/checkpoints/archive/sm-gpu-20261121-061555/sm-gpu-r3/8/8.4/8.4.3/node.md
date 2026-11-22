# N359: FP8 计算瓶颈判定条件：当模型参数量 P 和序列长度 S 满足 FLOPs/P < Memory_Bandwidth/2（即算术强度低于硬件平衡点）时，推理为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

FP8 计算瓶颈判定条件：当模型参数量 P 和序列长度 S 满足 FLOPs/P < Memory_Bandwidth/2（即算术强度低于硬件平衡点）时，推理为内存带宽受限；否则为计算受限。Qwen3-27B 在 32K 上下文下的算术强度需具体计算以判断 RTX 5090 是否进入计算瓶颈区。

## Corrected Claim

FP8 计算瓶颈判定条件：当模型参数量 P 和序列长度 S 满足 FLOPs/P < Memory_Bandwidth/2（即算术强度低于硬件平衡点）时，推理为内存带宽受限；否则为计算受限。Qwen3-27B 在 32K 上下文下的算术强度需具体计算以判断 RTX 5090 是否进入计算瓶颈区。

## Evidence

先验知识/题面给定，逻辑校验通过：Roofline 模型中算术强度（FLOPs/P）与硬件平衡点（Memory_Bandwidth/2，假设 FP8 为 2 字节/参数）的比较是判定计算/内存瓶颈的标准方法，逻辑自洽且量纲正确。

## Search Query

LLM inference arithmetic intensity compute bound vs memory bound threshold
