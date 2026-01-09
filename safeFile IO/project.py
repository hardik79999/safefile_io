def file_manager():
    file = None
    try:
        choice = input("Do you want to create a new file? (yes/no): ").lower()

        if choice == 'yes':
            filename = input("Enter new file name: ")
            if not filename.endswith(".txt"):
                filename += ".txt"
            file = open(filename, "w+")
            print(f"🆕 New file '{filename}' created successfully!")
        elif choice == 'no':
            filename = "default.txt"
            file = open(filename, "a+")
            print(f"📂 Default file '{filename}' opened successfully!")
        else:
            raise ValueError("Only 'yes' or 'no' is allowed")

        menu = """
        (1) Write to file
        (2) Read file
        """
        print(menu)

        option = input("Enter your choice (1/2): ")

        if option == '1':
            data = input("Enter text to write into the file: ")
            file.write(data + "\n")
            print("✅ Data written successfully!")
        elif option == '2':
            file.seek(0)
            print("📄 File Content:\n")
            print(file.read())
        else:
            raise ValueError("Invalid menu option selected")

    except FileNotFoundError:
        print("❌ Error: File not found.")

    except PermissionError:
        print("❌ Error: You do not have permission to access this file.")

    except ValueError as ve:
        print(f"❌ Input Error: {ve}")

    except IOError:
        print("❌ Error: File input/output operation failed.")

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

    finally:
        if file:
            file.close()
            print("🔒 File closed safely.")

file_manager()
