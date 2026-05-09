import tkinter

window= tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=350)
window.columnconfigure(0, weight=1)

title_label= tkinter.Label(text="BMI Calculator", font=("Arial", 20, "bold"))
title_label.pack(padx=10, pady=(30,15))

name_label= tkinter.Label(text="Enter your name:")
name_label.pack(padx=10, pady=5)

def check_name(input_string):
    return all(x.isalpha() or x.isspace() for x in input_string)
check_name_wrapper= window.register(check_name)

name_entry= tkinter.Entry(width=15, validate="key", validatecommand=(check_name_wrapper, '%P'))
name_entry.pack(padx=10, pady=5)

gender_var= tkinter.StringVar(value="Male")
radio_male= tkinter.Radiobutton(text="Male", variable=gender_var, value="Male")
radio_male.pack(padx=10, pady=5)
radio_female= tkinter.Radiobutton(text="Female", variable=gender_var, value="Female")
radio_female.pack(padx=10, pady=5)

label1= tkinter.Label(text="Enter Your Weight (kg)", font=("Arial", 10, "normal"))
label1.pack(padx=10, pady=5)

entry1= tkinter.Entry(width=15)
entry1.pack(padx=10, pady=5)

label2= tkinter.Label(text="Enter Your Height (cm)", font=("Arial", 10, "normal"))
label2.pack(padx=10, pady=5)

entry2= tkinter.Entry(width=15)
entry2.pack(padx=10, pady=5)

def calculate_bmi():
    try:
        name= name_entry.get()
        gender= gender_var.get()
        weight_val= float(entry1.get())
        height_val= float(entry2.get())
        if weight_val <= 0 or height_val <= 0:
            result_label.config(text="Enter numbers greater than zero!", fg="red")
            return
        height_val_converted= height_val / 100
        bmi= weight_val / (height_val_converted * height_val_converted)
    
        status= ""
        color= "black"
        if bmi < 18.5:
            status= "Underweight"
            color= "blue"
        elif 18.5 <= bmi < 25:
            status= "Normal"
            color= "green"
        elif 25 <= bmi < 30:
            status= "Overweight"
            color= "orange"
        else:
            status= "Obese"
            color= "red"
        
        result_label.config(text=f"Dear {name_entry.get()} BMI is {bmi:.2f}. You are {status}", fg=color)

        ideal_weight_top= 24.9 * (height_val_converted * height_val_converted)
        ideal_weight_below= 18.5 * (height_val_converted * height_val_converted)
        result_label2.config(text=f"Your ideal weight range is between {ideal_weight_below:.2f} and {ideal_weight_top:.2f}.", fg=color)

        with open("my_bmi_records.txt", mode="a") as data_file:
            data_file.write(f"Name: {name}, Gender: {gender}, BMI: {bmi:.2f}, Status: {status}\n")

        name_entry.delete(0, "end")
        entry1.delete(0, "end")
        entry2.delete(0, "end")

    except ValueError:
        result_label.config(text="Enter a valid number!", fg="red")

button1= tkinter.Button(text="Calculate", command=calculate_bmi)
button1.pack(padx=10, pady=5)

result_label= tkinter.Label(text="")
result_label.pack(padx=10, pady=5)

result_label2= tkinter.Label(text="")
result_label2.pack(padx=10, pady=5)

window.mainloop()