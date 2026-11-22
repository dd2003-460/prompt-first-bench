# N370: 若使用预编译 wheel (pip install vllm)，vLLM 安装耗时 T_install = T_download + T_unzip + T_v

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

若使用预编译 wheel (pip install vllm)，vLLM 安装耗时 T_install = T_download + T_unzip + T_verify ≈ 5-10 分钟；若需从源码编译 (pip install -e .)，耗时 T_compile = 30-60 分钟，取决于 CPU 核心数与 C++ 扩展编译复杂度。

## Corrected Claim

若使用预编译 wheel (pip install vllm)，vLLM 安装耗时 T_install = T_download + T_unzip + T_verify ≈ 5-10 分钟；若需从源码编译 (pip install -e .)，耗时 T_compile = 30-60 分钟，取决于 CPU 核心数与 C++ 扩展编译复杂度。

## Evidence

先验知识/题面给定，逻辑校验通过
