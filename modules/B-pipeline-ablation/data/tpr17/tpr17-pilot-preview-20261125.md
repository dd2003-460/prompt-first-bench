# T-PR-17 pilot 初步读数（PREVIEW，n=3 哨兵级，非最终结论）

# origin: ai · 2026-11-25 10:05 · 8/9 cells 落盘时跑 tpr17_analysis.py 的初步解读
# 数据源: modules/B-pipeline-ablation/data/tpr17/tpr17_analysis.json（本文件生成时刻, null-control 仅 2 reps）
# 状态: null-control r3 在跑（~10:00 完），完成后重跑 tpr17_analysis.py 出全量版，本文件被其取代

## 一句话

**在 381→719 续跑窗口内，verify/rework 阶段结构上惰性、成本上中性**——关掉 verify（verify-off 臂）不改变树结构、不省 token；verified_ratio 的 +0.173 差异是 harness 假象（见下），不是质量信号。

## 三个臂的实测（r3 checkpoint, 381 续跑至 budget 719）

| 指标 | canonical (n=3) | verify-off (n=3) | null-control (n=2) | 解读 |
|---|---|---|---|---|
| verified_ratio | 0.449 (0.434-0.474) | 0.622 (0.616-0.629) | 0.432 (0.417-0.447) | ⚠️ verify-off 高 +0.173，**harness 假象**（机制见下） |
| depth | 4 | 4 | 4 | 无差异（budget-clamp 338/381 节点，max_nodes=719 硬顶） |
| parent_link_accuracy | 0.9804 | 0.9804 | 0.9804 | **常数**（14 个 missing_link = gap_check bug 坏链，三臂 common-mode，t5_impact.json 已记录） |
| n_nodes | 719 | 719 | 719 | 无差异（budget 饱和） |
| duplicate_nodes | 3 (1-5) | 2 (1-4) | 1.5 (1-2) | 无一致方向，噪声级 |
| tokens_total | 622,933 | 622,577 | 615,541 | **verify-off 只省 356 tokens (0.06%)**——续跑窗口 verify 调用占比极小 |
| n_llm_calls | 87 | 84 | 85 | 同量级 |
| tool_calls (search) | 36.7 (19-69) | 19 | 119 (116-122) | ⚠️ **搜索后端降级期噪声**（WEBLLM/DDG broken，half-open probe 随机命中），非受控变量 |

## verified_ratio +0.173 的机制拆解（为什么是假象）

1. **fake_verify 直接标 verified**（runner L104-110 monkey-patch）：verify-off 臂所有进 verify 批次的节点无条件 status=verified → 账面 verified 比例机械抬高。
2. **rework 不触发**（patch docstring 明示）：canonical 臂 verify 失败的节点进 rework 周期重开成 pending（design notes L22 已记录 verified 状态非单调）→ canonical 账面 verified 比例被 rework 压低。
3. **搜索降级放大**（confound）：pilot 全程 WEBLLM/DDG broken（tpr17-search-degradation-20261125.md），canonical 的 verify 调用拿不到新证据 → 更多节点留在 pending → 差距被无搜索条件放大。**恢复搜索后此差距预期收窄**。

⟹ verified_ratio 在本实验里测的是"账面核验状态"，不是"节点质量"。质量要看结构指标——结构指标全部无差异。

## 统计效力声明（design notes 铁律）

- n=3/臂 < 5 → **UNDERPOWERED 哨兵**（analysis.json problems 字段明示），只能读方向粗检，不可下最终结论。
- welch_p=0.003 / d=10.6 是 n=3 内方差的产物（臂内 3 点恰好紧凑 → t 膨胀），**效应量无意义**。
- sequence_mechanism_effect（TOST 等效性，D 收敛假说直接检验）：null-control 仅 2 reps → estimator 被 guard 成 None，**r3 落盘后才可判**。

## 对 T4 问题的初步回答（"能否简化 pipeline 省预算?"）

**pilot 不支持简化**：verify-off 省 0.06% token（噪声级）、结构零差异 → 在续跑窗口 verify 既无可见成本也无可见收益。但"无可见收益"≠"无收益"——本窗口的 rework 只影响少数节点，且搜索降级剥夺了 verify 的证据获取能力（verify 的价值恰在证据核验）。**正式结论需：① 每臂 n≥5 ② 搜索恢复后重跑 ③ 全预算窗口（非仅续跑段）**。

## 待办（null-control r3 落盘后）

1. 重跑 `python3 experiments/stage-ablation/tpr17_analysis.py --out modules/B-pipeline-ablation/data/tpr17 --checkpoints r3` → 全量 tpr17_analysis.json（9 cells）
2. 读 sequence_mechanism_effect TOST 结果（depth 判等效 power 仅 17% @n=3，判不等效只能读 underpowered；verified/parent_link 判等效才是正向证据——power_note 已量化）
3. 出正式 pilot 报告（取代本 PREVIEW），含搜索降级 caveat + n=3 效力声明
