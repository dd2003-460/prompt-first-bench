# origin: ai (2026-11-28 G5 定案 · sub 隔离复现, 未跑队列)

## 判决: 是 — 假阳性确实发生 (00:42:30 / 00:47:37 两次 SKIP 300-r3), 现已自愈
现状: 真文件 q9-300-r3-20261128-135044.json 存在 (14:25, n_nodes=300, 13:50:44 补跑成功)。

## 根因 (两层叠加)
1. **v2 幂等检查本身对"真缺失"无误判**: `experiments/stage-ablation/q9_budget_scan_queue_v2.sh:23-28`
   (glob `q9-${budget}-r${rep}-*.json` + `[ -f ]` + n_nodes≥budget*99/100)。复现场景A: 无 r3 文件时返回 None → 正确 RUN。
2. **假阳性来自上游 v1 种下的陈旧假文件**: `experiments/stage-ablation/q9_budget_scan_resume.sh:28-29`
   无条件 `cp runs-s5-sm-q9-agi.json`(SM 固定输出名, 从不清理) — rc≠0 也 cp (fail-open)。300-r3 于 23:48:47 起跑,
   00:33 被 SIGKILL, v1 wrapper 把仍存 r2 内容的固定文件 cp 成 `q9-300-r3-20261127-234847.json` (mtime 00:33:29)。
   v2 的 already_done 只认 glob+n_nodes, 无出处/mtime 校验 → 读到假文件 n_nodes=300 ≥ 297 → SKIP。

## 铁证 (sha256 只读核验)
- q9-300-r2-20261127-225528.json 与 quarantine-20261127/FALSE-q9-300-r3-copy-of-r2.json
  sha256 均 = `f3ab7c6db3c142bc...` (字节级相同); 假文件 mtime 2026-11-28 00:33:29 (= kill 时刻)。
- /tmp/q9-budget-scan-queue.log: 00:42:30 与 00:47:37 两行 `budget=300 rep=3 SKIP (existing: q9-300-r3-20261127-234847.json)`;
  13:50:44 起 `rc=0 n_nodes=300 out=q9-300-r3-20261128-135044.json`。假文件已移入 quarantine-20261127/ (mtime 00:46) → 13:50 补跑正常, 假阳性自愈。

## 复现输出摘录 (scratch/g5-repro.py, 独立脚本喂假输入, 未碰队列)
```
== 场景A: 文件缺失 ==  already_done(300,3) -> None  => RUN (正确, 不误标)
== 场景B: 上游 fail-open cp 种下陈旧假文件 ==
already_done(300,3) -> '.../q9-300-r3-20261127-234847.json'
=> SKIP (existing: q9-300-r3-20261127-234847.json)  ← 假阳性
```

## 修复建议 (一行, 不实施)
already_done 增加出处校验: 要求同名 `q9-B-rR.stdout` 存在且含 rc=0 记录 (或 mtime 晚于最近 kill 时刻), 拒绝无 run 痕迹的孤儿 json。
