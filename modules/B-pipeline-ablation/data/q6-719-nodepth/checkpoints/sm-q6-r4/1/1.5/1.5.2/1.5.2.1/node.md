# N186: 图片处理延迟 T_processing_img：对于 JPEG/WebP 图片，源站通常不进行实时转码（已预生成多尺寸），主要延迟为存储 I/O 和 HTTP 

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

图片处理延迟 T_processing_img：对于 JPEG/WebP 图片，源站通常不进行实时转码（已预生成多尺寸），主要延迟为存储 I/O 和 HTTP 响应头生成；T_storage_io ≈ 100us (SSD随机读) + 网络栈处理 ≈ 1-5ms；因此 T_processing_img ≈ 2ms (P99)。

## Corrected Claim

图片处理延迟 T_processing_img：对于 JPEG/WebP 图片，源站通常不进行实时转码（已预生成多尺寸），主要延迟为存储 I/O 和 HTTP 响应头生成；T_storage_io ≈ 100us (SSD随机读) + 网络栈处理 ≈ 1-5ms；因此 T_processing_img ≈ 2ms (P99)。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（不同硬件配置/工作点），且覆盖了高、中、低三种典型场景，具备完备性。然而，这三个子节点本质上是同一参数（存储介质/硬件配置）的不同取值，结构上表现为‘枚举型’冗余，而非‘维度型’分解。在学术或工程分解中，若目的是解释延迟构成，通常应分解为‘I/O延迟’、‘网络栈处理’、‘CPU处理’等正交维度，而非按硬件配置罗列。）
