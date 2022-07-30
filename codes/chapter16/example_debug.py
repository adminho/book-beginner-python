try :	
	raise AttributeError("Error here!")
except NameError: # catch
    print("ตัวแปร x ยังไม่ได้ประกาศ")		
except ZeroDivisionError :
	print("หารด้วยศูนย์ไม่ได้") # ไม่มี raise รวมทั้งไม่ข้อผิดพลาด ไม่มี exception
except TypeError :
	print("Error จากชนิดข้อมูล")
except:
	print("Error อื่นๆ")
finally:
    print("ประโยค finally")

print("บรรทัดถัดมา")