# N68: 单卡可行性边界判定：BF16需≥67.1GB，仅H200(141GB)和MI300X(192GB)满足；FP8/INT8需≥35.6GB，A100 40GB(临

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

单卡可行性边界判定：BF16需≥67.1GB，仅H200(141GB)和MI300X(192GB)满足；FP8/INT8需≥35.6GB，A100 40GB(临界，需实测Overhead)、L40S 48GB、H100 80GB满足；NVFP4/W4需≥20.0GB，RTX 4090(24GB)、RX 7900 XTX(24GB)、A100 40GB均满足，但24GB卡需严格监控碎片化风险。

## Corrected Claim

单卡可行性边界判定：BF16需≥67.1GB，仅H200(141GB)和MI300X(192GB)满足；FP8/INT8需≥35.6GB，A100 40GB(临界，需实测Overhead)、L40S 48GB、H100 80GB满足；NVFP4/W4需≥20.0GB，RTX 4090(24GB)、RX 7900 XTX(24GB)、A100 40GB均满足，但24GB卡需严格监控碎片化风险。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了父节点中关于'显存需求计算公式'的部分，完全遗漏了父节点中核心的'硬件可行性判定'（如H200/MI300X满足BF16，A100/L40S/H100满足FP8，RTX 4090等满足W4，以及A100临界和24GB卡碎片化风险等关键结论）。此外，三个子节点结构高度重复，本质上是同一公式在不同精度参数下的实例化。）
