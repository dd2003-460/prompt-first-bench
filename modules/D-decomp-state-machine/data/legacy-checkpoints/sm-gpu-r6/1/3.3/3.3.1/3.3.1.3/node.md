# N151: 工作点3 (Apple Silicon 统一内存)：Mac Studio M2 Ultra 192GB。BF16 权重 55.6GB + KV Cache 4.

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

工作点3 (Apple Silicon 统一内存)：Mac Studio M2 Ultra 192GB。BF16 权重 55.6GB + KV Cache 4.0GB + 激活/开销 2.25GB = 61.85GB < 192GB。剩余 130.15GB 显存极大，但受限于 800GB/s 内存带宽，吞吐上限低 (~13-57 tokens/s，存在矛盾需修正)，适合低延迟、长上下文、低吞吐场景。

## Corrected Claim

工作点3 (Apple Silicon 统一内存)：Mac Studio M2 Ultra 192GB。BF16 权重 55.6GB + KV Cache 4.0GB + 激活/开销 2.25GB = 61.85GB < 192GB。剩余 130.15GB 显存极大，但受限于 800GB/s 内存带宽，吞吐上限受模型规模影响显著（通常低于同显存GPU方案），适合低延迟、长上下文、低吞吐场景。

## Evidence

[质询]陈述中明确包含‘存在矛盾需修正’的自我否定表述，且吞吐范围（13-57 tokens/s）跨度极大，缺乏具体模型规模（如参数量）作为推导前提，导致数值结论不严谨。 | 先验知识/题面给定，逻辑校验通过：内存占用计算（55.6+4.0+2.25=61.85GB）及剩余空间（192-61.85=130.15GB）算术正确；M2 Ultra 800GB/s 带宽符合硬件规格；但吞吐数值因缺乏模型参数假设而存在不确定性，且原文自述有矛盾，故降级。
