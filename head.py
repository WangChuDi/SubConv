head = """port: 7890
socks-port: 7891
allow-lan: true
mode: Rule
log-level: info
external-controller: :9090
"""
pp = """proxy-providers:
  subscription:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  hk:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: '🇭🇰'
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  sg:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: '🇸🇬'
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  jp:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: '🇯🇵'
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  us:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: '🇺🇸'
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
"""
pg = """proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - 🔯 故障转移
      - 🔮 负载均衡
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
      - DIRECT
  - name: 🚀 手动切换
    type: select
    use:
      - subscription
  - name: ♻️ 自动选择
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
  - name: 🔯 故障转移
    type: fallback
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
  - name: 🔮 负载均衡
    type: load-balance
    strategy: consistent-hashing
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
  - name: 📲 电报消息
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🇸🇬 狮城节点
      - 🇭🇰 香港节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
      - DIRECT
  - name: 📹 油管视频
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🇸🇬 狮城节点
      - 🇭🇰 香港节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
      - DIRECT
  - name: 🎥 奈飞视频
    type: select
    proxies:
      - 🎥 奈飞节点
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🇸🇬 狮城节点
      - 🇭🇰 香港节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
      - DIRECT
  - name: 📺 巴哈姆特
    type: select
    proxies:
      - 🚀 节点选择
      - 🚀 手动切换
      - DIRECT
  - name: 📺 哔哩哔哩
    type: select
    proxies:
      - 🎯 全球直连
      - 🇭🇰 香港节点
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
      - DIRECT
  - name: 🌏 国内媒体
    type: select
    proxies:
      - DIRECT
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
  - name: 📢 谷歌FCM
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
  - name: Ⓜ️ 微软云盘
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
  - name: 🍎 苹果服务
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
  - name: 🎮 游戏平台
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
  - name: 🎶 网易音乐
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🛑 广告拦截
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🍃 应用净化
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - DIRECT
      - 🇭🇰 香港节点
      - 🇸🇬 狮城节点
      - 🇯🇵 日本节点
      - 🇺🇸 美国节点
      - 🚀 手动切换
  - name: 🇭🇰 香港节点
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - hk
  - name: 🇯🇵 日本节点
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - jp
  - name: 🇺🇸 美国节点
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - us
  - name: 🇨🇳 台湾节点
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - DIRECT
  - name: 🇸🇬 狮城节点
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - sg
  - name: 🇰🇷 韩国节点
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
      - DIRECT
  - name: 🎥 奈飞节点
    type: select
    proxies:
      - DIRECT
"""
