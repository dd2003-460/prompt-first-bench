# N282: Latency_overhead 的构成项：包括 CPU-GPU 数据拷贝时间（约 5-10 ms）、框架初始化开销（首次请求约 50-100 ms，后续请求 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

Latency_overhead 的构成项：包括 CPU-GPU 数据拷贝时间（约 5-10 ms）、框架初始化开销（首次请求约 50-100 ms，后续请求 <5 ms）、以及调度器延迟（约 1-2 ms），总开销在 32K 上下文下约为 10-110 ms，具体数值取决于推理框架（vLLM vs TGI）和是否使用连续批处理。

## Corrected Claim

Latency_overhead 的构成项通常包括 CPU-GPU 数据拷贝时间、框架初始化开销（首次请求较高，后续请求较低）以及调度器延迟。在 32K 上下文下，总开销的具体数值高度依赖于推理框架（如 vLLM 或 TGI）及是否启用连续批处理，不同配置下波动范围较大，需根据具体基准测试确定。

## Evidence

[质询]数值量级与具体参数缺乏来源支持，且不同框架（vLLM vs TGI）及批处理策略下的延迟差异极大，笼统给出固定区间（如5-10ms拷贝、1-2ms调度）可能掩盖了实际部署中的显著波动，属于经验事实而非第一性原理可推导结论。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LLM inference TTFT latency overhead CPU GPU data copy vLLM TGI framework
