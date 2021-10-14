from tkinter import*
from tkinter import messagebox

window = Tk()
window.title("Cửa sổ login")
window.configure(width = 400, height = 400, background = "light blue")

#Khai báo kích thước mặc định
window.geometry('400x400')
#Khai báo label
def show():
    label = Label(window,text = "Hệ thống đăng nhập",fg = "black", bg = "white",font=("Arial Bold", 20))
    label.pack()

#Khai báo mess
def mess():
    #thông báo thông tin: đăng ký thành công
    messagebox.showinfo("Thông báo đăng ký","Đăng ký thành công")

#Thông tin user
username = Label(window, text = "Tên đăng ký:", fg = "black", bg = "light blue", font = ("Arial Bold", 10))
username.grid(row = 1, column = 0)
user = Entry(window, width = 25, bd = 5)
user.grid(row = 1, column = 1)
#Thông tin password
passid = Label(window, text = "Mật khẩu:",  fg = "black", bg = "light blue", font = ("Arial Bold", 10))
passid.grid(row = 3, column = 0)
password = Entry(window, width = 25, bd = 5, show = "*")
password.grid(row = 3, column = 1)

#Phím hiển thị

#Khai báo hàm hiển thị
def odette():
    print("Tên người đã nhập vào: ",user.get())
    print("Mật khẩu người dùng đã nhập vào: ",password.get())
    
#Khai báo button
button = Button(window,text = "Login", width = 10, height = 2, font = ("Arial Bold", 10), command = mess)
button.grid(row = 7, column = 1)
burh = Button(window, text = "Show", width = 10, heigh = 2, font = ("Arial Bold",10))
burh.grid(row = 7, column = 2)

def sel():
    selection = str(gt.get())
    print(selection)
gt = StringVar()
gt_nam = Radiobutton(window, text = "Nam", value = "Nam", variable = gt, command = sel)
gt_nam.grid(row = 4, column = 0)
gt_nu = Radiobutton(window, text = "Nữ", value = "Nữ", variable = gt, command = sel)
gt_nu.grid(row = 4, column = 1)
empty = Label(window, text = "", bg = "white")
empty.grid(row = 5, column = 0)
