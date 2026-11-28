# N305: 并行假设生成阶段的有效结论数期望值 E_parallel(N) = N * p_success * (1 - c_conflict(N))，其中 p_succe

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

并行假设生成阶段的有效结论数期望值 E_parallel(N) = N * p_success * (1 - c_conflict(N))，其中 p_success 为单个假设通过初步筛选的概率 (估算为 0.3)，c_conflict(N) 为假设间相互排斥或冗余导致的无效化比例，随 N 增加呈线性增长，系数 k=0.05 (即每增加一个并行假设，无效化率增加 5%)。

## Corrected Claim

在特定并行假设生成模型中，有效结论数期望值可建模为 E_parallel(N) = N * p_success * (1 - c_conflict(N))，其中 p_success 和冲突系数 k 需根据具体任务和数据集进行校准，而非固定为 0.3 和 0.05。

## Evidence

[质询]该公式及参数（p_success=0.3, k=0.05）属于特定系统或理论模型的假设性设定，并非通用物理定律或数学公理，缺乏普遍适用的实证数据支持，且参考来源均未涉及此具体模型。 | 逻辑自洽（量纲正确，线性增长假设在局部范围内合理），但参考来源[1]讨论LLM推理参数，[2]讨论并行文本生成综述，均与该特定假设生成模型无关，属经验事实且缺来源支持。

## Search Query

parallel hypothesis generation redundancy rate scientific agent system diminishing returns

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2081808629783597492&rut=414f7a84b83c519567b894447bde7c4a302d1198c775ecd8f7649c8f6f15eeae', 'type': 'ddg', 'title': '本地大模型推理的两个关键参数：parallel 和 MTP n-max 实测对比'}
- {'url': 'https://zhuanlan.zhihu.com/p/1946632863551300890&rut=ea5079a830e961ec5a333794c8e18bdad05998e8b041543bf4ed7ea2f230c8a0', 'type': 'ddg', 'title': '综述系列1：A Survey on Parallel Text Generation From Parallel Decoding to ...'}
