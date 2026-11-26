# 任务卡 T8c-FORMAL：harness 预算修复 + V100 翻转检查 + 预注册 v2 + 正式 n=9/臂 启动

# origin: ai
# 派发: 2026-11-26 · Lead 规划 · sub 执行（长进程启动型，启动验证后 sub 退出）
# 上游: T8c smoke 停止决策（round 2，B 臂 FINAL 截断 3/3）+ 根因诊断 t8c-stop-rootcause-20261125.md

## 背景（3 行）
T8c smoke 按 pre-commit 规则停止：B 臂 FINAL 截断 100%（harness per-stage cap 4096 < 模型需求 69227，
碎片化饿死 04/04.5 阶段）。根因文档给了修复方案（MAX_B 标量→按 stage 字典，04/04.5→8192，
MAX_A 同步保持 matched 口径）。本任务 = 修复 + 重冻预注册 + 启动正式 n=9/臂。

## 只读这些输入文件（不读其他，不联网）
1. `tasks/think-trigger/exp-results/t8c-stop-rootcause-20261125.md` — 根因 + 修复方案（runner 改动点 L18/L143）
2. `tasks/think-trigger/exp-results/run_exp_t8c.py` — 待修 runner
3. `tasks/think-trigger/exp-results/t8c-preregistration.md` — 旧预注册（跑数后只读，v2 另开文件）
4. `tasks/think-trigger/exp-results/t8c-spec-final.md` — 题面终稿（冻结 2c16f644f，不改）
5. `bench/rubric-v3/tasks/T0-local-27b/reference/calc.py` — c_pass（V100 翻转检查用）
6. `knowledge-base/hardware/v100-sxm2.json` — V100 卡（price=null，conf 0.9）
7. `bench/rubric-v3/ablation/formal-matrix/blind-eval/doc-D3.md` L40 — V100 ①类价 $775–975（gpudojo 2026-10-28）
8. `tasks/think-trigger/exp-results/gold_gpu_oracle.py` — oracle（V100 翻转检查用）

## 步骤（严格按序，每步落盘 + commit）

### S1 V100 翻转检查（纯本地计算，秒级，fail-fast）
旧预注册遗留 gate："V100 实价 ③类假设（<$2033 翻转，跑前复核）"。
- 用 doc-D3 的 ①类价 **$975**（区间 $775–975 取中位）代入 calc.py/oracle，算 V100×4/W4/n=2 的 c_pass，与 3090×4/W4/n=2（0.681）比较。
- **若 V100 翻转 winner（c_pass < 0.681）→ 立即停止，落盘 `t8c-formal-blocked.md`（翻转证据 + 含义：gold 锚点在 ①类 V100 价下失效，T8c 正式跑无意义，需 Lead 决策换锚点/换题面），commit，汇报，不执行 S2-S5。**
- 若不翻转 → 落盘检查结果（数字 + 来源标注 ①类），commit，继续。

### S2 修 runner（per-stage 预算字典）
- `run_exp_t8c.py` L18 `MAX_B = 4096` 标量 → 按 stage 字典 `{**{s:4096 for s in STAGES}, "04":8192, "04.5":8192}`（根因文档方案 3）。
- 同步 `MAX_A` 保持新 matched 口径：B 总预算变为 4096×4+8192×2=28672，MAX_A 同步 28672（等总预算，token-matched 设计不变）。
- 改完跑 runner 的 selfcheck（若有）或 dry-run 单 stage 验证字典生效（日志里能看到 per-stage cap 值）。
- commit。

### S3 预注册 v2（另开文件，旧预注册只读）
`tasks/think-trigger/exp-results/t8c-preregistration-v2.md`，相对 v1 的修订：
- ① 预算口径：per-stage 字典（04/04.5=8192，其余 4096）+ MAX_A=28672 matched。
- ② 新增第四断点型："计算对但综合断"（run0 已算出正确 winner 0.6798≈gold，死在 04.5 说出来）——Stage 0 机械检查增加：B 臂 04.5 截断但 04 已含正确 winner 的样本单独归类（不计入作废，计入"综合断"桶）。
- ③ secondary endpoint：三型断点分布（A1 候选构建断/A2 评估断/A3 排序分歧），工具 `research/judge_pipeline_v0.py`（`python3 judge_pipeline_v0.py <run文件> --qid gpu`），存量基线 17 条 A1×7/A2×9/A3×1 作对照先验；A3 稀有（n=9 功效低），判据写明"A3=0 不当无 A3"。
- ④ n=9/臂，Stage 0 截断率 ≤50% 机械检查保留。
- 冻结：文件头写冻结时间 + 派发时 HEAD commit。commit。

### S4 启动正式跑（长进程，脱离会话）
- `setsid nohup python3 tasks/think-trigger/exp-results/run_exp_t8c.py --n 9 > tasks/think-trigger/exp-results/t8c-formal-run.log 2>&1 &`（参数名以 runner argparse 实际为准，先 `--help` 核对）。
- 把真实 PID + 启动时刻写进 `t8c-formal-state.json`（status=running, pid, started_at, prereg_ref=v2 commit, v100_price_ref=doc-D3 ①类）。

### S5 验证真的在跑（三项判据，缺一不可）
1. `ps -o pid,etime,command -p <PID>` 活着。
2. log 有新行（>启动时刻，非缓冲假象）。
3. 第一个 stage 的 checkpoint/输出文件落盘（新于启动时刻）。
- 三项全过 → commit state 文件 → 汇报。
- 任一不过 → 排查（进程死了看 log 尾部 traceback），修不好就落盘失败证据 + 汇报，不硬启。

## 硬约束
- vLLM 8787 是本任务独占（当前无其他 vLLM 消费者）；启动前 `curl -s http://127.0.0.1:8787/v1/models` 确认可达。
- 跑数后预注册只读（v2 冻结后不改，post-hoc 另开文件）。
- 每步增量 commit（防截断丢工作）。
- 最终汇报 ≤15 行：S1 翻转结论 / S2 runner commit / S3 v2 commit / S4 PID+state / S5 三项判据结果。

## 验收（Lead 对照核）
- [ ] S1：V100 翻转检查数字落盘（或 blocked 文件）
- [ ] S2：runner diff 显示 per-stage 字典 + MAX_A=28672，commit 在
- [ ] S3：v2 预注册 4 项修订齐全，冻结头在
- [ ] S4：state 文件含真实 PID + started_at
- [ ] S5：三项判据证据（ps 输出 + log 尾部 + checkpoint 文件时间戳）
