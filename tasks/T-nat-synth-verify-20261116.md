# 任务书：nat 10-run synth mean 验证（phase1 gate）

> origin: ai (2026-11-16, lead 派发)
> 状态：待执行
> 前置：nat verify-only 已跑完（PID 6601, 26/30 批, cov 0.871, 预计 30 批跑完 cov ~0.88）

## 目标

验证 nat 臂 10-run synth mean 是否 ≥ 0.5801（gate）。

## 背景

- nat 基线（S0）：0.5801（2026-11-16 新 GOLD）
- nat 旧 10-run mean：0.5166（FAIL，gap 0.064）
- 根因：8787 prefix cache 漂移 + verify 假阳性（公式/推导类节点被要求外部来源）
- 修复已应用：
  1. P3_VERIFY 公式/推导类豁免（commit d6f0b15c）
  2. 反缓存扰动 4 空格 → 16 随机 token（commit e292f431）
- nat verify-only 进度：r28 verified 242/278, cov 0.871（基线 0.651, +0.220）

## 执行步骤

### 1. 等 nat verify-only 跑完

```bash
# 监控 PID 6601
ps -o pid,etime -p 6601
# 或看日志
tail -f /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/nat-verifyfix3.log
```

跑完标志：日志出现 `[SM] DONE` 或进程退出。

### 2. 核终值

```bash
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
python3 -c "
import json
from collections import Counter
import glob
f=sorted(glob.glob('checkpoints/sm-nat-r*.json'))[-1]
d=json.load(open(f))
c=Counter(n['status'] for n in d['nodes'])
print(f'{f}: verified={c[\"verified\"]} pending={c.get(\"pending\",0)} degraded={c.get(\"degraded\",0)} cov={c[\"verified\"]/len(d[\"nodes\"]):.3f}')
"
```

预期：cov ≥ 0.87（基线 0.651）。

### 3. 跑 10-run synth mean

```bash
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
python3 synth_multi_soc.py --qid=nat --runs=10 --output=runs-s5-sm-nat-synth-multi-v2.json
```

注意：synth_multi_soc.py 需要适配 nat（当前默认 soc）。检查 `--qid` 参数是否支持 nat，不支持则改脚本。

### 4. 核结果

```bash
python3 -c "
import json
d=json.load(open('runs-s5-sm-nat-synth-multi-v2.json'))
scores=[r['judge_coverage'] for r in d['runs']]
mean=sum(scores)/len(scores)
import statistics
sd=statistics.stdev(scores)
print(f'10-run mean: {mean:.4f} (sd={sd:.4f})')
print(f'gate: 0.5801')
print(f'PASS: {mean >= 0.5801}')
"
```

### 5. 更新 bench 报告

如果 PASS：
- 更新 `s5-sm-bench-report.md` #21：nat 0.5166 → 新值，gate PASS
- 更新 `runs-s5-sm-nat-synth-multi.json`（或新建 v2 文件）

如果 FAIL：
- 记录新值和 gap
- 分析根因（是 prefix cache 漂移还是其他）
- 更新 bench 报告 #21

### 6. Commit

```bash
cd /Users/a1-6/Desktop/workspace/pfb
git add experiments/stage-ablation/
git commit -m "feat(nat): 10-run synth mean 验证（公式豁免+反缓存扰动修复后）"
```

## 验收标准

1. nat verify-only 跑完（30/30 批），终值 cov ≥ 0.87
2. 10-run synth mean 跑完，结果落盘
3. bench 报告 #21 更新（PASS/FAIL + 新值）
4. commit 到 main

## 边界

- 只改 `experiments/stage-ablation/` 内文件
- 不动 checkpoint（verify-only 的 checkpoint 是只读输入）
- 不跑 gpu（gpu 排下一轮）
- 不跑 q6 SOTA bench（q6 在跑，PID 65415）

## 完成报告

（执行者填写：改了什么、测试输出、commit hash）
