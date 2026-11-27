# N135: V100-SXM2 在 Decode 阶段（Memory-Bound）的有效 HBM 带宽利用率通常为 70-75%，主要受限于 L2 Cache 命中率低及非

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

V100-SXM2 在 Decode 阶段（Memory-Bound）的有效 HBM 带宽利用率通常为 70-75%，主要受限于 L2 Cache 命中率低及非对齐访问。对于 Qwen3.8-27B 的 13.5GB 权重加载，实际有效带宽约为 630-675 GB/s，决定了理论 Decode 上限为 650e9 / 13.5e9 ≈ 48 tok/s（单卡），TP=4 下受通信限制降至 80-100 tok/s 区间。

## Corrected Claim

V100-SXM2 在 Decode 阶段（Memory-Bound）的有效 HBM 带宽利用率通常在 70-80% 之间，受限于内存访问模式及 KV Cache 管理。对于约 13.5GB 权重的模型，单卡理论 Decode 上限约为 45-50 tok/s；在 TP=4 配置下，受通信开销影响，实际吞吐通常低于线性扩展，具体数值取决于推理框架优化程度。

## Evidence

[质询]V100-SXM2 的 HBM 峰值带宽为 900 GB/s，70-75% 利用率对应 630-675 GB/s 在数值上自洽，但将 Decode 阶段的瓶颈完全归因于 'L2 Cache 命中率低及非对齐访问' 且忽略 KV Cache 读取开销和 Kernel Launch 延迟等常见因素，属于过度简化的经验性断言；此外，Qwen3.8-27B 的具体权重大小（13.5GB）及 TP=4 下的具体吞吐区间（80-100 tok/s）缺乏通用基准数据支持，易受具体实现（如 vLLM/TensorRT-LLM 版本、量化方式）影响。 | 先验知识/题面给定，逻辑校验通过：V100-SXM2 峰值带宽 900GB/s，70-75% 利用率计算无误；Decode 阶段 Memory-Bound 特性符合直觉；但具体利用率数值和 TP 扩展效率为经验估计，缺乏来源直接支持，故降级。
