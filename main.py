import tkinter

window= tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=250)
window.columnconfigure(0, weight=1)

label1= tkinter.Label(text="Enter Your Weight (kg)", font=("Arial", 10, "normal"))
label1.grid(row=0,column=0, padx=10, pady=(30,5))

entry1= tkinter.Entry(width=15)
entry1.grid(row=1, column=0, padx=10, pady=5)

label2= tkinter.Label(text="Enter Your Height (cm)", font=("Arial", 10, "normal"))
label2.grid(row=2,column=0, padx=10, pady=5)

entry2= tkinter.Entry(width=15)
entry2.grid(row=3, column=0, padx=10, pady=5)

def calculate_bmi():
    try:
        weight_val= float(entry1.get())
        height_val= float(entry2.get())
        if weight_val <= 0 or height_val <= 0:
            result_label.config(text="Enter numbers greater than zero!")
            return
        height_val_converted= height_val / 100
        bmi= weight_val / (height_val_converted * height_val_converted)
    
        status= ""
        if bmi < 18.5:
            status= "Underweight"
        elif 18.5 <= bmi < 25:
            status= "Normal"
        elif 25 <= bmi < 30:
            status= "Overweight"
        else:
            status= "Obese"
        
        result_label.config(text=f"Your BMI is {bmi:.2f}. You are {status}")
        entry1.delete(0, "end")
        entry2.delete(0, "end")

    except ValueError:
        result_label.config(text="Enter a valid number!")

button1= tkinter.Button(text="Calculate", command=calculate_bmi)
button1.grid(row=4, column=0, padx=10, pady=5)

result_label= tkinter.Label(text="")
result_label.grid(row=5, column=0, padx=10, pady=5)

window.mainloop()