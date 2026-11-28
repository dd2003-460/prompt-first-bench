# T8c smoke 重跑任务卡（2026-11-26）

# origin: ai · Lead 规划产出 · 执行者纯执行

## 任务
新锚点（V100 $704 / winner V100×4/W4/n=2）+ MAX_A 73728 下重跑 T8c smoke（n=3/臂），产出新 raw_outputs_t8c.json + t8c-smoke-eval.json。

## 前置（先核，任一不过 → 回执报 T-失配，不执行）
1. `grep -n "^MAX_A" tasks/think-trigger/exp-results/run_exp_t8c.py` 显示 `MAX_A = 73728`（ReAnchor-A 已改）。
2. `git log --oneline -3 | grep -i reanchor` 有 ReAnchor-A 的 commit（锚定已落盘）。

## 执行方式（严格按序）
1. 备份旧数据：`cp raw_outputs_t8c.json raw_outputs_t8c.pre-rerun.json && cp t8c-smoke-eval.json t8c-smoke-eval.pre-rerun.json 2>/dev/null; true`
2. 后台起跑（macOS 无 setsid，用 nohup）：
   `TS=$(date +%Y%m%d-%H%M%S); nohup python3 run_exp_t8c.py all > t8c-smoke-rerun-$TS.log 2>&1 & echo $! > t8c-smoke-rerun.pid`
   把 PID 和日志文件名记入回执 evidence。本 tick 到此为止（跑约 30-60 分钟）。
3. 后续 tick 接力：`kill -0 $(cat t8c-smoke-rerun.pid)` 探活；日志出现 `WROTE arm_b + finished` = 完成。
   进程死且无 finished 行 → 查日志尾部定位死因，记入回执，status=failed 报因（不盲目重跑，同一死法 2 次=换路报监督者）。
4. 完成后跑 eval：`python3 eval_t8c_smoke.py raw_outputs_t8c.json`（写 t8c-smoke-eval.json）。

## 验收（逐条跑，exit code + 关键行进回执 acceptance）
1. `grep -c "WROTE arm_a\|WROTE arm_b + finished" t8c-smoke-rerun-*.log` ≥ 2
2. `python3 -c "import json;d=json.load(open('raw_outputs_t8c.json'));print(len(d['arm_a']),len(d['arm_b']))"` = 3 3
3. `python3 -c "import json;d=json.load(open('t8c-smoke-eval.json'));print(d)"` 有逐臂分数（数字抄进回执 evidence，不解读）
4. `git add tasks/think-trigger/exp-results/raw_outputs_t8c.json tasks/think-trigger/exp-results/raw_outputs_t8c.pre-rerun.json tasks/think-trigger/exp-results/t8c-smoke-eval.json tasks/think-trigger/exp-results/t8c-smoke-eval.pre-rerun.json tasks/think-trigger/exp-results/t8c-smoke-rerun-*.log tasks/think-trigger/exp-results/t8c-smoke-rerun.pid tasks/agent-orchestration/receipts/T8c-smoke-rerun.json && git commit -m "T8c smoke rerun: new anchor V100 $704 + MAX_A 73728 (n=3/arm)"`

## 边界
- 只动本卡声明的文件 + 回执；不改 run_exp_t8c.py / eval_t8c_smoke.py / spec / prereg / 任何 calc 或 judge 代码
- 不解读结果、不下结论（Stage 0 过没过由监督者对照 prereg 判）
- 不动端口 8787 / 不动其他 runs-* 目录
