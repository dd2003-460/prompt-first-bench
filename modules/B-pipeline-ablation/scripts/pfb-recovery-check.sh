#!/bin/bash
# pfb-recovery-check.sh — 断点恢复 + 进程心跳检查
# 用法: ./pfb-recovery-check.sh (输出状态到 stdout + 写入 tasks/recovery-status.json)

cd "$(dirname "$0")"
python3 -c "
import json, glob, os, time, subprocess

status = {
    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
    'processes': {},
    'runs': {},
    'anomalies': []
}

# Check running processes
for name, pattern in [('v13_gpu', 'run_v13_50'), ('s5_prod_soc', 's5_pipeline')]:
    r = subprocess.run(['pgrep', '-f', pattern], capture_output=True, text=True)
    pids = r.stdout.strip().split('\n') if r.stdout.strip() else []
    status['processes'][name] = {'alive': len(pids) > 0, 'pids': pids}
    if not pids:
        status['anomalies'].append(f'{name}: PROCESS DEAD')

# Check run progress
for run_dir, prefix, total in [
    ('runs-s5-gpu-v13', 'S5-gpu-r', 50),
    ('runs-s5-prod', 'S5-nat-r', 100),
    ('runs-s5-prod', 'S5-soc-r', 100),
]:
    files = glob.glob(f'{run_dir}/{prefix}*.json')
    n = len(files)
    label = f'{run_dir}/{prefix}'
    status['runs'][label] = {'count': n, 'target': total, 'pct': f'{n/total:.0%}'}
    # check for errors
    errs = 0
    for f in files[-10:]:  # check last 10
        try:
            with open(f) as fh: d = json.load(fh)
            if d.get('error'): errs += 1
        except: pass
    if errs > 2:
        status['anomalies'].append(f'{label}: {errs}/10 recent files have errors')

# If v13 is dead but not complete → suggest restart
if not status['processes']['v13_gpu']['alive']:
    v13_n = status['runs'].get('runs-s5-gpu-v13/S5-gpu-r', {}).get('count', 0)
    if v13_n < 50:
        status['anomalies'].append(f'ACTION: v13 at {v13_n}/50, process dead → restart: nohup bash run_v13_50.sh >> run_v13_50.log 2>&1 &')

with open('tasks/recovery-status.json', 'w') as f:
    json.dump(status, f, ensure_ascii=False, indent=2)
print(json.dumps(status, ensure_ascii=False, indent=2))
"
