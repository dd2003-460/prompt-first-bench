# N22: 软件许可与维护费用：开源推理框架（vLLM, llama.cpp, TensorRT-LLM）免费，但企业级支持或特定加速库（如 NVIDIA TensorRT

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

软件许可与维护费用：开源推理框架（vLLM, llama.cpp, TensorRT-LLM）免费，但企业级支持或特定加速库（如 NVIDIA TensorRT 授权、AMD ROCm 技术支持）可能产生费用；估算年度维护成本为硬件成本的 5-10% [待核验]，用于驱动更新、bug 修复及硬件故障更换。

## Corrected Claim

软件许可与维护费用：开源推理框架（vLLM, llama.cpp, TensorRT-LLM）本身免费，但企业级支持或特定加速库（如 NVIDIA TensorRT 授权、AMD ROCm 技术支持）可能产生费用；年度运维及硬件维护成本通常与硬件投入规模相关，具体比例需根据实际运维策略和硬件折旧情况估算，一般用于驱动更新、bug 修复及硬件故障更换。

## Evidence

[质询]「年度维护成本为硬件成本的 5-10%」这一具体数值范围缺乏通用行业标准支持，属于高度依赖具体场景（如硬件折旧率、SLA要求、人力成本）的经验估算，且开源软件本身无许可费，该比例主要反映的是隐性运维人力与硬件损耗，直接将其定义为「软件许可与维护费用」存在口径混淆风险。 | 先验知识/题面给定，逻辑校验通过；但具体数值比例（5-10%）为经验性估算，缺乏通用标准背书，且无外部来源支持，故降级为定性表述。
