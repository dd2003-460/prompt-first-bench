# N22: NVFP4或W4（4-bit）量化下Qwen3-27B显存占用降至约13.5GB（27B × 0.5 bytes/param），但4-bit量化对大语言模型的质

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

NVFP4或W4（4-bit）量化下Qwen3-27B显存占用降至约13.5GB（27B × 0.5 bytes/param），但4-bit量化对大语言模型的质量损失通常导致困惑度增加>15%，且需要额外的量化感知训练（QAT）或先进量化算法（如GPTQ/AWQ）来缓解

## Corrected Claim

NVFP4或W4（4-bit）量化下Qwen3-27B的纯权重显存占用理论值约为13.5GB，但实际推理显存占用通常在17GB-22GB之间（含KV Cache及量化开销）；4-bit量化对大语言模型的质量损失通常导致困惑度增加，需借助QAT或GPTQ/AWQ等算法缓解。

## Evidence

[质询]数值量级错误：27B参数在4-bit量化下，仅权重部分理论最小显存占用约为13.5GB（27e9 * 0.5 bytes），但实际部署还需包含KV Cache、激活值及量化元数据（如scale/zero-point），参考来源[1]和[3]均指出实际占用远高于13.5GB（分别为22GB和17GB），陈述将理论权重下限误作实际显存占用。 | 来源[1]指出NVFP4量化后显存约为22GB，来源[3]指出4-bit量化后显存约为17GB，均与陈述中的13.5GB矛盾；且13.5GB仅为纯权重理论值，未计入推理必需的其他显存开销，逻辑上不成立。

## Search Query

4-bit quantization LLM perplexity increase GPTQ AWQ quality degradation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01106/article/details/168111467&rut=4656c8b0bb90a8c61ac16354a3a742e3f4aeb46755b5b0c16d71beecf1c6a31b', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4完整指南：4位NVFP4量化如何玩转27B多模态大模型-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00251/article/details/155252364&rut=c70cf48e5527365aa137ce6d4d70b2c69618fc8a461d17429f05178b6d70cf4c', 'type': 'ddg', 'title': '什么是Qwen3.8-27B-NVFP4？27B视觉语言模型与NVFP4量化的完整入门指南-CSDN博客'}
- {'url': 'https://blog.csdn.net/patrickstar231/article/details/163851680&rut=5015e90108e515c59340b302f9e4e6abde45768219ccddef447878c06773bba8', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署实战：4-bit 量化后 17GB 显存跑起 27B 开源模型_本地运行qwen3.8'}
