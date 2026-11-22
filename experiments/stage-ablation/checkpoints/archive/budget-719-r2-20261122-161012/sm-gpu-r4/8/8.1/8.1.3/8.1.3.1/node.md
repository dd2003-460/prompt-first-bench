# N669: Apple Silicon M2/M3 Ultra 的内存控制器仲裁延迟 (Arbitration Latency) 并非固定 0.5-1.0 ms/token

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N277, N278, N279

## Claim

Apple Silicon M2/M3 Ultra 的内存控制器仲裁延迟 (Arbitration Latency) 并非固定 0.5-1.0 ms/token，而是随并发内存请求队列深度动态变化；在 LLM Decode 这种单流高带宽访问模式下，实测附加延迟约为 0.1-0.3 ms/token，导致实际吞吐量折损系数为 0.95-0.97（而非 0.92），修正后理论峰值 13.7 tokens/s 的实际值约为 13.0-13.3 tokens/s。

## Corrected Claim

Apple Silicon M2/M3 Ultra 的内存控制器仲裁延迟随并发内存请求队列深度动态变化；在 LLM Decode 模式下，实测附加延迟及吞吐量折损系数需依据具体硬件版本和负载情况实测确定，理论峰值 13.7 tokens/s 的实际值会因内存仲裁开销而低于理论值。

## Evidence

[质询]该陈述包含具体的经验性数值（0.1-0.3 ms/token, 0.95-0.97 折损系数, 13.0-13.3 tokens/s），这些属于特定硬件架构下的实测性能参数，无法从第一性原理或数学公理严格推导得出，且缺乏公开权威基准测试数据的直接支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能参数非第一性原理可推导范畴）

## Search Query

Apple Silicon M2 Ultra memory controller arbitration latency LLM inference overhead tokens/s
