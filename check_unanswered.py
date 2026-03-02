import json, os, glob, sys
SESSION_DIR = '/home/riverbank1229/.openclaw/agents/main/sessions/'
files = sorted([f for f in glob.glob(SESSION_DIR + '*.jsonl') if '.reset.' not in f], key=os.path.getmtime, reverse=True)
main_session = None
for f in files[:10]:
    try:
        lines = open(f).readlines()[:6]
        is_cron = any('[cron:' in l or '[system:' in l for l in lines if l.strip())
        if not is_cron:
            main_session = f
            break
    except: pass
if not main_session:
    print('NO_MAIN_SESSION'); sys.exit(0)
messages = []
for line in open(main_session):
    try:
        d = json.loads(line)
        if d.get('type') == 'message':
            m = d.get('message', {})
            r = m.get('role', '')
            if r in ('user','assistant'):
                t = ''.join(c.get('text','') for c in m.get('content',[]) if isinstance(c,dict) and c.get('type')=='text')
                messages.append({'role':r,'text':t.strip(),'ts':d.get('timestamp','')})
    except: pass
unanswered = []
for i,msg in enumerate(messages):
    if msg['role']=='user' and msg['text'] and not msg['text'].startswith('[cron:'):
        if not any(m['role']=='assistant' for m in messages[i+1:]):
            unanswered.append(msg)
if unanswered:
    print('UNANSWERED:')
    [print(f"  [{m['ts']}] {m['text'][:200]}") for m in unanswered]
else:
    print('ALL_ANSWERED')
