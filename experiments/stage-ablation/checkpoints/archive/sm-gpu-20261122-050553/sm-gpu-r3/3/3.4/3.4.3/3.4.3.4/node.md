# N230: 长上下文量化累积误差的归因分解：ΔPPL_total = ΔPPL_quantization + ΔPPL_length_decay + ΔPPL_intera

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

长上下文量化累积误差的归因分解：ΔPPL_total = ΔPPL_quantization + ΔPPL_length_decay + ΔPPL_interaction；其中 ΔPPL_interaction 代表量化误差在长序列注意力计算中的非线性放大效应，需通过对比 (PPL_W4_32K - PPL_W4_4K) 与 (PPL_BF16_32K - PPL_BF16_4K) 的差值来量化该交互项的具体数值贡献。

## Corrected Claim

长上下文量化累积误差的归因分解：ΔPPL_total = ΔPPL_quantization + ΔPPL_length_decay + ΔPPL_interaction；其中 ΔPPL_interaction 代表量化误差在长序列注意力计算中的非线性放大效应，需通过对比 (PPL_W4_32K - PPL_W4_4K) 与 (PPL_BF16_32K - PPL_BF16_4K) 的差值来量化该交互项的具体数值贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：该分解公式符合误差分析的基本线性叠加原理（总误差=主效应+交互项），且通过差分法（Double Difference）隔离交互项的数学逻辑自洽，量纲与定义合理。
