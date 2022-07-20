try :
	"Python".upper();
except:
	print("Error อื่นๆ")
except NameError :
	print("ตัวแปร x ยังไม่ได้ประกาศ")	
except ZeroDivisionError :
	print("หารด้วยศูนย์ไม่ได้")
except TypeError :
	print("Error จากชนิดข้อมูล")
print("บรรทัดถัดมา")
