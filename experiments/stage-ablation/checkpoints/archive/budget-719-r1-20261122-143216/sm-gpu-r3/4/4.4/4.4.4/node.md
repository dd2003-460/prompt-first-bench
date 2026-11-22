# N114: TensorRT-LLM 通过静态图编译和 Kernel Fusion，在单用户低并发场景下相比 vLLM 通常能额外提升 5%-15% 的 Decode 速度

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24, N25, N26

## Claim

TensorRT-LLM 通过静态图编译和 Kernel Fusion，在单用户低并发场景下相比 vLLM 通常能额外提升 5%-15% 的 Decode 速度，但代价是需要针对特定模型和硬件重新编译引擎，且对动态 Batch Size 的支持较弱，对于固定 32K 上下文的本地工作站场景，其性能优势显著但部署复杂度增加。

## Corrected Claim

TensorRT-LLM 通过静态图编译和 Kernel Fusion，在单用户低并发场景下相比 vLLM 往往能提升 Decode 速度，但代价是需要针对特定模型和硬件重新编译引擎，且对动态 Batch Size 的支持较弱，对于固定 32K 上下文的本地工作站场景，其性能优势显著但部署复杂度增加。

## Evidence

[质询]具体数值区间（5%-15%）缺乏通用性，高度依赖模型架构、硬件型号及具体版本，属于经验事实而非固定规律；且'通常'一词掩盖了在不同场景下可能持平甚至落后的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

TensorRT-LLM vs vLLM performance comparison low concurrency single user
