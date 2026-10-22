import json
import os

print("fygfuewgwu")
FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(tasks):
    title = input("أدخل اسم المهمة: ")
    tag = input("أدخل تصنيف أو وسم للمهمة (اختياري): ")

    new_id = 1 if not tasks else tasks[-1]["id"] + 1

    task = {"id": new_id, "title": title, "is_done": False, "tag": tag}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ تمت إضافة المهمة بنجاح!")


def view_tasks(tasks):
    if not tasks:
        print("📭 لا توجد مهام حالياً.")
        return

    print("\n--- قائمة المهام ---")
    for task in tasks:
        status = "[✓]" if task["is_done"] else "[ ]"
        tag_info = f" ({task['tag']})" if task["tag"] else ""
        print(f"{task['id']}. {status} {task['title']}{tag_info}")


def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_id = int(input("أدخل رقم المهمة لتحديدها كمكتملة: "))
        for task in tasks:
            if task["id"] == task_id:
                task["is_done"] = True
                save_tasks(tasks)
                print("✅ تم تحديث حالة المهمة!")
                return
        print("❌ لم يتم العثور على مهمة بهذا الرقم.")
    except ValueError:
        print("❌ الرجاء إدخال رقم صحيح.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_id = int(input("أدخل رقم المهمة لحذفها: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                del tasks[i]
                save_tasks(tasks)
                print("🗑️ تم حذف المهمة بنجاح!")
                return
        print("❌ لم يتم العثور على مهمة بهذا الرقم.")
    except ValueError:
        print("❌ الرجاء إدخال رقم صحيح.")


def main():
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 20)
        print("مدير المهام (To-Do List)")
        print("=" * 20)
        print("1. إضافة مهمة")
        print("2. عرض المهام")
        print("3. تحديد مهمة كمكتملة")
        print("4. حذف مهمة")
        print("5. إنهاء البرنامج")

        choice = input("اختر عملية (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("إلى اللقاء! 👋")
            break
        else:
            print("❌ اختيار غير صحيح، يرجى المحاولة مرة أخرى.")


if __name__ == "__main__":
    main()
