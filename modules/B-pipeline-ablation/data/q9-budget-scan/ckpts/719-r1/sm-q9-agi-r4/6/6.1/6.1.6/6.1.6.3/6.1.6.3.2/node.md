# N717: V100-SXM2 模块本身无风扇，风扇控制依赖于服务器主板 BMC（基板管理控制器），软件层面无法直接通过 CUDA API 或 nvidia-smi 调整 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N263

## Claim

V100-SXM2 模块本身无风扇，风扇控制依赖于服务器主板 BMC（基板管理控制器），软件层面无法直接通过 CUDA API 或 nvidia-smi 调整 fan_speed，只能调整 GPU 功耗上限（Power Limit）或触发 P-State 切换，200ms 干预窗口的实现需通过降低功耗限制（如 nvidia-smi -pl 200）来实现，而非直接控温

## Corrected Claim

V100-SXM2 模块本身无风扇，风扇控制依赖于服务器主板 BMC（基板管理控制器），软件层面无法直接通过 CUDA API 或 nvidia-smi 调整 fan_speed，只能调整 GPU 功耗上限（Power Limit）或触发 P-State 切换，200ms 干预窗口的实现需通过降低功耗限制（如 nvidia-smi -pl 200）来实现，而非直接控温

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2 为被动散热模组，依赖机箱风道，nvidia-smi 确实不提供直接风扇转速控制接口（fan_speed 通常显示为 N/A 或不可控），只能通过 Power Limit 间接影响发热和频率，符合硬件架构常识。

## Search Query

V100 SXM2 fan control software limitation BMC power limit adjustment nvidia-smi pl
