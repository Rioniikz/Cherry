from flask import Flask, request, jsonify, make_response
import random, requests, re, base64, zlib, time, ipaddress
from vercel_python_wsgi import make_wsgi_handler

app = Flask(__name__)
app.config["ENV"] = "production"
app.config["DEBUG"] = False

u = "https://cherrydlc.com/Cherry/FREEMODS/KEYSSSSSSSSSSSSSSSSSSSSSSSSSSSS343423432423423423423423423434545634653464645645345345.php"
mods = ['U1RBTkQgQ0hJTExPVw==','U1RBTkQgS05JRkU=']
blocked_agents = ["translate.googleusercontent.com","googleusercontent.com","Google-Translate","Translate"]

def is_suspicious_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_multicast:
            return True
    except:
        return True
    return False

def e(s):
    return base64.b64encode(zlib.compress(s.encode())).decode()

def d(s):
    return zlib.decompress(base64.b64decode(s)).decode()

html_parts = [
    e("<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>"),
    e("<title>Генератор ключей</title><style>"),
    e("*{box-sizing:border-box;margin:0;padding:0;}"),
    e("body{font-family:'Segoe UI','Roboto',Arial,sans-serif;background:linear-gradient(135deg,#0f0f23,#1a1a2e,#16213e);color:#e2e8f0;display:flex;justify-content:center;align-items:center;min-height:100vh;padding:10px;}"),
    e("#x{width:100%;max-width:550px;text-align:center;background:linear-gradient(135deg,#1e293b,#334155);padding:35px 30px;border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,0.7),0 0 0 1px rgba(255,255,255,0.05);border:1px solid #475569;backdrop-filter:blur(10px);}"),
    e("h1{margin:0 0 30px 0;font-size:2.2em;font-weight:700;color:#f1f5f9;text-shadow:0 2px 10px rgba(0,0,0,0.5);letter-spacing:1px;}"),
    e(".b{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:30px 0;}"),
    e("button{padding:18px 30px;background:linear-gradient(135deg,#3b82f6,#2563eb);color:#ffffff;border:none;border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);box-shadow:0 4px 15px rgba(59,130,246,0.3),0 1px 3px rgba(0,0,0,0.1);text-transform:uppercase;letter-spacing:0.8px;position:relative;overflow:hidden;min-height:60px;display:flex;align-items:center;justify-content:center;}"),
    e("button::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.15),transparent);transition:left 0.6s ease;}"),
    e("button:hover{background:linear-gradient(135deg,#2563eb,#1d4ed8);transform:translateY(-3px);box-shadow:0 8px 25px rgba(59,130,246,0.4),0 4px 10px rgba(0,0,0,0.15);}"),
    e("button:hover::before{left:100%;}"),
    e("button:active{transform:translateY(-1px);box-shadow:0 4px 15px rgba(59,130,246,0.3);}"),
    e("button:disabled{background:linear-gradient(135deg,#6b7280,#4b5563);cursor:not-allowed;transform:none;box-shadow:0 2px 8px rgba(0,0,0,0.2);opacity:0.7;color:#d1d5db;}"),
    e(".k{margin:25px 0;padding:20px 25px;background:linear-gradient(135deg,#0f172a,#1e293b);border:2px solid #334155;border-radius:12px;font-family:'JetBrains Mono','Courier New',monospace;font-size:18px;font-weight:500;cursor:pointer;word-break:break-all;user-select:all;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);box-shadow:0 4px 15px rgba(0,0,0,0.4),inset 0 1px 0 rgba(255,255,255,0.05);color:#e2e8f0;line-height:1.5;}"),
    e(".k:hover{background:linear-gradient(135deg,#1e293b,#334155);border-color:#0ea5e9;box-shadow:0 6px 20px rgba(14,165,233,0.15),0 0 0 1px rgba(14,165,233,0.2);transform:translateY(-2px);color:#f1f5f9;}"),
    e(".i{color:#94a3b8;font-size:15px;margin-top:15px;line-height:1.6;font-weight:500;}"),
    e(".loading{display:none;color:#64748b;margin:25px 0;font-size:16px;font-weight:500;}.loading.show{display:block;}"),
    e("@media (max-width:480px){.b{grid-template-columns:1fr;gap:15px;}button{padding:16px 20px;font-size:15px;min-height:55px;}#x{padding:25px 20px;margin:10px;}h1{font-size:1.8em;margin-bottom:25px;}}"),
    e("</style></head><body><div id='x'></div><script>"),
    e("(function(){var x=document.getElementById('x'),h=document.createElement('h1');h.textContent='Генератор Ключей';x.appendChild(h);var b=document.createElement('div');b.className='b';"),
    e("var m=['" + mods[0] + "','" + mods[1] + "'],t=['SC','SK'],n=['STANDCHILLOW','STANDKNIFE'];"),
    e("function cr(tag,cls){var el=document.createElement(tag);if(cls)el.className=cls;return el;}"),
    e("function dec(s){return atob(s);}"),
    e("function cb(btn,tp,nm){btn.onclick=function(){gk(tp,nm,btn)};}"),
    e("function gk(tp,nm,btn){var ld=cr('div','loading show');ld.textContent='⏳ Генерация ключа...';r.innerHTML='';r.appendChild(ld);btn.disabled=true;var currentMinute=Math.floor(Date.now()/(1000*60));fetch('/api/key_'+currentMinute,{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'type='+tp+'&name='+nm}).then(resp=>resp.json()).then(data=>{r.innerHTML='';var k=cr('div','k');k.textContent=data.token;k.onclick=function(){if(navigator.clipboard){navigator.clipboard.writeText(data.token).then(()=>alert('✅ Ключ скопирован в буфер обмена!')).catch(()=>fallbackCopy(data.token));}else{fallbackCopy(data.token);}};var inf=cr('div','i');inf.innerHTML='🖱️ Нажмите на ключ для копирования<br>⏱️ Ключ действует 1 час';r.appendChild(k);r.appendChild(inf);btn.disabled=false;}).catch(()=>{alert('❌ Ошибка при генерации ключа');r.innerHTML='';btn.disabled=false;});}"),
    e("function fallbackCopy(text){var ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.top='0';ta.style.left='0';ta.style.width='2em';ta.style.height='2em';ta.style.padding='0';ta.style.border='none';ta.style.outline='none';ta.style.boxShadow='none';ta.style.background='transparent';document.body.appendChild(ta);ta.focus();ta.select();try{document.execCommand('copy');alert('✅ Ключ скопирован в буфер обмена!');}catch(err){alert('❌ Не удалось скопировать ключ');}document.body.removeChild(ta);}"),
    e("for(var i=0;i<m.length;i++){var btn=cr('button');btn.textContent=dec(m[i]);cb(btn,t[i],n[i]);b.appendChild(btn);}"),
    e("x.appendChild(b);var r=cr('div');x.appendChild(r);})();"),
    e("</script></body></html>")
]

@app.before_request
def block_suspicious():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent", "")
    if is_suspicious_ip(ip):
        return make_response("🤬 You are a sheep.", 403)
    for bad in blocked_agents:
        if bad.lower() in ua.lower():
            return make_response("🤬 You are a sheep.", 403)

@app.route("/", methods=["GET"])
@app.route("/api", methods=["GET"])
def index():
    html = ''.join([d(part) for part in html_parts])
    return html

@app.route("/api/key_<int:minute>", methods=["POST"])
def get_key(minute):
    current_minute = int(time.time() // 60)
    if abs(current_minute - minute) > 1:
        return jsonify({"error": "Invalid request"}), 400
    x = request.form.get("type")
    y = request.form.get("name")
    k = ""
    attempts = 0
    while not k and attempts < 10:
        attempts += 1
        i = ".".join(str(random.randint(1,255)) for _ in range(4))
        h = {"Client-IP": i, "User-Agent": "Mozilla/5.0"}
        try:
            r = requests.post(u, data={"type": x, "name": y}, headers=h, timeout=10)
            m = re.search(r"show_key\.php\?token=([A-Z0-9]+)", r.text)
            if m:
                k = m.group(1)
        except:
            continue
    if not k:
        return jsonify({"error": "Failed"}), 500
    return jsonify({"token": k})

handler = make_wsgi_handler(app)
