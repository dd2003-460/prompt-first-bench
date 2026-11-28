# T8c n=9 正式跑任务卡（2026-11-27）

# origin: ai · Lead 规划产出 · 执行者纯执行

## 任务
`python3 run_exp_t8c_n9.py all` 补 run4-9（A×6 + B×6，共 9/臂），追加到 raw_outputs_t8c.json（保留已有 run1-3，不覆盖）。复用 run_exp_t8c 的冻结 Q/STAGES/caps/call（import 防题面漂移）。产出 9/臂。

## 前置（先核，任一不过 → 回执报 T-失配，不执行）
1. `grep -n "^MAX_A =" run_exp_t8c.py` 显示 `MAX_A = 73728`。
2. `grep -n "^MAX_B_REVIEW" run_exp_t8c.py` 显示 `MAX_B_REVIEW = 16384`（CapFix 已落）。
3. `python3 -c "import json;d=json.load(open('raw_outputs_t8c.json'));print(len(d['arm_a']),len(d['arm_b']))"` = `3 3`（干净的 n=9 前状态）。
4. `python3 -c "import run_exp_t8c_n9"` exit 0（import 干净，不发起实验请求）。
5. `git log --oneline -6 | grep -qiE "n9|trunc"`（三前置 commit 1c5489ff8/41104aa19/15c3c4309 已落盘）。

## 执行方式（严格按序）
1. 手工备份（区别于脚本内部 .pre-n9，后者每次启动都会被覆盖）：`cp raw_outputs_t8c.json raw_outputs_t8c.pre-n9-manual.json`
2. 后台起跑（macOS 无 setsid 二进制，用 os.setsid() 包装保证新会话脱离进程组——比裸 nohup 更强，防 Hermes 会话压缩/切换时进程组被回收；execvp 保持同 PID，pid 文件有效）：
   `TS=$(date +%Y%m%d-%H%M%S); nohup python3 -c "import os,sys; os.setsid(); os.execvp('python3',['python3','run_exp_t8c_n9.py','all'])" > t8c-n9-rerun-$TS.log 2>&1 & echo $! > t8c-n9.pid`
   把 PID 和日志文件名记入回执 evidence。**同时把 PID 写入 goal state**（goal_id=research-agi-budget，从 pid 文件读，不手填）：
   `PID=$(cat t8c-n9.pid); python3 -c "import json,sys;p='/Users/a1-6/.hermes/.stage-gate/research-agi-budget.json';d=json.load(open(p));c=d.setdefault('context',{});c['restart_pid']=int(sys.argv[1]);c['restart_pid_task']='T8c-N9';json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)" "$PID"`
   本 tick 到此为止（跑约 50 分钟）。
3. 后续 tick 接力：`kill -0 $(cat t8c-n9.pid)` 探活；日志出现 `WROTE arm_b n9 + finished` = 完成。
   - 进程死且无 finished 行 → 查日志尾部定位死因，记入回执。**脚本已幂等（跳过磁盘上已有的 run 号），接力 = 重跑第 2 步同一条命令**（自动跳过已完成 run，无重复、不浪费重跑；新日志文件名带新 TS）。同一死法 2 次 = 换路报监督者（status=failed 报因）。
4. 完成后清 goal state PID：`python3 -c "import json;p='/Users/a1-6/.hermes/.stage-gate/research-agi-budget.json';d=json.load(open(p));c=d.get('context',{});c.pop('restart_pid',None);c.pop('restart_pid_task',None);json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)"`
5. **不跑 eval**（eval_t8c_n9.py 是 Lead 的活，出 W1/W2/W3；执行者只报数，不判分流）。

## 验收（逐条跑，exit code + 关键行进回执 acceptance）
1. `grep -c "WROTE arm_a n9\|WROTE arm_b n9 + finished" t8c-n9-rerun-*.log` ≥ 2
2. `python3 -c "import json;d=json.load(open('raw_outputs_t8c.json'));print(len(d['arm_a']),len(d['arm_b']))"` = `9 9`
3. 18 样本 run 号列表（抄进 evidence，不解读）：`python3 -c "import json;d=json.load(open('raw_outputs_t8c.json'));print('A_runs',[s['run'] for s in d['arm_a']]);print('B_runs',[s['run'] for s in d['arm_b']])"`（期望 A_runs=B_runs=[1..9]）
4. 截断计数（A 臂平铺 finish_reason / B 臂逐 stage finish_reason；抄进 evidence，不解读）：`python3 -c "import json;d=json.load(open('raw_outputs_t8c.json'));a=sum(1 for s in d['arm_a'] if s.get('finish_reason')=='length');b=sum(1 for s in d['arm_b'] for st in s.get('stages',{}).values() if st.get('finish_reason')=='length');print('A_trunc',a,'B_trunc',b)"`
5. `git add tasks/think-trigger/exp-results/raw_outputs_t8c.json tasks/think-trigger/exp-results/raw_outputs_t8c.pre-n9-manual.json tasks/think-trigger/exp-results/t8c-n9-rerun-*.log tasks/think-trigger/exp-results/t8c-n9.pid tasks/agent-orchestration/receipts/T8c-N9.json && git commit -m "T8c n=9: 补 run4-9 (9/arm, A×6+B×6)"`

## 边界
- 只动本卡声明的文件 + 回执；不改 run_exp_t8c.py / run_exp_t8c_n9.py / eval_*.py / spec / prereg / 任何 calc 或 judge 代码
- 不解读结果、不下结论（W1/W2/W3 与分流判决由 Lead 用 eval_t8c_n9.py 出）
- 不跑 eval_t8c_n9.py（那是 Lead 的）
- 不动端口 8787 / 不动其他 runs-* 目录
