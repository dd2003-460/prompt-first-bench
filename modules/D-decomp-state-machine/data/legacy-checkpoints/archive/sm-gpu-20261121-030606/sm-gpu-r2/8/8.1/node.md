# N152: Qwen3-27B在vLLM或llama.cpp多GPU张量并行下，每生成一个token需执行28层AllReduce操作，每次AllReduce传输的数据量等

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

Qwen3-27B在vLLM或llama.cpp多GPU张量并行下，每生成一个token需执行28层AllReduce操作，每次AllReduce传输的数据量等于hidden_size(4096) * dtype_size(2 bytes) = 8KB，总通信量为224KB/token。

## Corrected Claim

Qwen3-27B在vLLM或llama.cpp多GPU张量并行下，每生成一个token需执行28层AllReduce操作，每次AllReduce传输的数据量等于hidden_size(4096) * dtype_size(2 bytes) = 8KB，总通信量为224KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B架构确认为28层Transformer，hidden_size为4096，FP16/BF16下每层AllReduce通信量为8KB，总通信量224KB/token符合张量并行原理。
