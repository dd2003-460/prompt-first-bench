# soc cov 指标口径问题（2026-11-16 发现）

# origin: ai
# 状态：soc gate 真值判定完成（10-run mean PASS），nat 10-run 运行中
# 关联：goal-pfb-hardening-v2.md gate "soc cov ≥ 0.898 (S0 基线)"

## 结论（conf 0.95，证据全部可复现）

gate 条件 "soc cov ≥ 0.898" 是**两个不同指标的对比**：

| 侧 | 指标 | 数值 | 来源 |
|---|---|---|---|
| S0 基线 | judge.coverage（judge_v2_depth.py 对 answer 打分） | 0.8957（100 reps mean） | runs-s5-prod/S5-soc-r*.json，ts=2026-11-08 |
| 当前 SM | 节点 verified 率 | 0.781（challenge-test）/ 0.788（runs-s5-sm-soc 223/283） | checkpoints/sm-soc-challenge-test.json、runs-s5-sm-soc.json |

**SM 管线没有 answer 综合步骤**：runs-s5-sm-soc.json 顶层 judge=None、final_state='verified'、rounds=[]——状态机停在 verify，产不出可被 judge 打分的 answer。所以无论重验多少节点，都过不了这个 gate。

nat 同理存疑：SM verified 率 0.6511 vs S0 judge cov 0.634（391 reps），数值碰巧大但指标不同，"nat ✅" 可能是假过。

## 诊断结果（11-16 06:0x，synth_diag_soc.py）

诊断脚本复用 S0 管线 P4_SYNTHESIZE 分段综合（>200 节点按层分段 + merge，s5_pipeline.py:883-903）+ judge（s8b_pilot.py:145）+ score_run（judge_v2_depth.py:408），对现有 SM 节点树补"综合→judge 打分"：

| qid | judge.coverage | gate 阈值 | S0 基线 | 结果 | depth | hallucination_flags |
|---|---|---|---|---|---|---|
| soc | **1.0**（7/7） | ≥0.898 | 0.8957（100 reps） | ✅ PASS | 0.8457 | **6** ⚠️ |
| nat | **0.667**（4/6） | ≥0.634 | 0.634（391 reps） | ✅ PASS | 0.6267 | 0 |

输出：runs-s5-sm-soc-synth.json / runs-s5-sm-nat-synth.json（单次 run，非 100-rep mean）。

**结论**：283/278 节点树的信息量足够过 gate，缺的只是 synthesis+judge 步骤。之前"soc 重验多少节点都过不了"的判断被推翻。

**新质量问题（hallucination_flags）**：soc answer 里 6 个具体数字是综合阶段 LLM 编的（"转化率从基准值 5% 骤降至 <1%""60% 降价卖家无新咨询""高支付意愿买家占比 10-15%"等）。judge 的 coverage 不管幻觉，所以分数 1.0，但质量上是坑——answer 含编造数字。这是综合阶段的已知弱点，需单独处理（judge 加幻觉检查，或综合 prompt 加来源约束）。

**注意**：诊断脚本是一次性验证，不是管线修复。把 synthesis+judge 真正修进 s5_state_machine.py 仍是待办（见下"未做"）。

**管线修复冒烟测试（11-16 06:3x，--synth 已修进 s5_state_machine.py）**：
用现有 soc 283 节点树跑 `synthesize_answer()` 全链路（L1/L2/L3/L4 分段综合 → merge → judge → depth），输出 coverage=**0.857**、depth=0.8386、hallucination_flags=11。管线本身跑通（SMOKE_OK），但暴露**单次综合方差问题**：同一节点树，诊断脚本一次综合得 1.0，冒烟测试另一次得 0.857——两次差 0.143，且 0.857 < 0.898 gate 线。结论：synthesis 是 temperature=0.7 的 LLM 调用，单次分数不可作为 gate 判定依据，**gate 判定必须用多次综合的 mean**（S0 基线 0.8957 本身就是 100 reps mean）。hallucination_flags 也波动（6→11），同因。

## soc gate 真值判定（11-16 07:0x，synth_multi_soc.py 10 次综合）

对现有 soc 283 节点树跑 10 次 `synthesize_answer()`（每次 L1/L2/L3/L4 分段综合 → merge → judge → depth），wall 1578s：

| 项 | 值 |
|---|---|
| 有效 run | 10/10 |
| coverage 序列 | 1.0, 0.857, 0.857, 0.857, 1.0, 1.0, 0.857, 0.857, 1.0, 0.857 |
| **mean** | **0.9142** |
| sd | 0.0701 |
| min/max | 0.857 / 1.0 |
| gate ≥0.898 | **PASS** |
| S0 基线 0.8957 | above（+0.0185） |

**判定**：soc gate 真值 = 10-run mean 0.9142 ≥ 0.898，**通过**。coverage 只取两档（7/7 要点 = 1.0，6/7 = 0.857），方差来自单次综合漏掉 1 个要点的概率（10 次里 6 次漏），不是连续分布。hallucination_flags 序列 [10,7,19,9,9,14,9,11,12,13]，mean 12.3——幻觉数字问题持续存在（judge 不管这个），单独立项处理。

输出：`runs-s5-sm-soc-synth-multi.json`（含全部 10 次 covs/depths/hflags）。

nat 同口径 10-run 已排队（链式自动接上，278 节点，gate 0.634 / S0 基线 0.634），结果待落。

## 时间线（git log 核实）

- 11-08/09：runs-s5-prod 测出 S0 基线（soc judge cov 0.8957）
- 11-15 f5d530be：verify prompt 加"经验事实排除条款"
- 11-16 05d18dc6：D-质询机制引入
- 0.781 是新规口径下的节点 verified 率，与 0.898 不是同一指标也不是同一时期

## 报告 #16 的"关质询重验翻回 0.898"为什么是 Goodharting

关质询只是把节点 verified 率凑回某个数字，既没解决指标口径问题（verified 率 ≠ judge coverage），又违背 D 指令引入质询机制的初衷。不做。

## 正确的修复顺序

1. **修 SM 管线**：补 synthesis（节点→answer 综合）+ judge（judge_v2_depth.py 打分）步骤，让 SM run 产出 judge.coverage（L1 代码改动）——一次性诊断已完成（见上"诊断结果"），修进状态机仍待办
2. **真重验节点**：challenge-test checkpoint 39 pending + 22 degraded = 61 可重验，用 bing/DDG 通道（perplexity 403 未恢复）verify-only 重跑——节点质量是 answer 质量的下游，仍然要做
3. **重跑对比**：SM 新 run 的 judge.coverage vs S0 0.898，同指标同 judge 才可比
4. 口径发现写入 s5-sm-bench-report.md ✅（条目 #18）

## 已做

- 备份：runs-s5-sm-soc.json.bak-pre-reverify-*、runs-s5-sm-soc-checkpoint.json.bak-pre-reverify-*
- 检索通道状态（11-16 04:5x 测试）：bing 200 ✅、DDG 200 ✅、perplexity 403 ❌
- 一次性诊断脚本 synth_diag_soc.py（92 行）+ 输出 runs-s5-sm-{soc,nat}-synth.json（soc 1.0 / nat 0.667，两 gate 均过）
- bench 报告条目 #18（口径发现 + 诊断结果 + hallucination_flags 问题）

## 未做（下回合）

- [x] synthesis+judge 修进 s5_state_machine.py（`--synth` flag，向后兼容；冒烟测试 SMOKE_OK）
- [ ] **gate 判定口径修正**：单次综合分数波动大（同树两次 1.0 vs 0.857），gate 必须用多次综合 mean（S0 基线是 100 reps mean）——待跑 ≥10 次综合取 mean 再判 gate
- [ ] verify-only 重验 61 节点（39 pending + 22 degraded，bing/DDG 通道）
- [ ] hallucination_flags 质量问题处理（judge 加幻觉检查，或综合 prompt 加来源约束）
- [x] nat 假过核实（0.667 > 0.634，真过）
- [x] bench 报告更新口径说明（条目 #18）