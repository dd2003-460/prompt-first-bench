# N162: 标准化评估基准：定义'基准测试套件'为 32K 上下文输入、1024 token 输出、Batch Size=1、Temperature=0.7；吞吐量指标取 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

标准化评估基准：定义'基准测试套件'为 32K 上下文输入、1024 token 输出、Batch Size=1、Temperature=0.7；吞吐量指标取 Decode 阶段的平均 tokens/s（排除 Prefill 干扰）；所有硬件对比必须在此统一基准下进行，否则吞吐量数据不可比；需引用 vLLM 或 llama.cpp 的特定 commit 版本以确保软件栈一致性

## Corrected Claim

标准化评估基准：定义'基准测试套件'为 32K 上下文输入、1024 token 输出、Batch Size=1、Temperature=0.7；吞吐量指标取 Decode 阶段的平均 tokens/s（排除 Prefill 干扰）；所有硬件对比必须在此统一基准下进行，否则吞吐量数据不可比；需引用 vLLM 或 llama.cpp 的特定 commit 版本以确保软件栈一致性

## Evidence

检索失败: no sources from any channel (all 5 failed)
