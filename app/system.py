import tkinter.messagebox

# ========= >>> error pop ups <<< =========
class error:
    def user_not_found():
        tkinter.messagebox.showwarning(f"Login Error", f"User not found")

    def empty():
        tkinter.messagebox.showwarning(
            f"Fields Empty", f"Fields can't be empty. Please check and try again"
        )

    def password():
        tkinter.messagebox.showwarning(
            f"Password Error", f"Passwords do not match. Please check and try again."
        )

    def email_exist():
        tkinter.messagebox.showwarning(
            f"Email Error", f"Email already exist. Please check and try again."
        )

    def user_exist():
        tkinter.messagebox.showwarning(
            f"Username Error", f"Username already exist. Please check and try again."
        )
    
    def no_account():
        tkinter.messagebox.showwarning(
            f"Transaction Error", f"To create a transaction, you must first have a valid account. \nPlease check and try again."
        )


# ========= >>> success pop ups <<< =========
class success:
    def user_added():
        tkinter.messagebox.showinfo(
            f"Account Created", f"Account created successfully!"
        )

    def personal_info_added():
        tkinter.messagebox.showinfo(
            f"Personal Info", f"Personal Informations added successfully!"
        )
        return True

    def login():
        tkinter.messagebox.showinfo(f"Login Success", f"User found!")
        return True

    def tos():
        tkinter.messagebox.showinfo(
            f"Terms of Service", f"You accepted Terms of Service"
        )
        return True
    
    def add_acc():
        tkinter.messagebox.showinfo(
                f"Account Added", f"Account added susccessfully."
            )
        return True
    
    def del_acc():
        tkinter.messagebox.showinfo(
                f"Account Unbinded", f"Account unbinded susccessfully."
            )
        return True
    
    def transac():
        tkinter.messagebox.showinfo(
                f"Transaction Completed", f"Account transaction completed successfully."
            )
        return True


# ========= >>> system process checker/validator <<< =========
class validate:
    def fields(string):
        if len(string) == 0:
            return True
        else:
            return False


class message:
    def hello_user(user):
        tkinter.messagebox.showinfo(
            f"New user",
            f"Hi, {user}!\nThe system recognized that you are a new user of this app.\nLet us help you run a quick setup.",
        )
        return True

    def add_info():
        tkinter.messagebox.showinfo(
            f"Personal Info", f"Let's start with your personal informations."
        )
        return True

    
