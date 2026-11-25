# T-PR-17 pilot 正式报告（9/9 cells, r3 checkpoint, 381→719 续跑窗口）

# origin: ai · 2026-11-25 10:25 · 取代 tpr17-pilot-preview-20261125.md（PREVIEW 有两处结论被本报告的测量核验推翻，见 §2）
# 数据源: tpr17_analysis.json（9 cells, 10:18 全量重跑）+ run JSON final_tree 逐节点统计 + stdout harness 层 call 计数
# 效力声明: n=3/臂 < 5 → UNDERPOWERED 哨兵（analysis.json problems 明示），方向粗检级，非最终结论

## 1. 一句话（修正版）

**verify 是 pipeline 的主要成本中心**（新窗口 60% LLM 调用 + 70% wall time + 89% rework），砍掉它（verify-off）树结构零变化、成本大降；但本 pilot **测不出 verify 的质量价值**（搜索降级期 verify 无证据可核，三臂 corrected_claim 全 0），且 run JSON 的 token 计数器有盲区（§2），成本结论以 call 数 + wall time 为准。

## 2. 测量盲区（本报告最重要的发现，推翻 PREVIEW 两处结论）

**run JSON 的 n_llm_calls 和 tokens_total 都只数了 ~85 个 decompose 级调用，漏掉了 verify/rework 的 ~1150 个调用。**

证据链：
1. runner 的 `_wrap_call_llm` 只 patch 了 `s5_state_machine` 模块的 `call_llm` 绑定（`sm_mod.call_llm = wrapped`）。
2. 但 `verify_node` 在 `s5_pipeline.py`，有自己的 `from ablation_harness import call_llm`（L39）——verify 调用走自己的绑定，绕过计数器。
3. s5_state_machine 内部还有 7 处函数级局部 import（L166/230/264/660/750/792/834），同样绕过。
4. 铁证：stdout 的 `[LLM] call done`（ablation_harness 层打印，数全部真实 HTTP 调用）canonical ~1234-1241 vs verify-off ~491-496（差 60%），但 run JSON 的 n_llm_calls 三臂全 83-90、tokens_total 三臂全 ~615-628k（几乎一样）。

**被推翻的 PREVIEW 结论**：
- ❌ "verify-off 只省 356 tokens (0.06%)" → 真实 token 节省未测（计数器坏了），但 call 数省 60%、wall time 省 70%，方向明确。
- ❌ "n_llm_calls 三臂同量级（87/84/85）" → 该字段本身是坏的，不可用。
- ✅ 未被推翻：结构指标（n_nodes/depth/parent_link/duplicates）来自 final_tree 逐节点统计，不经 LLM 计数器，有效。

**修复（已做）**：runner 改为 patch `ablation_harness.call_llm` 模块属性（唯一咽喉点，所有 import 路径都经它）→ 正式 n≥5 跑之前计数器已修好。

## 3. 三臂实测（新窗口 382-719，386 节点；种子 381 节点三臂相同，common-mode 已剥离）

| 指标 | canonical (n=3) | verify-off (n=3) | null-control (n=3) | 解读 |
|---|---|---|---|---|
| LLM calls（stdout 真实计数） | 1234/1241/~1238 | 493/496/491 | 1252/1217/1263 | **verify-off 省 60%** |
| wall time (min) | 81/70 | 23/22/23 | 58/52/71 | **verify-off 快 3.3×** |
| 新窗口 reworked 节点 | 171/195/193 | **21/21/21** | 205/188/203 | **verify-off 砍 89% rework** |
| n_nodes | 719 | 719 | 719 | 无差异（budget 硬顶） |
| depth / depth_repaired | 4 / 5 | 4 / 5 | 4 / 5 | 无差异（clamp 常数） |
| parent_link_accuracy | 0.9804 | 0.9804 | 0.9804 | 常数（14 missing_link = gap_check bug，common-mode） |
| duplicate_nodes | 3 (1-5) | 2 (1-4) | 2.3 | 无一致方向，噪声级 |
| verified_ratio | 0.449 | 0.622 | 0.427 | ⚠️ harness 假象（§4） |
| corrected_claim 节点 | 0 | 0 | 0 | ⚠️ 三臂全 0 = 搜索降级期无矛盾证据可核，质量维度本 pilot 不可测 |
| tool_calls (search) | 36.7 | 19 | 119 | 搜索后端降级噪声（非受控变量） |

## 4. verified_ratio +0.173 仍是 harness 假象（机制不变，PREVIEW 正确）

fake_verify 无条件标 verified + rework 不触发 → 账面抬高。MWU p=0.1（非参检验不支持差异），welch p=0.003/d=10.6 是 n=3 内方差产物（臂内 3 点紧凑 → t 膨胀），效应量无意义。

## 5. sequence_mechanism_effect（TOST，D 收敛假说直接检验）——首次可判

null-control（去序列排序）vs canonical，TOST δ_min=0.1：

| 指标 | diff (nc-can) | CI95 | equivalent |
|---|---|---|---|
| verified_ratio | -0.022 | [-0.057, +0.008] | ✅ TRUE（p_low=0.005, p_high=0.001） |
| failure_rate | +0.022 | [-0.008, +0.057] | ✅ TRUE |
| depth / parent_link / n_nodes | 0 | 点（clamp 零方差退化） | ✅ TRUE（但零方差下 TOST 无信息量） |
| duplicate_nodes | 无显著差 | — | 噪声级 |

**判读**：有方差的指标（verified_ratio/failure_rate）CI 完全落在 ±0.1 内 → 去序列排序的结构效应 < 0.1 → **D 收敛假说（"序列只是搬运工?"）在 pilot 层面得到支持**。clamp 常数的 TOST 等价是退化的（零方差），不作正向证据。n=3 下 TOST 的 power 有限，正式结论需 n≥5。

## 6. 对 T4 问题的回答（"能否简化 pipeline 省预算?"）——PREVIEW 结论翻转

PREVIEW 说"pilot 不支持简化"（基于坏计数器的 0.06% token 结论）。修正后：

**成本侧强支持简化**：verify-off 省 60% 调用、70% wall time、89% rework，树结构（本窗口、clamp 条件下）零变化。
**质量侧本 pilot 不可判**：搜索降级期 verify 无证据输入（三臂 corrected=0），verify 的质量价值（矛盾检测/claim 修正/证据核验）没被测到。**不能据此说 verify 无价值**——只能说"在无搜索证据的条件下，verify 的成本远大于其可观测收益"。
**正式结论需**：① 搜索恢复后重跑（verify 有证据可核时成本-质量权衡才完整）② 每臂 n≥5 ③ 放开 depth/budget clamp（否则结构效应测不出）④ 用修好的计数器测真实 token。

## 7. 负结果/异常的价值（红队自检）

- **测量盲区发现**：排除了"token 成本三臂相同"的错误解释 → 导出设计规则：harness 计数器必须 patch 在 import 咽喉点（ablation_harness 模块属性），不能 patch 下游模块绑定。
- **clamp 边界**：结构惰性结论仅在 clamp 条件成立 → 导出设计规则：结构效应实验必须放开 depth/budget 顶。
- **搜索降级 confound**：本 pilot 全部结论限于"无实时搜索"条件 → 正式跑前必须确认 WEBLLM/DDG 恢复。
- **verify-off 的 21 个 reworked 节点**：fake_verify 下 _should_rework 仍会触发——机制是搜索降级把节点标 degraded（非 verified）→ 批次 verified rate 掉到阈值下 → angle rework。说明 rework 触发源有两个（verify 失败 + 检索失败），verify-off 只砍了前者。

## 8. 待办

1. ~~r3 落盘~~ ✅（10:18:09, 71min, 1263 calls）
2. ~~全量 9-cell 分析~~ ✅（本报告）
3. 正式 n≥5 跑：等搜索恢复 + 队列 4 实验跑完（L4/gptr/J4/ArmC 占用 vLLM）
4. 若 D 认可方向：设计"搜索恢复 + 放开 clamp"的正式 T-PR-17 实验（新 prereg）
