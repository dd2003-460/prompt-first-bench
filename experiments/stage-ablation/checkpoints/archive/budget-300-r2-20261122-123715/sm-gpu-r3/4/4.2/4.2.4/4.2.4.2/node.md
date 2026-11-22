# N306: RTX 4090 实测吞吐的置信区间：在 Qwen3-27B INT8 (AWQ) + 32K 上下文下，单卡 4090 的实测吞吐通常为 40-50 tok/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N90

## Claim

RTX 4090 实测吞吐的置信区间：在 Qwen3-27B INT8 (AWQ) + 32K 上下文下，单卡 4090 的实测吞吐通常为 40-50 tok/s (Decode 阶段)，但受 KV Cache 大小和并发数影响；若上下文缩短至 8K，吞吐可提升至 60-70 tok/s；需以 32K 为基准计算 TCO/Throughput，避免高估性价比

## Corrected Claim

RTX 4090 在 Qwen3-27B INT8 (AWQ) 下的实测吞吐受 KV Cache 大小和并发数显著影响：32K 上下文下 Decode 阶段吞吐通常低于 8K 上下文下的吞吐（具体数值需依据特定推理框架和硬件环境实测确定，常见范围可能在 40-70 tok/s 之间波动）；计算 TCO/Throughput 时应基于实际业务场景的上下文长度基准，避免使用非典型高吞吐数据高估性价比。

## Evidence

[质询]具体吞吐数值（40-50 tok/s 和 60-70 tok/s）属于高度依赖具体硬件配置、驱动版本、推理框架（如 vLLM/TensorRT-LLM）及量化实现细节的经验事实，且不同测试环境下的波动较大，缺乏通用标准值，存在以偏概全或特定环境数据泛化的风险。 | 经验事实，逻辑自洽（上下文越长KV Cache越大，显存带宽压力越大，吞吐下降符合物理直觉），但检索无可用来源支持具体数值，无法排除其他可能性。

## Search Query

RTX 4090 Qwen3 27B INT8 AWQ 32k context tokens per second benchmark
