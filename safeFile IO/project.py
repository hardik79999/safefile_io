# Q 132: Use Finally Block for Resource Cleanup
# Write a function open_and_close_file(filename) that opens a file, performs some read/write operations, and ensures that the file is closed properly in the finally block, even if an exception occurs during the operations.

def open_and_close_file(filename):
    f = None  
    try:    
        menu = """
                you want write a file click (1)
                you want read  a file click (2)
               """
        print(menu)
        choice = int(input("Enter your choice (1/2): "))

        if choice == 1:
            f = open(filename, "w") 
            f.write(input("file me likhiye : "))
            print("✅ Data likh diya gaya hai!")
        elif choice == 2:
            f = open(filename, "r") 
            print(f"📄 Content: {f.read()}")
        else:
            print("❌ Out of range sorry ...!!")

    except FileNotFoundError:
        print("❌ File nhi mill rahi...")
    except ValueError:
        print("❌ Please number daaliye (1 ya 2)...")
    except Exception as e:
        print(f"❌ Kuch galat hua: {e}")

    finally:
        # Ye block hamesha chalega!
        if f is not None:
            f.close()
            print("🔒 Safe Cleanup: File ko band kar diya gaya hai.")   
        else:
            print("⚠️ Cleanup: File khuli hi nahi thi.")

filename = "132.txt"
open_and_close_file(filename)



# def open_and_close_file():
#     f = None  
#     try:
#         ask = input("Kya aap ek nayi file banana chahte hain? (yes/no): ").lower()
        
#         if ask == 'yes':
#             # Agar yes hai toh naam poocho
#             name = input("Nayi file ka naam kya rakhen? : ")
#             if not name.endswith(".txt"):
#                 name += ".txt"
#             filename = name # Naya naam set kiya
#             f = open(filename, "w+") 
#             print(f"🆕 Nayi file '{filename}' ban gayi hai!")
#         else:
#             # Agar no hai toh bina pooche ye naam fix kar do
#             filename = "132.txt" 
#             f = open(filename, "a+") 
#             print(f"📂 Default file '{filename}' open ho gayi!")

#         # Menu Logic (Dhyan rahe ye if-else ke bahar hai taaki dono ke liye chale)
#         menu = """
#                 (1) Write (Likhna)
#                 (2) Read (Padhna)
#                """
#         print(menu)
#         choice = input("Enter choice (1/2): ") # Int hata diya taaki crash na ho

#         if choice == '1':
#             data = input("File me kya likhna hai? : ")
#             f.write(data + "\n")
#             print("✅ Data save ho gaya!")
#         elif choice == '2':
#             f.seek(0)
#             print(f"📄 Content:\n{f.read()}")
#         else:
#             print("❌ Galat choice!")

#     except Exception as e:
#         print(f"❌ Error: {e}")

#     finally:
#         if f is not None:
#             f.close()
#             print("🔒 Safe Cleanup: File closed.")

# open_and_close_file()