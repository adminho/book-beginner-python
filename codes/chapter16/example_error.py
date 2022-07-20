try :
	#raise AttributeError("Error here!")
	x = 10
except AttributeError :
	print("Error จากแอทริบิวต์")	
except TypeError :
	print("Error จากชนิดข้อมูล")
else:
	print("ไม่ได้เกิด error")

print("บรรทัดถัดมา")