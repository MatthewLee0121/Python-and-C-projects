import BackEnd

def create_main(open_file_command, get_image_path_command):

        #create the main window of the GUI
        main_window = tk.Tk()
        main_window.title("Settings for your generation!")
        main_window.geometry("400x600")
        main_window.configure(bg="#f0f0f0")

        # Create the generate artwork button
        get_art_button = tk.Button(
            main_window,
            text="Generate artwork",
            font=("Rockabilly", 10),
            command=lambda: open_file_command(font_size_var.get()),
            width=20,
            height=2
        )
        get_art_button.pack(pady=10)


        # Create the select image button
        get_image_path_button = tk.Button(
            main_window,
            text="Select image",
            font=("Rockabilly", 10),
            command=get_image_path_command,
            width=20,
            height=2
        )
        get_image_path_button.pack(pady=10)

        # GUI variables
        font_size_var = tk.IntVar(value=1)
        rows = tk.IntVar(value=1)
        columns = tk.IntVar(value=1)
        line_detection = tk.IntVar()

        # Create font size scale
        font_size_scale = tk.Scale(
            main_window,
            from_=1,
            to=20,
            orient=tk.HORIZONTAL,
            variable=font_size_var,
            label="Font Size"
        )
        font_size_scale.pack(pady=10)

        # Create rows scale
        rows_scale = tk.Scale(
            main_window,
            from_=1,
            to=10,
            orient=tk.HORIZONTAL,
            variable=rows,
            label="Adjust Y Scaling"
        )
        rows_scale.pack(pady=10)

        # Create columns scale
        columns_scale = tk.Scale(
            main_window,
            from_=1,
            to=10,
            orient=tk.HORIZONTAL,
            variable=columns,
            label="Adjust X Scaling"
        )
        columns_scale.pack(pady=10)

        LineDetection_box = tk.Checkbutton(
            main_window,
            text= 'Line Detection?(untick for mp4)',
            variable= line_detection,
            onvalue= True,
            offvalue= False,
        )
        LineDetection_box.pack(pady=10)

        # Return the main window
        return main_window, font_size_var, columns, rows, line_detection

    #creates the main window
    main_window, font_size_var, columns, rows, line_detection = create_main(open_file, get_image_path)

    # Start the Tkinter event loop
    main_window.mainloop()