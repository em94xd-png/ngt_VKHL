import pygetwindow as gw
import pyautogui
import pyperclip
import time

target_title = "Edge"

# 1. ใช้ตัวแปรนี้เก็บ "ชื่อแท็บล่าสุด" เท่านั้น
old_title = "" 

while True:
    try:
        find_title = gw.getWindowsWithTitle(target_title)

        if find_title:
            found_title = find_title[0]

            if not found_title.isMinimized:
                # ดึงชื่อแท็บปัจจุบันมาเก็บไว้
                current_title = found_title.title

                # 2. เช็กว่า "ชื่อแท็บปัจจุบัน" เปลี่ยนไปจาก "ชื่อแท็บล่าสุด" หรือยัง
                if current_title != old_title:
                    found_title.activate()
                    time.sleep(0.5)

                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(0.1) # หน่วงเวลาเล็กน้อยให้คีย์บอร์ดทำงานทัน
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(0.2) # รอให้ข้อความเข้าคลิปบอร์ดเสร็จสมบูรณ์
                    
                    # 3. ดึงเนื้อหาเว็บมาใช้งาน (เก็บแยกไว้คนละตัวแปร)
                    web_content = pyperclip.paste()

                    # ทดสอบพิมพ์ผลลัพธ์ดูใน Terminal
                    print(f"\n[เปลี่ยนหน้าเว็บเป็น]: {current_title}")
                    print("--- เนื้อหาที่ก๊อปปี้ได้ ---")
                    print(web_content[:150]) # พิมพ์ 150 ตัวแรก
                    print("-" * 30)

                    # 4. อัปเดต "ชื่อแท็บล่าสุด" ให้เป็นชื่อปัจจุบัน เพื่อล็อกไม่ให้ก๊อปปี้ซ้ำในหน้านี้
                    old_title = current_title

    except Exception as e:
        pass
    
    # 5. ใส่เวลาพักให้ CPU นิดนึง (เช่น 0.5 วินาที) เครื่องจะได้ไม่รันลูปเร็วเกินไปจนค้าง
    time.sleep(0.5)
