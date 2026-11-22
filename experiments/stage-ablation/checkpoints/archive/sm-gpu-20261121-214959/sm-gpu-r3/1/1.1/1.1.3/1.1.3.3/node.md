# N139: INT4 量化运行时必需的临时缓冲区（如 CUDA Context、算子中间结果）通常占用 0.5-1.0 GB，该部分不随 group_size 变化，是 N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

INT4 量化运行时必需的临时缓冲区（如 CUDA Context、算子中间结果）通常占用 0.5-1.0 GB，该部分不随 group_size 变化，是 N39 中‘2.16GB 额外开销’的主要构成部分之一，需从总显存预算中预留。

## Corrected Claim

INT4 量化运行时必需的临时缓冲区（如 CUDA Context、算子中间结果）通常占用 0.5-1.0 GB，该部分不随 group_size 变化，是 N39 中‘2.16GB 额外开销’的主要构成部分之一，需从总显存预算中预留。

## Evidence

先验知识/题面给定，逻辑校验通过
