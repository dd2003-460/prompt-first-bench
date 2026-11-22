# N27: 首字延迟（TTFT）由预填充阶段（Prefill）的计算复杂度决定，与序列长度呈二次方关系；对于32K输入，TTFT = f(序列长度², GPU计算能力TFL

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

首字延迟（TTFT）由预填充阶段（Prefill）的计算复杂度决定，与序列长度呈二次方关系；对于32K输入，TTFT = f(序列长度², GPU计算能力TFLOPS)，消费级GPU（如RTX 4090约82.6 TFLOPS FP16）处理32K prefill可能需要15-30秒，而数据中心GPU（如A100 80GB约312 TFLOPS）可缩短至5-10秒。

## Corrected Claim

首字延迟（TTFT）由预填充阶段（Prefill）的计算复杂度决定，与序列长度呈二次方关系；对于32K输入，TTFT = f(序列长度², GPU计算能力TFLOPS)，消费级GPU（如RTX 4090约82.6 TFLOPS FP16）处理32K prefill可能需要15-30秒，而数据中心GPU（如A100 80GB约312 TFLOPS）可缩短至5-10秒。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算量确实与序列长度平方成正比（O(N^2)），且RTX 4090与A100的FP16算力量级及由此推导的耗时比例符合物理直觉与工程常识。
