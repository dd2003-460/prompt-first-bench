# N230: NVLink 带宽利用率在 TP=2 场景下受限于 AllReduce 算法效率，实际有效带宽通常为理论峰值的 60%-80%。若利用率为 70%，有效带宽为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

NVLink 带宽利用率在 TP=2 场景下受限于 AllReduce 算法效率，实际有效带宽通常为理论峰值的 60%-80%。若利用率为 70%，有效带宽为 315 GB/s，768 KB 通信时间增至 2.4 µs/step。需验证 vLLM 或 TensorRT-LLM 在 NVLink 上的实际通信效率，以准确估算延迟。

## Corrected Claim

NVLink 带宽利用率在 TP=2 场景下受限于 AllReduce 算法效率，实际有效带宽通常为理论峰值的 60%-80%。若利用率为 70%，有效带宽为 315 GB/s，768 KB 通信时间增至 2.4 µs/step。需验证 vLLM 或 TensorRT-LLM 在 NVLink 上的实际通信效率，以准确估算延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：315 GB/s 对应 450 GB/s 理论峰值的 70%，768 KB / 315 GB/s ≈ 2.44 µs，数值量级与工程经验一致。

## Search Query

NVLink bandwidth utilization efficiency allreduce
