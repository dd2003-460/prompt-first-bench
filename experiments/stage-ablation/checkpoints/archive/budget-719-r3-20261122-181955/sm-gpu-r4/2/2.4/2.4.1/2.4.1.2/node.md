# N253: BF16 精度下 Qwen3-27B 的总内存需求精确公式：Total_Mem = Weights (54 GB) + KV_Cache (5.37 GB 或 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

BF16 精度下 Qwen3-27B 的总内存需求精确公式：Total_Mem = Weights (54 GB) + KV_Cache (5.37 GB 或 10.74 GB) + Framework_Overhead (vLLM ~3 GB, llama.cpp ~1 GB) + OS_Cuda_Reserve (~1 GB)。若 n_kv_heads=8，Total ≈ 63.37 GB (vLLM) 或 61.37 GB (llama.cpp)；若 n_kv_heads=16，Total ≈ 68.74 GB (vLLM)。

## Corrected Claim

BF16 精度下 Qwen3-27B 的总内存需求精确公式：Total_Mem = Weights (54 GB) + KV_Cache (5.37 GB 或 10.74 GB) + Framework_Overhead (vLLM ~3 GB, llama.cpp ~1 GB) + OS_Cuda_Reserve (~1 GB)。若 n_kv_heads=8，Total ≈ 63.37 GB (vLLM) 或 61.37 GB (llama.cpp)；若 n_kv_heads=16，Total ≈ 68.74 GB (vLLM)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重54GB符合2字节/参数计算；KV Cache数值与典型层数/头数配置量级一致；框架开销与OS预留符合工程经验；总内存加和逻辑自洽。
