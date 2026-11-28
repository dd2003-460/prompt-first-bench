# N160: 延迟注入实现：通过 Mock Server 在工具响应头添加 Sleep(t) 延迟，t ∈ {1, 2, ..., 10}s，确保网络延迟可精确控制且不影响计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

延迟注入实现：通过 Mock Server 在工具响应头添加 Sleep(t) 延迟，t ∈ {1, 2, ..., 10}s，确保网络延迟可精确控制且不影响计算逻辑

## Corrected Claim

延迟注入实现：通过 Mock Server 在工具响应头添加 Sleep(t) 延迟，t ∈ {1, 2, ..., 10}s，确保网络延迟可精确控制且不影响计算逻辑

## Evidence

先验知识/题面给定，逻辑校验通过：Mock Server 拦截请求并人为增加固定时间延迟是标准的网络模拟手段，Sleep(t) 实现精确可控且隔离于业务逻辑，符合工程常识。
