# N327: RTX 5090 的 575W TDP 中，GPU 核心与 GDDR7 显存的实际动态功耗占比约为 85-90%，剩余 10-15% 为 PCB 供电损耗；在 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N107

## Claim

RTX 5090 的 575W TDP 中，GPU 核心与 GDDR7 显存的实际动态功耗占比约为 85-90%，剩余 10-15% 为 PCB 供电损耗；在 32K 上下文长文本推理负载下，由于 KV Cache 读取密集，显存功耗占比可能上升至 40-50%，导致实际墙插功耗接近 TDP 标称值的 95-100%，而短文本/低负载场景下仅为 60-70%。

## Corrected Claim

RTX 5090 的 575W TDP 中，GPU 核心与 GDDR7 显存构成主要功耗来源，PCB 供电损耗占比较小；在 32K 上下文长文本推理负载下，由于 KV Cache 读取密集，显存功耗占比显著上升，导致实际墙插功耗接近 TDP 标称值，而短文本/低负载场景下功耗明显低于 TDP。

## Evidence

[质询]具体数值占比（如85-90%、40-50%、95-100%）缺乏公开权威基准测试支持，属于高度推测性的工程估算，不同负载和驱动版本下波动较大，难以作为固定事实。 | 先验知识/题面给定，逻辑校验通过：GPU+显存为主要功耗源符合物理直觉，KV Cache密集读取增加显存功耗符合架构原理，但具体百分比为经验估算，无来源直接支持。

## Search Query

RTX 5090 GDDR7 power consumption breakdown inference load
