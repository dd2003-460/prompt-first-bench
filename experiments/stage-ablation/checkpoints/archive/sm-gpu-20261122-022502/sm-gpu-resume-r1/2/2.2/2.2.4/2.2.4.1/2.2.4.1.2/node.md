# N594: 在 ROCm 6.1+ 环境下，针对大模型推理（Memory-bound 场景）的实测有效带宽利用率基准值约为 92%（即 ~4876 GB/s），低于 NVI

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N182

## Claim

在 ROCm 6.1+ 环境下，针对大模型推理（Memory-bound 场景）的实测有效带宽利用率基准值约为 92%（即 ~4876 GB/s），低于 NVIDIA H100 在 CUDA 下的 ~95% 利用率，主要归因于 HIP 运行时对 HBM 访问模式的调度差异。

## Corrected Claim

在 ROCm 6.1+ 环境下，针对大模型推理（Memory-bound 场景）的实测有效带宽利用率通常较高（接近理论峰值），但具体数值（如92%）及与 NVIDIA H100 的对比差异需依赖特定硬件配置和基准测试数据，且性能差异归因于 HIP 运行时调度差异的说法缺乏普遍共识，建议表述为‘实测带宽利用率略低于 NVIDIA H100 在 CUDA 下的表现，具体数值因测试环境而异’。

## Evidence

[质询]该陈述包含具体的经验性数值（92%利用率、4876 GB/s）和具体的归因（HIP调度差异），属于硬件性能基准和软件实现细节，无法从第一性原理推导。且‘主要归因于HIP运行时调度差异’这一因果解释缺乏普遍公认的权威文献支持，通常HBM带宽利用率受多种因素（如内存控制器、驱动、内核优化）影响，单一归因可能存在过度简化或错误。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值及归因无法从第一性原理推出，符合经验事实排除条款）

## Search Query

AMD MI300X HBM3 effective bandwidth utilization ROCm 6.1 benchmark LLM inference
