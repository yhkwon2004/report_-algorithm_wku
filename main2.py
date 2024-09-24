s = {
    "이름": "자기이름",
    "학번": "자기 학번",
    "점수": {"영어": 90, "국어": 87, "수학": 85},
    "점수2": [80, 70, 50, 90]
}
for key in ["이름", "학번"]:
    print(f"{key} : {s[key]}")

for key in ["점수", "점수2"]:
    if key == "점수":
        for subject, score in s[key].items():
            print(f"{subject} : {score}")
    else:
        for score in s[key]:
            print(f"{key} : {score}")
