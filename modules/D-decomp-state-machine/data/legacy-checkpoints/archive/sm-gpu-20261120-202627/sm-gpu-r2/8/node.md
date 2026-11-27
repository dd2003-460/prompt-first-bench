# N31: 非典型方案筛选标准：Apple M3 Ultra (512GB/800GB) 和 AMD MI300X (192GB) 纳入候选是因为其统一内存架构或大显存容量

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

非典型方案筛选标准：Apple M3 Ultra (512GB/800GB) 和 AMD MI300X (192GB) 纳入候选是因为其统一内存架构或大显存容量可原生支持 BF16 全精度 + 32K 上下文而无需量化，需评估其软件栈对 Qwen3 的支持延迟（如 llama.cpp vs vLLM 性能差异）及单节点价格对比 NVIDIA 方案。

## Corrected Claim

Apple M3 Ultra (512GB) 因统一内存架构可原生支持大模型推理（来源支持）；AMD MI300X 及 M3 Ultra 800GB 配置、软件栈性能对比等具体规格与评估结论缺乏当前来源直接支持，需进一步核验。

## Evidence

[质询]陈述中关于AMD MI300X的具体显存容量（192GB）及Apple M3 Ultra支持800GB配置属于具体硬件规格经验事实，参考来源仅证实了M3 Ultra 512GB的存在及本地推理能力，未覆盖MI300X规格、800GB配置或软件栈性能对比，且192GB MI300X规格与常见256GB版本存在潜在冲突风险，缺乏多源一致支持。 | 来源[1][2]直接支持Apple M3 Ultra 512GB统一内存架构及本地LLM推理能力，但来源未覆盖AMD MI300X规格、800GB配置及软件栈性能对比，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1928856739001927267&rut=fa4f9f415c7129ecb06af59f90715076c249fe09bb0a90bacc1260e3b11d07c9', 'type': 'ddg', 'title': 'Apple M3 Ultra（512GB统一内存）本地LLM推理全面分析'}
- {'url': 'https://zhuanlan.zhihu.com/p/28533341247&rut=e351680739e35a3cdb92e491590cea1bff777be05afe6bc91d4b6c3a4f03269d', 'type': 'ddg', 'title': '苹果最强M3 Ultra首发逆天，512GB「桌面超算」在家跑DeepSeek-R1!'}
