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

## 补充分析：cov↔verdict 关系（17 条扩展集, 仅描述关系, 非质量 claim）

- **cov 均值按 verdict 单调**：A1×7 均值 0.179 < A2×9 均值 0.259 < A3×1 均值 0.278。
  A2（候选集粒度断点）cov 系统性高于 A1（winner 卡型从未进候选集）——A2 词汇覆盖到了 gold 单位,
  但断点在"winner 配置从未构造/评估"层, 正是 coverage 陷阱的量化形态。
- **cov 最高样本 = A2**：S5 cov=0.389 为全批最高, verdict=A2——最高覆盖的样本恰好是断点样本,
  单看 cov 会误判"覆盖最好", 三型判别把它暴露出来。
- **Pearson(cov, CORR) = 0.462**（n=17）：cov 只解释 CORR 方差的一部分, 两轴互补非冗余——
  这是"为什么需要 correctness 层"的定量依据（coverage 单轴不足以定位断点）。
- **S0 flat cov 系统性低于 S5**：S0 10 条 cov ∈ [0.056, 0.222]（mean 0.158, line-as-node 口径）,
  全部 < S5 节点级 0.389——flat 自由文本无节点结构, cov 口径不可与 S5 节点级直接横比。

## 交叉验证：S0 cov 口径独立核验（J1 cov_score 重算, 10/10 一致）

J1 dry-run 只报了 T8b+S5 的 cov（上文已 100% 复现）；S0 10 条 cov 是本整合层自算、J1 未报过。
本轮用 J1 的 `cov_score` 函数（独立于本整合层, 同一份 gold-gpu-units.json 36 单元）对 S0 逐条重算,
与本整合层报值对账——**10/10 完全一致**：

| sample | J1 cov_score | 本整合层 | 一致 |
|---|---|---|---|
| S0-gpu-r1 | 0.222 | 0.222 | ✅ |
| S0-gpu-r2 | 0.111 | 0.111 | ✅ |
| S0-gpu-r3 | 0.056 | 0.056 | ✅ |
| S0-gpu-r4 | 0.139 | 0.139 | ✅ |
| S0-gpu-r5 | 0.194 | 0.194 | ✅ |
| S0-gpu-r6 | 0.139 | 0.139 | ✅ |
| S0-gpu-r7 | 0.222 | 0.222 | ✅ |
| S0-gpu-r8 | 0.139 | 0.139 | ✅ |
| S0-gpu-r9 | 0.167 | 0.167 | ✅ |
| S0-gpu-r10 | 0.194 | 0.194 | ✅ |

**意义**：cov 口径对齐从 T8b/S5（J1 已报, 复现）扩展到 S0（J1 未报, 独立重算核验）——
本整合层在 flat/nested/t8b 三类 schema 上 cov 均与 J1 同源（同一 gold 文件 + 同一非空行节点构造 +
同一 COS≥0.7 阈值）。correctness 轴（CORR/verdict）纯规则无模型, 本就与 J1 同函数（`judge_text`）,
无口径漂移风险。→ 整合层 17 条联合分（cov+CORR+verdict）口径可信, 可用于后续跨 run 比较。
