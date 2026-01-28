print("🧠 AI Weekly Planner & Burnout Detector\n")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
work_hours = []

for d in days:
    h = float(input(f"Work hours planned on {d}: "))
    work_hours.append(h)

rest_hours = float(input("\nAverage rest hours per day: "))

total_work = sum(work_hours)
avg_work = total_work / 7

print("\n📊 WEEKLY ANALYSIS")
print(f"Total weekly work hours: {total_work:.1f}")
print(f"Average daily work: {avg_work:.1f} hrs")

print("\n🧠 Burnout Analysis")

if avg_work <= 6 and rest_hours >= 7:
    print("✅ Healthy workload. Great balance!")
elif avg_work <= 8:
    print("⚠️ Overworked. Consider reducing workload.")
else:
    print("🚨 Burnout risk detected! Immediate rest needed.")

print("\n🧭 AI Advice")
if rest_hours < 6:
    print("• Increase sleep & rest time")
if avg_work > 8:
    print("• Reduce daily work hours")
if avg_work <= 6:
    print("• Maintain this healthy routine")
