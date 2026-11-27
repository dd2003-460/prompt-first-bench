# N25: 双卡方案硬件成本 C_dual 的计算公式为 C_dual = 2 * P_gpu_consumption + C_dual_slot_chassis + C_

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

双卡方案硬件成本 C_dual 的计算公式为 C_dual = 2 * P_gpu_consumption + C_dual_slot_chassis + C_psu_1200W + C_cooling_high_density，其中 P_gpu_consumption 为消费级显卡均价（如 RTX 4090/3090），需量化双卡机箱与电源溢价（通常增加 $150-$300 成本）

## Corrected Claim

双卡方案硬件成本 C_dual 的计算公式为 C_dual = 2 * P_gpu_consumption + C_dual_slot_chassis + C_psu_1200W + C_cooling_high_density，其中 P_gpu_consumption 为消费级显卡均价（如 RTX 4090/3090），需量化双卡机箱与电源溢价（具体数值需根据市场实时价格确定，通常涉及额外硬件成本）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点之间逻辑清晰且正交：子节点1聚焦于基础设施（机箱/电源/散热）的溢价量化，子节点2和3则分别针对两种具体显卡（3090/4090）给出总成本估算及性能/显存分析。虽然子节点2和3在结构上相似（都是‘显卡+基础设施’的总和），但它们代表的是不同的硬件配置选项（不同显卡型号、不同价格区间、不同功耗/互连带宽特性），属于枚举不同方案，而非简单的参数冗余。父节点中的核心变量（GPU价格、机箱/电源/散热溢价）均被覆盖，且子节点补充了具体的数值范围和适用场景（如Qwen3-27B的显存需求），覆盖了父节点的关键方面。）

## Search Query

dual GPU workstation chassis power supply cost premium vs single GPU

## Retrieval Sources

- {'url': 'https://duckduckgo.com/y.js?ad_domain=amazon.com&ad_provider=bingv7aa&ad_type=txad&click_metadata=H0XWUmf3vokMsJDD7qdGpyAXzvu3FDxMIlUm9dRgKke4OvS98zjWCm3xPMQWt2pkeqzY%2DTDs_AkzibJo9S8s0YvJmICQ9nbJbp68I9qOv0%2DSPISup1oWtPIEdXE21KEWWNiSNvcc4%2DpNCZLYlGBspvDt4i52RNoIspISDZ2zYsM.1mEAdzIu8fh0Y2OpTMVbSg&rut=ce7978747935f087aba1c1397ff81ed75a82fd540646c5332b031f55275ec5f3&u3=https%3A%2F%2Fwww.bing.com%2Faclick%3Fld%3De8bUjvwAPlhRGU6I4OSHCdCTVUCUyfVjqUy4Z7CuR0k7QxK9cuWgVcMVGSIr%2DnxDRcTAKUglnT7xNOf8oyfDB0EaqjnrP1yzJZjrdkR01Jb15Xl9c803VFlTy%2D8N7RzWjbnekLVNLW0W%2DRBjpcBE4MoWoXx_6WBHgQ7vNdvYxLF2W0GAwGTnaYK8AcvRAWspx1JP64BqovlpFE07R7JMhjGfcvHhI%26u%3DaHR0cHMlM2ElMmYlMmZ3d3cuYW1hem9uLmNvbSUyZnMlMmYlM2ZpZSUzZFVURjglMjZrZXl3b3JkcyUzZGR1YWwlMmJncHUlMmJwb3dlciUyYnN1cHBseSUyNmluZGV4JTNkYXBzJTI2dGFnJTNkdHh0c3RkYmdkdC0yMCUyNnJlZiUzZHBkX3NsXzJxb3Yzc2M2dmhfcCUyNmFkZ3JwaWQlM2QxMjM1ODUyMDU4OTIyNTIyJTI2aHZhZGlkJTNkNzcyNDA4ODQwOTgyOTUlMjZodm5ldHclM2RzJTI2aHZxbXQlM2RwJTI2aHZibXQlM2RicCUyNmh2ZGV2JTNkYyUyNmh2bG9jaW50JTNkJTI2aHZsb2NwaHklM2QxMzk2NTAlMjZodnRhcmdpZCUzZGt3ZC03NzI0MTA3MDM3Mzc3MiUzYWxvYy05NiUyNmh5ZGFkY3IlM2QyNTU1MF8xMzU5MzM5MSUyNm1jaWQlM2RmMTM1MWJkODJkZTMzYWI4OWI1NDdhMzMzZWMzYTE1YiUyNmxhbmd1YWdlJTNkZW5fVVMlMjZtc2Nsa2lkJTNkMmRkNjlhZjYyYjk1MTUzNWJmOGRmMWY0NzNhODlhMmU%26rlid%3D2dd69af62b951535bf8df1f473a89a2e&vqd=4-22710612500534247052498427967063896537&iurl=%7B1%7DIG%3D371C46884934422F90F7CEF75765C739%26CID%3D35E6ABF725416DF9134BB3EE24916CA6%26ID%3DDevEx%2C5039.1&rut=a6fd246435400fd394822d7e92bfc5771b559fbbdeadb9fcc130f19d9ae06c79', 'type': 'ddg', 'title': 'Shop dual gpu power supply - Amazon.com®'}
- {'url': 'https://pctechkits.com/best-dual-gpu-power-supply-for-pc/&rut=d85074fd50af8077b9ad73ba6bce31aa1e0e11bf22d1c4c991ad8c4afb041f56', 'type': 'ddg', 'title': '10 Best Dual GPU Power Supplies for PC in 2026: Reliable, High-Headroom ...'}
- {'url': 'https://pcpartsgeek.com/best-premium-pc-power-supply-for-dual-gpu-build/&rut=f1fdab699ac3422e26e0b46cd11c9b246468bab86cb7521763a70838c5ac9779', 'type': 'ddg', 'title': '10 Best Premium PC Power Supplies for Dual GPU Builds in 2026'}
