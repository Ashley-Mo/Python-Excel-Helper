from tkinter import *
from tkinter import filedialog
import csv
import webbrowser


def inputs():
    inputs.file_path = filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
    done = Label(window, text="Input File Uploaded!\n\nFile Path: "+inputs.file_path+"\n\n\nPlease choose your Output text File", font=("Verdana Bold", 8))
    done.grid()
    print('Input File received')
    return inputs.file_path

def output():
    output.outfile = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    writeOut = open(output.outfile, "w")
    print('Processing...')

    # strings to hold text header and result
    result = ""
    header = ""
    # Open CSV file
    with open(inputs.file_path) as csvFile:
        readInput = csv.reader(csvFile)
        row1 = next(readInput)
        for col in range(0, len(row1)):
            if col == 0:
                header = header + '|||:' + row1[col]
            elif col < len(row1):
                header = header + '|:' + row1[col]
        # print(header)
        # writing header to output text file
        writeOut.write(str(header))
        writeOut.write('\n')
        for line in readInput:
            for col in range(0, len(line)):
                for each in line[col]:
                    if '\n' in each:
                        line[col]=line[col].replace('\n', '')
                        print('Line break handled')
                if col == 0:
                    result = result + '||' + line[col]
                elif col < len(line):
                    result = result + '|' + line[col]
            # print(result)
            # writing result to output text file
            writeOut.write(str(result))
            writeOut.write('\n')
            result = ''
    print('File processed successfully\n\n\n')
    success = Label(window, text="\nFile processed successfully",font=("Verdana Bold", 8))
    success.grid()
    clicks = Button(window, text="Click to open Output", bg="grey", fg="black", command=click)
    clicks.grid()

def click():
    click.clicked=webbrowser.open(output.outfile)

window = Tk()
window.geometry('600x400')
window.title("TestRail Helper Tool")
lbl = Label(window, text="Please choose your files",font=("Verdana Bold", 18))
lbl.grid(column=0, row=1,padx=(100, 100), pady=(10, 10))


btnInput = Button(window, text="Input File",bg="grey", fg="black",command=inputs)
btnInput.grid()


btnOut = Button(window, text="Output File",bg="grey", fg="black",command=output)
btnOut.grid()



window.mainloop()


