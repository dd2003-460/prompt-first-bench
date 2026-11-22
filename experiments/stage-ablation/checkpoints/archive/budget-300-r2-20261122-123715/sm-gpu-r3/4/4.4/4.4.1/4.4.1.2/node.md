# N317: 分支1 的 '无可行解' 边界条件量化：若强制要求 32K 上下文且无 Offload (即 VRAM_Required <= 24GB)，则需满足 Weigh

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

分支1 的 '无可行解' 边界条件量化：若强制要求 32K 上下文且无 Offload (即 VRAM_Required <= 24GB)，则需满足 Weight_GB + KV_GB <= 24GB。INT8 权重 27GB 已超限，故必须降至 W4 量化 (13.5GB)。W4 + 32K KV Cache (GQA, ~9GB) + Activation (~3GB) ≈ 25.5GB，仍超 24GB，需启用 PagedAttention 或进一步压缩 KV 至 INT4，此时精度损失 ΔPPL > 1.0，违反 Quality=Low 隐含的 <0.5 阈值，确认该分支在 32K 约束下确实无可行解。

## Corrected Claim

在假设模型参数量及GQA配置使得32K KV Cache约为9GB、Activation约为3GB的前提下，W4量化+32K上下文总显存需求约为25.5GB，超过24GB限制，导致该分支无可行解。

## Evidence

[质询]数值量级与模型架构假设存在潜在冲突：INT8权重27GB通常对应约35B参数模型（如Llama-3-70B的INT8约为70GB，Llama-3-8B的INT8约为8GB，27GB更接近30B-35B级别）。若为30B+模型，32K上下文下的KV Cache（即使使用GQA）通常远超9GB（例如Llama-3-70B 32K KV Cache约为10-15GB，30B模型若GQA比例低则更高），且Activation内存也随模型大小增加。此外，'Quality=Low隐含<0.5阈值'属于特定业务定义而非通用标准，缺乏上下文支持。 | 先验知识/题面给定，逻辑校验通过：算术推导（27>24, 13.5+9+3=25.5>24）自洽，但具体KV Cache和Activation数值依赖于未明确指定的模型架构（参数量、GQA头数等），属于经验事实且缺乏来源支持，故降级。
