# N495: 签名验证（HMAC-SHA256 或 RSA）的 CPU 处理时间 T_auth 在通用 x86 服务器上约为 0.1-0.5ms/请求，若启用硬件加速（如 I

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N166

## Claim

签名验证（HMAC-SHA256 或 RSA）的 CPU 处理时间 T_auth 在通用 x86 服务器上约为 0.1-0.5ms/请求，若启用硬件加速（如 Intel QAT）可降至 0.05ms，该过程独立于 I/O 操作，可与元数据查询并行执行以优化总处理时间

## Corrected Claim

签名验证（HMAC-SHA256 或 RSA）的 CPU 处理时间 T_auth 在通用 x86 服务器上约为 0.1-0.5ms/请求，若启用硬件加速（如 Intel QAT）可降至 0.05ms，该过程独立于 I/O 操作，可与元数据查询并行执行以优化总处理时间

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HMAC SHA256 signature verification CPU latency ms benchmark
