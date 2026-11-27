# N168: Mac Studio M2 Ultra 的内存子系统架构：800 GB/s 带宽由 8 个 LPDDR5 通道共享，每个通道 100 GB/s；在 LLM 推理

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

Mac Studio M2 Ultra 的内存子系统架构：800 GB/s 带宽由 8 个 LPDDR5 通道共享，每个通道 100 GB/s；在 LLM 推理中，由于 KV Cache 和权重访问模式不同，实际有效带宽通常降至标称值的 85-90% (即 680-720 GB/s)，需引用 Apple 技术白皮书或第三方内存带宽测试 (如 Geekbench Memory Score) 修正

## Corrected Claim

Mac Studio M2 Ultra 的内存子系统架构：800 GB/s 带宽由 8 个 LPDDR5 通道共享，每个通道 100 GB/s；在 LLM 推理中，实际有效带宽受访问模式影响，通常低于标称值，具体效率需根据实际负载和测试数据（如 Geekbench 或特定推理框架基准）确定。

## Evidence

[质询]85-90% 的有效带宽效率是一个经验性统计值，并非物理定律或数学公理，无法从第一性原理严格推导；且不同 LLM 推理框架（如 vLLM, llama.cpp）及硬件微架构优化程度不同，该比例波动较大，缺乏通用性。 | source=knowledge，逻辑自洽（8*100=800 GB/s 符合 M2 Ultra 规格），但 85-90% 的效率系数属于经验事实，无来源直接支持且无法排除其他可能性，依据经验事实排除条款降级。

## Search Query

Apple M2 Ultra memory bandwidth efficiency LLM inference overhead LPDDR5
