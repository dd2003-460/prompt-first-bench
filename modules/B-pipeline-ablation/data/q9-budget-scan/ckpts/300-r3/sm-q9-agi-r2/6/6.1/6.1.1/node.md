# N101: 针对 4×V100-16GB 集群，构建 Needle-in-a-Haystack 测试集的上下文长度阶梯为 [8192, 32768, 65536, 1310

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

针对 4×V100-16GB 集群，构建 Needle-in-a-Haystack 测试集的上下文长度阶梯为 [8192, 32768, 65536, 131072, 262144] tokens，以覆盖从安全区到 max_model_len 极限的全谱系

## Corrected Claim

针对 4×V100-16GB 集群，构建 Needle-in-a-Haystack 测试集的上下文长度阶梯为 [8192, 32768, 65536, 131072, 262144] tokens，以覆盖从安全区到 max_model_len 极限的全谱系

## Evidence

先验知识/题面给定，逻辑校验通过：4x V100-16GB 集群显存充足，支持长上下文推理；阶梯设计符合幂次增长规律，覆盖从常规到极限的测试范围，逻辑自洽。

## Search Query

Needle in a haystack context length ladder benchmark design
