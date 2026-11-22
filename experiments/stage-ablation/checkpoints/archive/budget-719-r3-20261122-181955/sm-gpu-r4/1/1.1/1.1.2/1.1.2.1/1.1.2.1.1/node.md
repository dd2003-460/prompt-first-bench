# N410: RTX 4080 Super 在 32K 上下文约束下的不可行性边界条件：16GB 显存减去 INT4 权重 13.5GB 和框架开销 2GB 后，剩余 0.5

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N135

## Claim

RTX 4080 Super 在 32K 上下文约束下的不可行性边界条件：16GB 显存减去 INT4 权重 13.5GB 和框架开销 2GB 后，剩余 0.5GB 显存，仅能支持 0.5GB / 256KB ≈ 2,000 tokens 的 KV Cache；若要支持 32K 上下文（需 8GB KV），必须使用 INT2 量化或 Offload 技术，但 INT2 质量损失通常 >5% [待核验]，Offload 会导致 PCIe 带宽成为新瓶颈（理论吞吐降至 <5 tokens/s），故该方案在本题‘质量可接受’前提下被彻底排除。

## Corrected Claim

RTX 4080 Super 在 32K 上下文约束下，若使用 16GB 显存且 INT4 权重占用 13.5GB、框架开销 2GB，剩余 0.5GB 显存仅能支持约 2,000 tokens 的 KV Cache（基于 256KB/token 估算）。若要支持 32K 上下文，需大幅降低 KV Cache 精度（如 INT2）或使用 Offload 技术，但前者可能导致显著质量损失，后者受限于 PCIe 带宽导致吞吐下降，因此在‘质量可接受’前提下该方案可行性极低。

## Evidence

[质询]KV Cache 大小估算严重依赖模型架构（如 GQA/MQA 头数、层数、隐藏维度），不同模型（如 Llama-3-8B vs 70B）在 32K 上下文下的 KV Cache 占用差异巨大，直接断言‘需 8GB KV’缺乏具体模型参数支撑，属于经验事实且数值可能不准确；此外，INT2 量化质量损失 >5% 也是经验性结论，缺乏统一标准。 | 先验知识/题面给定，逻辑校验通过（显存算术自洽：16-13.5-2=0.5GB），但 KV Cache 具体数值（8GB）和 INT2 质量损失（>5%）为经验事实，缺乏来源直接支持，且受模型架构影响大，故降级。

## Search Query

RTX 4080 Super 16GB LLM 32K context offload performance penalty
