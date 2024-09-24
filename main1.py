# 초기 딕셔너리
ch = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불검",
        "armor": "갑옷"
    },
    "skill": ["베기", "세게배기", "아주세게 베기"]
}
print("초기:", ch)
ch["life"] = 400
ch["level"] = 15
del ch["name"]
print("세게배기:", ch["skill"][1])
print("변경:", ch)
