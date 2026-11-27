# N162: Intel Arc 运行 LLM 推理的最低驱动版本要求：Linux 下需 Mesa 24.0+ 以支持 Vulkan 1.3 及最佳内存管理；Windows 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Intel Arc 运行 LLM 推理的最低驱动版本要求：Linux 下需 Mesa 24.0+ 以支持 Vulkan 1.3 及最佳内存管理；Windows 下需 Intel Graphics Driver 31.0.101.6558+；低于此版本会导致 Vulkan 设备枚举失败或显存分配错误，阻断推理启动。

## Corrected Claim

Intel Arc 运行 LLM 推理的最低驱动版本要求：Linux 下需 Mesa 24.0+ 以支持 Vulkan 1.3 及最佳内存管理；Windows 下需 Intel Graphics Driver 31.0.101.6558+；低于此版本会导致 Vulkan 设备枚举失败或显存分配错误，阻断推理启动。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Intel Arc minimum driver version Vulkan LLM inference requirement
