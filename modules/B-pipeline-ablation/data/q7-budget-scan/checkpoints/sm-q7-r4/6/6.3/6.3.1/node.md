# N331: C_cluster=¥5000/h 的构成拆解：C_cluster = C_compute + C_memory + C_network + C_storage

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

C_cluster=¥5000/h 的构成拆解：C_cluster = C_compute + C_memory + C_network + C_storage_IO，假设集群含 10 台服务器，每台 ¥500/h（含折旧、电力、运维分摊），则 C_cluster = 10 * 500 = ¥5000/h；若仅部分节点参与扫描，C_cluster 应按实际占用节点数调整 [knowledge]

## Corrected Claim

C_cluster=¥5000/h 的构成拆解：C_cluster = C_compute + C_memory + C_network + C_storage_IO，假设集群含 10 台服务器，每台 ¥500/h（含折旧、电力、运维分摊），则 C_cluster = 10 * 500 = ¥5000/h；若仅部分节点参与扫描，C_cluster 应按实际占用节点数调整 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 10 * 500 = 5000 正确，成本构成拆解符合集群资源计费的常规逻辑，且明确指出了动态调整条件，内部自洽。
