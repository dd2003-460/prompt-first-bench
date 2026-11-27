# N571: Mac Studio (M2/M3 Ultra) 运行 Qwen3-27B 时的实际内存带宽利用率 (Bandwidth_Efficiency) 约为 0.85

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N238, N239, N240

## Claim

Mac Studio (M2/M3 Ultra) 运行 Qwen3-27B 时的实际内存带宽利用率 (Bandwidth_Efficiency) 约为 0.85-0.90，导致有效吞吐为理论值的 85-90%；该效率主要受 Apple Metal 推理引擎在 LLM Decode 阶段的内存访问模式（非连续读取、小批量合并）及内存控制器仲裁延迟限制。

## Corrected Claim

Mac Studio (M2/M3 Ultra) 运行 Qwen3-27B 时受限于统一内存带宽，实际推理吞吐显著低于理论峰值，主要瓶颈在于内存带宽限制及 Apple Metal 引擎在 LLM Decode 阶段的调度效率，具体带宽利用率需实测确定。

## Evidence

[质询]具体数值区间（0.85-0.90）缺乏公开基准测试支持，且将效率归因于‘非连续读取’在LLM Decode阶段（通常为连续KV Cache读取）存在技术细节上的潜在混淆，实际瓶颈更多在于内存带宽绝对值限制而非访问模式导致的低效。 | 先验知识/题面给定，逻辑校验通过；但具体效率数值属于经验事实，无外部来源直接支持，故降级。

## Search Query

Mac Studio M2 Ultra LLM inference bandwidth efficiency llama.cpp metal
