# N197: 散热风扇功耗具体值：2×4090方案需3-4个140mm风扇，平均功耗约30-40W；1×A100方案需2-3个140mm风扇，平均功耗约20-30W；风扇数量

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

散热风扇功耗具体值：2×4090方案需3-4个140mm风扇，平均功耗约30-40W；1×A100方案需2-3个140mm风扇，平均功耗约20-30W；风扇数量和风压对功耗影响约±5W，需根据具体散热方案确定

## Corrected Claim

散热风扇功耗取决于具体型号与转速：2×4090方案通常需3-4个140mm风扇，总功耗通常在20-50W区间；1×A100方案需2-3个140mm风扇，总功耗通常在15-40W区间；具体数值需根据所选风扇的额定功率及实际运行转速确定。

## Evidence

[质询]具体数值（30-40W, 20-30W）属于经验事实，缺乏具体风扇型号、转速及风道设计的限定，不同品牌/型号风扇功耗差异较大，该数值范围可能过于宽泛或基于特定假设，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

140mm fan power consumption LLM inference workstation cooling solution measured watts
