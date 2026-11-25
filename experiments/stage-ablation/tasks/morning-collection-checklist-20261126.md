# 过夜链收数清单（2026-11-26 早）
# origin: ai · 2026-11-25 12:45 写 · 覆盖 T-REPAIR-1 → postcheck → vllm-catchup → armc-prime-post 全链
# 用途: 明早按序收数, 每项给预期范围(基于 baseline-r1 实测), 出界=链条异常, 先查 log 再下结论。

## 0. 进程终态（全应已退出）
| PID | 角色 | 预期终态 |
|---|---|---|
| 15606 | T-REPAIR-1 executor | 退出, 12 rep 全完 (baseline/fixA/fixAB/fixB × 3) |
| 19059 | t-repair1-postcheck | 退出, 已跑 t-repair1-analysis.py |
| 36173 | vllm-catchup | 退出, C1-C4 全跑 |
| 43915 | armc-prime-post | 退出, armC' 3 样本 + screen + judge 全跑 |
```bash
for p in 15606 19059 36173 43915; do kill -0 $p 2>/dev/null && echo "$p STILL ALIVE (查为何)" || echo "$p exited"; done
```

## 1. T-REPAIR-1 4 臂（research-agi-budget ⑥ 主产出）
- 读 `experiments/stage-ablation/logs/t-repair1-4arm-*.log`（执行器）+ `logs/t-repair1-postcheck-*.log`
- 产物: `modules/B-pipeline-ablation/data/t-repair1/arms/{baseline,fixA,fixAB,fixB}/{arm}-r{1,2,3}-<ts>.json`
- **预期基线（baseline-r1 实测）**: n_nodes=300, n_rounds=3, leak_hits=0, rework≈50(angle)+47(parent-review), repair_rate≈0.06(3/50), status verified≈218/pending≈35/degraded≈47, 每 rep≈54min
- **异常检测**: 任一 rep rc≠0 / n_nodes<300 / leak_hits>0 / 某臂 3 rep 不齐 → 析因不可做, 查 executor log
- **析因结果**: `modules/B-pipeline-ablation/data/t-repair1/t-repair1-analysis.json`
  - P-B: fixB vs baseline repair_rate（claim: >3.7% 基线）
  - P-A: value_mismatch 分母=0(Q6 域) → 看 indirect（angle + 节点级是否随 A 升）
  - P-A+B: interaction ∈ {orthogonal, superadditive, subadditive}
  - discriminant: A、B 都不升 → 瓶颈在 fixer 能力/contradiction 证据
  - **TOST 读法（13:05 修正后）**: P-B 差值 CI 落在 [-0.1, +0.1] 内才可判"等效/无效"；落在外且不显著 = 功效不足（power=0.8 需 p1≈0.16，即救回 ~15 节点/臂），不下"无效"结论
- **Fix-A/B 效应方向（已预注册）**: 降 degraded 计数（baseline 缺陷=改写后过不了验证, 43/50 angle→degraded）

## 2. L4 消歧主判读（learn-to-think H1 残留机制判别）
- 读 `logs/vllm-catchup-*.log`（C1 synth-recover + C2 judge）
- 产物: `experiments/stage-ablation/runs-s5-sm-l4-disambig-synth.json`（C1 恢复）
- **判读**: C2 输出的 verdict ∈ {A, C, B, B?, D}
  - **预期: C（conf 0.7）**——4 卡出现但 A100 而非 3090（7/12 四卡在 L4 收敛层 + 全 A100×4 + 3090×4 定价候选=0）
  - A: 结论区 3090×4（概率低, 树内 0 个 3090×4 定价节点）
  - B: 仍 1-2 卡（已基本排除, 4 卡候选 12 个 + 收敛层 7 个）
  - B?: 无显式组合 → 人工核对 concl_lines
  - D: run 失败 → 重跑（换 seed 或 budget 150）
- **机制归因（已预注册）**: C 的成因=卡型×卡数耦合（3090↔低卡/A100↔高卡）, 非选择偏差; 反事实 c_pass(3090×4)/c_pass(A100×4)≈1.08 打平 → 机会成本真实
- 详见 `experiments/stage-ablation/tasks/l4-disambig-judgement-20261125.md`

## 3. armC' ε_pred 终审（learn-to-think 05-accept 重判）
- 读 `logs/armc-prime-post-*.log`
- 产物: `tasks/learn-to-think/exp03-armc/armc_prime_raw_outputs.json`（3 样本）+ `_judge.json`（eps-judge 终审）
- **两级判定**:
  - 机械屏 armc-eps-screen: flip（T3 原词表 CHAOS/DMECH/DINFO）+ ε_pred gold 轴（信息论/条件数/batch/强凸）
  - LLM 终审 eps-judge: 结构对齐（信息流角色, 防鹦鹉学舌）
- **预期**: 不确定（上次 armC ε_pred 0/3 FAIL; armC' 加了信息论轴锚点, 若仍 0/3 = 有效负结果: 27b 机制深度上限=几何层, 信息论洞察 prompt 不可达）
- **05-accept 重判**: 爬机制层✓ ∧ ε_pred≥1/3 → 过; 否则维持 REJECTED（负结果入档）

## 4. 收数顺序（依链序）
1. 进程终态（§0）
2. t-repair1-analysis.json（§1, 最重, 4 臂析因）
3. vllm-catchup log → L4 verdict（§2）
4. armc-prime-post log → ε_pred（§3）
5. 异常项先查对应 log, 再查产物文件, 最后才怀疑链条

## 5. 已知 caveat（不影响收数, 备查）
- t-repair1-analysis load_arm_runs: glob 排序不严谨（同 rep 双文件才歧义, 今晚每 rep 单文件不触发）
- l4-disambig-judge 1-2卡 regex 已修（数字在前 2×card + 中文 N张, 11-25 鉴别力测试发现）
- vllm-catchup C3 gptr 用 .venv-gptr（系统 python3 无 gpt_researcher）
- armC' prompt 只给轴名不给 gold 结论（防鹦鹉学舌, ε_pred 不退化成复述测试）

- **13:45 进度修正 → 13:58 再修正（r2 已完成，推翻"卡住"误判）**：13:45 基于 SM 事件率误判 r2 减速卡住、ETA 13-16h；实际 r2 已于 **13:48 DONE（91min）**，LLM 中位耗时与 r1 持平（2.9s vs 2.8s），慢在尾部（p90 20.4s vs 9.6s，树长→verify 批变大，max prompt 193k vs 106k），r2 调用量 755 已超 r1 全程 686。**正确 ETA：每 rep ~90min，剩 10 reps ≈ 15h → 11-26 凌晨~清晨完成**。chain gated on PID 退出，不受时间影响。判活标准：stdout mtime 持续推进 + LLM call 交替 start/done（勿用 SM 事件率，它不是限速因子）。
- **14:05 已知限制（收数时带上）**：执行器未设 Q6_REP → 检索缓存跨 rep 共享（r2 有 17 次命中复用 r1 快照）。LLM temp=0.0 确定性 + 早期树各臂对称 → 非差异化混淆，定性为已知限制不中断 run；若重跑须在 rep 循环加 `export Q6_REP=$rep`。rep_spread caveat 是运行时兜底。详见设计文档 14:05 条。
