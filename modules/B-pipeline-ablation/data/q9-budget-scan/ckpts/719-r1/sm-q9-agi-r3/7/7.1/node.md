# N86: Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 上的单步 AllReduce 通信开销时间为 12ms，占单步推理总时间 80ms 的

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 上的单步 AllReduce 通信开销时间为 12ms，占单步推理总时间 80ms 的 15%（计算依据：V100 NVLink 理论带宽 300GB/s，27B模型激活参数同步量估算为 30MB，双向通信耗时 2*30MB/300GB/s ≈ 0.2ms，加上序列化与同步锁开销，实测通常在 10-15ms 区间，需通过 vLLM profiling 工具 nsight systems 验证实际值）

## Corrected Claim

Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 上的单步 AllReduce 通信开销时间远低于 12ms（理论估算 <1ms），占单步推理总时间的比例极低；具体实测值需通过 vLLM profiling 工具 nsight systems 验证，且需确认模型版本及量化格式在 V100 上的兼容性。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 859)

## Search Query

vLLM TP4 V100 AllReduce latency profile Qwen27B NVFP4
