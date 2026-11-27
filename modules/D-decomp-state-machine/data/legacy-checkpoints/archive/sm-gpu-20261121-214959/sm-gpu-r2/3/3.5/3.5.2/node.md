# N85: AMD ROCm 软件栈稳定性量化：ROCm 6.1+ 对 MI300X 支持较好，但对消费级 RX 7900 XTX 的 FP8/INT4 内核支持仍有限（主

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

AMD ROCm 软件栈稳定性量化：ROCm 6.1+ 对 MI300X 支持较好，但对消费级 RX 7900 XTX 的 FP8/INT4 内核支持仍有限（主要依赖 llama.cpp 而非 vLLM）；驱动崩溃率在高负载下约为 0.5-1%（每 100 小时运行一次），导致平均每周需 2-4 小时进行驱动重置和日志分析，调试时间成本约为 NVIDIA 方案的 2-3 倍 [待核验：具体崩溃率数据]。

## Corrected Claim

AMD ROCm 软件栈在 MI300X 上支持较好，但对消费级 RX 7900 XTX 的 FP8/INT4 内核支持仍有限（主要依赖 llama.cpp 而非 vLLM）；在高负载场景下，用户普遍反馈存在较高的驱动稳定性问题及调试时间成本，具体崩溃率与维护耗时因环境而异，通常显著高于 NVIDIA 方案。

## Evidence

[质询]具体数值（0.5-1%崩溃率、每周2-4小时维护、2-3倍调试成本）缺乏公开权威基准测试支持，属于高度依赖特定环境（驱动版本、内核配置、工作负载）的经验性观察数据，极易因环境差异产生巨大偏差，且将‘驱动崩溃’与‘软件栈稳定性’直接量化挂钩存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体崩溃率与维护成本非第一性原理可推导，属特定环境经验数据）

## Search Query

AMD ROCm 6.1 stability issues RX 7900 XTX vLLM support FP8 kernel
