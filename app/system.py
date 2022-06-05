import tkinter.messagebox

# ========= >>> error pop ups <<< =========
class error(): 

    def user_not_found():
        tkinter.messagebox.showwarning(f'Login Error', f'User not found')
    
    def empty():
        tkinter.messagebox.showwarning(f'Fields Empty', f'Fields can\'t be empty. Please check and try again')
    
    def password():
        tkinter.messagebox.showwarning(f'Password Error', f'Passwords do not match. Please check and try again.')

    def email_exist():
        tkinter.messagebox.showwarning(f'Email Error', f'Email already exist. Please check and try again.')
    
    def user_exist():
        tkinter.messagebox.showwarning(f'Username Error', f'Username already exist. Please check and try again.')

# ========= >>> success pop ups <<< =========    
class success():

    def user_added():
        tkinter.messagebox.showinfo(f'Account Created', f'Account created successfully!')

    def login():
        tkinter.messagebox.showinfo(f'Login Success', f'User found!')
        return True

    def tos():
        tkinter.messagebox.showinfo(f'Terms of Service', f'You accepted Terms of Service')
        return True

# ========= >>> system process checker/validator <<< =========  
class validate():

    def fields(string):
        if len(string) == 0:
            return True
        else:
            return False