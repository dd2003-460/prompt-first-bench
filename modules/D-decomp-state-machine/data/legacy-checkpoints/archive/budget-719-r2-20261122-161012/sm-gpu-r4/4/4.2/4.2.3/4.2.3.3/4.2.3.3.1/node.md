# N515: Apple M3 Ultra (或 M2 Ultra，需确认 M3 Ultra 是否已发布，目前最新为 M2 Ultra/M3 Max) 的统一内存带宽 800

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N212

## Claim

Apple M3 Ultra (或 M2 Ultra，需确认 M3 Ultra 是否已发布，目前最新为 M2 Ultra/M3 Max) 的统一内存带宽 800 GB/s 在 BF16 Decode 下理论上限 14.5 tokens/s，但 macOS 对 LLM 推理的 CPU/GPU 协同调度效率通常低于 Linux+CUDA 环境，实测吞吐往往仅为理论值的 60-70% (约 8.7-10.1 tokens/s)，且无法利用 Tensor Core 加速，导致其在交互式场景下的 TCO 劣势明显，除非用户极度重视静音与低功耗 (年电费节省 < $50)。

## Corrected Claim

Apple M2 Ultra（M3 Ultra尚未发布）的统一内存带宽为800 GB/s。在BF16精度下，其LLM推理吞吐量取决于具体模型规模（如7B、13B、70B等）及软件优化程度，通常显著高于14.5 tokens/s（例如7B模型可达30-50+ tokens/s）。macOS对LLM推理的调度效率受框架影响较大，无法简单概括为理论值的60-70%。Apple芯片无Tensor Core，但通过GPU和ANE协同优化，在交互式场景下具有低功耗和静音优势，TCO需结合具体使用场景和电价综合评估。

## Evidence

[质询]数值量级与硬件规格存在严重矛盾：Apple M2 Ultra 的统一内存带宽为 800 GB/s，但 M3 Ultra 尚未发布（截至2024年最新为M2 Ultra），且即便按800 GB/s计算，BF16下14.5 tokens/s的理论上限对于现代大模型（如7B-70B）而言数值偏低或偏高取决于模型大小，但更关键的是，M系列芯片拥有强大的GPU和ANE，其LLM推理性能通常远超此数值（例如M2 Max/Ultra在运行Llama 2 7B时可达数十tokens/s），14.5 tokens/s的理论上限缺乏明确的模型规模前提，且‘无法利用Tensor Core’虽正确（Apple无Tensor Core），但‘实测仅为理论值60-70%’这一具体效率系数缺乏通用性，不同模型和框架下差异巨大。 | 来源不可用。逻辑校验发现：1. M3 Ultra未发布，事实前提错误；2. 14.5 tokens/s的理论上限未指定模型规模，且与M2 Ultra实际性能表现（通常更高）不符，数值量级存疑；3. 60-70%的效率系数过于绝对，缺乏普适性。

## Search Query

Mac Studio M2 Ultra LLM inference benchmark tokens per second vs GPU
