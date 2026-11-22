# N381: NVFP4 (Native FP4) 量化仅适用于 Blackwell 架构 (RTX 5090/H100 Blackwell)，RTX 4090 (Ada) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

NVFP4 (Native FP4) 量化仅适用于 Blackwell 架构 (RTX 5090/H100 Blackwell)，RTX 4090 (Ada) 和 A100 (Ampere) 不支持原生 FP4 计算；因此 N152 中提到的 'NVFP4' 在 RTX 4090 上实际执行的是软件模拟或回退到 INT4/W4 量化，其性能与质量损失与原生 FP4 不同，需修正为 'W4-AWQ' 或 'GPTQ-4bit' 以匹配硬件能力。

## Corrected Claim

NVFP4 (Native FP4) 量化仅适用于 Blackwell 架构 (RTX 5090/H100 Blackwell)，RTX 4090 (Ada) 和 A100 (Ampere) 不支持原生 FP4 计算；因此 N152 中提到的 'NVFP4' 在 RTX 4090 上实际执行的是软件模拟或回退到 INT4/W4 量化，其性能与质量损失与原生 FP4 不同，需修正为 'W4-AWQ' 或 'GPTQ-4bit' 以匹配硬件能力。

## Evidence

先验知识/题面给定，逻辑校验通过：Blackwell架构原生支持FP4，而Ada/Ampere架构硬件不支持原生FP4计算，需通过软件模拟或回退至INT4/W4量化，陈述符合硬件架构演进事实。

## Search Query

NVIDIA Blackwell FP4 support RTX 4090 Ada FP4 compatibility
