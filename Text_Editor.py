import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
import re

root=tk.Tk()
root.title("Text Editor")
# root.wm_iconbitmap('icon.ico')

############################  main menu ########################################################3################

main_menu=tk.Menu()

# file menu
files=tk.Menu(main_menu,tearoff=False)
# file_menu icon
new_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\new.png")
open_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\open.png")
save_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\save.png")
save_as_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\\save_as.png")
exit_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\exit.png")


# edit menu
edit=tk.Menu(main_menu,tearoff=False)
# edit_menu icon
copy_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\copy.png")
paste_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\paste.png")
cut_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\cut.png")
clear_all_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\clear_all.png")
find_all_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\find.png")


# view menu
view=tk.Menu(main_menu,tearoff=False)
# view_menu icons
status_bar_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\status_bar.png")
tool_bar_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\tool_bar.png")


# color_theme menu
color_theme=tk.Menu(main_menu,tearoff=False)
# color_theme icons
dark_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\dark.png")
red_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\red.png")
night_blue_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\night_blue.png")
monokai_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\monokai.png")
light_plus_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\light_plus.png")
light_default_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\light_default.png")

# main menu cascade
main_menu.add_cascade(label="File",menu=files)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color Theme",menu=color_theme)

# ---------------------------------  end main menu --------------------------------------------------------------


########################### tool bar ############################################################################

# creating toolbar lavel
tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# creating font family
#getting font family
font_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuples
font_box.current(font_tuples.index('Times New Roman'))
font_box.grid(row=0,column=0,padx=5)


# font size
font_size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=20,textvariable=font_size_var,state='readonly')
font_size['values']=tuple(range(10,81))
font_size.current(6)
font_size.grid(row=0,column=1,padx=5)


# bold button
bold_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\bold.png")
bold_button=tk.Button(tool_bar,image=bold_icon,)
bold_button.grid(row=0,column=3,padx=5)

#italic button
italic_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\italic.png")
italic_button=tk.Button(tool_bar,image=italic_icon,)
italic_button.grid(row=0,column=4,padx=5)

#underline button
underline_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\underline.png")
underline_button=tk.Button(tool_bar,image=underline_icon,)
underline_button.grid(row=0,column=5,padx=5)

# font color
font_color_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\font_color.png")
font_button=tk.Button(tool_bar,image=font_color_icon,)
font_button.grid(row=0,column=6,padx=5)

#left alignment
left_align_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\align_left.png")
left_align_button=tk.Button(tool_bar,image=left_align_icon,)
left_align_button.grid(row=0,column=7,padx=5)

# center alignment
center_align_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\align_center.png")
center_align_button=tk.Button(tool_bar,image=center_align_icon,)
center_align_button.grid(row=0,column=8,padx=5)

# right alignment
right_align_icon=tk.PhotoImage(file=r"F:\CSE\PYTHON\mohit text editor\icons2\align_right.png")
right_align_button=tk.Button(tool_bar,image=right_align_icon,)
right_align_button.grid(row=0,column=9,padx=5)

#------------------------------------------- end tool bar -------------------------------------------------------


######################################### text editor ###########################################################

text_editor=tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)
text_editor.focus()

scroll_bar=tk.Scrollbar(root)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


# font family functionality
current_font_family='Times New Roman'
current_font_size=16

def change_font_family(events=None):      # because of binding of fn one more arguments is passed
    global current_font_family
    current_font_family=font_family.get()
    text_editor.config(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font_family)

#font size functionality
def change_font_size(events=None):
    global current_font_size
    current_font_size=font_size_var.get()
    text_editor.config(font=(current_font_family,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_font_size)


# Bold button functionality
def bold_button_func(events=None):
    text_property=tk.font.Font(font=(text_editor['font']))   # return a dict of all font applied on it like font family ,font size,bold or normal,italic or roman etc
    if text_property.actual()['weight']=='normal':
        text_editor.config(font=(current_font_family,current_font_size,'bold'))
    else:
        text_editor.config(font=(current_font_family,current_font_size,'normal'))

bold_button.configure(command=bold_button_func)


#italic button functionality
def italic_button_func(event=None):
    text_property=tk.font.Font(font=(text_editor['font']))   # return a dict of all font applied on it like font family ,font size,bold or normal,italic or roman etc
    if text_property.actual()['slant']=='roman':
        text_editor.config(font=(current_font_family,current_font_size,'italic'))
    else:
        text_editor.config(font=(current_font_family,current_font_size,'roman'))

italic_button.configure(command=italic_button_func)


#underline button functionality
def underline_button_func(event=None):
    text_property=tk.font.Font(font=(text_editor['font']))   # return a dict of all font applied on it like font family ,font size,bold or normal,italic or roman etc
    if text_property.actual()['underline']==0:
        text_editor.config(font=(current_font_family,current_font_size,'underline'))
    else:
        text_editor.config(font=(current_font_family,current_font_size,'normal'))

underline_button.configure(command=underline_button_func)


#font color functionality
def font_color_func():
    color_value=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_value[1])

font_button.configure(command=font_color_func)


# align left functionality
def left_align_func():
    text_content=text_editor.get('1.0','end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete('1.0','end')
    text_editor.insert(tk.INSERT,text_content,'left')

left_align_button.configure(command=left_align_func)


# align center functionality
def center_align_func():
    text_content=text_editor.get('1.0','end')
    print(text_content)
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete('1.0',tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

center_align_button.configure(command=center_align_func)


# align right functionality
def right_align_func():
    text_content=text_editor.get('1.0','end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete('1.0',tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

right_align_button.configure(command=right_align_func)


text_editor.config(font=('Times New Roman',16))

#----------------------------------------- end text editor ------------------------------------------------------


########################################## status bar #########################################################

status_bar=tk.Label(root,text='Status bar')
status_bar.pack(side=tk.BOTTOM)

text_change=False

def change_status_value(events=None):
    global text_change
    # text_editor.edit_modified()  this will return if something is modified in the texteditor
    if text_editor.edit_modified():
        text_change=True        # helpfull in edit menu functionality
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c')) # count space as a character also
        # characters=len(text_editor.get(1.0,'end-1c').replace(" ","")) not count the spaces
        status_bar.config(text=f"Character : {characters} Words : {words}")
    text_editor.edit_modified(False)   # after modification count it get false and again work if modified

text_editor.bind("<<Modified>>",change_status_value)


#---------------------------------------------- end status bar---------------------------------------------------


###################  main menu functionality #########################################################

# variable that keep the information of open file name
url=''

# new functionality
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)
    root.title('Mohit Text Editor')


# open functionality
def open_file(event=None):
    global url
    url=tk.filedialog.askopenfilename(initialdir=os.getcwd(),title='Select file',filetype=(('text file','*.txt'),('All Files','*.*')))
    # print(url)      # print location of file which u open
    try:
        with open(url,'r') as tr:
            text_editor.delete(1.0,tk.END)
            value=tr.read()
            text_editor.insert(1.0,value)
            tr.close()
    except FileNotFoundError:
        return
    except:
        return

    root.title(os.path.basename(url))       # extract the file name from the location


# save functionality
def save_file(event=None):
    global url
    try:
        if url:
            values=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as tw:
                tw.write(values)
                tw.close()
        else:
            url=tk.filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All File','*.*')))
            # print(url)      #not a file location only
            # print(url.name)    # extract the file location
            values2=text_editor.get(1.0,tk.END)
            # url.write(values2)
            # url.close()
            with open(url.name,'a') as tw:
                tw.write(values2)
                # print(tw)      # the above url is as behave as this tw is  so u may also write url.write(..)
                root.title(os.path.basename(url.name))
    except:
        return



#save_as  functionality
def save_as_file(event=None):
    global url
    try:
        values=text_editor.get(1.0,tk.END)
        url=tk.filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All File','*.*')))
        url.write(values)
        root.title(os.path.basename(url.name))
        url.close()
    except:
        return


# exit functionality
def exit_func(event=None):
    global url,text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save this file ?')
            if mbox is True:
                if url:
                    values=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as tw:
                        tw.write(values)
                        root.destroy()
                else:
                    values=str(text_editor.get(1.0,tk.END))
                    url=tk.filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All File','*.*')))
                    url.write(values)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return


# file menu command
files.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl + N",command=new_file)
files.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl + O",command=open_file)
files.add_separator()
files.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl + S",command=save_file)
files.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl + Alt + S",command=save_as_file)
files.add_separator()
files.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl + Q",command=exit_func)


##### find and replace functionality
def find_replace(evnt=None):
    def find_words():
        words=find_entry.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if words:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(words,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(words)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace_words():
        word_find=find_entry.get()
        word_replace=replace_entry.get()
        strings=text_editor.get(1.0,tk.END)
        # new_strings=strings.replace(word_find,word_replace)   # also done like this 
        values=re.sub(word_find,word_replace,strings)     # replace the words
        text_editor.delete(1.0,tk.END)
        # text_editor.insert(1.0,new_strings)    # for line number 384
        text_editor.insert(1.0,values)

    find_dialogue_box=tk.Toplevel()
    find_dialogue_box.geometry("500x250+500+200")
    find_dialogue_box.title('Find')
    find_dialogue_box.resizable(0,0)

    #frame
    find_frame=tk.LabelFrame(find_dialogue_box,text='Find and Replace')
    find_frame.pack(pady=40)
    

    # labels
    find_label=ttk.Label(find_frame,text='Find :')
    replace_label=ttk.Label(find_frame,text='Replace :')

    # entry box
    find_entry=ttk.Entry(find_frame,width=30)
    replace_entry=ttk.Entry(find_frame,width=30)

    # buttons
    find_button=ttk.Button(find_frame,text='Find',command=find_words)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace_words)

    # labels grids
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label.grid(row=1,column=0,padx=4,pady=4)

    # entry box grids
    find_entry.grid(row=0,column=1,padx=8,pady=4)
    replace_entry.grid(row=1,column=1,padx=8,pady=4)

    #button grids
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue_box.mainloop()


# edit menu command
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT ,accelerator="Ctrl + C",command=lambda:text_editor.event_generate("<Control c>"))

edit.add_command(label="Cut",image=copy_icon,compound=tk.LEFT ,accelerator="Ctrl + x",command=lambda:text_editor.event_generate("<Control x>"))

edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT ,accelerator="Ctrl + v",command=lambda:text_editor.event_generate("<Control v>"))

edit.add_separator()

edit.add_command(label="Undo",image=new_icon,compound=tk.LEFT,accelerator="Ctrl + U",command=text_editor.edit_undo)

edit.add_command(label="Redo",image=new_icon,compound=tk.LEFT,accelerator="Ctrl + Z",command=text_editor.edit_redo)

edit.add_separator()
edit.add_cascade(label="Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator="Ctrl + alt + x",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="Findall",image=find_all_icon,compound=tk.LEFT,accelerator="Ctrl + F",command=find_replace)


# view menu functionality
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

                #################### toolbar functionality#######################

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True



#  view_menu command
view.add_checkbutton(label="Status bar",onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
view.add_separator()
view.add_checkbutton(label="Tool bar",onvalue=1,offvalue=False,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)



# color_theme command
theme_choice=tk.StringVar()
theme_icon=(light_default_icon,dark_icon,red_icon,night_blue_icon,light_plus_icon,monokai_icon)
color_dict={
    'Light Default':("#000000","#ffffff"),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Night Blue':('#ededed','#6b9dc2'),
    'Light Plus' :('#474747','#e0e0e0'),
    'monokai':('#d3b774','#6b9dc2')
}

def change_theme():
    choosen_theme=theme_choice.get()
    # print(choosen_theme)
    color_tuple=color_dict.get(choosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,foreground=fg_color)


count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=theme_icon[count],compound=tk.LEFT,variable=theme_choice,command=change_theme)
    count=count+1

# print(theme_choice.get())   

#--------------------------- end main menu functality-------------------------------------------




root.config(menu=main_menu)

#####################################   binding ################################################
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Alt-s>", save_as_file)
root.bind("<Control-q>", exit_func)
root.bind("<Control-r>",find_replace)
root.bind("<Control-b>",bold_button_func)
root.bind("<Control-u>",underline_button_func)

root.geometry("1530x825+0+0")
root.mainloop()