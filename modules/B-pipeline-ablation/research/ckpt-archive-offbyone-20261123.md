# ckpt 归档 off-by-one bug（2026-11-23）

## 现象

`checkpoints/archive/budget-B-rR-*/` 目录名和实际内容错位一格：
目录 `budget-50-r1` 装的是 423 节点（results 无此 run），
目录 `budget-50-r2` 才是 results 的 `budget50_r1`（175 节点）。
全 15 个目录整体 off-by-one。

## 根因（budget_scan_batch.sh:30-38）

归档动作发生在 **run 之前**，目录名却用**当前 run** 的名字：

```bash
for B in ...; for R in ...; do
  RUN="gpu_budget${B}_r${R}"
  ARCHIVE=".../budget-${B}-r${R}-$(date ...)"   # ← 当前 run 的名字
  mkdir -p "$ARCHIVE"
  mv checkpoints/sm-gpu-r* "$ARCHIVE/"          # ← 移走的是上一 run 的残留
  python3 s5_state_machine.py ...                # ← 然后才跑当前 run
```

所以 `budget-B-rR` 目录 = run (B,R) 开始前 live 目录里的内容 = run (B,R-1) 的输出。

## 影响范围

- **分数（results-budget-scan.json）不受影响**：run 结束后从 live 文件
  `runs-s5-sm-gpu-synth.json` 读，对应正确。K7 15-run 的 depth/cov/节点数
  全部可信。
- **节点级数据（ckpt 目录）错位**：任何按目录名取节点数据的分析都对应错
  run。2026-11-23 第一版后台重算（按目录名匹配）全部无效，已改用 n_nodes
  全局唯一值匹配（15 个 n_nodes 无重复，可靠）。
- **719_r3（709 节点）节点数据丢失**：它是最后一个 run，输出从未被归档
  （归档属于下一个 run），留在 live 目录后被 idea2 A-r1（23:00）覆盖。
  分数幸存（depth 0.4782 / cov 0.133 在 results）。719 档去重 cov 只能 n=2。

## 修复（budget_scan_batch.sh）

归档改为 **run 之后**，或目录名用"上一 run"。最小改法：把 mv 块移到
run + bookkeeping 之后。rep_scan_queue.sh 同构，需同样检查。

## 教训

- 归档/快照类操作：目录名必须和内容生成时刻对齐，"先归档后生成"用当前名
  = 系统性 off-by-one。
- 节点级分析取数前必须验证对应关系（n_nodes 交叉核对），不能信目录名。

## 文件

- 根因: `experiments/stage-ablation/budget_scan_batch.sh` (line 30-38)
- 重算: `modules/B-pipeline-ablation/research/k7-dedup-cov-recompute.py`
  （已改 n_nodes 匹配; 719_r3 缺失, 719 档 n=2）
- 本记录: `modules/B-pipeline-ablation/research/ckpt-archive-offbyone-20261123.md`
