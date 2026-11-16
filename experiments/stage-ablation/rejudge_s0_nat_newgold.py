# S0 nat 391 reps 用新 GOLD 重判（2026-11-16）
# 背景：GOLD nat 要点 5 措辞修正（"有效驻留时间~100天" → "平均更新间隔~100天 + 折扣公式 1-exp(-驻留/100)"），
#       修测量错误后 S0 基线必须用同一新 GOLD 重判，否则与 SM 不可比。
# 输入：runs-prod/S0-nat-r*.json（answer 在盘上，不重跑生成）
# 输出：runs-prod/S0-nat-rejudge-newgold.json（old/new coverage + 新逐点 scores）
import json, glob, time, statistics
from concurrent.futures import ThreadPoolExecutor, as_completed
from s8b_pilot import judge

files = sorted(glob.glob('runs-prod/S0-nat-r*.json'),
               key=lambda f: int(f.split('-r')[-1].split('.json')[0]))
print(f'S0 nat rejudge: {len(files)} runs, new GOLD', flush=True)

def rejudge(f):
    d = json.load(open(f))
    old = d['judge'].get('coverage')
    t0 = time.time()
    try:
        j = judge('nat', d['answer'])
        return {'file': f, 'old': old, 'new': j.get('coverage'),
                'scores': j.get('scores'), 'reasons': j.get('reasons'),
                'wall': round(time.time() - t0, 1)}
    except Exception as e:
        return {'file': f, 'old': old, 'error': f'{type(e).__name__}: {e}'}

t_start = time.time()
results = {}
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = {ex.submit(rejudge, f): f for f in files}
    done = 0
    for fut in as_completed(futs):
        r = fut.result()
        results[r['file']] = r
        done += 1
        if done % 25 == 0:
            print(f'{done}/{len(files)} {time.time()-t_start:.0f}s', flush=True)

json.dump(results, open('runs-prod/S0-nat-rejudge-newgold.json', 'w'), ensure_ascii=False, indent=1)

olds = [r['old'] for r in results.values() if r.get('old') is not None]
news = [r['new'] for r in results.values() if r.get('new') is not None]
errs = [r['file'] for r in results.values() if 'error' in r]
print(f'\n=== S0 nat rejudge (new GOLD) ===', flush=True)
print(f'ok={len(news)} errors={len(errs)}', flush=True)
print(f'old mean = {statistics.mean(olds):.4f} (n={len(olds)})', flush=True)
print(f'new mean = {statistics.mean(news):.4f} (n={len(news)}) sd={statistics.stdev(news):.4f}', flush=True)
# 新 GOLD 逐点漏点分布
gold_n = 6
miss = [0]*gold_n
for r in results.values():
    s = r.get('scores') or []
    for gi in range(min(gold_n, len(s))):
        if s[gi] == 0: miss[gi] += 1
for gi in range(gold_n):
    print(f'要点{gi+1}: {miss[gi]}/{len(news)} 次漏', flush=True)
print(f'wall={time.time()-t_start:.0f}s', flush=True)