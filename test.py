import requests

# URL ของ Webhook
webhook_url = "https://discord.com/api/webhooks/1421697869458706533/W2UqZa7gD95EU7ixa4gQN3QLz3pWc3oFepvpv16XWxfpuMMTTiqbNULZWrBBmPfPlYBY"

# ข้อมูลที่จะส่ง (ข้อความปกติ + embed)
data = {
    "content": ":zap: Notification!",
    "embeds": [
        {
            "title": "📢 Build success",
            "description": "No error no bug  ✅",
            "color": 0x00ff00,  # สีเขียว
            "fields": [
                {
                    "name": "เวลาที่เสร็จ",
                    "value": "2025-09-28 14:35",
                    "inline": True
                },
                {
                    "name": "สถานะ",
                    "value": "Success",
                    "inline": True
                }
            ],
            "footer": {
                "text": "ระบบแจ้งเตือนอัตโนมัติ",
                "icon_url": "https://cdn-icons-png.flaticon.com/512/1828/1828817.png"
            }
        }
    ]
}

# ส่ง POST request
response = requests.post(webhook_url, json=data)

# แสดงผลลัพธ์
if response.status_code == 204:
    print("✅ ส่ง Embed สำเร็จ!")
else:
    print(f"❌ ส่งไม่สำเร็จ: {response.status_code} - {response.text}")
