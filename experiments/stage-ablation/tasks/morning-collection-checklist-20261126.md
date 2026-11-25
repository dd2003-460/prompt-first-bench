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

- 18:55 夜间进度快照：baseline 97/121/93 reworks（r3 仅 229 节点），fixA 128/122/92（r3 仅 203 节点），fixAB-r1 148 reworks（300 节点）。**异常已查明**：两个 r3 节点数 <300 是因命中 `max_depth=4 hit`（深度上限，合法终止非 bug）——r3 树长得更深更早触顶。析因脚本按 rate 归一化不受影响，但 rep 间节点数不同（300/300/229、300/300/203）→ 节点级池化时勿假设等 n。

- 19:00 口径澄清（防析因混淆）：析因脚本 t-repair1-analysis.py 用**节点级**口径（rework_count>0 且 status==verified，与设计文档 §验收 一致）。stdout 的 `reworks=` 是**事件级**（含重复 rework）。r1 对照：节点级 base 50 / fixA 84 / fixAB 79（fixAB 不偏高，之前 148 事件级是重复 rework 所致，max_rework=2）。**明早只看节点级，stdout 事件级仅作监控。**
- 19:00 链条重挂：armc-prime-post 新 PID 69029（等 36173 退出 → vLLM ready → armC' 3 样本 + 机械评分 + eps-judge）。全链 4 PID 存活：15606(exec)→19059(postcheck)→36173(catchup)→69029(armc-prime)。

- 19:10 eps-judge 鉴别力测试：机械半边离线验证 PASS（POS 构造正例 HIT=7 / armC 3 负例信息论轴=0 / FP 无关语境"先验"过命中→证实两级设计必要）。判官半边挂链 PID 71865（gate 36173，vLLM 释放后 ~30s 跑完，先于 armC-prime 验证判官可信度；FAIL 则明早 armC' 判决需 D 人工终核）。
- 19:10 夜间链最终形态：15606(exec fixAB-r2)→19059(postcheck)→36173(catchup)→{69029 armc-prime, 71865 eps-judge-discrim} 同门 36173 退出后并发，eps-judge 仅 2 样本 ~30s 先完。

- 19:12 ETA 前移：fixAB-r2 18:55 完成（162n, 也命中 max_depth=4），r3 18:55 起跑中。fixAB 是倒数第二臂，最后一臂 fixB 未跑。按 ~50min/rep 估：fixAB-r3 ~19:45 完 → fixB 3 rep ~22:15 完 → **全链 ETA 从"凌晨~清晨"前移到今晚 ~22:00-23:00**（若 fixB rep 慢则顺延，明早收数不受影响）。
- 19:12 r1 机械指纹闭合（commit 70b28d7bd）：baseline directed=0（缺陷铁证）/ fixA directed=4（Fix-A ✓）/ fixAB multi-rework=25（Fix-B ✓）但 25/25 全 degraded 救回 0 → 悲观支（墙在 verify 标准非尝试次数）。r1-only 不定论。

- 19:14 t-repair1-analysis.py 真实数据预跑验证（9/12 runs, 脚本未在跑, 安全）：✅ 正确池化 9 runs + bootstrap CI + 臂数守卫（<4 臂 FATAL rc=1, 不算垃圾析因）+ 部分数据优雅降级（fixAB 2 reps/fixB 0 reps 标"不可用"）。**重要 caveat（脚本自动标, 明早必读）**：fixA rep 间修复率 spread=0.036 超过池化 CI 宽度一半 → bootstrap 把 rep 当独立样本低估不确定性 → TOST/显著性读法降权, **以 rep 级方向一致性为准**。部分文件 t-repair1-analysis.json 已落（明早真跑覆盖）。
- 19:14 gateway 重启（第 7 次）未杀后台：5 PID 全活, 无需重挂。fixAB-r3 跑到 201/831 调用。

- 19:16 ARM4 (fixB) reverse-apply 预检 PASS（/tmp 副本模拟, 不碰运行中 SM）：`git apply -R fix-a.diff` 干净 + py_compile OK + marker 门禁正确（Fix-B=1/Fix-A=0）+ diff 仅 -33/+5（只撤 Fix-A 路由, 不动 Fix-B pool 构造）。**夜间链最大单点故障（reverse 失败→FATAL→fixB 整臂丢→4 臂析因做不了）已排除**。fixAB-r3 完→ARM4 起跑时无需人工干预。

- 19:20 交叉验证手工补做（析因脚本头部声称的"stats.json 交叉验证 + q6-300 外部参照"代码未实现, 只写在注释——文档/实现落差, 明早不改脚本, 手工补）：
  ① stats.json vs 手工重算（从 runs json）：**8/8 runs 全对上**（n_rc_pos/n_verified/repair_rate 逐项一致, baseline 0.060/0.039/0.061, fixA 0.048/0.012/0.046, fixAB 0.013/0.021）→ 数据管道无损坏。
  ② **judge.err="No module named 'sentence_transformers'" 全 8 rep**：已知坑（4e9c175db, 后台 PATH 缺用户 python 目录）, 且 t-repair1-analysis.py 0 处引用 judge → **不影响主析因**。**域错配定性（19:22）**：judge_v1 的 gold 是 GPU 域（gold-gpu-units.json 36 units, COS_THRESHOLD 0.70 按 GPU gold 标定）, T-REPAIR-1 是 Q6-network-arch → 覆盖层 cosine 对 Q6 节点无效, judge 成功分数也无意义。**judge 缺口非真缺口, 明早不用补**（域错配 + 析因不依赖双保险）。
  ③ q6-300 外部参照（11-23 未修改 SM 3 reps）文件齐全, 但析因未纳入 → 明早如需"同日跨臂 vs 跨日同臂"方差对照, 手工算。
- 19:24 **跨日复现性对照（手工算, 效度点正式确立）**：q6-300 (11-23) rr=0.059/0.042/0.098, degraded=47/63/50 vs baseline (今天) rr=0.060/0.039/0.061, degraded=47/60/55。同 SM 同题隔两天同带 → **baseline 跨日复现, 4 臂析因的臂间差异可归因于 Fix 而非 baseline 漂移**。"verify 标准 × L4 经验常数结构性不兼容"的墙（degraded 47-63 量级）跨日稳定。
