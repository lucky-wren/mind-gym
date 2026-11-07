# -*- coding: utf-8 -*-
# 趣学益智馆 · 极简本地桥（仅标准库）
# 1) MODELSCOPE_TOKEN=ms-你的令牌 python3 bridge.py
#    （本机页面填 http://localhost:8787/v1/chat/completions）
# 2) 想跨设备 / HTTPS 页面再开一条：
#    cloudflared tunnel --url http://localhost:8787
#    把打印出的 https://xxx.trycloudflare.com 加上 /v1/chat/completions 填进页面
import os, json, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 也可改用本机 Ollama：UPSTREAM=http://localhost:11434/v1/chat/completions
UPSTREAM = os.environ.get("UPSTREAM", "https://api-inference.modelscope.cn/v1/chat/completions")
TOKEN = os.environ.get("MODELSCOPE_TOKEN", "")

class H(BaseHTTPRequestHandler):
    def cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
    def do_OPTIONS(self):
        self.send_response(204); self.cors(); self.end_headers()
    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        headers = {"Content-Type": "application/json"}
        if TOKEN: headers["Authorization"] = "Bearer " + TOKEN
        req = urllib.request.Request(UPSTREAM, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as r: out, code = r.read(), 200
        except Exception as e:
            out, code = json.dumps({"error": str(e)}).encode(), 502
        self.send_response(code); self.cors()
        self.send_header("Content-Type", "application/json")
        self.end_headers(); self.wfile.write(out)
    def log_message(self, *a): pass

print("bridge  ->  http://localhost:8787/v1/chat/completions")
print("跨设备  ->  cloudflared tunnel --url http://localhost:8787")
ThreadingHTTPServer(("127.0.0.1", 8787), H).serve_forever()