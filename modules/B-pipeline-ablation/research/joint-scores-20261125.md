# J2 联合分表 — S0-r1..r10 + S5 + T8b

# origin: ai (J2, 2026-11-25) — judge_v1(coverage) + correctness_layer_v0(correctness) 联合重算

**口径**：cov = judge_v1.layer_coverage（bge-m3 节点级, COS≥0.7, frozen spec f6072397f）；CORR/五轴/verdict = correctness_layer_v0（纯规则三型 A1/A2/A3, J1 验收）。cov 节点构造镜像 J1 load_samples：nested=真实节点 claim；flat/t8b 自由文本=非空行作伪节点（line-as-node，与 J1 dry-run 的 T8b cov 同口径；整篇当单节点会低估 cov）。

| sample | cov | CORR | 三轴关键值(C/E/R/S/N + P_A1/P_A3/C2BP) | verdict | 备注 |
|---|---|---|---|---|---|
| S0-gpu-r1 | 0.222 | 0.232 | C=0.500 E=0.000 R=0.500 S=0.000 N=0.286 P_A1=0.500 P_A3=0.000 C2BP=True | A2 | flat answer[10480]ch |
| S0-gpu-r2 | 0.111 | 0.414 | C=0.500 E=0.500 R=0.500 S=0.000 N=0.571 P_A1=0.500 P_A3=0.000 C2BP=True | A2 | flat answer[8990]ch |
| S0-gpu-r3 | 0.056 | 0.086 | C=0.000 E=0.000 R=0.500 S=0.000 N=0.429 P_A1=1.000 P_A3=0.000 C2BP=False | A1 | flat answer[11884]ch |
| S0-gpu-r4 | 0.139 | 0.086 | C=0.000 E=0.000 R=0.500 S=0.000 N=0.429 P_A1=1.000 P_A3=0.000 C2BP=False | A1 | flat answer[9767]ch |
| S0-gpu-r5 | 0.194 | 0.229 | C=0.125 E=0.000 R=0.500 S=0.500 N=0.429 P_A1=0.875 P_A3=0.000 C2BP=False | A1 | flat answer[10253]ch |
| S0-gpu-r6 | 0.139 | 0.210 | C=0.375 E=0.000 R=0.500 S=0.250 N=0.143 P_A1=0.625 P_A3=0.000 C2BP=True | A2 | flat answer[7479]ch |
| S0-gpu-r7 | 0.222 | 0.279 | C=0.375 E=0.250 R=0.500 S=0.000 N=0.429 P_A1=0.625 P_A3=0.000 C2BP=True | A2 | flat answer[11227]ch |
| S0-gpu-r8 | 0.139 | 0.173 | C=0.250 E=0.000 R=0.500 S=0.000 N=0.429 P_A1=0.750 P_A3=0.000 C2BP=True | A1 | flat answer[11730]ch |
| S0-gpu-r9 | 0.167 | 0.221 | C=0.125 E=0.250 R=0.500 S=0.000 N=0.571 P_A1=0.875 P_A3=0.000 C2BP=False | A1 | flat answer[8668]ch |
| S0-gpu-r10 | 0.194 | 0.129 | C=0.125 E=0.000 R=0.500 S=0.000 N=0.429 P_A1=0.875 P_A3=0.000 C2BP=False | A1 | flat answer[9374]ch |
| runs-s5-sm-gpu | 0.389 | 0.414 | C=0.500 E=0.500 R=0.500 S=0.000 N=0.571 P_A1=0.500 P_A3=0.000 C2BP=True | A2 | nested nodes[355] |
| raw_outputs_t8b.arm_a[0] | 0.361 | 0.114 | C=0.000 E=0.000 R=0.500 S=0.000 N=0.571 P_A1=1.000 P_A3=0.000 C2BP=False | A1 | arm_a[0] content+reasoning[12374]ch |
| raw_outputs_t8b.arm_a[1] | 0.333 | 0.452 | C=0.500 E=0.250 R=0.500 S=0.500 N=0.571 P_A1=0.500 P_A3=0.000 C2BP=True | A2 | arm_a[1] content+reasoning[21759]ch |
| raw_outputs_t8b.arm_a[2] | 0.278 | 0.652 | C=1.000 E=0.750 R=1.000 S=0.000 N=0.571 P_A1=0.000 P_A3=1.000 C2BP=False | A3 | arm_a[2] content+reasoning[20617]ch |
| raw_outputs_t8b.arm_b[0] | 0.333 | 0.352 | C=0.500 E=0.250 R=0.500 S=0.000 N=0.571 P_A1=0.500 P_A3=0.000 C2BP=True | A2 | arm_b[0] final+stages[48591]ch |
| raw_outputs_t8b.arm_b[1] | 0.306 | 0.308 | C=0.375 E=0.250 R=0.500 S=0.000 N=0.571 P_A1=0.625 P_A3=0.000 C2BP=True | A2 | arm_b[1] final+stages[41317]ch |
| raw_outputs_t8b.arm_b[2] | 0.278 | 0.282 | C=0.500 E=0.000 R=0.500 S=0.250 N=0.286 P_A1=0.500 P_A3=0.000 C2BP=True | A2 | arm_b[2] final+stages[44324]ch |

## 口径对齐证据
- **S5 cov 复现**: 本脚本=0.3889 vs 基准 0.389 → ✅ 对齐(±0.01)
- **T8b verdict 复现** (J1 dry-run: arm_a[0]=A1, arm_a[1]=A2, arm_a[2]=A3, arm_b[0/1/2]=A2):
  - ✅ raw_outputs_t8b.arm_a[0]: 期望 A1 / 实得 A1
  - ✅ raw_outputs_t8b.arm_a[1]: 期望 A2 / 实得 A2
  - ✅ raw_outputs_t8b.arm_a[2]: 期望 A3 / 实得 A3
  - ✅ raw_outputs_t8b.arm_b[0]: 期望 A2 / 实得 A2
  - ✅ raw_outputs_t8b.arm_b[1]: 期望 A2 / 实得 A2
  - ✅ raw_outputs_t8b.arm_b[2]: 期望 A2 / 实得 A2
  - **全部 6/6 复现** ✅

## A1/A2/A3 分布统计

| 组 | n | A1 | A2 | A3 | indeterminate |
|---|---|---|---|---|---|
| S0 | 10 | 6 | 4 | 0 | 0 |
| S5 | 1 | 0 | 1 | 0 | 0 |
| T8b | 6 | 1 | 4 | 1 | 0 |
| **合计** | **17** | **7** | **9** | **1** | **0** |

## 结论（只答：存量数据里三型断点分布如何）

- **S0 基线 10 条**：A1×6 / A2×4 / A3×0 / indeterminate×0。A1（winner 卡型 3090 从未进候选集）是 S0 主导断点（6/10），A2（卡型在候选集但 4×3090 配置从未构造/评估）次之（4/10），S0 无 A3（无一条把 winner 配置完整评估后排垫底）。
- **S5（节点级, cov 最高 0.389）**：判 **A2**——cov 本批最高但 winner 配置从未构造/评估，正是 coverage 陷阱样本（词汇覆盖高、结构断点在候选集粒度）。
- **T8b 6 条**：A1×1 / A2×4 / A3×1 / indeterminate×0。三型齐备（arm_a[0]=A1, arm_a[1]=A2, arm_a[2]=A3, arm_b[0/1/2]=A2），A2 占 4/6 为主导失败模式。
- **总体**：17 条中 A1×7 / A2×9 / A3×1 / indeterminate×0。A2（候选集粒度断点）是存量数据的主导断点类型；A3 仅出现在 T8b arm_a[2]（唯一把 winner 配置完整评估后又排垫底的样本）。断点分布呈 A2 > A1 > A3 的梯度，indeterminate 为 0（本批每条都落在某一断点型上）。
- **边界**：本表只描述断点类型分布，不 claim 任何质量提升/退化；S0 为 flat 自由文本（cov 为 line-as-node 口径，非节点级）。

