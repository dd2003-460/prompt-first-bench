#!/bin/bash
# q7 719 过夜 watcher (2026-11-24 20:55): 等队列 DONE → post-run 协议 → 复现核验 → 报告.
# 只读队列产物 + 写自己的报告, 不碰运行中进程.
set -u
OUT=/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q7-budget-scan
LOG=/tmp/q7-budget-scan.log
REP="$OUT/q7-719-postrun-report-$(date +%Y%m%d-%H%M%S).md"
QUEUE_PID=99447

# 1) 等队列结束 (DONE 行 或 队列 PID 消失)
while true; do
  if grep -q 'queue DONE' "$LOG" 2>/dev/null; then break; fi
  if ! kill -0 "$QUEUE_PID" 2>/dev/null; then
    # PID 没了但没 DONE 行 = 队列异常退出, 仍继续核验已落盘的 rep
    echo "[watcher] queue PID $QUEUE_PID gone without DONE line — verifying anyway" >> "$REP"
    break
  fi
  sleep 120
done
echo "[watcher] queue ended $(date '+%F %T'), starting post-run protocol" >> "$REP"

# 2) post-run 协议: 每个 719 rep 的 claim-set 哈希 + n_nodes 健全性
/usr/bin/python3 - "$OUT" "$REP" << 'PYEOF'
import sys, os, json, glob, hashlib
out, rep = sys.argv[1], sys.argv[2]
lines = ["\n## post-run 协议 (719 档)\n"]
files = sorted(glob.glob(os.path.join(out, 'q7-719-r*.json')))
seen = {}
for f in files:
    try:
        d = json.load(open(f))
        n = len(d['nodes'])
        cs = hashlib.sha1('|'.join(sorted(nd.get('claim','')[:40] for nd in d['nodes'])).encode()).hexdigest()[:12]
        tag = os.path.basename(f)
        flags = []
        if n < 500: flags.append(f'n_nodes={n} 偏低(应~719, 疑似跨 budget 污染)')
        if cs in seen: flags.append(f'claim-set 与 {seen[cs]} 相同 = 复制污染')
        else: seen[cs] = tag
        lines.append(f"- {tag}: n={n} claim-set={cs} {'; '.join(flags) if flags else 'OK'}")
    except Exception as e:
        lines.append(f"- {os.path.basename(f)}: ERR {e}")
open(rep, 'a').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
PYEOF

# 3) 复现核验 (r1 vs r2 机制判定)
/usr/bin/python3 "$OUT/q7-719-replication-check.py" >> "$REP" 2>&1
echo "[watcher] done $(date '+%F %T') report=$REP"
exit 0
