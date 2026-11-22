# N246: M3 Ultra 256GB 在 BF16 单卡推理（batch=1, seq=32K）下的实测有效带宽利用率约为 50-60%，受限于 Apple GPU 架

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88, N89, N90

## Claim

M3 Ultra 256GB 在 BF16 单卡推理（batch=1, seq=32K）下的实测有效带宽利用率约为 50-60%，受限于 Apple GPU 架构对大模型 KV Cache 访问的优化不足及内存控制器延迟，对应实测吞吐为 7.0-8.4 tokens/s。

## Corrected Claim

M3 Ultra 256GB 在 BF16 单卡推理（batch=1, seq=32K）下受限于 Apple GPU 架构对大模型 KV Cache 访问的优化不足及内存控制器延迟，实测有效带宽利用率通常低于理论峰值，具体吞吐数值需根据实际测试环境确定。

## Evidence

[质询]该陈述包含具体的实测性能数值（7.0-8.4 tokens/s）和带宽利用率（50-60%），属于经验事实。虽然逻辑上自洽（大模型推理受内存带宽限制，Apple GPU在长序列KV Cache访问上确实存在优化瓶颈），但缺乏直接来源支持具体数值，且不同测试环境、软件栈版本可能导致数值波动，无法排除其他可能性。 | 经验事实，逻辑自洽但缺来源支持。M3 Ultra 256GB 在 BF16 单卡推理长序列时受内存带宽限制是已知现象，但具体吞吐数值需实测验证，当前无可用外部证据直接确认该特定数值范围。

## Search Query

Apple M3 Ultra LLM inference throughput BF16 tokens/s
