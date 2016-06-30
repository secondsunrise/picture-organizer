import os, shutil, tkFileDialog

while True:

    # Prompt for the source directory
    print "Select the source directory..."
    source_dir = str(tkFileDialog.askdirectory())  # "C:/Users/<username>/Downloads/20150902_183347"
    print source_dir
    print ""
    
    # Prompt for the target directory where the pictures will be copied to
    print "Select the target directory..."
    target_dir = str(tkFileDialog.askdirectory())  # "C:/Users/<username>/Pictures/test_dir"
    print target_dir
    print ""
    
    # Prompt for the text that is to be appended to each folder created in the target_dir
    text_to_append = raw_input("What do you want to append to each folder name?\n> ")
    print ""

	# Get all of the source file names
    source_files = os.listdir(source_dir)
    print "Found " + str(len(source_files)) + " files to copy"

	# Modify each source file name, redacting each to its first eight characters
    modified_source_files = source_files
    for i in range(0, len(source_files)):
        modified_source_files[i] = source_files[i][:8]

	# Filter out duplicate names to get a list of only unique ones
    unique_source_file_dates = sorted(list(set(source_files)))
	modified_unique_source_file_dates = unique_source_file_dates
    print "Found " + str(len(unique_source_file_dates)) + " unique dates"

	# Format each unique name 
    for i in range(0, len(unique_source_file_dates)):
        modified_unique_source_file_dates[i] = unique_source_file_dates[i][:4] + "-" + unique_source_file_dates[i][4:6] + "-" + unique_source_file_dates[i][6:]
        modified_unique_source_file_dates[i] = modified_unique_source_file_dates[i] + " " + text_to_append

	# Sort the unique dates and make the directories inside of the target_dir
    unique_source_file_dates = sorted(list(set(source_files)))
    for i in range(0, len(modified_unique_source_file_dates)):
        if not os.path.exists(target_dir + "/" + modified_unique_source_file_dates[i]):
            os.makedirs(target_dir + "/" + modified_unique_source_file_dates[i])

	# Since the variable source_files was modified, it needs to be reset to its original value
    source_files = os.listdir(source_dir)

	# Copy the files into their respective directories within the target_dir
    print "Please wait while the program copies the files..."
    for i in range(0, len(modified_source_files)):
        for j in range(0, len(unique_source_file_dates)):
            if modified_source_files[i] == unique_source_file_dates[j]:
                shutil.copy(source_dir + "/" + source_files[i], target_dir + "/" + modified_unique_source_file_dates[j])

    print ""
    print "Transfer complete, would you like to start again?"
    print "Enter 1 for 'yes'"
    print "Enter 2 for 'no'"
    go_again = int(raw_input("> "))
    if go_again == 1:
        continue
    elif go_again == 2:
        exit()
