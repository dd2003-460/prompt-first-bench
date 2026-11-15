#!/bin/bash
# Monitor M-arm, launch M1+M2 on completion
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation

echo "[$(date '+%H:%M:%S')] Waiting for M-arm (PID 27188) to finish..."

while pgrep -f "s5_state_machine.*minimal" > /dev/null 2>&1; do
    sleep 30
done

echo "[$(date '+%H:%M:%S')] M-arm done. Checking output..."
if [ -f runs-s5-sm-gpu-minimal.json ]; then
    echo "[$(date '+%H:%M:%S')] M-arm output: $(wc -c < runs-s5-sm-gpu-minimal.json) bytes"
else
    echo "[$(date '+%H:%M:%S')] WARNING: M-arm output not found"
fi

echo "[$(date '+%H:%M:%S')] Launching M1 (method, qid=gpu-method)..."
nohup python3 s5_state_machine.py gpu --obj-mode=method --qid=gpu-method > sm-gpu-method.log 2>&1 &
M1_PID=$!
echo "[$(date '+%H:%M:%S')] M1 PID: $M1_PID"

echo "[$(date '+%H:%M:%S')] Launching M2 (method_challenge, qid=gpu-method-challenge)..."
nohup python3 s5_state_machine.py gpu --obj-mode=method_challenge --qid=gpu-method-challenge > sm-gpu-method-challenge.log 2>&1 &
M2_PID=$!
echo "[$(date '+%H:%M:%S')] M2 PID: $M2_PID"

echo "[$(date '+%H:%M:%S')] Both arms launched. Monitoring..."

while pgrep -f "s5_state_machine.*method" > /dev/null 2>&1; do
    sleep 30
done

echo "[$(date '+%H:%M:%S')] All arms done. Summary:"
for f in runs-s5-sm-gpu-minimal.json runs-s5-sm-gpu-method.json runs-s5-sm-gpu-method-challenge.json; do
    if [ -f "$f" ]; then
        echo "  $f: $(wc -c < "$f") bytes"
    else
        echo "  $f: MISSING"
    fi
done
echo "[$(date '+%H:%M:%S')] Done."
