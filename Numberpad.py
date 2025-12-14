from tkinter import*
root=Tk()
root.title('Number pad')
root.geometry('250x300')
nums=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
for i in range(4):
    root.rowconfigure(i,weight=1)
    for j in range(3):
        root.columnconfigure(j,weight=1)
        frame=Frame(master=root,relief=SUNKEN,borderwidth=1,bg="#d0efff")
        frame.grid(row=i,column=j,sticky="nsew",padx=3,pady=5)
        label=Label(master=frame,text=nums[i][j],bg="#d0efff",font=("Arial",16))
        label.pack(expand=True,padx=1,pady=5)
root.mainloop()