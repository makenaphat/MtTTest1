# นำเข้าโมดูลทั้งหมด 10 โมดูล
import lights
import temperature
import security
import music
import weather
import energy
import notifications
import timer
import user_profile
import diagnostics

def main():
    print("=== เริ่มต้นการทำงานของ Smart Home Dashboard ===\n")
    
    # 1. ทักทายผู้ใช้ (user_profile)
    print(user_profile.get_greeting("สมชาย"))
    
    # 2. ตรวจสอบสภาพอากาศ (weather)
    print(weather.get_weather())
    
    # 3. ตรวจสอบระบบความปลอดภัย (security)
    print(security.check_doors())
    
    # 4. เปิดไฟบ้าน (lights)
    print(lights.set_status("on"))
    
    # 5. ปรับอุณหภูมิแอร์ (temperature)
    print(temperature.set_temp(25))
    
    # 6. เปิดเพลงโปรด (music)
    print(music.play_song("Lo-Fi Chill Beats"))
    
    # 7. เช็คพลังงาน (energy)
    print(energy.get_usage())
    
    # 8. ตั้งเวลาปิดระบบ (timer)
    print(timer.set_timer(60))
    
    # 9. ตรวจสอบความสมบูรณ์ของระบบ (diagnostics)
    print(diagnostics.run_check())
    
    # 10. ส่งการแจ้งเตือนสรุป (notifications)
    print(notifications.send_alert("บ้านพร้อมใช้งานแล้วในโหมด 'พักผ่อน'"))
    
    print("\n=== ทำงานครบทุก 10 โมดูลเรียบร้อย ===")

if __name__ == "__main__":
    main()