# 状态机现状报告（v18/T53 + v19 langgraph）

> origin: ai · 2026-11-26 · 回答 D 问「状态机到底怎么样，lg 和 pfb 的，能使用吗，效果如何」
> 口径基准：S5 canonical = v3 gate-fixed（n=90，same-source 27B judge，S5≈0.579 / S0≈0.397，`modules/A-eval-infra/research/scoring-v3-gatefixed.md`）

## §1 两版本现状

| | v18/T53 | v19 langgraph |
|---|---|---|
| 文件 | `experiments/stage-ablation/s5_state_machine.py` | `experiments/stage-ablation/langgraph-pfb-full.py` |
| 机制 | 5 状态 {IDLE,DECOMPOSE,VERIFY,REWORK,STOP} + 3 机器判定（J_necessary/J_verify/J_stop），目标函数 S_α 驱动 | langgraph 控制流 + sqlite checkpoint（SqliteSaver）+ 5 轮循环 |
| 最近 commit | `112b03f38` 2026-11-19 15:30 「feat(s5-sm): --beta N CLI 参数（β=0 复现 v13 无冗余惩罚）」；此前 `8975685d6` synth 修复 v2、`bfe29a7c9` T53 验收 4/7 | `3c30e8521` 2026-11-19 02:38 「修 recursion limit（nat N254 超限挂了）」；此前 `b0fb66a29` WIP |
| 是否在跑 | 否（`ps aux \| grep -E 'state_machine\|langgraph'` 无匹配，2026-11-26 14:xx 实测） | 否（同上；/tmp 仅剩 11-19 的 sqlite-wal 残骸） |
| 数据目录 | `ablation-runs/gpu_formula_r{NN}*.json` + `runs-s5-sm-*.json` + `runs-qc-compare/` + `checkpoints/sm-*` | 应产出 `runs-langgraph-pfb-{qid}.json` —— **磁盘上不存在**（VERSION.md 引用的 nat 结果文件缺失，只剩 `/tmp/langgraph-pfb-full-nat.sqlite-wal` 11-19 03:01） |

**v19 checkpoint 抢救（11-26 14:30 新增）**：主 `.sqlite` 已删，但 WAL 帧含完整页镜像，可重建——用空库 + 同名 WAL 让 sqlite 回放，成功恢复 `checkpoints`(6 行) + `writes`(14 行)，ormsgpack 解码全部 checkpoint 成功。**三个节点数是三次不同事件，不是一次 run**（按精确时间戳厘清）：① **N254**（fix commit `3c30e8521` 02:38 之前）= 原始全量 nat run 撞 langgraph recursion limit 挂掉，**数据已失**（无 WAL 幸存）；② **~N25**（抢救出的 WAL，thread `pfb-full-nat`，末写 11-19 03:01:32，**在 fix 之后**）= 修复后的 run，跑到 round 1 verify 中途停下：`round=1`/`stop=False`/`pending_verify=[N5..N25]`（21 个）/`rounds_log=[]`，**未跑完**。关键：fix `3c30e8521` **仅改 recursion_limit 25→300**（单文件 5+/1-，`git show` 实测），故 round 1 停**不是** recursion limit 复发，是**另一停因**（静默死亡 / 8787 代理 502 / verify 卡住，WAL 无 stop_reason 字段，无法定因）——这正是 §4「重跑+加日志」要解的；③ **559 节点/verified_rate 70.5%**（VERSION.md 15:24 由 `e09fac301` 写入）= 事后文档声称，**磁盘无任何对应产物**，无法证实（可能源自 ① 那次 N254 run 的 stdout 日志，未落 json）。脚本 `--max-nodes` 默认 None（用原生 ObjectiveConfig），故 ② 不是被 cap 截断的小 smoke，是真实跑到 round 1 的自然停止。**结论：v19 唯一可考的落盘 run（②）只到 round 1，无可判分数据；①③ 均无数据。** 抢救库留档：`/Users/a1-6/.hermes/cache/scratch/lgtest/`（临时目录，24h 清理；要长期留需复制进仓）。

## §2 效果数据表

口径标注：`total`=judge overall（逐点加权，v18 ablation-runs 口径）；`cov`=gold 要点覆盖率；`depth`=depth_score 连续分；`gate`=S0 基线门限（synth-multi 口径，与新 GOLD 重判 S0 对齐，nat 0.5801 / soc 0.898）。与 canonical 0.579（n=90 总分）不同口径，跨行比较只看方向。

| 版本 | runs 目录/文件 | 题 | n | depth | cov | total | leaks/备注 |
|---|---|---|---|---|---|---|---|
| v18 | `ablation-runs/gpu_formula_r01-r08`（r06 缺） | gpu | 7（6 有效） | — | — | mean **0.393**（r01 .395/r02 .351/r04 .509/r05 .395/r07 .402/r08 .310；**r03 实为 judge 伪影**：raw 100 点全 0.33→真实覆盖≈0.33，但 point_scores 全 0 致 overall=0.0，剔除后 6 有效） | nodes 114-440，final_state 全 rework；旧格式无 leak 字段 |
| v18 | `runs-qc-compare/{nat,soc,gpu}-pfb-sm-qc.json` | nat/soc/gpu | 3 | 0.888/0.716/0.463 | 1.0/1.0/0.2 | — | nodes 244/264/263，verified_rate 0.873/0.735/0.578 |
| v18 | `runs-s5-sm-nat-synth-multi.json`（11-26） | nat | 10 | mean 0.627-0.668 | mean **0.517** sd 0.263 | — | gate 0.5801 → **FAIL**（2 个 rep cov 0.167 拉低） |
| v18 | `runs-s5-sm-soc-synth-multi.json`（11-26） | soc | 10 | mean 0.802 | mean **0.914** sd 0.070 | — | gate 0.898 → **PASS** |
| v18 | `runs-s5-sm-{nat,soc}-synth.json`（11-16 单跑） | nat/soc | 1/1 | 0.627/0.846 | 0.667/1.0 | — | 单跑均过 gate（nat 0.634 / soc 0.8957） |
| v18 | `runs-s5-sm-l4-disambig-synth.json`（11-25 恢复） | l4 | 1 | null | 1.0 | — | synth 曾崩（GOLD KeyError），仅恢复 synth+judge，树未重跑 |
| v18 | `runs-s5-sm-q7-rd-judge-final.json` | q7-rd | 1 | — | 0.8（8/10 要点） | — | 51 节点/19 verified 终盘判分 |
| v18 | `runs-s5-sm-q8-nvda.json` | q8-nvda | 0 | — | — | — | **blocked**：沙箱无 8787 生成端/1234 judge 端点（环境问题，非代码） |
| v18 smoke | （lineage 报告引用 sm-modification-log） | — | — | — | — | — | smoke v5=75 nodes/2 rounds/0 leaks；r7=133 nodes/2 rounds/0 leaks |
| v19 | `runs-langgraph-pfb-nat.json`（**缺失**）+ `/tmp/...sqlite-wal` 抢救 | nat | 1（未完成） | — | — | — | 抢救 WAL（fix 后 03:01 重跑）：round=1/stop=False/pending_verify 21 个(N5-N25)/~25 节点，死于 verify 中途；另有 N254 撞 limit 挂的更早 run（数据已失）；VERSION.md「559 节点/verified 70.5%」无产物可证 |
| v19 | `runs-langgraph-pfb-gpu.json`（**缺失**） | gpu | 0 | — | — | — | VERSION.md 标「在跑」，无产物 |
| v19 | `runs-qc-ablation{,-smoke}/step-log/`（A0-A13 矩阵） | nat/gpu | 0/126 | — | — | — | 仅 A0 臂 decompose 步日志（nat 20 节点/gpu 50 节点，11-18 07:xx），126 runs 实质未跑 |

## §3 能否使用判定

**v18/T53：工程上能用，效果未达 S5 基线；官方验收 4/7（11-16），3 项未过中 1 项已修。**
- 能跑通：✅ 稳定。多题（nat/soc/gpu/q6/q7/l4）完整跑通，0 leaks，checkpoint/resume、synth/judge 链齐全，`--beta` 消融臂可用。
- **官方验收（一手来源 `loop-artifacts/stages/05/T53-05-accept.md`，2026-11-16，Lead 逐项核验）：4/7 过，不 complete**——AC1 节点效率 ✅（gpu 163 节点 ≤200，v17 是 1930）/ AC2 防泄漏 ✅ / AC3 核验覆盖≥90% ⚠️（soc 0.982、gpu 0.953 ✅，**nat 0.649 ❌**，70 节点 pending，归因 8787 proxy 502 中断非状态机逻辑缺陷）/ **AC4 打赢 SOTA ❌ 未跑**（需 ≥5 题，当前 0 题完成，SOTA 基线分数 [待核验]）/ AC5 返工生效 ✅（gpu 40 次 rework 有翻回 verified）/ AC6 SOP 落盘 ✅ / **AC7 可复现 ❌→已修**（`random.sample` 无 seed，`bfe29a7c9` 加 SM_SEED 环境变量，向后兼容；LLM 采样侧可复现性受 8787 后端限制 [待核验]）。
- 阻塞：无代码级阻塞。AC4（SOTA bench ≥5 题）是唯一实质未启动项，8787 单路串行每题 1-2h；q8-nvda blocked 是沙箱无 LLM 端点（环境）；l4-disambig synth 崩溃已恢复但树未重跑。
- 效果方向（vs 基线）：
  - gpu 题：v18 judge total mean 0.393 ≈ v13 判决 0.389（flat，略好），**显著低于 S5 基线 0.579**（-0.186，注意口径不同：逐点 overall vs n=90 总分，方向可信绝对值不可直接比）。
  - nat 题：synth-multi mean 0.517 < S0 门限 0.5801 → FAIL，且方差大（sd 0.263，10 个 rep 里 2 个 cov 0.167）。**注意：验收文档 §4 指出后 5 个 run（0.333/0.167/0.333/0.167）幻觉标记 hf 从 2-3 涨到 5-13 = 8787 长会话质量漂移，混了基础设施噪声**——0.517 不能直接当管线能力用，需 8787 稳定窗口重跑确认。
  - soc 题：0.914 > 0.898 → PASS（soc 题难度/门限与 canonical 题集不同，不与 0.579 直接比）。
- 一句话：状态机本身是可靠的执行底座（不漏、可恢复、可复现），但产出质量在 gpu/nat 题上没打过 v13/S5 基线——问题在质量不在可用性。
- **nat 弱项根因（11-26 14:35 诊断，节点级定位）**：nat 的高方差是**双因**——① 概念混淆 + P4 选错节点（系统性，见下）；② 8787 长会话漂移（后 5 run hf 5-13，基础设施噪声，验收文档 §4 已记录）。①的证据：逐点看 5 个诊断 rep（`runs-s5-sm-nat-points-diag.json` 3 + `runs-s5-sm-nat-lowdiag.json` 2，6 点 gold）：要点 3（LFU 频率表因 1%/天更新而老化）**5/5 全 0**、要点 5（1%/天更新率 → ~100 天失效/驻留量级）**5/5 全 0**、要点 4（字节 vs 请求命中率口径分离）3/5 过；要点 1/2/6 稳定过。**节点级证据（`runs-s5-sm-nat.json` 278 节点）**：正确的 100 天节点**存在且已 verified**——N247(L4) 明写「u=1%/天 → 每对象平均每 100 天被替换一次新内容」；但树里同时有竞争节点 N28/N58/N60 用 T_res=缓存驻留(1.5-3.7 天) 算 P(stale)≈1.5-3.65%。**P4 综合时选了 T_res 驻留口径、丢了 N247 的 100 天更新间隔口径**——把「对象在缓存里待多久」(dwell) 和「对象内容多久后被更新/失效」(1/u=100 天) 混为一谈。要点 3 则树里只有 2 处 stale 提及、缺「LFU 频率表老化」的具体机制表述（材料偏弱）。**修法**：① P4 prompt 强制「驻留/失效量级须区分 dwell(T_res) 与更新间隔(1/u) 并分别报告」；② 树层让 decompose/verify 显式消解 N247 vs N28/N58 的概念冲突（二者答的不是同一问题）；③ 补 LFU 老化机制节点；④ 8787 稳定窗口重跑 nat synth-multi 剥离基础设施噪声后再判 gate。与 v13 P4 口径分离根因（commit `2db5f907`）同类但更细：不是漏推导，是**同树两个口径并存、综合选错了**。

**v19 langgraph：当前不可用（无有效数据 + 未验证跑通 + 唯一 run 抢救证实未跑完）。**
- 能跑通：❌ 未验证且证据偏负。精确时间线（11-19 当天）：原始全量 nat run 在 N254 撞 recursion limit 挂（数据已失）→ 02:38 修 limit（`3c30e8521`）→ 03:01 修复后重跑（即抢救出的 WAL），只到 round 1 verify 中途（~25 节点、21 个 pending_verify、stop=False）就停了 → gpu 跑无产物。修复后从未有完整成功 run 落盘。
- 阻塞：① nat 结果 json 缺失（checkpoint 已从 WAL 抢救，但只到 round 1，无法判分；且「559 节点/70.5%」无产物可证）；② A0-A13 消融矩阵 126 runs 只留下 A0 臂 decompose 步日志，实质 0 完成；③ 无近期运行记录（11-19 后 7 天无动静）；④ 03:01 那次 run 为何在 round 1 停下（stop=False 无 stop_reason）未查明——可能是进程被杀/超时，也可能是 verify 环节 hang，需重跑时加日志确认。
- 效果：无正式分数可比，且唯一可考的 run 未完成、无判分。

## §4 下一步

1. **v19 重跑落盘**（最高优先）：按 `cc-tasks/langgraph-verify.md` 任务书跑 nat+gpu（`--max-nodes 12 --max-depth 2` 先 smoke 验证修好的 recursion limit，再全量），确保 `runs-langgraph-pfb-{qid}.json` 落盘。WAL 抢救已完成（见 §1 新增段）：唯一可考 run（fix 后 03:01 那次）只到 round 1 且 stop=False 无 stop_reason（停止原因未查明，重跑时加日志），无可判分数据，**必须重跑**；抢救库在 scratch 临时目录，如需留档复制到仓内。
2. **A0-A13 矩阵补齐**：126 runs 目前 0 完成，至少先跑 A0/A1/A2 基线三臂×3 题，拿到质询/分析层/质检门的消融方向。
3. **v18 gpu 题（r03 已定性）**：r03=0.0 是 **judge 聚合伪影**（raw 100 点全 0.33→真实覆盖≈0.33，point_scores 却全 0 致 overall=0.0），非真实 0 分，应从均值剔除（已剔，6 有效）。真实问题在 6 有效 rep 方差 0.31-0.51 + 偏低（mean 0.393 < S5 0.579）：需逐点看低分 rep（r02 .351/r08 .310）是节点质量还是判分口径，与 nat 的 P4 选错口径问题是否同源。
4. **v18 nat 题（已定位根因，节点级，见 §3）**：高方差 = 概念混淆（dwell T_res vs 更新间隔 1/u）+ P4 选错节点。正确节点 N247(100 天, verified) 在树里，但 P4 综合选了 N28/N58/N60 的 T_res 驻留口径。修 = ① P4 prompt 强制区分 dwell/更新间隔并分别报告；② decompose/verify 显式消解同树概念冲突；③ 补 LFU 老化机制节点（要点 3 树材料偏弱）。修完重判 nat synth-multi 看 mean 是否过 0.5801 门限。
5. **口径统一**：v18/v19 要与 S5 0.579 可比，需在同一 judge + 同一题集（canonical n=90 口径）下重判，当前各行口径混杂（已在 §2 标注）。
