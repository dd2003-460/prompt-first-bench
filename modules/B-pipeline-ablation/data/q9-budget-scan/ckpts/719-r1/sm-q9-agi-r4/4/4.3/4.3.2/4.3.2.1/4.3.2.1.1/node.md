# N628: OpenSSL 1.1.1+ 在 Intel Xeon 级别 CPU 上启用 AES-NI 指令集后，SHA-256 吞吐量实测为 1.2-1.8 GB/s，具

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N224

## Claim

OpenSSL 1.1.1+ 在 Intel Xeon 级别 CPU 上启用 AES-NI 指令集后，SHA-256 吞吐量实测为 1.2-1.8 GB/s，具体数值受 CPU 微架构（如 Skylake vs Ice Lake）影响；Ice Lake 因引入 AVX-512 优化，吞吐量可达 1.8 GB/s，而 Skylake 通常为 1.2 GB/s，需根据服务器 CPU 型号选择对应参数。

## Corrected Claim

OpenSSL 1.1.1+ 在 Intel Xeon 级别 CPU 上启用硬件加速指令集后，SHA-256 吞吐量显著高于软件实现，具体数值受 CPU 微架构影响较大，Ice Lake 等较新架构通常优于 Skylake，建议根据具体服务器 CPU 型号进行基准测试以确定准确参数。

## Evidence

[质询]数值量级存疑：现代 Intel Xeon CPU（Skylake/Ice Lake）配合 OpenSSL 1.1.1+ 及 AES-NI/SHA-NI 指令集，单核 SHA-256 吞吐量通常远高于 1.2-1.8 GB/s（通常在 3-5 GB/s 甚至更高，取决于具体微架构和 OpenSSL 版本优化程度）。1.2-1.8 GB/s 更接近较旧架构或未充分优化的场景，将 Ice Lake 标定为 1.8 GB/s 可能严重低估了实际性能。 | 经验事实，逻辑自洽但缺来源支持；且数值量级与现代主流 Xeon 平台实测数据可能存在偏差，无法确认具体数值准确性。

## Search Query

OpenSSL SHA-256 throughput AES-NI Intel Xeon Skylake Ice Lake benchmark
