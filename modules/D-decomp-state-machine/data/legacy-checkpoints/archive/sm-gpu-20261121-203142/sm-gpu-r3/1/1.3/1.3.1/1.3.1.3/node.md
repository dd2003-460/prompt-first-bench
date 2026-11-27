# N145: GPTQ/AWQ等主流4-bit量化方法的Index/Codebook开销：通常每个1x128或1x256 block存储一个FP16/FP32 scale和z

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

GPTQ/AWQ等主流4-bit量化方法的Index/Codebook开销：通常每个1x128或1x256 block存储一个FP16/FP32 scale和zero-point，开销约为权重的1-2%；对于27B模型，额外开销约 0.14-0.28 GB，总显存 ≈ 13.74-13.88 GB

## Corrected Claim

GPTQ/AWQ等主流4-bit量化方法的Index/Codebook开销：通常每个1x128或1x256 block存储一个FP16/FP32 scale和zero-point，开销约为权重的1-2%；对于27B模型，额外开销约 0.14-0.28 GB，总显存 ≈ 13.74-13.88 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型4-bit量化后权重约13.5GB，1x128 block的scale/zero-point开销约为权重的1/64（~1.5%），计算结果0.14-0.28GB及总显存13.74-13.88GB符合工程常识与数学推导。

## Search Query

GPTQ AWQ 4-bit quantization memory overhead index codebook size
